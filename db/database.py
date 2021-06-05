import psycopg2
from psycopg2 import extras as psycopg2_extras


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

    data = "not"
    cur = connect_db().cursor(cursor_factory=psycopg2_extras.DictCursor)
    cur.execute('insert into "posts"."post"("title", "content", "picture_blob") values (%s,%s,%s);', (
        title,
        content,
        data
    ))
    # print(cur.fetchone()[0])
    # print("I am here")

    cur.close()
    connect_db().commit()
    return True


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
