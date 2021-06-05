import psycopg2


def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        database="posts",
        user="postgres",
        password="asdilyos98*"
    )

    print(conn)
    return conn


def close_db():
    if connect_db() is not None:
        connect_db().close()


# save post
def savePost(title, content, pictureBlob):
    pass


# fetch post data
def fetchPostTitle(id):
    pass


def fetchPostContent(id):
    pass


def fetchPostPictureBlob(id):
    pass


def fetchPostTitles(k):
    for i in range(k + 1):
        fetchPostTitle(i)


def fetchPostContents(k):
    for i in range(k + 1):
        fetchPostContent(i)


def fetchPostPictureBlobs(k):
    for i in range(k + 1):
        fetchPostPictureBlob(i)
