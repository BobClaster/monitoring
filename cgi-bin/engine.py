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
        self.name_db = 'metheo_station'
        self.__connect_to_db(self.name_db)
        # self.__create_table_in_db()
        self.__close_db()

    def __connect_to_db(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor_db = self.conn.cursor()

    def __create_table_in_db(self):
        sql_stmt = '''CREATE TABLE light (id INTEGER PRIMARY KEY AUTOINCREMENT, lux INTEGER, date DATETIME)'''
        self.cursor_db.execute(sql_stmt)
        sql_stmt = '''CREATE TABLE humidity (id INTEGER PRIMARY KEY AUTOINCREMENT, hum BYTE)'''
        self.cursor_db.execute(sql_stmt)
        sql_stmt = '''CREATE TABLE temperature (id INTEGER PRIMARY KEY AUTOINCREMENT, temp BYTE)'''
        self.cursor_db.execute(sql_stmt)


    def __close_db(self):
        self.cursor_db.close()
        self.conn.close()        


    def _add_meas_ligth(self, lux, date):
        self.__connect_to_db(self.name_db)
        sql_stmt = '''INSERT INTO light (lux, date) 
                      VALUES (?, ?)'''
        self.cursor_db.execute(sql_stmt, (lux, date))
        self.conn.commit()
        self.__close_db()
    

    def _add_meas_humi(self, hum):
        self.__connect_to_db(self.name_db)
        sql_stmt = '''INSERT INTO humidity (hum) 
                      VALUES (?)'''
        self.cursor_db.execute(sql_stmt, (hum,))
        self.conn.commit()
        self.__close_db()
    

    def _add_meas_temp(self, temp):
        self.__connect_to_db(self.name_db)
        sql_stmt = '''INSERT INTO temperature (temp) 
                      VALUES (?)'''
        self.cursor_db.execute(sql_stmt, (temp,))
        self.conn.commit()
        self.__close_db()

    
    def add_record(self, lux, hum, temp):
        self._add_meas_ligth(lux, datetime.datetime.now())
        self._add_meas_humi(hum)
        self._add_meas_temp(temp)
        

    
    def get_all_records(self):
        self.__connect_to_db(self.name_db)
        sql_stmt = '''SELECT light.date, light.lux, hum.hum, temp.temp
                      FROM main.light light, main.humidity hum, main.temperature temp
                      WHERE light.id = hum.id AND light.id = temp.id'''
        self.cursor_db.execute(sql_stmt)
        return self.cursor_db.fetchall()


    # def get_article(self, id):
    #     self.__connect_to_db(self.name_db)
    #     sql_stmt = '''SELECT oper.id, oper.operator, ex.text, descr.text
    #                   FROM main.operators oper, main.example ex, main.description descr
    #                   WHERE oper.id = (?) AND ex.id = oper.id AND descr.id = oper.id'''
    #     self.cursor_db.execute(sql_stmt, (id,))
    #     self.conn.commit()
    #     self.__close_db()
        

    def delete_record(self, id):
        self.__connect_to_db(self.name_db)
        sql_stmt = '''DELETE FROM main.light
                      WHERE main.light.id = ?'''
        self.cursor_db.execute(sql_stmt, (id,))
        self.conn.commit()

        sql_stmt = '''DELETE FROM main.humidity
                      WHERE main.humidity.id = ?'''
        self.cursor_db.execute(sql_stmt, (id,))
        self.conn.commit()

        sql_stmt = '''DELETE FROM main.temperature 
                      WHERE main.temperature.id = ?'''
        self.cursor_db.execute(sql_stmt, (id,))
        self.conn.commit()

        self.__close_db()


    # def search_operators(self, query):
    #     self.__connect_to_db(self.name_db)
    #     sql_stmt = '''SELECT oper.id, oper.operator, ex.text, descr.text
    #                   FROM main.operators oper, main.example ex, main.description descr
    #                   WHERE (oper.operator LIKE "%{0}%" OR ex.text LIKE "%{1}%" OR descr.text LIKE "%{2}%") 
    #                   AND oper.id = ex.id AND ex.id = descr.id'''.format(query, query, query)
    #     self.cursor_db.execute(sql_stmt)
    #     return self.cursor_db.fetchall()



class Session:
    def __init__(self):
        self.db = DataBase() 

    def get_all_records(self,):
        return self.db.get_all_records()

    # def get_single_article(self, id):
    #     return self.db.get_article(id)
    
    def add_record(self, lux, hum, temp):
        return self.db.add_record(lux, hum, temp)
    
    def delete_record(self, id):
        self.db.delete_record(id)

    # def search_operators(self, query):
    #     return self.db.search_operators(query)