from concurrent import futures
import grpc
import time

# import generated files
from db.database import connect_db
from generated_files import posts_pb2
from generated_files import posts_pb2_grpc
from db import database


class PostServices(posts_pb2_grpc.PostServiceServicer):

    def uploadPost(self, request, context):
        response = posts_pb2.UploadPost.Response()
        response.success = False
        print(request.picture_blob)
        response.success = database.savePost(request.title, request.content, request.picture_blob)

        return response

    def fetchPostDetails(self, request, context):
        list = []
        response = posts_pb2.FetchPostDetails.Response()
        response.success = False
        response.title = database.fetchSinglePost(request.post_id)["title"]
        response.content = database.fetchSinglePost(request.post_id)["content"]
        response.pictureBlob = bytes(database.fetchSinglePost(request.post_id)["picture_blob"])

        response.success = True

        return response

    def fetchPosts(self, request, context):
        list = []
        response = posts_pb2.FetchKPostIds.Response()
        rows= database.fetchAllPostIds(request.k)

        for row in rows:
            list.append(row["id"])

        print(list)
        response.id.extend(list)
        return response


connect_db()
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

posts_pb2_grpc.add_PostServiceServicer_to_server(PostServices(), server)
print('Starting server. Listening on port 50051')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop()
