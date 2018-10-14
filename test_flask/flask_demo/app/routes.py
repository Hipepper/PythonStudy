from flask import render_template, flash, redirect, url_for
from test_flask.flask_demo.app import app
from test_flask.flask_demo.app.forms import LoginForm


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
