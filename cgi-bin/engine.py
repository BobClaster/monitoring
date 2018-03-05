import os
import random
import time
import sqlite3
import hashlib
import datetime
from random import choice
from string import ascii_letters
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class DataBase:
    def __init__(self):
        self.name_db = 'monitoring'
        self.__connect_to_db(self.name_db)
        try:
            self.__create_table_in_db
        except:
            pass
        self.__close_db()


    def __connect_to_db(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor_db = self.conn.cursor()


    def __create_table_in_db(self):
        sql_stmt = '''CREATE TABLE monitoring (id INTEGER PRIMARY KEY AUTOINCREMENT, volt FLOAT,
                      amper FLOAT, watt FLOAT, watt_hour FLOAT, dt DATETIME)'''
        self.cursor_db.execute(sql_stmt)


    def __close_db(self):
        self.cursor_db.close()
        self.conn.close()


    def add_record(self, volt, amper, watt, watt_hour):
        self.__connect_to_db(self.name_db)
        sql_stmt = '''INSERT INTO monitoring (volt, amper, watt, watt_hour, dt)
                      VALUES (?, ?, ?, ?, ?)'''
        date = datetime.datetime.now()
        self.cursor_db.execute(sql_stmt, (volt, amper, watt, watt_hour, date))
        self.conn.commit()
        self.__close_db()


    def get_all_records(self):
        self.__connect_to_db(self.name_db)
        sql_stmt = '''SELECT mon.id, mon.volt, mon.amper, mon.watt, mon.watt_hour, mon.dt
                      FROM main.monitoring mon
                      ORDER BY mon.id DESC'''
        self.cursor_db.execute(sql_stmt)
        return self.cursor_db.fetchall()


    def get_last_records(self):
        self.__connect_to_db(self.name_db)
        sql_stmt = '''SELECT mon.volt, mon.amper, mon.watt, mon.watt_hour, mon.dt
                      FROM main.monitoring mon
                      ORDER BY mon.id DESC LIMIT 5'''
        self.cursor_db.execute(sql_stmt)
        return self.cursor_db.fetchall()


    def delete_record(self, id):
        self.__connect_to_db(self.name_db)
        sql_stmt = '''DELETE FROM main.monitoring
                      WHERE main.monitoring.id = ?'''
        self.cursor_db.execute(sql_stmt, (id,))
        self.conn.commit()

        self.__close_db()
