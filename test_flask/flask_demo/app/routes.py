from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'glj'}
    posts = [
        {
            'author': {'username': 'test1'},
            'body': 'sample 1'

        },
        {
            'author': {'username': 'test2'},
            'body': 'sample 2'
        }
    ]
    return render_template('index.html', title='glj', user=user, posts=posts)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('用户登录的名户名是:{} , 是否记住我:{}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='登 录', form=form)


@app.route('/user/<username>')
# @login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author':user,'body':'测试Post #1号'},
        {'author':user,'body':'测试Post #2号'}
    ]

    return render_template('user.html',user=user,posts=posts)

