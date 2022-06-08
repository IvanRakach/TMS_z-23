import os  # library for work file system
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# configuration
DATABASE = '/tmp/news_app.db'  # path to our DB


app = Flask(__name__)  # создаем экзампляр приложения
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news_app.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/news_app.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/news_app.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://user:password@127.0.0.1:1521/news_app.db'

# создадим ЭК SQLAlchemy ('db') через который и осуществляется работа с БД посредством передачи ссылки
# на наше приложение 'app'
db = SQLAlchemy(app)


class Users(db.Model):
    """Defining table in 'news_app' DB"""
    id = db.Column(db.Integer, primary_key=True)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'news_app.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='admin'
))













if __name__ == "__main__":
    app.run(debug=True)