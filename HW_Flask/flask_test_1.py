import os  # работа с файловой системой
import sqlite3  # система упр БД
from flask_login import LoginManager  # управление процессом авторизации

from flask import Flask, render_template, url_for, request, flash, abort, session, g, redirect
# from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash

from FDataBase import *  # FDataBase
from UserLogin import *  # UserLogin

DATABASE = '/tmp/flsite.db'  # путь к нашей БД
DEBUG = True
SECRET_KEY = 'KASHDBJKQHBE12B31JHB4JNASKDJNdfssfegvc#'

app = Flask(__name__)  # __name__ - имя нашего приложения / файла
# app.config["SECRET_KEY"] = "KASHDBJKQHBE12B31JHB4JNASKDJNdfssfegvc#"
# загружаем конфигурацию (переменные большими буквами) из нашего приложения:
# директива __name__, которая будет ссылаться на этот текущий модуль
# config - определяет начальную конфигурацию нашего приложения
app.config.from_object(__name__)
# далее мы переопределим путь к БД нашего приложения
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    print("load_user")
    return UserLogin().from_db(user_id, dbase)

menu = [
    {"name": "Установка", "url": "install-flask"},
    {"name": "Первое приложение", "url": "first-app"},
    {"name": "Обратная связь", "url": "contact"},
    {"name": "О нас", "url": "about"},
    {"name": "Логин", "url": "login"}]

def connect_db():
    """функция для установления соединения с БД"""
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row  # записи будут представлены не в виде кортежа, а в виде словаря
    return conn  # возврат установленного соединения


def create_db():
    """
    это функция создает БД без запуска веб сервера
    это вспомогательная функция для создания таблиц в БД
    """
    # вызываем функцию, которую объявили выше для установления соединения с БД:
    db = connect_db()
    # далее используем менеджер контекста (with), для запуска файла на чтение (mode='r') с SQL скриптами (sq_db.sql)
    # по созданию таблиц:
    with app.open_resource('sq_db.sql', mode='r') as f:
        # Далее мы обращаемся к классу "cursor",
        # т.е. мы берем из установленного соединения с БД ("db = connect_db()") класс "cursor"
        # и через этот класс выполняем след. метод "executescript(f.read())":
        db.cursor().executescript(f.read())  # т.е. это команда запускает скрипты из читаемого файла
    # Затем мы должны записать все изменения в БД:
    db.commit()
    # и затем закрыть соединение:
    db.close()


def get_db():
    """
    Соединение с БД, если оно еще не установлено
    Когда приходит запрос - создается контекст приложения и в этом контексте приложения
    есть такая глобальная переменная "g", в которую мы можем 
    записывать любую пользовательскую информацию.
    
    В нашем случае мы запишем след информацию - установление соединения с БД
    """
    # делам это след обр-м:
    # проверям: существует ли у объекта "g" свойство "link_db",
    # т.е. если существует, то соединение с БД уже было установлено и
    # нам нужно его просто возвратить: >>> return g.link_db
    # иначе вызываем прописанную нам функцию для установки соединения с БД
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
        return g.link_db

# НО КАК ЗАКРЫТЬ/РАЗОРВАТЬ СОЕДИНЕНИЯ ПОСЛЕ ТОГО КАК ЗАПРОС ПОЛЬЗОВАТЕЛЯ ЗАВЕРШЕН?
# для этого во фласк есть след декоратор: @app.teardown_appcontext
# он срабатывает тогда, когда происходит уничтожение контекста приложения
# А ЭТО ОБЫЧНО ПРОИСХОДИТ  в момент завершения обработки запроса
# в итоге: пропишем следующий обработчик для завершения соединения с базой данных:
@app.teardown_appcontext
def close_db(error):  # error - передаем этот параметр и в нем это будет фигурировать
    """Закрываем соединение с БД, если оно было установлено"""
    if hasattr(g, 'link_db'):
        g.link_db.close()
#
#
#
dbase = None
@app.before_request
def before_request():
    """Установка соединения перед выполнением запроса"""
    global dbase
    db = get_db()
    dbase = FDataBase(db)

@app.route("/")
def index():
    # index - имя функции; вызывается в контексте обработчика запроса - функции запроса (def index)
    print(url_for("index"))
    # db = get_db()
    # dbase = FDataBase(db)
    return render_template("index.html", menu=dbase.get_menu(), posts=dbase.get_posts_anonce())


@app.route("/add-post", methods=['GET', 'POST'])
def add_post():
    print(url_for("add_post"))
    # db = get_db()
    # dbase = FDataBase(db)

    if request.method == "POST":  # если данные пришли по пост запросу
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.add_post_in_db(request.form['name'], request.form['post'], request.form['url'])
            if not res:
                flash('Ошибка добавления статьи', category='error')
            else:
                flash('Статья успешно добавлена', category='success')
        else:
            flash('Ошибка добавления статьи', category='error')

    return render_template("add_post.html", title="Добавить статью", menu=dbase.get_menu())


# @app.route("/post/<int:id_post>")  # через id
@app.route("/post/<alias>")  # через url
def show_post(alias):
    # db = get_db()
    # dbase = FDataBase(db)
    title, post = dbase.get_post_from_db(alias)
    if not title:
        abort(404)

    return render_template('post.html', menu=dbase.get_menu(), title=title, post=post)


@app.route("/about")
def about():
    print(url_for("about"))  # about - имя функции
    return render_template("about.html", title="О сайте", menu=menu)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        if len(request.form["username"]) > 2:
            flash("Сообщение отправлено", category="success")
        else:
            flash("Ошибка отправки", category="error")
        print(request.form)  # так можем брать данные из формы
        print(f"username: {request.form['username']}")
    return render_template("contact.html", title="contact", menu=menu)


# path: - это конвертер и он говорит о том, что все,
# что указано после "profile" нужно поместить в переменную "username"
# int: - это конвертер; должны присутствовать только цифры
# float: - это конвертер; числа с плавающей точкой
# path: - это конвертер; любые допустимые символы URL плюс символ "/"
# @app.route("/profile/<int:username>/<path>")
# def profile(username, path):
#     return f"Пользователь: {username}, {path}"
@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f"Профиль пользователя: {username}"


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if 'userLogged' in session:
#         print(url_for("login"))
#         print(url_for("profile"))
#         print('1')
#         return redirect(url_for("profile", username=session["userLogged"]))
#     elif request.method == ["POST"] and request.form["username"] == "ivan" and request.form["psw"] == 'qqq':
#         print(url_for("login"))
#         print(url_for("profile"))
#         print('2')
#         session['userLogged'] = request.form["username"]
#         return redirect(url_for("profile", username=session["userLogged"]))
#     # if request.method == ["POST"]:
#     #     print(f"{request.form['username']}")
#     #     print(f"{request.form['psw']}")
#     #     return redirect(url_for("profile"))
#     print('/login')
#     return render_template("login.html", title="Авторизация", menu=menu)


@app.errorhandler(404)
def pagenotfound(error):  # error - передается ошибка сервера
    return render_template('page404.html', title="Страница не найдена")
# если у нас есть необходимость в том, чтобы сервер возвращал не код "200"
# который мы получаем, если наш обработчик (handler) обработал ошибку "404",
# а код 404, то нам нужно просто через запятую указать "404"
# return render_template('page404.html', title="Страница не найдена"), 404

@app.route("/login")
def login():
    return render_template("login2.html", menu=dbase.get_menu(), title="Авторизация")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['email']) > 4 \
            and len(request.form['psw']) > 4 and request.form['psw'] == request.form['psw2']:
            hash = generate_password_hash(request.form['psw'])
            res = dbase.add_user(request.form['name'], request.form['email'], hash)
            if res:
                flash("Вы успешно зарегестрированы", "success")
                return redirect(url_for('login'))
            else:
                flash("Ошибка при добавлении в базу данных", "error")
        else:
            flash("Неверно заполнены поля", "error")

    return render_template("register.html", menu=dbase.get_menu(), title="Регистрация")


# -------------------------------------------------------------------------
# когда мы запускаем лок веб сервер name принимает значение main
# на удаленном сервере main писать не надо, надо писать имя файла


if __name__ == "__main__":
    app.run(debug=True)  # запуск локального вебсервера

# Если нам необходимо осуществить проверку функции url_for для разных обработчиков
# Фреймворк Flask позволяет нам это сделать искусственно БЕЗ АКТИВАЦИИ ВЕБ СЕРВЕРА:
# комменитруем след строки:
# if __name__ == "__main__":
#     app.run(debug=True)  # запуск локального вебсервера

# вместо них пишем:
# with - менеджер контекста
# test_request_context - создаем тестовый контекст запроса
# with app.test_request_context():
#     print(url_for("index"))
#     print(url_for("about"))
#     print(url_for("profile", username="123abcd"))
