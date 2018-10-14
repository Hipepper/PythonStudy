from test_flask.flask_demo.app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<用户名:{}>'.format(self.username)


if __name__=='__main__':
    u = User(username='glj', email='glj@163.com')
    print(u)
    import sys
    print()