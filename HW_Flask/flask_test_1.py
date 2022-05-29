from flask import Flask, render_template

app = Flask(__name__)  # __name__ - имя нашего приложения / файла

menu = ["Установка", "Первое приложение", "Обратная связь"]


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html", menu=menu)


@app.route("/about")
def about():
    return render_template("about.html", title="О сайте", menu=menu)


@app.route("/contact")
def contact():
    return render_template("contact.html", title="contact", menu=menu)

# когда мы запускаем лок веб сервер name принимает значение main
# на удаленном сервере main писать не надо, надо писать имя файла
if __name__ == "__main__":
    app.run(debug=True)  # запуск локального вебсервера
