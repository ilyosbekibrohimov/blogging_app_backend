from concurrent import futures
import grpc
import time
from google.auth.transport import requests as oauth_requests
from google.oauth2 import id_token as oauth_id_token

# import generated files
from tools.database import connect_db
from generated_files import protos_pb2
from generated_files import protos_pb2_grpc
from tools import database


class PostServices(protos_pb2_grpc.PostServiceServicer):

    def uploadPost(self, request, context):
        response = protos_pb2.UploadPost.Response()
        response.success = False
        print(request.picture_blob)
        response.success = database.savePost(request.title, request.content, request.picture_blob, request.id,
                                             request.timestamp)

        return response

    def fetchPostDetails(self, request, context):
        print("hey")
        response = protos_pb2.FetchPostDetails.Response()
        response.success = False
        response.title = database.fetchSinglePost(request.post_id)["title"]
        response.content = database.fetchSinglePost(request.post_id)["content"]
        response.pictureBlob = bytes(database.fetchSinglePost(request.post_id)["picture_blob"])
        response.user_id = database.fetchSinglePost(request.post_id)["user_id"]
        response.creator_name = database.getUserById(response.user_id)["name"]
        response.creator_photoUrl = database.getUserById(response.user_id)["photo_url"]
        response.numberOfLikes = database.fetchSinglePost(request.post_id)["number_likes"]

        response.isLiked = database.isPostLikedByMe(request.post_id, request.user_id)

        print("post is liked", response.isLiked)

        response.success = True

        return response

    def fetchPosts(self, request, context):
        response = protos_pb2.FetchPostsByPage.Response()
        response.success = False

        for row in database.fetchPostsByPage(request.pageNumber, 15):
            userId = row["user_id"]
            response.id.append(row["id"])
            response.title.append(row["title"])
            response.content.append(row["content"])
            response.pictureBlob.append(bytes(row["picture_blob"]))
            response.creator_names.append(database.getUserById(userId)["name"])
            response.creators_photo_url.append(database.getUserById(userId)["photo_url"])

        response.success = True

        return response

    def authenticateUser(self, request, context):
        response = protos_pb2.AuthenticateUser.Response()
        response.success = False

        google_id_details = oauth_id_token.verify_oauth2_token(id_token=request.id_token,
                                                               request=oauth_requests.Request())
        if google_id_details['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            print('google auth failure, wrong issuer')
        else:
            print(request.id_token)
            row = database.signIn(google_id_details['name'], google_id_details['email'], google_id_details["picture"])
            response.userId = row["id"]
            if response.userId is not None:
                response.success = True
            print(google_id_details['name'])
            print(google_id_details["email"])

            return response

    def createComment(self, request, context):
        response = protos_pb2.CreateComment.Response()
        response.success = False

        response.success = database.createComment(request.user_id, request.post_id, request.content)

        return response

    def fetchComments(self, request, context):
        response = protos_pb2.FetchCommentsByPost.Response()
        response.success = False

        for row in database.fetchComments(request.post_id):
            userId = row["user_id"]
            user = database.getUserById(userId)

            response.userName.append(user["name"])
            response.userPhotoUrl.append(user["photo_url"])
            response.content.append(row["content"])
            response.success = True

        return response

    def likePost(self, request, context):
        response = protos_pb2.LikePost.Response()
        response.success = False
        response.success = database.likePost(request.user_id, request.post_id, request.timestamp)
        return response

    def unlikePost(self, request, context):
        response = protos_pb2.UnlikePost.Response()
        response.success = False
        response.success = database.unlikePost(request.user_id, request.post_id, request.timestamp)
        return response

    def editPost(self, request, context):
        response = protos_pb2.EditPost.Response()
        response.success = False


        response.success = database.editPost(request.user_id, request.post_id, request.title, request.content,
                                             request.pictureBlob)

        return response

    def deletePost(self, request, context):
        response = protos_pb2.EditPost.Response()
        response.success = False

        response.success = database.deletePost(request.user_id,  request.post_id)
        return  response.success


connect_db()
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

protos_pb2_grpc.add_PostServiceServicer_to_server(PostServices(), server)
print('Starting server. Listening on port 50051')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop()
