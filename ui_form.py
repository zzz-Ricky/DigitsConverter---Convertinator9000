# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(365, 270)
        Widget.setAutoFillBackground(True)
        Widget.setStyleSheet(u"font: 9pt \"Noto Sans\";")
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(9, 90, 351, 24))
        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QRect(60, 20, 251, 31))
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"font: 700 italic 18pt \"Noto Sans\";")
        self.layoutWidget = QWidget(Widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 61, 351, 27))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.Input1 = QLineEdit(self.layoutWidget)
        self.Input1.setObjectName(u"Input1")

        self.horizontalLayout.addWidget(self.Input1)

        self.layoutWidget1 = QWidget(Widget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(11, 121, 351, 120))
        self.formLayout = QFormLayout(self.layoutWidget1)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.binout = QLineEdit(self.layoutWidget1)
        self.binout.setObjectName(u"binout")
        self.binout.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.binout)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.octout = QLineEdit(self.layoutWidget1)
        self.octout.setObjectName(u"octout")
        self.octout.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.octout)

        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.hexout = QLineEdit(self.layoutWidget1)
        self.hexout.setObjectName(u"hexout")
        self.hexout.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.hexout)

        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.grayout = QLineEdit(self.layoutWidget1)
        self.grayout.setObjectName(u"grayout")
        self.grayout.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.grayout)

        self.label_7 = QLabel(Widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 250, 141, 16))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"CONVERTINATOR 9000", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Convert", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"CONVERTINATOR 9000", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Input (Decimal Value)", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Unsigned Binary", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Octal", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Hexadecimal", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Gray code", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Project by: Ricky Huynh", None))
    # retranslateUi

