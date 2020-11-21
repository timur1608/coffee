import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QTableWidgetItem


class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()
        result = self.cur.execute('''SELECT * FROM [coffee]''').fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        for i, name in enumerate(['Id', 'name', 'level', 'type', 'description', 'price', 'size']):
            item = QTableWidgetItem()
            item.setText(name)
            self.tableWidget.setHorizontalHeaderItem(i, item)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
