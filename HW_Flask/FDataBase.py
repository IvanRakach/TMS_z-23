import math
import sqlite3
import time


class FDataBase:
    def __init__(self, db):  # db - ссылка на связь с БД
        self.__db = db  # __db - сохраняем ее в ЭК этого класса
        self.__cur = db.cursor()  # __cur - созд ЭК курсора; через ннего мы и работаем с табл из БД

    def get_menu(self):  # в этом методе происходит выборка всех записей из БД из табл menu
        sql = """SELECT * FROM mainmenu"""
        try:  # в этом блоки пытаемся прочитать данные
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except Exception:
            print("Ошибка чтения из БД")
        return []

    # пропишем метод в классе, который будет добавлять данные в таблицу post
    def add_post_in_db(self, title, text, url):
        try:
            self.__cur.execute(f"SELECT COUNT() as 'count' FROM posts WHERE url LIKE '{url}'")
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("Статья с таким url уже существует")
                return False

            # для добавления поста нужно взять время time.time() и
            # вспомогательный модуль math (для округления, поскольку там миллисекунды есть)
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?, ?)", (title, text, url, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления статьи в БД" + str(e))
            return False
        return True

    # пропишем метод в классе, который будет БРАТЬ ДАННЫЕ ИЗ БД
    def get_post_from_db(self, alias):
        try:
            # self.__cur.execute(f"SELECT title, text FROM posts WHERE id = {post_id} LIMIT 1")
            self.__cur.execute(f"SELECT title, text FROM posts WHERE url LIKE '{alias}' LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД " + str(e))

        return (False, False)

    # пропишем метод в классе, который будет БРАТЬ ДАННЫЕ ИЗ БД для ГЛАВНОЙ СТРАНИЦЫ
    def get_posts_anonce(self):
        try:
            self.__cur.execute(f"SELECT id, title, text, url FROM posts ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД " + str(e))

        return []

    def add_user(self, name, email, hpsw):
        try:
            self.__cur.execute(f"SELECT COUNT() as 'count' FROM users WHERE email LIKE '{email}'")
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("Пользователь с таким email уже существует")
                return False

            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO users VALUES(NULL, ?, ?, ?, ?)", (name, email, hpsw, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления пользователя в БД"+str(e))
            return False

        return True

    def get_user_user_login(self, user_id):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE id = '{user_id}'")
            res = self.__cur.fetchone()
            if not res:
                print("Пользователь не найден")
                return False
            return res

        except sqlite3.Error as e:
            print("Ошибка получения данных из БД"+str(e))

        return False
