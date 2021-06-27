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

        for row in database.fetchPostsByPage(request.pageNumber, 10):
            response.id.append(row["id"])
            response.title.append(row["title"])
            response.content.append(row["title"])
            response.pictureBlob.append(bytes(row["picture_blob"]))

        response.success = True

        return response

    def authenticateUser(self, request, context):
        response = protos_pb2.AuthenticateUser.Response()
        response.success = False

        google_id_details = oauth_id_token.verify_oauth2_token(id_token=request.id_token, request=oauth_requests.Request())
        if google_id_details['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            print('google auth failure, wrong issuer')
        else:
            print(request.id_token)
            row = database.signIn(google_id_details['name'], google_id_details['email'], 'data:image/jpeg;base64,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')
            response.userId = row["id"]
            if response.userId is not None:
                response.success = True
            print(google_id_details['name'])
            print(google_id_details["email"])

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
