from app import db
from app.models import User, Post


def test_add_user(username, email):
    try:
        u = User(username=username, email=email)
        db.session.add(u)
        db.session.commit()
        print("add user: %s success, email: %s" % (username, email))
    except Exception as e:
        print(e)
        db.session.rollback()


def test_del_user(username=None):
    users = User.query.all()
    for u in users:
        if username is None or u.username == username:
            try:
                db.session.delete(u)
                db.session.commit()
                print("del user: %s success" % (username))
            except Exception as e:
                print(e)
                db.session.rollback()
            return


def test_query_user():
    users = User.query.all()
    for u in users:
        print("user: %s, id: %d, email: %s" % (u.username, u.id, u.email))


def test_add_post(body, author):
    try:
        p = Post(body=body,author=author)
        db.session.add(p)
        db.session.commit()
        print("add post success, body: %s" % (body))
    except Exception as e:
        print(e)
        db.session.rollback()


def test_del_post(body=None):
    posts = Post.query.all()
    for p in posts:
        if body is None or p.body == body:
            try:
                db.session.delete(p)
                db.session.commit()
                print("del post success, body: %s" % (body))
            except Exception as e:
                print(e)
                db.session.rollback()
            return


def test_query_post():
    posts = Post.query.all()
    for p in posts:
        print("post body: %s, id: %d, user id: %s" % (p.body, p.id, p.user_id))


if __name__ == '__main__':
    test_add_user(username='glj', email='glj@163.com')
    test_add_user(username='jrj', email='jrj@163.com')
    test_query_user()
    # test_del_user(username='glj')
    # test_del_user(username='jrj')
    u = User.query.get(1)
    print(u)
    # test_add_post(body='我第一次提交数据！',author=u)
    # test_add_post(body='我第二次提交数据！',author=u)
    test_query_post()

    u.set_password("mytest")
    print(u.check_password("yourtest"))
    print(u.check_password("mytest"))
