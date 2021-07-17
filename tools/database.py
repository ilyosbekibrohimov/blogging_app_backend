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


def savePost(title, content, pictureBlob, id, timestamp):
    cur = connect_db().cursor(cursor_factory=psycopg2_extras.DictCursor)
    cur.execute('insert into "posts"."post"("title", "content", "picture_blob", "user_id", "timestamp") values (%s,'
                '%s,%s, %s, %s);',
                (title, content, pictureBlob, id, timestamp))
    cur.close()
    return True


def fetchSinglePost(id):
    cur = connect_db().cursor(cursor_factory=psycopg2_extras.DictCursor)
    cur.execute('select * from "posts"."post" where id = %s;', [id])
    row = cur.fetchone()
    cur.close()

    return row


def isPostLikedByMe(postId, userId):
    try:
        cur = connect_db().cursor(cursor_factory=psycopg2_extras.DictCursor)

        if userId != -1:
            cur.execute('select * from  "posts"."likes"  where user_id = %s  and post_id = %s;', [userId, postId])
            if cur.rowcount == 0:
                return False
            else:
                return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


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
        print("An exception happened ", e)
        return None


def likePost(userId, postId, timestamp):
    cur = connect_db().cursor(cursor_factory=psycopg2_extras.DictCursor)
    try:
        cur.execute('insert into "posts"."likes"("user_id", "post_id", "timestamp") values (%s,'
                    '%s,%s);',
                    (userId, postId, timestamp))

        incrementLikes(postId)
        cur.close()
        return True

    except Exception as e:
        print(e)
        cur.close()
        return False


def unlikePost(userId, postId, timestamp):
    cur = connect_db().cursor(cursor_factory=psycopg2_extras.DictCursor)
    try:
        cur.execute('delete from  "posts"."likes" where "post_id" = %s and  "user_id" = %s;', [postId, userId])
        decrement(postId)
        cur.close()
        return True
    except Exception as e:
        print(e)
        cur.close()
        return False


def incrementLikes(postId):
    try:
        cur = connect_db().cursor(cursor_factory=psycopg2_extras.DictCursor)
        cur.execute('select * from "posts"."post"  where "id" = %s;', [postId])
        row = cur.fetchone()
        if row["number_likes"] is None:
            likes = 0
        else:
            print(row["number_likes"])
            likes = int(row["number_likes"])

        cur.execute('update "posts"."post" set "number_likes" = %s where  "id" = %s;', [likes + 1, postId])
        cur.close()
        return True
    except Exception as e:
        print(e)
        return False


def decrement(postId):
    try:
        cur = connect_db().cursor(cursor_factory=psycopg2_extras.DictCursor)
        cur.execute('select * from "posts"."post"  where "id" = %s;', [postId])
        row = cur.fetchone()
        if row["number_likes"] is None:
            likes = 0
        else:
            print(row["number_likes"])
            likes = int(row["number_likes"])
        if likes > 0:
            cur.execute('update "posts"."post" set "number_likes" = %s where  "id" = %s;', [likes - 1, postId])
        cur.close()
        return True
    except Exception as e:
        print(e)
        return False


def editPost(userId, postId, newTitle, newContent, newPictureBlob):
    cur = connect_db().cursor(cursor_factory=psycopg2_extras.DictCursor)

    try:
        cur.execute('update "posts"."post" set "title" = %s, "content" = %s, "picture_blob" = %s where "id" = %s and'
                    '"user_id" = %s;', [newTitle, newContent, newPictureBlob, postId, userId])
        cur.close()
        return True
    except Exception as e:
        print(e)
        cur.close()
        return False


def deletePost(userId, postId):
    cur = connect_db().cursor(cursor_factory=psycopg2_extras.DictCursor)

    try:
        cur.execute('delete  from  "posts"."likes" where "post_id" = %s', [postId])
        cur.execute('delete  from  "posts"."comments" where "post_id" = %s', [postId])
        cur.execute('delete from  "posts"."post" where "id" = %s and "user_id" = %s;', [postId, userId])
        cur.close()
        return True
    except Exception as e:
        print(e)
        cur.close()
        return False
