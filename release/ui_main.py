# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainOVZQiE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_mainForm(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(767, 404)
        Form.setStyleSheet(u"background-color: rgb(255, 218, 181);")
        self.sort_name = QComboBox(Form)
        self.sort_name.setObjectName(u"sort_name")
        self.sort_name.setGeometry(QRect(30, 50, 211, 22))
        self.sort_name.setStyleSheet(u"background-color: rgb(255, 238, 221);\n"
"font: 9pt \"Candara\";")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 161, 16))
        self.label.setStyleSheet(u"font: 75 italic 9pt \"Candara\";")
        self.roasting = QSlider(Form)
        self.roasting.setObjectName(u"roasting")
        self.roasting.setGeometry(QRect(40, 130, 241, 22))
        self.roasting.setStyleSheet(u"")
        self.roasting.setOrientation(Qt.Horizontal)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 100, 161, 16))
        self.label_2.setStyleSheet(u"font: 75 italic 9pt \"Candara\";")
        self.taste = QPlainTextEdit(Form)
        self.taste.setObjectName(u"taste")
        self.taste.setGeometry(QRect(390, 50, 301, 87))
        self.taste.setStyleSheet(u"background-color: rgb(255, 238, 221);\n"
"font: 9pt \"Candara\";")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(390, 30, 161, 16))
        self.label_6.setStyleSheet(u"font: 75 italic 9pt \"Candara\";")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(390, 180, 55, 16))
        self.label_7.setStyleSheet(u"font: 75 italic 9pt \"Candara\";")
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(390, 220, 55, 16))
        self.label_8.setStyleSheet(u"font: 100 italic 9pt \"Candara\";")
        self.price = QLabel(Form)
        self.price.setObjectName(u"price")
        self.price.setGeometry(QRect(470, 180, 71, 16))
        self.price.setStyleSheet(u"font: 9pt \"Candara\";")
        self.volume = QLabel(Form)
        self.volume.setObjectName(u"volume")
        self.volume.setGeometry(QRect(470, 220, 71, 16))
        self.volume.setStyleSheet(u"font: 9pt \"Candara\";")
        self.edit = QPushButton(Form)
        self.edit.setObjectName(u"edit")
        self.edit.setGeometry(QRect(290, 310, 121, 28))
        self.edit.setStyleSheet(u"background-color: rgb(255, 238, 221);\n"
"font: 9pt \"Candara\";")
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 160, 341, 20))
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

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 240, 91, 20))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.in_grains = QRadioButton(self.layoutWidget1)
        self.in_grains.setObjectName(u"in_grains")
        self.in_grains.setStyleSheet(u"font: 9pt \"Candara\";")

        self.horizontalLayout_2.addWidget(self.in_grains)

        self.label_10 = QLabel(self.layoutWidget1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 9pt \"Candara\";")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.layoutWidget2 = QWidget(Form)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(30, 210, 91, 20))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ground = QRadioButton(self.layoutWidget2)
        self.ground.setObjectName(u"ground")
        self.ground.setStyleSheet(u"font: 9pt \"Candara\";")

        self.horizontalLayout_3.addWidget(self.ground)

        self.label_9 = QLabel(self.layoutWidget2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 9pt \"Candara\";")

        self.horizontalLayout_3.addWidget(self.label_9)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u043e\u0440\u0442\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0435\u043f\u0435\u043d\u044c \u043e\u0431\u0436\u0430\u0440\u043a\u0438", None))
        self.taste.setPlainText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0432\u043a\u0443\u0441\u0430", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0430:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u044a\u0451\u043c:", None))
        self.price.setText("")
        self.volume.setText("")
        self.edit.setText(QCoreApplication.translate("Form", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0441\u043b\u0430\u0431\u0430\u044f", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0441\u0440\u0435\u0434\u043d\u044f\u044f", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0442\u0451\u043c\u043d\u0430\u044f", None))
        self.in_grains.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"\u0432 \u0437\u0451\u0440\u043d\u0430\u0445", None))
        self.ground.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"\u043c\u043e\u043b\u043e\u0442\u044b\u0439", None))
    # retranslateUi

