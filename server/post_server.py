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
        response.success = database.savePost(request.title, request.content, request.picture_blob, request.id)

        return response

    def fetchPostDetails(self, request, context):
        response = protos_pb2.FetchPostDetails.Response()
        response.success = False
        response.title = database.fetchSinglePost(request.post_id)["title"]
        response.content = database.fetchSinglePost(request.post_id)["content"]
        response.pictureBlob = bytes(database.fetchSinglePost(request.post_id)["picture_blob"])

        print(response.title)
        print(response.content)

        response.success = True

        return response

    def fetchPosts(self, request, context):
        response = protos_pb2.FetchPostsByPage.Response()
        response.success = False

        for row in database.fetchPostsByPage(request.pageNumber, 15):
            response.id.append(row["id"])
            response.title.append(row["title"])
            response.content.append(row["content"])
            response.pictureBlob.append(bytes(row["picture_blob"]))

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
