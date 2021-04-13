import os,sys,sqlite3
from PyQt5 import QtWidgets, uic,QtGui,QtCore
from PyQt5.QtCore import QThread,Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QFontDialog,QFileDialog,QMessageBox,QTableWidgetItem,QMenu,QShortcut,QApplication

class ui_handler:
    def __init__(self,parent):
        self.parent = parent
        self.setup_tables_header()
        self.fill_tables()
        self.setup_triggers()

    # Привязка кнопок и сигналов к функциям и командам (в будущем)
    #def setup_triggers(self):


    # РАБОТА С ТАБЛИЦАМИ

    # ЗАПОЛНЕНИЕ ВСЕХ ТАБЛИЦ ПО ОЧЕРЕДИ 
    def fill_tables(self):                                          
        self.parent.db.load_base()                                  
        self.clear_table(self.parent.nazv_table)
        self.fill_nazv()


    # ОЧИСТКА УКАЗАННОЙ ТАБЛИЦЫ
    def clear_table(self,table):            
        while table.rowCount() > 0:         
            table.removeRow(0)              


    # ЗАПОЛНЕНИЕ ТАБЛИЦЫ ОСНОВЫВАЯСЬ НА ПЕРЕДАННЫХ АРГУМЕНАХ
    def fill_data(self,table,append_data):                                              
        cur_row = table.rowCount()                                                      
        table.insertRow(cur_row)                                                        
        for counter in range(len(append_data)):                                         
                table.setItem(cur_row,counter,QTableWidgetItem(append_data[counter]))   


    # ЗАПОЛНЕНИЕ (из таблицы, при наличии более чем 2-х таблиц, число функций будет увеличено)
    def fill_nazv(self):
        for nazv in self.parent.db.nazv:
            append_data = [str(nazv.ID),
                           nazv.Name,nazv.Create,
                           str(cli.Key)]                        
            self.fill_data(self.parent.users_table,append_data) 



    # НАСТРОЙКА ЗАГОЛОВКОВ У ТАБЛИЦ  (Таблицы нужна, на данном этапе, чтобы проверить работоспособность взаимодействий gui и db)
    #def setup_tables_header(self):
        header_list = [[self.parent.nazv_table.horizontalHeader(),3],

        #for header in header_list:
            #for current in range(header[1]):
                #header[0].setSectionResizeMode(current, QtWidgets.QHeaderView.Stretch)

# Требует фикса, из-за ошибок в расчётах взаимодействия таблиц и тач экрана