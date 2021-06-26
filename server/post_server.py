from concurrent import futures
import grpc
import time

# import generated files
from db.database import connect_db
from generated_files import protos_pb2
from generated_files import protos_pb2_grpc
from db import database


class PostServices(protos_pb2_grpc.PostServiceServicer):

    def uploadPost(self, request, context):
        response = protos_pb2.UploadPost.Response()
        response.success = False
        print(request.picture_blob)
        response.success = database.savePost(request.title, request.content, request.picture_blob)

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
        response = protos_pb2.FetchPostsByPage.Response()
        response.success = False



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
