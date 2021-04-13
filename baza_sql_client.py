import os,sys
#sqlite3
import requests
from baza_objects import *
import datetime


# Клиент - это только графическое отображение для базы
# Данный файл содержит класс для работы с базой данных     
# Загрузка данных в переменные по объектам из baza_objects  


class data_base:
    def __init__(self):
        #self.data_base  = sqlite3.connect("data.db")
        self.clear_variables()


    # Переменные для хранения данных из базы 
    def clear_variables(self):
        self.Nazv      = list()


    # Функция загрузки данных из бд (будет доработанна, примерный прототип)
    def load_nazv(self):
        request = requests.get("http://localhost/SELECT * FROM Nazv")
        resp = request.text[:-1].split("\n")
        print(resp)
        for nazv_line in resp:
            nazv_line = nazv_line.split(";")
            temp_nazv            = Nazv()
            temp_nazv.ID         = nazv_line[0]
            temp_nazv.Name     = self.get_nazv(nazv_line[1])
            temp_nazv.Create      = self.get_nazv(nazv_line[2])
            temp_nazv.Vid       = self.get_nazv(nazv_line[3])
            temp_nazv.Release       = nazv_line[4]
            self.nazv.append(temp_ren)


    # Фукнции получения объекта по ID (так жу будет доработанна до версию со сканером QR)

    def get_nazv(self,nazv_id):
        for nazv in self.naz:
            if nazv_id == nazv.ID:
                return nazv




    def load_base(self):
        self.clear_variables()
        self.load_nazv()

if __name__ == "__main__":
    print("debug")
    db=data_base()
    db.load_base()
