from http.server import BaseHTTPRequestHandler, HTTPServer
import os,sys,sqlite3
# Не полный пример сервера с использованием sqlite3, позже работа с sqlite будет заменена на более лучший аналог (по типу Lite DB, но это не точно)
# Был в надежде его переделать, после первых тестов с db, но пока не дошли руки
class HttpProcessor(BaseHTTPRequestHandler):
    def _resp(self,code):
        self.send_response(code)
        self.send_header(b'content-type','text/html')     # ('Content-type', 'text/html; charset=UTF-8')
        self.end_headers()
                                
    def do_UPDATE(self,executable):
        cursor = data_base.cursor()
        cursor.execute(executable)
        data_base.commit()
                
    def do_GET(self):
        self._resp(200) #404
        text1 = self.path
        text1=text1[1:]
        text1=text1.replace("%20"," ")
        translate = {"%D0%90":"А","%D0%B0":"а",
                     "%D0%91":"Б","%D0%B1":"б",
                     "%D0%92":"В","%D0%B2":"в",
                     "%D0%93":"Г","%D0%B3":"г",
                     "%D0%94":"Д","%D0%B4":"д",
                     "%D0%95":"Е","%D0%B5":"е",
                     "%D0%81":"Ё","%D1%91":"ё",
                     "%D0%96":"Ж","%D0%B6":"ж",
                     "%D0%97":"З","%D0%B7":"з",
                     "%D0%98":"И","%D0%B8":"и",
                     "%D0%99":"Й","%D0%B9":"й",
                     "%D0%9A":"К","%D0%BA":"к",
                     "%D0%9B":"Л","%D0%BB":"л",
                     "%D0%9C":"М","%D0%BC":"м",
                     "%D0%9D":"Н","%D0%BD":"н",
                     "%D0%9E":"О","%D0%BE":"о",
                     "%D0%9F":"П","%D0%BF":"п",
                     "%D0%A0":"Р","%D1%80":"р",
                     "%D0%A1":"С","%D1%81":"с",
                     "%D0%A2":"Т","%D1%82":"т",
                     "%D0%A3":"У","%D1%83":"у",
                     "%D0%A4":"Ф","%D1%84":"ф",
                     "%D0%A5":"Х","%D1%85":"х",
                     "%D0%A6":"Ц","%D1%86":"ц",
                     "%D0%A7":"Ч","%D1%87":"ч",
                     "%D0%A8":"Ш","%D1%88":"ш",
                     "%D0%A9":"Щ","%D1%89":"щ",
                     "%D0%AA":"Ъ","%D1%8A":"ъ",
                     "%D0%AB":"Ы","%D1%8B":"ы",
                     "%D0%AC":"Ь","%D1%8C":"ь",
                     "%D0%AD":"Э","%D1%8D":"э",
                     "%D0%AE":"Ю","%D1%8E":"ю",
                     "%D0%AF":"Я","%D1%8F":"я"}
                
        for letters in translate:
            text1=text1.replace(letters, translate[letters])
        if "SELECT" in self.path:
            self.do_SELECT(text1)
        elif "INSERT" in self.path:
            self.do_INSERT(text1)
        elif "DELETE" in self.path:
            self.do_DELETE(text1)

if __name__ == "__main__":
    serv = HTTPServer(("localhost",8080),HttpProcessor)
    data_base  = sqlite3.connect("data.db")
    serv.serve_forever()
