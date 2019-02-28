from app import app,db
from app.models import User
import sqlite3

def test_add_user(username, email):
    try:
        u = User(username=username, email=email)
        db.session.add(u)
        db.session.commit()
    except Exception as e:
        print(e)

def test_del_user(username):
    users = User.query.all()
    for u in users:
        if u.username == username:
            db.session.delete(u)
            db.session.commit()
            return


def test_query_user():
    users = User.query.all()
    for u in users:
        print(u.id, u.username, u.email)


if __name__=='__main__':
    test_add_user(username='glj', email='glj@163.com')
    # test_query_user()
    # test_del_user(username='glj')

    # app.run()