import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys

top = 400
left = 400
width = 500
height = 500

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        w=uic.loadUi("qtDesign.ui", self)
        self.db=0
        w.actionSet_connection.triggered.connect(self.getConnectionDB)
        w.actionClose_connection.triggered.connect(self.closeConnectionDB)
        w.pushButton.clicked.connect(self.button1Select)
        w.pushButton_3.clicked.connect(self.button2Select)
        w.pushButton_4.clicked.connect(self.button3Select)
        w.comboBox.currentTextChanged.connect(self.selectCombo)
    def addTableRow(self,table, row_data):
        row = table.rowCount()
        table.setRowCount(row + 1)
        col = 0
        for item in row_data:
            cell = QTableWidgetItem(str(item))
            table.setItem(row, col, cell)
            col += 1

    def getConnectionDB(self):
        print("rrrr")
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE if not exists stocks
                             (name text, id text, age number, country text)''')
        purchases = [('Tany', '1', 23,'Russia'),
                     ('Maksim', '2', 23, 'USA'),
                     ('Dasha', '3', 24, 'China' ),
                     ('Krubs', '4', 100, 'Germany')]
        if (c.execute('SELECT count(*) FROM stocks').fetchall()[0][0] == 0):
            c.executemany('INSERT INTO stocks VALUES (?,?,?,?)', purchases)
            conn.commit()
        data = c.execute('SELECT * FROM stocks').fetchall()

        info_table = c.execute('PRAGMA table_info(stocks)').fetchall()
        window.tableWidget.setColumnCount(len(info_table))
        columnsName = []
        for row in info_table:
            columnsName.append(row[1])
        window.tableWidget.rowCount()
        window.tableWidget.setHorizontalHeaderLabels(columnsName)

        if window.tableWidget.rowCount() == 0:
            for row in data:
                self.addTableRow(window.tableWidget, row)

        window.tabWidget.setCurrentIndex(0)
        self.db = conn
    def closeConnectionDB(self):
        if self.db != 0:
            while (window.tableWidget.rowCount() > 0):
                window.tableWidget.removeRow(0)
            window.tableWidget.setColumnCount(0)

            while (window.tableWidget_2.rowCount() > 0):
                window.tableWidget_2.removeRow(0)
            window.tableWidget_2.setColumnCount(0)

            while (window.tableWidget_3.rowCount() > 0):
                window.tableWidget_3.removeRow(0)
            window.tableWidget_3.setColumnCount(0)

            while (window.tableWidget_4.rowCount() > 0):
                window.tableWidget_4.removeRow(0)
            window.tableWidget_4.setColumnCount(0)

            while (window.tableWidget_5.rowCount() > 0):
                window.tableWidget_5.removeRow(0)
            window.tableWidget_5.setColumnCount(0)

            self.db.close()
            self.db = 0
    def button1Select(self):
        data = self.db.cursor().execute('SELECT name FROM stocks').fetchall()

        window.tableWidget_2.setColumnCount(1)
        columnsName = ['name']
        window.tableWidget_2.rowCount()
        window.tableWidget_2.setHorizontalHeaderLabels(columnsName)

        if window.tableWidget_2.rowCount() == 0:
            for row in data:
                self.addTableRow(window.tableWidget_2, row)
        window.tabWidget.setCurrentIndex(1)
    def button2Select(self):
        if self.db != 0:
            data = self.db.cursor().execute('SELECT * FROM stocks').fetchall()

            info_table = self.db.cursor().execute('PRAGMA table_info(stocks)').fetchall()
            window.tableWidget_4.setColumnCount(len(info_table))
            columnsName = []
            for row in info_table:
                columnsName.append(row[1])
            window.tableWidget_4.rowCount()
            window.tableWidget_4.setHorizontalHeaderLabels(columnsName)

            if window.tableWidget_4.rowCount() == 0:
                for row in data:
                    self.addTableRow(window.tableWidget_4, row)

            window.tabWidget.setCurrentIndex(3)

    def button3Select(self):
        if self.db != 0:
            data = self.db.cursor().execute('SELECT * FROM stocks').fetchall()

            info_table = self.db.cursor().execute('PRAGMA table_info(stocks)').fetchall()
            window.tableWidget_5.setColumnCount(len(info_table))
            columnsName = []
            for row in info_table:
                columnsName.append(row[1])
            window.tableWidget_5.rowCount()
            window.tableWidget_5.setHorizontalHeaderLabels(columnsName)

            if window.tableWidget_5.rowCount() == 0:
                for row in data:
                    self.addTableRow(window.tableWidget_5, row)

            window.tabWidget.setCurrentIndex(4)
    def selectCombo(self, val):
        if self.db != 0:
                data = self.db.cursor().execute('SELECT ' + val + ' FROM stocks').fetchall()

                window.tableWidget_3.setColumnCount(1)
                columnsName = [val]
                window.tableWidget_3.rowCount()
                window.tableWidget_3.setHorizontalHeaderLabels(columnsName)

                while (window.tableWidget_3.rowCount() > 0):
                    window.tableWidget_3.removeRow(0)

                for row in data:
                    self.addTableRow(window.tableWidget_3, row)
        else:
            while (window.tableWidget_3.rowCount() > 0):
                window.tableWidget_3.removeRow(0)
        window.tabWidget.setCurrentIndex(2)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()