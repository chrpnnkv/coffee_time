import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


class CoffeeWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.cur = sqlite3.connect('coffee.sqlite').cursor()
        self.names = list(map(lambda x: x[0], self.cur.execute("""select name from coffee""").fetchall()))
        self.sort_name.addItem('Не выбрано')
        self.sort_name.addItems(self.names)
        self.sort_name.currentTextChanged.connect(self.run)

        self.taste.setReadOnly(True)
        self.in_grains.setEnabled(False)
        self.ground.setEnabled(False)
        self.roasting.setEnabled(False)

    def run(self):
        name = self.sort_name.currentText()
        if name == 'Не выбрано':
            self.taste.setPlainText('')
            self.in_grains.setChecked(False)
            self.ground.setChecked(False)
            self.roasting.setValue(0)
            self.price.setText('')
            self.volume.setText('')
        else:
            data = self.cur.execute(f"""select * from coffee where name = '{name}'""").fetchone()
            if data[2] == 'слабая':
                self.roasting.setValue(0)
            elif data[2] == 'средняя':
                self.roasting.setValue(50)
            else:
                self.roasting.setValue(100)
            if data[3] == 'молотый':
                self.ground.setChecked(True)
            else:
                self.in_grains.setChecked(True)
            self.taste.setPlainText(data[4])
            self.price.setText(str(data[5]))
            self.volume.setText(str(data[6]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffeeWidget()
    ex.show()
    sys.exit(app.exec())
