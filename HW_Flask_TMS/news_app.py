import os  # library for work file system
from datetime import datetime

from flask import Flask, render_template, url_for, redirect, request, flash, session, abort
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, login_required, logout_user

# configuration
from werkzeug.security import generate_password_hash, check_password_hash

DATABASE = '/tmp/news_app.db'  # path to our DB

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news_app.db'
app.config['SECRET_KEY'] = 'KASHDBJKQHBE12B31JHB4JNASKDJNdfssfegvc#'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/news_app.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/news_app.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://user:password@127.0.0.1:1521/news_app.db'

db = SQLAlchemy(app)
# login_manager = LoginManager(app)


class Author(db.Model):
    """Defining table 'authors' in 'news_app' DB"""
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(80), unique=True, nullable=False)
    author_email = db.Column(db.String(120), unique=True, nullable=False)
    author_password = db.Column(db.String(70), nullable=True)
    author_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<users {self.author_name}>"


class NewsArticle(db.Model):
    """Defining table 'news_articles' in 'news_app' DB"""
    __tablename__ = 'news_articles'
    id = db.Column(db.Integer, primary_key=True)
    article_title = db.Column(db.String(70))
    article_body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    author = db.relationship('Author', backref=db.backref('news_articles', lazy=True))

    category_id = db.Column(db.Integer, db.ForeignKey('news_category.id'), nullable=False)
    category = db.relationship('NewsCategory', backref=db.backref('news_articles', lazy=True))

    def __repr__(self):
        return f"<news_articles {self.article_title}>"


class NewsCategory(db.Model):
    __tablename__ = 'news_category'
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<news_articles {self.category_name}>"


@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', title='Home page')


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='About us')


@app.route('/add-article', methods=['GET', 'POST'])
def add_article():
    print(url_for('add_article'))
    # return redirect(url_for('index'))
    if request.method == 'POST':
        print(request.form['title'])
        print(request.form['post'])
        # try:
        #     posts = NewsArticle(article_title=request.form['title'], article_body=request.form['post'])
        #     db.session.add(posts)  # ссылка на ЭК 'NewsArticle'
        #     print('db.session.add - ok')
        #     # db.session.flush()  # перемещение записи из сессии в табл, но пока все еще в памяти устройства
        #     print('db.session.flush - ok')
        #     db.session.commit()
        #     print('db.session.commit - ok')
        #     flash('Congratulations! You have added an article!', category='success')
        # except:
        #     db.session.rollback()
        #     flash('Error in adding article process', category='error')
    return render_template('add_article.html', title='Add article')


@app.route('/user-registration', methods=['GET', 'POST'])
def user_registration():
    print(url_for('user_registration'))
    if request.method == 'POST':
        # print('POST - ok')
        user = Author.query.filter_by(author_email=request.form['email']).first()
        if user:
            flash('Such user is already exists', category='error')
        else:
            try:
                hash = generate_password_hash(request.form['psw'])
                # print('hash - ok')
                authors = Author(author_name=request.form['name'],
                                 author_email=request.form['email'],
                                 author_password=hash)
                # print('authors - ok')
                db.session.add(authors)  # ссылка на ЭК 'authors'
                # print('db.session.add - ok')
                db.session.flush()  # перемещение записи из сессии в табл, но пока все еще в памяти устройства
                # print('db.session.flush - ok')

                db.session.commit()
                # print('db.session.commit - ok')
                flash('Congratulations! You have been registered!', category='success')
            except:
                db.session.rollback()
                flash('Error in saving process', category='error')
    # if request.method == 'POST':
    #     # print(request.form)
    #     # print(request.form['name'])
    #     if len(request.form['name']) > 2:
    #         flash('Congratulations! Author has been registered!', category='success')
    #     else:
    #         flash('Error in field "name"', category='error')

    return render_template('user_registration.html', title='Registration')
# author_name,author_email ,author_password ,author_date

@app.route('/login', methods=['GET', 'POST'])
def login():
    print(url_for('login'))
    if request.method == 'POST':
        print('POST - ok')
        email = request.form.get('email')
        print(f"email - {email}")
        password = request.form.get('psw')
        print(f"password - {password}")

        author = Author.query.filter_by(author_email=email).first()

        print('Starting checking...')
        if not author or not check_password_hash(author.author_password, request.form['psw']):
            print(f"author_email_db - {author}")
            flash('Please check your login details and try again.', category='error')
            return redirect('login')

        return redirect(url_for('about'))

    # if 'userLogged' in session:
    #     return redirect(url_for('profile', email=session['userLogged']))  # name=session['userLogged']
    # elif request.method == 'POST' and request.form['email'] == 'ivan@gmail.com' and request.form['psw'] == '123':
    #     session['userLogged'] = request.form['email']
    #     return redirect(url_for('profile', email=session['userLogged']))  # name=session['userLogged']

    return render_template('login.html', title='Login')


# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('login'))

@app.route('/profile/<email>')
def profile(email):
    if 'userLogged' not in session or session['userLogged'] != email:
        abort(401)
    return f"Profile (email): {email}"


@app.route('/subscriptions-catalog')
def subscriptions_catalog():
    print(url_for('subscriptions_catalog'))
    return render_template('subscriptions_catalog.html', title='Subscribe')


@app.route('/contacts')
def contacts():
    print(url_for('contacts'))
    return render_template('contacts.html', title='Contacts')


if __name__ == "__main__":
    app.run(debug=True)
