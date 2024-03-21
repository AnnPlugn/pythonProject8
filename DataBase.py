
import pymysql.cursors
import tkinter.messagebox
class DataBase:
    def __init__(self, db, tb):
        self.name_db = db
        self.name_tb = tb

    def check_db(self):
        try:
            conn = pymysql.connect(host="localhost",
                                   user="root",
                                   password="root",
                                   database=self.name_db,
                                   cursorclass=pymysql.cursors.Cursor)
            print("Вы подключились")
            tkinter.messagebox.showinfo("Вы подключились", self.name_db)
        except pymysql.err.MySQLError:
            conn = pymysql.connect(host="localhost",
                                   user="root",
                                   password="root",
                                   cursorclass=pymysql.cursors.Cursor)

            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.name_db}")
            print("Вы создали БД")
            tkinter.messagebox.showinfo("Вы создали БД", self.name_db)
        return conn

    def con_db(self):
        return pymysql.connect(host="localhost",
                               user="root",
                               password="root",
                               database=self.name_db,
                               cursorclass=pymysql.cursors.Cursor)

    def check_table(self):
        connection = self.con_db()
        cursor = connection.cursor()
        try:
            cursor.execute(f"SELECT * FROM {self.name_db}")
            print("Таблица подключена")
            tkinter.messagebox.showinfo("Таблица подключена", self.name_tb)
        except pymysql.err.MySQLError:

            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {self.name_tb} (id bigint NOT NULL AUTO_INCREMENT,"
                f" list varchar(1000) NOT NULL,"
                f" glasn int NOT NULL,"
                f" sogl int NOT NULL,"
                f" f_20 varchar(1000) NOT NULL,"
                f" last_15 varchar(1000) NOT NULL,"
                f" PRIMARY KEY (id)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;")
        connection.commit()
        print("Таблица создана и подключена")
        tkinter.messagebox.showinfo("Таблица создана и подключена", self.name_tb)
        return

    def list_tb(self):
        connection = self.con_db()
        cursor = connection.cursor()
        tb_in_db = "SHOW TABLES;"
        cursor.execute(tb_in_db)
        tables = cursor.fetchall()

        table_list = [table[0] for table in tables]
        table_list_str = "\n".join(table_list)

        tkinter.messagebox.showinfo("Список таблиц", table_list_str)


