import os,sys,sqlite3
from baza_objects import *
import datetime


# Данный файл содержит класс для работы с базой данных
# Загрузка данных в переменные по объектам из baza_objects


class data_base:
    def __init__(self):
        self.data_base  = sqlite3.connect("data.db")  # , encoding='utf-8')
        self.clear_variables()


    # Переменные для хранения данных из базы
    def clear_variables(self):                          
        self.nazv      = list()


    def sql_del_nazv(self,nazv_id):
        cursor = self.data_base.cursor()                                                                            
        cursor.execute("DELETE FROM Nazv WHERE ID={}".format(nazv_id))
        self.data_base.commit()

    # Функция загрузки из базы * (любое название, в нашем случае "Nazv")
    def load_nazv(self):
        cursor = self.data_base.cursor()
        cursor.execute("SELECT * FROM Nazv")
        print(cursor.fetchall())
        for nazv_line in cursor.fetchall():
            temp_nazv                = Nazv()
            temp_nazv.ID             = nazv_line[0]
            temp_nazv.Name         = self.get_name(nazv_line[1])
            temp_nazv.Create          = self.get_create(nazv_line[2])
            temp_nazv.Vid           = self.get_vid(nazv_line[3])
            temp_nazv.Release           = ren_line[4]
            self.rents.append(temp_nazv)



    # Фукнции получения объекта по ID

    def get_nazv(self,nazv_id):
        for nazv in self.nazv:
            if nazv_id == nazv.ID:
                return nazv
                                                                                                                          

                                                                                                                 


    def load_base(self):
        self.clear_variables()
        self.load_nazv()
