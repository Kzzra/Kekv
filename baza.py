from baza_sql_client import *
from baza_ui_handler import *


# Этот основной файл создан для запуска интерфейса


class ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(ui, self).__init__()
        uic.loadUi('interface.ui', self)    # Загружаем файл.
        self.db = data_base()               # Загружаем базу.
        self.show()                         # Показываем наш GUI (Графический интерфейс пользователя)
        self.uih = ui_handler(self)         # Загружаем обработчик кнопок\интерфейса
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ui()
    app.exec_()
