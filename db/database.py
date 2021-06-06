import psycopg2
import base64
from psycopg2 import extras as psycopg2_extras


def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        database="posts",
        user="postgres",
        password="asdilyos98*"
    )

    conn.set_session(autocommit=True)

    print(conn)
    return conn


def close_db():
    if connect_db() is not None:
        connect_db().close()


# save post
def savePost(title, content, pictureBlob):
    cur = connect_db().cursor(cursor_factory=psycopg2_extras.DictCursor)
    cur.execute('insert into "posts"."post"("title", "content", "picture_blob") values (%s,%s,%s);',
                (title, content, pictureBlob))
    cur.close()
    return True


# fetch post data
def fetchSinglePost(id):

    cur = connect_db().cursor(cursor_factory=psycopg2_extras.DictCursor)
    cur.execute('select * from "posts"."post" where id = %s;',[id])
    row = cur.fetchone()
    cur.close()

    return row


def fetchAllPostIds(k):
    cur = connect_db().cursor(cursor_factory=psycopg2_extras.DictCursor)
    cur.execute('select * from "posts"."post" limit %s;', [k])
    rows = cur.fetchall()
    cur.close()

    return rows



