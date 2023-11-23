# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addEditCoffeeFormDjOUle.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_addForm(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(664, 380)
        Form.setStyleSheet(u"background-color: rgb(255, 218, 181);")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 641, 351))
        self.tabWidget.setStyleSheet(u"border-color: rgb(255, 218, 181);\n"
"font: 9pt \"Candara\";\n"
"background-color: rgb(255, 218, 181);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 110, 161, 16))
        self.label_2.setStyleSheet(u"font: 75 italic 9pt \"Candara\";")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 50, 161, 16))
        self.label.setStyleSheet(u"font: 75 italic 9pt \"Candara\";")
        self.roasting_edit = QSlider(self.tab)
        self.roasting_edit.setObjectName(u"roasting_edit")
        self.roasting_edit.setGeometry(QRect(20, 140, 241, 22))
        self.roasting_edit.setStyleSheet(u"")
        self.roasting_edit.setOrientation(Qt.Horizontal)
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(370, 200, 55, 16))
        self.label_8.setStyleSheet(u"font: 100 italic 9pt \"Candara\";")
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(370, 160, 55, 16))
        self.label_7.setStyleSheet(u"font: 75 italic 9pt \"Candara\";")
        self.layoutWidget = QWidget(self.tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 170, 341, 20))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 9pt \"Candara\";")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 9pt \"Candara\";")

        self.horizontalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 9pt \"Candara\";")

        self.horizontalLayout.addWidget(self.label_5)

        self.layoutWidget_2 = QWidget(self.tab)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 250, 91, 20))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.in_grains_edit = QRadioButton(self.layoutWidget_2)
        self.in_grains_edit.setObjectName(u"in_grains_edit")
        self.in_grains_edit.setStyleSheet(u"font: 9pt \"Candara\";")

        self.horizontalLayout_2.addWidget(self.in_grains_edit)

        self.label_10 = QLabel(self.layoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 9pt \"Candara\";")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.layoutWidget_3 = QWidget(self.tab)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 220, 91, 20))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ground_edit = QRadioButton(self.layoutWidget_3)
        self.ground_edit.setObjectName(u"ground_edit")
        self.ground_edit.setStyleSheet(u"font: 9pt \"Candara\";")

        self.horizontalLayout_3.addWidget(self.ground_edit)

        self.label_9 = QLabel(self.layoutWidget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 9pt \"Candara\";")

        self.horizontalLayout_3.addWidget(self.label_9)

        self.taste_edit = QPlainTextEdit(self.tab)
        self.taste_edit.setObjectName(u"taste_edit")
        self.taste_edit.setGeometry(QRect(370, 30, 251, 87))
        self.taste_edit.setStyleSheet(u"background-color: rgb(255, 238, 221);\n"
"font: 9pt \"Candara\";")
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(370, 10, 161, 16))
        self.label_6.setStyleSheet(u"font: 75 italic 9pt \"Candara\";")
        self.save = QPushButton(self.tab)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(270, 260, 111, 31))
        self.save.setStyleSheet(u"background-color: rgb(255, 238, 221);\n"
"font: 9pt \"Candara\";")
        self.price_edit = QLineEdit(self.tab)
        self.price_edit.setObjectName(u"price_edit")
        self.price_edit.setGeometry(QRect(430, 160, 113, 22))
        self.price_edit.setStyleSheet(u"background-color: rgb(255, 238, 221);\n"
"font: 9pt \"Candara\";")
        self.volume_edit = QLineEdit(self.tab)
        self.volume_edit.setObjectName(u"volume_edit")
        self.volume_edit.setGeometry(QRect(430, 200, 113, 22))
        self.volume_edit.setStyleSheet(u"background-color: rgb(255, 238, 221);\n"
"font: 9pt \"Candara\";")
        self.sort_name_edit = QLineEdit(self.tab)
        self.sort_name_edit.setObjectName(u"sort_name_edit")
        self.sort_name_edit.setGeometry(QRect(10, 70, 221, 22))
        self.sort_name_edit.setStyleSheet(u"background-color: rgb(255, 238, 221);\n"
"font: 9pt \"Candara\";")
        self.layoutWidget1 = QWidget(self.tab)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 114, 24))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.layoutWidget1)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_7.addWidget(self.label_21)

        self.id = QComboBox(self.layoutWidget1)
        self.id.setObjectName(u"id")
        self.id.setStyleSheet(u"background-color: rgb(255, 238, 221);\n"
"font: 9pt \"Candara\";")

        self.horizontalLayout_7.addWidget(self.id)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.layoutWidget_4 = QWidget(self.tab_2)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(0, 140, 341, 20))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 9pt \"Candara\";")

        self.horizontalLayout_4.addWidget(self.label_11)

        self.label_12 = QLabel(self.layoutWidget_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font: 9pt \"Candara\";")

        self.horizontalLayout_4.addWidget(self.label_12)

        self.label_13 = QLabel(self.layoutWidget_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 9pt \"Candara\";")

        self.horizontalLayout_4.addWidget(self.label_13)

        self.layoutWidget_5 = QWidget(self.tab_2)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(10, 220, 91, 20))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.in_grains = QRadioButton(self.layoutWidget_5)
        self.in_grains.setObjectName(u"in_grains")
        self.in_grains.setStyleSheet(u"font: 9pt \"Candara\";")

        self.horizontalLayout_5.addWidget(self.in_grains)

        self.label_14 = QLabel(self.layoutWidget_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font: 9pt \"Candara\";")

        self.horizontalLayout_5.addWidget(self.label_14)

        self.label_15 = QLabel(self.tab_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 80, 161, 16))
        self.label_15.setStyleSheet(u"font: 75 italic 9pt \"Candara\";")
        self.price = QLineEdit(self.tab_2)
        self.price.setObjectName(u"price")
        self.price.setGeometry(QRect(430, 160, 113, 22))
        self.price.setStyleSheet(u"background-color: rgb(255, 238, 221);\n"
"font: 9pt \"Candara\";")
        self.label_16 = QLabel(self.tab_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(370, 200, 55, 16))
        self.label_16.setStyleSheet(u"font: 100 italic 9pt \"Candara\";")
        self.label_17 = QLabel(self.tab_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(370, 160, 55, 16))
        self.label_17.setStyleSheet(u"font: 75 italic 9pt \"Candara\";")
        self.layoutWidget_6 = QWidget(self.tab_2)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(10, 190, 91, 20))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ground = QRadioButton(self.layoutWidget_6)
        self.ground.setObjectName(u"ground")
        self.ground.setStyleSheet(u"font: 9pt \"Candara\";")

        self.horizontalLayout_6.addWidget(self.ground)

        self.label_18 = QLabel(self.layoutWidget_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"font: 9pt \"Candara\";")

        self.horizontalLayout_6.addWidget(self.label_18)

        self.label_19 = QLabel(self.tab_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 10, 161, 16))
        self.label_19.setStyleSheet(u"font: 75 italic 9pt \"Candara\";")
        self.volume = QLineEdit(self.tab_2)
        self.volume.setObjectName(u"volume")
        self.volume.setGeometry(QRect(430, 200, 113, 22))
        self.volume.setStyleSheet(u"background-color: rgb(255, 238, 221);\n"
"font: 9pt \"Candara\";")
        self.taste = QPlainTextEdit(self.tab_2)
        self.taste.setObjectName(u"taste")
        self.taste.setGeometry(QRect(370, 30, 251, 87))
        self.taste.setStyleSheet(u"background-color: rgb(255, 238, 221);\n"
"font: 9pt \"Candara\";")
        self.add = QPushButton(self.tab_2)
        self.add.setObjectName(u"add")
        self.add.setGeometry(QRect(270, 260, 111, 31))
        self.add.setStyleSheet(u"background-color: rgb(255, 238, 221);\n"
"font: 9pt \"Candara\";")
        self.roasting = QSlider(self.tab_2)
        self.roasting.setObjectName(u"roasting")
        self.roasting.setGeometry(QRect(20, 110, 241, 22))
        self.roasting.setStyleSheet(u"")
        self.roasting.setOrientation(Qt.Horizontal)
        self.label_20 = QLabel(self.tab_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(370, 10, 161, 16))
        self.label_20.setStyleSheet(u"font: 75 italic 9pt \"Candara\";")
        self.sort_name = QLineEdit(self.tab_2)
        self.sort_name.setObjectName(u"sort_name")
        self.sort_name.setGeometry(QRect(10, 30, 221, 22))
        self.sort_name.setStyleSheet(u"background-color: rgb(255, 238, 221);\n"
"font: 9pt \"Candara\";")
        self.error = QLabel(self.tab_2)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(20, 270, 201, 21))
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0435\u043f\u0435\u043d\u044c \u043e\u0431\u0436\u0430\u0440\u043a\u0438", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u043e\u0440\u0442\u0430", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u044a\u0451\u043c:", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0430:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0441\u043b\u0430\u0431\u0430\u044f", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0441\u0440\u0435\u0434\u043d\u044f\u044f", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0442\u0451\u043c\u043d\u0430\u044f", None))
        self.in_grains_edit.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"\u0432 \u0437\u0451\u0440\u043d\u0430\u0445", None))
        self.ground_edit.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"\u043c\u043e\u043b\u043e\u0442\u044b\u0439", None))
        self.taste_edit.setPlainText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0432\u043a\u0443\u0441\u0430", None))
        self.save.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"ID", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u0441\u043b\u0430\u0431\u0430\u044f", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u0441\u0440\u0435\u0434\u043d\u044f\u044f", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u0442\u0451\u043c\u043d\u0430\u044f", None))
        self.in_grains.setText("")
        self.label_14.setText(QCoreApplication.translate("Form", u"\u0432 \u0437\u0451\u0440\u043d\u0430\u0445", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0435\u043f\u0435\u043d\u044c \u043e\u0431\u0436\u0430\u0440\u043a\u0438", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u044a\u0451\u043c:", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0430:", None))
        self.ground.setText("")
        self.label_18.setText(QCoreApplication.translate("Form", u"\u043c\u043e\u043b\u043e\u0442\u044b\u0439", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u043e\u0440\u0442\u0430", None))
        self.taste.setPlainText("")
        self.add.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0432\u043a\u0443\u0441\u0430", None))
        self.error.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

