from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QApplication, QMainWindow
import main

import sys

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Простая программа")
        self.setGeometry(500, 450, 550, 400)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Привет всем людям")
        self.main_text.move(150, 150)
        self.main_text.setFixedWidth(200) # Фиксирует размер объекта 
        self.main_text.adjustSize() # Автоматически выставляет размер объекта

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(150, 200)
        self.btn.setText("Нажми на меня")
        self.btn.adjustSize()
        self.btn.clicked.connect(self.btn_click)

    def btn_click(self):
        print("Нажато")

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()