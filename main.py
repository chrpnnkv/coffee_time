import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup


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

        self.edit.clicked.connect(self.edit_form)

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

    def edit_form(self):
        self.new_form = EditWidget(self)
        self.new_form.show()


class EditWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.parent = parent

        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()
        self.ids = list(map(lambda x: str(x[0]), self.cur.execute("""select id from coffee""").fetchall()))
        self.id.addItem('0')
        self.id.addItems(self.ids)
        self.id.currentTextChanged.connect(self.run)
        self.data = []
        self.save.clicked.connect(self.update_db)
        self.edit_bttns = QButtonGroup()
        self.edit_bttns.addButton(self.in_grains_edit)
        self.edit_bttns.addButton(self.ground_edit)

        self.add.clicked.connect(self.add_db)
        self.add_bttns = QButtonGroup()
        self.add_bttns.addButton(self.in_grains)
        self.add_bttns.addButton(self.ground)

    def run(self):
        id = self.id.currentText()
        if id != '0':
            self.data = self.cur.execute(f"""select * from coffee where id = {id}""").fetchone()
            self.sort_name_edit.setText(self.data[1])
            if self.data[2] == 'слабая':
                self.roasting_edit.setValue(0)
            elif self.data[2] == 'средняя':
                self.roasting_edit.setValue(50)
            else:
                self.roasting_edit.setValue(100)
            if self.data[3] == 'молотый':
                self.ground_edit.setChecked(True)
            else:
                self.in_grains_edit.setChecked(True)
            self.taste_edit.setPlainText(self.data[4])
            self.price_edit.setText(str(self.data[5]))
            self.volume_edit.setText(str(self.data[6]))
        else:
            self.taste_edit.setPlainText('')
            self.in_grains_edit.setChecked(False)
            self.ground_edit.setChecked(False)
            self.roasting_edit.setValue(0)
            self.price_edit.setText('')
            self.volume_edit.setText('')
            self.data = []

    def update_db(self):
        new_data = []
        if self.data:
            new_data.append(self.data[0])
            new_data.append(self.sort_name_edit.text() if self.sort_name_edit.text() else self.data[1])
            if self.roasting_edit.value() < 26:
                new_data.append('слабая')
            else:
                new_data.append('темная' if self.roasting_edit.value() > 74 else 'средняя')
            new_data.append('в зернах' if self.in_grains_edit.isChecked() else 'молотый')
            new_data.append(self.taste_edit.toPlainText())
            new_data.append(self.price_edit.text() if self.price_edit.text() else self.data[5])
            new_data.append(self.volume_edit.text() if self.volume_edit.text() else self.data[6])
            self.cur.execute(f"""delete from coffee where id = {self.data[0]}""")
            self.cur.execute(f"""insert into coffee values(?, ?, ?, ?, ?, ?, ?)""", new_data)
            self.con.commit()

    def add_db(self):
        self.error.setText('')
        new_data = [len(self.ids) + 1]
        if self.sort_name.text():
            new_data.append(self.sort_name.text())
            self.error.setText('')
            if self.roasting.value() < 26:
                new_data.append('слабая')
            else:
                new_data.append('темная' if self.roasting.value() > 74 else 'средняя')
            if self.in_grains.isChecked() or self.ground.isChecked():
                new_data.append('в зернах' if self.in_grains.isChecked() else 'молотый')
                new_data.append(self.taste_edit.toPlainText())
                if self.price.text():
                    self.error.setText('')
                    new_data.append(self.price.text())
                    if self.volume.text():
                        self.error.setText('')
                        new_data.append(self.volume.text())
                        self.cur.execute(f"""insert into coffee values(?, ?, ?, ?, ?, ?, ?)""", new_data)
                        self.con.commit()
                        self.ids = list(
                            map(lambda x: str(x[0]), self.cur.execute("""select id from coffee""").fetchall()))
                        self.id.clear()
                        self.id.addItem('0')
                        self.id.addItems(self.ids)
                    else:
                        self.error.setText('Введите объём')
                else:
                    self.error.setText('Введите цену')
            else:
                self.error.setText('Выберите степень помола')
        else:
            self.error.setText('Введите название')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffeeWidget()
    ex.show()
    sys.exit(app.exec())
