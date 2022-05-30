from flask import Flask, render_template, url_for

app = Flask(__name__)  # __name__ - имя нашего приложения / файла

menu = ["Установка", "Первое приложение", "Обратная связь"]


@app.route("/index")
@app.route("/")
def index():
    # index - имя функции; вызывается в контексте обработчика запроса - функции запроса (def index)
    print(url_for("index"))
    return render_template("index.html", menu=menu)


@app.route("/about")
def about():
    print(url_for("about"))  # about - имя функции
    return render_template("about.html", title="О сайте", menu=menu)


@app.route("/contact")
def contact():
    return render_template("contact.html", title="contact", menu=menu)


@app.route("/profile/<username>")
# path: - это конвертер и он говорит о том, что все,
# что указано после "profile" нужно поместить в переменную "username"
# int: - это конвертер; должны присутствовать только цифры
# float: - это конвертер; числа с плавающей точкой
# path: - это конвертер; любые допустимые символы URL плюс символ "/"
# @app.route("/profile/<int:username>/<path>")
# def profile(username, path):
#     return f"Пользователь: {username}, {path}"
def profile(username):
    return f"Пользователь: {username}"


# когда мы запускаем лок веб сервер name принимает значение main
# на удаленном сервере main писать не надо, надо писать имя файла

# if __name__ == "__main__":
#     app.run(debug=True)  # запуск локального вебсервера



# Если нам необходимо осуществить проверку функции url_for для разных обработчиков
# Фреймворк Flask позволяет нам это сделать искусственно БЕЗ АКТИВАЦИИ ВЕБ СЕРВЕРА:
# комменитруем след строки:
# if __name__ == "__main__":
#     app.run(debug=True)  # запуск локального вебсервера

# вместо них пишем:
# with - менеджер контекста
# test_request_context - создаем тестовый контекст запроса
with app.test_request_context():
    print(url_for("index"))
    print(url_for("about"))
    print(url_for("profile", username="123abcd"))
