import psycopg2
import settings
from psycopg2 import extras as psycopg2_extras


def connect_db():
    if settings.connect is None:
        settings.connect = psycopg2.connect(
            host="localhost",
            database="posts",
            user="postgres",
            password="asdilyos98*"
        )

    settings.connect.set_session(autocommit=True)

    print(settings.connect)
    return settings.connect


def close_db():
    if connect_db() is not None:
        connect_db().close()


# save post
def savePost(title, content, pictureBlob, id):
    cur = connect_db().cursor(cursor_factory=psycopg2_extras.DictCursor)
    cur.execute('insert into "posts"."post"("title", "content", "picture_blob") values (%s,%s,%s);',
                (title, content, pictureBlob))
    cur.close()
    return True


# fetch post data
def fetchSinglePost(id):
    cur = connect_db().cursor(cursor_factory=psycopg2_extras.DictCursor)
    cur.execute('select * from "posts"."post" where id = %s;', [id])
    row = cur.fetchone()
    cur.close()

    return row


def fetchPostsByPage(pageNumber, rowsOfPage):
    cur = connect_db().cursor(cursor_factory=psycopg2_extras.DictCursor)
    print((pageNumber - 1) * rowsOfPage)

    cur.execute('select * from "posts"."post" offset %s rows fetch next %s rows only;',
                [(pageNumber - 1) * rowsOfPage, rowsOfPage])

    rows = cur.fetchall()
    cur.close()
    return rows


def signIn(name, email, photo_url):

    cur = connect_db().cursor(cursor_factory=psycopg2_extras.DictCursor)

    print("1")
    cur.execute('select * from "posts"."users" where email  = %s;', [email])
    row = cur.fetchone()
    if row is not None:
        print("2")

        cur.close()
        return row
    else:
        print("3")

        cur.execute('insert into "posts"."users"("name", "email", "photo_url") values (%s,%s,%s);',
                    (name, email, photo_url))
        cur.execute('select * from "posts"."users" where email  = %s;', [email])
        row = cur.fetchone()
        cur.close()
        return row


def createComment(user_id, post_id, content):
    cur = connect_db().cursor(cursor_factory=psycopg2_extras.DictCursor)
    try:
        cur.execute('insert into "posts"."comments"("user_id", "post_id", "content") values (%s,%s,%s);',
                    (user_id, post_id, content))
        cur.close()

        return True
    except Exception as e:
        cur.close()
        print("An exception occurred: ", e)
        return False


def fetchComments(post_id):
    cur = connect_db().cursor(cursor_factory=psycopg2_extras.DictCursor)
    try:
        cur.execute('select * from "posts"."comments"  where post_id = %s;', [post_id])
        rows = cur.fetchall()
        cur.close()
        return rows
    except Exception as e:
        cur.close()
        print("An  exception happened ", e)
        return None


def getUserById(userId):
    cur = connect_db().cursor(cursor_factory=psycopg2_extras.DictCursor)
    try:
        cur.execute('select * from  "posts"."users" where id = %s', [userId])
        row = cur.fetchone()
        cur.close()
        return row
    except Exception as e:
        cur.close()
        print("An  exeception happened ", e)
        return None
