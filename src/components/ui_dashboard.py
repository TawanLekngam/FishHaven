# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPlainTextEdit,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1440, 1048)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        Form.setFont(font)
        Form.setStyleSheet(u"background-color: \"white\";")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 50, 641, 51))
        font1 = QFont()
        font1.setPointSize(36)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: \"black\";")
        self.ap_box = QWidget(Form)
        self.ap_box.setObjectName(u"ap_box")
        self.ap_box.setGeometry(QRect(80, 400, 231, 231))
        self.ap_box.setStyleSheet(u"background-color: \"#FFF3F1\"; border-radius:8;")
        self.ap_title = QLabel(self.ap_box)
        self.ap_title.setObjectName(u"ap_title")
        self.ap_title.setGeometry(QRect(20, 60, 191, 31))
        font2 = QFont()
        font2.setPointSize(24)
        font2.setBold(False)
        self.ap_title.setFont(font2)
        self.ap_title.setStyleSheet(u"color: \"black\";")
        self.ap_title.setAlignment(Qt.AlignCenter)
        self.ap_fish = QLabel(self.ap_box)
        self.ap_fish.setObjectName(u"ap_fish")
        self.ap_fish.setGeometry(QRect(20, 130, 191, 41))
        self.ap_fish.setFont(font1)
        self.ap_fish.setStyleSheet(u"color:\"black\";")
        self.ap_fish.setAlignment(Qt.AlignCenter)
        self.mgp_box = QWidget(Form)
        self.mgp_box.setObjectName(u"mgp_box")
        self.mgp_box.setGeometry(QRect(330, 400, 231, 231))
        self.mgp_box.setStyleSheet(u"background-color: \"#EEF1FF\"; border-radius:8;")
        self.mgp_title = QLabel(self.mgp_box)
        self.mgp_title.setObjectName(u"mgp_title")
        self.mgp_title.setGeometry(QRect(20, 60, 191, 31))
        self.mgp_title.setFont(font2)
        self.mgp_title.setStyleSheet(u"color: \"black\";")
        self.mgp_title.setAlignment(Qt.AlignCenter)
        self.mgp_fish = QLabel(self.mgp_box)
        self.mgp_fish.setObjectName(u"mgp_fish")
        self.mgp_fish.setGeometry(QRect(20, 130, 191, 41))
        self.mgp_fish.setFont(font1)
        self.mgp_fish.setStyleSheet(u"color:\"black\";")
        self.mgp_fish.setAlignment(Qt.AlignCenter)
        self.ag_box = QWidget(Form)
        self.ag_box.setObjectName(u"ag_box")
        self.ag_box.setGeometry(QRect(80, 660, 231, 231))
        self.ag_box.setStyleSheet(u"background-color: \"#EEF1FF\"; border-radius:8;")
        self.ag_title = QLabel(self.ag_box)
        self.ag_title.setObjectName(u"ag_title")
        self.ag_title.setGeometry(QRect(20, 60, 191, 31))
        self.ag_title.setFont(font2)
        self.ag_title.setStyleSheet(u"color: \"black\";")
        self.ag_title.setAlignment(Qt.AlignCenter)
        self.ag_fish = QLabel(self.ag_box)
        self.ag_fish.setObjectName(u"ag_fish")
        self.ag_fish.setGeometry(QRect(20, 130, 191, 41))
        self.ag_fish.setFont(font1)
        self.ag_fish.setStyleSheet(u"color:\"black\";")
        self.ag_fish.setAlignment(Qt.AlignCenter)
        self.mtp_box = QWidget(Form)
        self.mtp_box.setObjectName(u"mtp_box")
        self.mtp_box.setGeometry(QRect(330, 660, 231, 231))
        self.mtp_box.setStyleSheet(u"background-color: \"#FFF3F1\"; border-radius:8;")
        self.mtp_title = QLabel(self.mtp_box)
        self.mtp_title.setObjectName(u"mtp_title")
        self.mtp_title.setGeometry(QRect(20, 60, 191, 31))
        self.mtp_title.setFont(font2)
        self.mtp_title.setStyleSheet(u"color: \"black\";")
        self.mtp_title.setAlignment(Qt.AlignCenter)
        self.mtp_fish = QLabel(self.mtp_box)
        self.mtp_fish.setObjectName(u"mtp_fish")
        self.mtp_fish.setGeometry(QRect(20, 130, 191, 41))
        self.mtp_fish.setFont(font1)
        self.mtp_fish.setStyleSheet(u"color:\"black\";")
        self.mtp_fish.setAlignment(Qt.AlignCenter)
        self.total_box = QWidget(Form)
        self.total_box.setObjectName(u"total_box")
        self.total_box.setGeometry(QRect(80, 920, 480, 81))
        self.total_box.setStyleSheet(u"background-color: \"#FFF7F0\"; border-radius:8;")
        self.total_fish = QLabel(self.total_box)
        self.total_fish.setObjectName(u"total_fish")
        self.total_fish.setGeometry(QRect(130, 20, 221, 41))
        self.total_fish.setFont(font2)
        self.total_fish.setStyleSheet(u"color: \"black\";")
        self.total_fish.setAlignment(Qt.AlignCenter)
        self.total_label = QLabel(self.total_box)
        self.total_label.setObjectName(u"total_label")
        self.total_label.setGeometry(QRect(40, 20, 71, 41))
        font3 = QFont()
        font3.setPointSize(24)
        font3.setBold(True)
        self.total_label.setFont(font3)
        self.total_label.setStyleSheet(u"color:\"black\";")
        self.total_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.fish_label = QLabel(self.total_box)
        self.fish_label.setObjectName(u"fish_label")
        self.fish_label.setGeometry(QRect(370, 20, 71, 41))
        self.fish_label.setFont(font2)
        self.fish_label.setStyleSheet(u"color: \"black\";")
        self.log_frame = QFrame(Form)
        self.log_frame.setObjectName(u"log_frame")
        self.log_frame.setGeometry(QRect(600, 140, 761, 861))
        self.log_frame.setStyleSheet(u"background-color: \"#EAEAEA\"; border-radius:8;\n"
"")
        self.log_frame.setFrameShape(QFrame.StyledPanel)
        self.log_frame.setFrameShadow(QFrame.Raised)
        self.log_title = QLabel(self.log_frame)
        self.log_title.setObjectName(u"log_title")
        self.log_title.setGeometry(QRect(30, 20, 111, 21))
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        self.log_title.setFont(font4)
        self.log_title.setStyleSheet(u"color:black;")
        self.born_box = QWidget(self.log_frame)
        self.born_box.setObjectName(u"born_box")
        self.born_box.setGeometry(QRect(30, 580, 341, 121))
        self.born_box.setStyleSheet(u"background-color:white;")
        self.born_title = QLabel(self.born_box)
        self.born_title.setObjectName(u"born_title")
        self.born_title.setGeometry(QRect(100, 30, 141, 21))
        font5 = QFont()
        font5.setPointSize(12)
        self.born_title.setFont(font5)
        self.born_title.setStyleSheet(u"color:black;")
        self.born_title.setAlignment(Qt.AlignCenter)
        self.born_fish = QLabel(self.born_box)
        self.born_fish.setObjectName(u"born_fish")
        self.born_fish.setGeometry(QRect(60, 60, 221, 30))
        self.born_fish.setFont(font3)
        self.born_fish.setStyleSheet(u"color:black;")
        self.born_fish.setAlignment(Qt.AlignCenter)
        self.died_box = QWidget(self.log_frame)
        self.died_box.setObjectName(u"died_box")
        self.died_box.setGeometry(QRect(390, 580, 341, 121))
        self.died_box.setStyleSheet(u"background-color:white;")
        self.died_title = QLabel(self.died_box)
        self.died_title.setObjectName(u"died_title")
        self.died_title.setGeometry(QRect(100, 30, 141, 21))
        self.died_title.setFont(font5)
        self.died_title.setStyleSheet(u"color:black;")
        self.died_title.setAlignment(Qt.AlignCenter)
        self.died_fish = QLabel(self.died_box)
        self.died_fish.setObjectName(u"died_fish")
        self.died_fish.setGeometry(QRect(60, 60, 221, 30))
        self.died_fish.setFont(font3)
        self.died_fish.setStyleSheet(u"color:black;")
        self.died_fish.setAlignment(Qt.AlignCenter)
        self.male_box = QWidget(self.log_frame)
        self.male_box.setObjectName(u"male_box")
        self.male_box.setGeometry(QRect(30, 720, 341, 121))
        self.male_box.setStyleSheet(u"background-color:\"#EEF1FF\";")
        self.male_title = QLabel(self.male_box)
        self.male_title.setObjectName(u"male_title")
        self.male_title.setGeometry(QRect(100, 30, 141, 21))
        self.male_title.setFont(font5)
        self.male_title.setStyleSheet(u"color:black;")
        self.male_title.setAlignment(Qt.AlignCenter)
        self.male_fish = QLabel(self.male_box)
        self.male_fish.setObjectName(u"male_fish")
        self.male_fish.setGeometry(QRect(60, 60, 221, 30))
        self.male_fish.setFont(font3)
        self.male_fish.setStyleSheet(u"color:black;")
        self.male_fish.setAlignment(Qt.AlignCenter)
        self.female_box = QWidget(self.log_frame)
        self.female_box.setObjectName(u"female_box")
        self.female_box.setGeometry(QRect(390, 720, 341, 121))
        self.female_box.setStyleSheet(u"background-color:\"#FFF3F1\";")
        self.female_title = QLabel(self.female_box)
        self.female_title.setObjectName(u"female_title")
        self.female_title.setGeometry(QRect(100, 30, 141, 21))
        self.female_title.setFont(font5)
        self.female_title.setStyleSheet(u"color:black;")
        self.female_title.setAlignment(Qt.AlignCenter)
        self.female_fish = QLabel(self.female_box)
        self.female_fish.setObjectName(u"female_fish")
        self.female_fish.setGeometry(QRect(60, 60, 221, 30))
        self.female_fish.setFont(font3)
        self.female_fish.setStyleSheet(u"color:black;")
        self.female_fish.setAlignment(Qt.AlignCenter)
        self.log_details = QPlainTextEdit(self.log_frame)
        self.log_details.setObjectName(u"log_details")
        self.log_details.setGeometry(QRect(30, 60, 701, 501))
        self.log_details.setStyleSheet(u"background-color:white;")
        self.kp_box = QWidget(Form)
        self.kp_box.setObjectName(u"kp_box")
        self.kp_box.setGeometry(QRect(330, 140, 231, 231))
        self.kp_box.setStyleSheet(u"background-color: \"#FFF3F1\"; border-radius:8;")
        self.kp_title = QLabel(self.kp_box)
        self.kp_title.setObjectName(u"kp_title")
        self.kp_title.setGeometry(QRect(20, 60, 191, 31))
        self.kp_title.setFont(font2)
        self.kp_title.setStyleSheet(u"color: \"black\";")
        self.kp_title.setAlignment(Qt.AlignCenter)
        self.kp_fish = QLabel(self.kp_box)
        self.kp_fish.setObjectName(u"kp_fish")
        self.kp_fish.setGeometry(QRect(20, 130, 191, 41))
        self.kp_fish.setFont(font1)
        self.kp_fish.setStyleSheet(u"color:\"black\";")
        self.kp_fish.setAlignment(Qt.AlignCenter)
        self.dp_box = QWidget(Form)
        self.dp_box.setObjectName(u"dp_box")
        self.dp_box.setGeometry(QRect(80, 140, 231, 231))
        self.dp_box.setStyleSheet(u"background-color: \"#EEF1FF\"; border-radius:8;")
        self.dp_title = QLabel(self.dp_box)
        self.dp_title.setObjectName(u"dp_title")
        self.dp_title.setGeometry(QRect(20, 60, 191, 31))
        self.dp_title.setFont(font2)
        self.dp_title.setStyleSheet(u"color: \"black\";")
        self.dp_title.setAlignment(Qt.AlignCenter)
        self.dp_fish = QLabel(self.dp_box)
        self.dp_fish.setObjectName(u"dp_fish")
        self.dp_fish.setGeometry(QRect(20, 130, 191, 41))
        self.dp_fish.setFont(font1)
        self.dp_fish.setStyleSheet(u"color:\"black\";")
        self.dp_fish.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Fish Haven Vivisystem Dashboard", None))
        self.ap_title.setText(QCoreApplication.translate("Form", u"Auay Pond", None))
        self.ap_fish.setText(QCoreApplication.translate("Form", u"0", None))
        self.mgp_title.setText(QCoreApplication.translate("Form", u"Mega Pond", None))
        self.mgp_fish.setText(QCoreApplication.translate("Form", u"0", None))
        self.ag_title.setText(QCoreApplication.translate("Form", u"Aqua Gang", None))
        self.ag_fish.setText(QCoreApplication.translate("Form", u"0", None))
        self.mtp_title.setText(QCoreApplication.translate("Form", u"Matrix Pond", None))
        self.mtp_fish.setText(QCoreApplication.translate("Form", u"0", None))
        self.total_fish.setText(QCoreApplication.translate("Form", u"0", None))
        self.total_label.setText(QCoreApplication.translate("Form", u"Total:", None))
        self.fish_label.setText(QCoreApplication.translate("Form", u"Fishes", None))
        self.log_title.setText(QCoreApplication.translate("Form", u"Doo Pond Log", None))
        self.born_title.setText(QCoreApplication.translate("Form", u"Fish Born in Doo Pond", None))
        self.born_fish.setText(QCoreApplication.translate("Form", u"0", None))
        self.died_title.setText(QCoreApplication.translate("Form", u"Fish Died in Doo Pond", None))
        self.died_fish.setText(QCoreApplication.translate("Form", u"0", None))
        self.male_title.setText(QCoreApplication.translate("Form", u"Total Male Fishes", None))
        self.male_fish.setText(QCoreApplication.translate("Form", u"0", None))
        self.female_title.setText(QCoreApplication.translate("Form", u"Total Female Fishes", None))
        self.female_fish.setText(QCoreApplication.translate("Form", u"0", None))
        self.kp_title.setText(QCoreApplication.translate("Form", u"Khor Pond", None))
        self.kp_fish.setText(QCoreApplication.translate("Form", u"0", None))
        self.dp_title.setText(QCoreApplication.translate("Form", u"Doo Pond", None))
        self.dp_fish.setText(QCoreApplication.translate("Form", u"0", None))
    # retranslateUi
