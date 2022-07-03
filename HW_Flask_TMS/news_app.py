from flask import Flask, render_template, redirect, url_for, request, flash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, EmailField
from wtforms.validators import DataRequired, EqualTo, Length, Email
from wtforms.widgets import TextArea

from flask_ckeditor import CKEditor
from flask_ckeditor import CKEditorField

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '1234567890qwerty'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initializing database
db = SQLAlchemy(app)

# Initializing CKEditor
ckeditor = CKEditor(app)

# Flask_login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'sign_in'


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class SignUpForm(FlaskForm):
    """Create Sign Up Form"""
    username = StringField("Username", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password_hash = PasswordField("Password",
                                  validators=[DataRequired(),
                                              EqualTo("password_hash_2", message='Passwords must match!')])
    password_hash_2 = PasswordField("Confirm Password", validators=[DataRequired()])
    agreement = BooleanField("I accept the privacy policy", validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    """Create Login Form"""
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign in')


class AddArticleForm(FlaskForm):
    """Create form for adding, editing and deleting articles"""
    title = StringField("Title", validators=[DataRequired()])
    content = StringField("Content", validators=[DataRequired()], widget=TextArea())
    submit = SubmitField("Publish")
####################################################################################################


@app.route("/", methods=['GET', 'POST'])
def index():
    all_news_query = Posts.query.order_by(Posts.date_posted)
    return render_template('index.html', all_news_query=all_news_query)


@app.route("/article/<int:id>")
def article(id):
    """Creating full article page"""
    post = Posts.query.get_or_404(id)
    return render_template("article.html", post=post)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contacts")
def contacts():
    return render_template('contacts.html')


@app.route("/subscriptions-catalog")
def subscriptions_catalog():
    return render_template('subscriptions_catalog.html')


@app.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    name = None
    form = SignUpForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            hashed_pswrd = generate_password_hash(form.password_hash.data, "sha256")
            new_user = Users(
                username=form.username.data,
                name=form.name.data,
                email=form.email.data,
                password_hash=hashed_pswrd,
                agreement=form.agreement.data,
                remember_me=form.remember_me.data,
            )

            db.session.add(new_user)
            db.session.commit()

            form.username.data = ''
            form.name.data = ''
            form.email.data = ''
            form.password_hash.data = ''
            form.agreement.data = False
            form.remember_me.data = False

            flash('You have signed up!', category='success')
        else:
            flash('User with such Email address already exists!', category='danger')

    our_users = Users.query.order_by(Users.date_added)
    return render_template('sign_up.html', name=name, form=form, our_users=our_users)


@app.route("/sign-in", methods=['GET', 'POST'])
def sign_in():
    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        # if there is a user:
        if user:
            # Check the hash
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                # flash(f"Welcome! {user.username}!", category='success')
                return redirect(url_for('profile'))
            else:
                flash('Wrong password! Please try again...', category='danger')
        else:
            flash("That user doesn't exist! Please try again...", category='danger')

    return render_template('sign_in.html', form=form)


@app.route("/logout", methods=['GET', 'POST'])
@login_required
def sign_out():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for('sign_in'))


@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html')


@app.route("/add-article", methods=['GET', 'POST'])
@login_required
def article_add():
    form = AddArticleForm()

    if form.validate_on_submit():
        poster = current_user.id
        post = Posts(title=form.title.data, content=form.content.data, poster_id=poster)

        db.session.add(post)
        db.session.commit()

        form.title.data = ''
        form.content.data = ''

        flash('Article have been successfully added!', category='success')

    return render_template('article_add.html', form=form)


@app.route("/article/edit/<int:id>", methods=['GET', 'POST'])
@login_required
def article_edit(id):
    post = Posts.query.get_or_404(id)
    form = AddArticleForm()

    if form.validate_on_submit():
        post.title = form.title.data
        # post.author = form.author.data
        # post.slug = form.slug.data
        post.content = form.content.data

        # Update Database
        db.session.add(post)
        db.session.commit()
        flash("Article has been updated!", category="success")

        return redirect(url_for('article', id=post.id))

    if current_user.id == post.poster_id:
        form.title.data = post.title
        # form.author.data = post.author
        # form.slug.data = post.slug
        form.content.data = post.content

        return render_template("article_edit.html", form=form)
    else:
        flash("You aren't authorized to edit this post", category="warning")
        all_news_query = Posts.query.order_by(Posts.date_posted)
        return render_template('index.html', all_news_query=all_news_query)


@app.route('/article/delete/<int:id>')
@login_required
def article_delete(id):
    post_to_delete = Posts.query.get_or_404(id)
    id = current_user.id
    if id == post_to_delete.poster.id:

        try:
            db.session.delete(post_to_delete)
            db.session.commit()

            # Return a message
            flash('Blog post has been deleted', category="success")

            # Grab all the posts from database
            all_news_query = Posts.query.order_by(Posts.date_posted)
            return render_template('index.html', all_news_query=all_news_query)

        except:
            # Return an error message
            flash('whoops! There was a problem deleting post... Try again...', category="warning")

            # Grab all the posts from database
            all_news_query = Posts.query.order_by(Posts.date_posted)
            return render_template('index.html', all_news_query=all_news_query)

    else:
        # Return a message
        flash("You aren't authorized to delete that post", category="warning")

        # Grab all the posts from database
        all_news_query = Posts.query.order_by(Posts.date_posted)
        return render_template('index.html', all_news_query=all_news_query)


#######################################################################################################################
class Posts(db.Model):
    __tablename__ = 'news_app_posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    author = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    # slug = db.Column(db.String(255))
    # Foreign key to Link users (refer to primary key of the user)
    poster_id = db.Column(db.Integer, db.ForeignKey('news_app_user.id'))


@app.template_filter("datetimeformat")
def datetimeformat(value, format="%d.%m.%Y %H:%M"):
    """Changing date format in html doc using Jinja2"""
    return value.strftime(format)
# app.jinja_env.filters['datetimeformat'] = datetimeformat


class Users(db.Model, UserMixin):
    __tablename__ = 'news_app_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    # Do some password stuff
    password_hash = db.Column(db.String(128))
    agreement = db.Column(db.Boolean, default=False, nullable=False)
    remember_me = db.Column(db.Boolean, default=False, nullable=False)
    # User can have many posts
    posts = db.relationship('Posts', backref='poster')

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute!')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Create a string
    def __repr__(self):
        return f'<Name{self.name}>'


if __name__ == '__main__':
    app.run(debug=True)
