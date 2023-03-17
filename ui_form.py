# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QProgressBar, QPushButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 480)
        self.horizontalLayoutWidget = QWidget(Widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(27, 380, 751, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.BrakeButton = QPushButton(self.horizontalLayoutWidget)
        self.BrakeButton.setObjectName(u"BrakeButton")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BrakeButton.sizePolicy().hasHeightForWidth())
        self.BrakeButton.setSizePolicy(sizePolicy)
        self.BrakeButton.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"color: white;\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.BrakeButton)

        self.AccelerationButton = QPushButton(self.horizontalLayoutWidget)
        self.AccelerationButton.setObjectName(u"AccelerationButton")
        sizePolicy.setHeightForWidth(self.AccelerationButton.sizePolicy().hasHeightForWidth())
        self.AccelerationButton.setSizePolicy(sizePolicy)
        self.AccelerationButton.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"color: white;\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.AccelerationButton)

        self.AutocrossButon = QPushButton(self.horizontalLayoutWidget)
        self.AutocrossButon.setObjectName(u"AutocrossButon")
        sizePolicy.setHeightForWidth(self.AutocrossButon.sizePolicy().hasHeightForWidth())
        self.AutocrossButon.setSizePolicy(sizePolicy)
        self.AutocrossButon.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"color: white;\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.AutocrossButon)

        self.SkidpadButton = QPushButton(self.horizontalLayoutWidget)
        self.SkidpadButton.setObjectName(u"SkidpadButton")
        sizePolicy.setHeightForWidth(self.SkidpadButton.sizePolicy().hasHeightForWidth())
        self.SkidpadButton.setSizePolicy(sizePolicy)
        self.SkidpadButton.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"color: white;\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.SkidpadButton)

        self.EnduranceButton = QPushButton(self.horizontalLayoutWidget)
        self.EnduranceButton.setObjectName(u"EnduranceButton")
        sizePolicy.setHeightForWidth(self.EnduranceButton.sizePolicy().hasHeightForWidth())
        self.EnduranceButton.setSizePolicy(sizePolicy)
        self.EnduranceButton.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"color: white;\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.EnduranceButton)

        self.Odometro = QFrame(Widget)
        self.Odometro.setObjectName(u"Odometro")
        self.Odometro.setGeometry(QRect(260, 30, 300, 300))
        self.Odometro.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"}")
        self.Odometro.setFrameShape(QFrame.StyledPanel)
        self.Odometro.setFrameShadow(QFrame.Raised)
        self.CircularPB = QFrame(self.Odometro)
        self.CircularPB.setObjectName(u"CircularPB")
        self.CircularPB.setGeometry(QRect(50, 50, 200, 200))
        sizePolicy.setHeightForWidth(self.CircularPB.sizePolicy().hasHeightForWidth())
        self.CircularPB.setSizePolicy(sizePolicy)
        self.CircularPB.setLayoutDirection(Qt.LeftToRight)
        self.CircularPB.setStyleSheet(u"QFrame{\n"
"	border-radius: 100px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:240, stop:0.4 rgba(210, 22, 116, 0), stop:1 rgba(23, 165, 0, 255));\n"
"}")
        self.CircularPB.setFrameShape(QFrame.NoFrame)
        self.CircularPB.setFrameShadow(QFrame.Raised)
        self.CircularBg = QFrame(self.Odometro)
        self.CircularBg.setObjectName(u"CircularBg")
        self.CircularBg.setGeometry(QRect(50, 50, 200, 200))
        self.CircularBg.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"	border-radius: 100px;\n"
"	background-color:  rgba(108, 108, 108, 120);\n"
"}")
        self.CircularBg.setFrameShape(QFrame.StyledPanel)
        self.CircularBg.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.Odometro)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(60, 60, 180, 180))
        self.container.setStyleSheet(u"QFrame{\n"
"	border-radius: 90px;\n"
"	background-color: rgb(44, 44, 44);\n"
"}")
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.container)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 40, 80, 80))
        self.label.setStyleSheet(u"font-size: 80px;\n"
"color: white;")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.container)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(55, 120, 67, 17))
        self.label_2.setStyleSheet(u"color: white;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.outsideCircle = QFrame(self.Odometro)
        self.outsideCircle.setObjectName(u"outsideCircle")
        self.outsideCircle.setGeometry(QRect(40, 40, 220, 220))
        self.outsideCircle.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"	border-radius: 110px;\n"
"	background-color: rgb(44, 44, 44);\n"
"}")
        self.outsideCircle.setFrameShape(QFrame.StyledPanel)
        self.outsideCircle.setFrameShadow(QFrame.Raised)
        self.outsideCircle.raise_()
        self.CircularBg.raise_()
        self.CircularPB.raise_()
        self.container.raise_()
        self.BrakeStatus = QFrame(Widget)
        self.BrakeStatus.setObjectName(u"BrakeStatus")
        self.BrakeStatus.setGeometry(QRect(77, 440, 45, 5))
        self.BrakeStatus.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"	border-radius: 2px;\n"
"	background-color: rgb(108, 108, 108);\n"
"}\n"
"\n"
"QFrame::hover{\n"
"	background-color: rgb(23, 165, 0);\n"
"}")
        self.BrakeStatus.setFrameShape(QFrame.StyledPanel)
        self.BrakeStatus.setFrameShadow(QFrame.Raised)
        self.AutocrossStatus = QFrame(Widget)
        self.AutocrossStatus.setObjectName(u"AutocrossStatus")
        self.AutocrossStatus.setGeometry(QRect(379, 440, 45, 5))
        self.AutocrossStatus.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"	border-radius: 2px;\n"
"	background-color: rgb(108, 108, 108);\n"
"}")
        self.AutocrossStatus.setFrameShape(QFrame.StyledPanel)
        self.AutocrossStatus.setFrameShadow(QFrame.Raised)
        self.AccelerationStatus = QFrame(Widget)
        self.AccelerationStatus.setObjectName(u"AccelerationStatus")
        self.AccelerationStatus.setGeometry(QRect(228, 440, 45, 5))
        self.AccelerationStatus.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"	border-radius: 2px;\n"
"	background-color: rgb(108, 108, 108);\n"
"}")
        self.AccelerationStatus.setFrameShape(QFrame.StyledPanel)
        self.AccelerationStatus.setFrameShadow(QFrame.Raised)
        self.EnduranceStatus = QFrame(Widget)
        self.EnduranceStatus.setObjectName(u"EnduranceStatus")
        self.EnduranceStatus.setGeometry(QRect(681, 440, 45, 5))
        self.EnduranceStatus.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"	border-radius: 2px;\n"
"	background-color: rgb(108, 108, 108);\n"
"}")
        self.EnduranceStatus.setFrameShape(QFrame.StyledPanel)
        self.EnduranceStatus.setFrameShadow(QFrame.Raised)
        self.SkidpadStatus = QFrame(Widget)
        self.SkidpadStatus.setObjectName(u"SkidpadStatus")
        self.SkidpadStatus.setGeometry(QRect(530, 440, 45, 5))
        self.SkidpadStatus.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"	border-radius: 2px;\n"
"	background-color: rgb(108, 108, 108);\n"
"}")
        self.SkidpadStatus.setFrameShape(QFrame.StyledPanel)
        self.SkidpadStatus.setFrameShadow(QFrame.Raised)
        self.HighVoltage = QFrame(Widget)
        self.HighVoltage.setObjectName(u"HighVoltage")
        self.HighVoltage.setGeometry(QRect(30, 50, 221, 151))
        self.HighVoltage.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"color: white;")
        self.HighVoltage.setFrameShape(QFrame.StyledPanel)
        self.HighVoltage.setFrameShadow(QFrame.Raised)
        self.BatteryLevelHV = QProgressBar(self.HighVoltage)
        self.BatteryLevelHV.setObjectName(u"BatteryLevelHV")
        self.BatteryLevelHV.setGeometry(QRect(27, 50, 161, 23))
        self.BatteryLevelHV.setStyleSheet(u"QProgressBar {\n"
"     border: none;\n"
"     background-color: rgb(44, 44, 44);\n"
" }\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: rgb(23, 165, 0);\n"
"	border-radius: 10px;\n"
"}")
        self.BatteryLevelHV.setValue(24)
        self.TitleHV = QLabel(self.HighVoltage)
        self.TitleHV.setObjectName(u"TitleHV")
        self.TitleHV.setGeometry(QRect(70, 10, 71, 16))
        self.VoltsHV = QLabel(self.HighVoltage)
        self.VoltsHV.setObjectName(u"VoltsHV")
        self.VoltsHV.setGeometry(QRect(30, 110, 31, 16))
        self.CelsiusHV = QLabel(self.HighVoltage)
        self.CelsiusHV.setObjectName(u"CelsiusHV")
        self.CelsiusHV.setGeometry(QRect(95, 110, 31, 16))
        self.AmperesHV = QLabel(self.HighVoltage)
        self.AmperesHV.setObjectName(u"AmperesHV")
        self.AmperesHV.setGeometry(QRect(160, 110, 31, 16))
        self.LowVoltage = QFrame(Widget)
        self.LowVoltage.setObjectName(u"LowVoltage")
        self.LowVoltage.setGeometry(QRect(30, 230, 221, 131))
        self.LowVoltage.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"color: white;")
        self.LowVoltage.setFrameShape(QFrame.StyledPanel)
        self.LowVoltage.setFrameShadow(QFrame.Raised)
        self.TitleLV = QLabel(self.LowVoltage)
        self.TitleLV.setObjectName(u"TitleLV")
        self.TitleLV.setGeometry(QRect(80, 10, 71, 16))
        self.BatteryLevelLV = QProgressBar(self.LowVoltage)
        self.BatteryLevelLV.setObjectName(u"BatteryLevelLV")
        self.BatteryLevelLV.setGeometry(QRect(27, 40, 161, 23))
        self.BatteryLevelLV.setStyleSheet(u"QProgressBar {\n"
"     border: none;\n"
"     background-color: rgb(44, 44, 44);\n"
" }\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: rgb(23, 165, 0);\n"
"	border-radius: 10px;\n"
"}")
        self.BatteryLevelLV.setValue(24)
        self.VoltslV = QLabel(self.LowVoltage)
        self.VoltslV.setObjectName(u"VoltslV")
        self.VoltslV.setGeometry(QRect(50, 90, 31, 16))
        self.CelsiusLV = QLabel(self.LowVoltage)
        self.CelsiusLV.setObjectName(u"CelsiusLV")
        self.CelsiusLV.setGeometry(QRect(140, 90, 31, 16))
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(550, 220, 221, 141))
        self.frame.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"color: white;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.TitleSystem = QLabel(self.frame)
        self.TitleSystem.setObjectName(u"TitleSystem")
        self.TitleSystem.setGeometry(QRect(90, 10, 41, 16))
        self.StatusTitle = QLabel(self.frame)
        self.StatusTitle.setObjectName(u"StatusTitle")
        self.StatusTitle.setGeometry(QRect(80, 58, 81, 16))
        self.CarStatus = QFrame(self.frame)
        self.CarStatus.setObjectName(u"CarStatus")
        self.CarStatus.setGeometry(QRect(40, 50, 31, 31))
        self.CarStatus.setStyleSheet(u"border: none;\n"
"border-radius: 15px;\n"
"background-color: rgb(23, 165, 0);")
        self.CarStatus.setFrameShape(QFrame.StyledPanel)
        self.CarStatus.setFrameShadow(QFrame.Raised)
        self.Motor = QFrame(Widget)
        self.Motor.setObjectName(u"Motor")
        self.Motor.setGeometry(QRect(550, 50, 221, 141))
        self.Motor.setStyleSheet(u"background-color: rgb(44, 44, 44);\n"
"color: white;")
        self.Motor.setFrameShape(QFrame.StyledPanel)
        self.Motor.setFrameShadow(QFrame.Raised)
        self.TitleMotor = QLabel(self.Motor)
        self.TitleMotor.setObjectName(u"TitleMotor")
        self.TitleMotor.setGeometry(QRect(90, 10, 41, 16))
        self.label_3 = QLabel(self.Motor)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 50, 31, 16))
        self.progressBar = QProgressBar(self.Motor)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 110, 201, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"     border: none;\n"
"     background-color: rgb(44, 44, 44);\n"
" }\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: rgb(23, 165, 0);\n"
"	border-radius: 10px;\n"
"}")
        self.progressBar.setValue(24)
        self.OdometroMotor = QFrame(self.Motor)
        self.OdometroMotor.setObjectName(u"OdometroMotor")
        self.OdometroMotor.setGeometry(QRect(40, 30, 70, 70))
        self.OdometroMotor.setStyleSheet(u"QFrame{\n"
"	border-radius: 35px;\n"
"	background-color: rgb(44, 44, 44);\n"
"}")
        self.OdometroMotor.setFrameShape(QFrame.StyledPanel)
        self.OdometroMotor.setFrameShadow(QFrame.Raised)
        self.CircularPBMotor = QFrame(self.OdometroMotor)
        self.CircularPBMotor.setObjectName(u"CircularPBMotor")
        self.CircularPBMotor.setGeometry(QRect(5, 5, 60, 60))
        self.CircularPBMotor.setStyleSheet(u"QFrame{\n"
"	border-radius: 30px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:240, stop:0.4 rgba(210, 22, 116, 0), stop:1 rgba(23, 165, 0, 255));\n"
"}")
        self.CircularPBMotor.setFrameShape(QFrame.StyledPanel)
        self.CircularPBMotor.setFrameShadow(QFrame.Raised)
        self.CircularBg_3 = QFrame(self.CircularPBMotor)
        self.CircularBg_3.setObjectName(u"CircularBg_3")
        self.CircularBg_3.setGeometry(QRect(0, 0, 60, 60))
        self.CircularBg_3.setStyleSheet(u"QFrame{\n"
"	border-radius: 30px;\n"
"	background-color: rgba(44, 44, 44, 120);\n"
"}")
        self.CircularBg_3.setFrameShape(QFrame.StyledPanel)
        self.CircularBg_3.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.CircularBg_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(4, 4, 50, 50))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"	border-radius: 25px;\n"
"	background-color: rgb(44, 44, 44);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(13, 10, 31, 16))
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(12, 25, 31, 16))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.BrakeButton.setText(QCoreApplication.translate("Widget", u"Brake", None))
        self.AccelerationButton.setText(QCoreApplication.translate("Widget", u"Acceleration", None))
        self.AutocrossButon.setText(QCoreApplication.translate("Widget", u"Autocross", None))
        self.SkidpadButton.setText(QCoreApplication.translate("Widget", u"Skidpad", None))
        self.EnduranceButton.setText(QCoreApplication.translate("Widget", u"Endurance", None))
        self.label.setText(QCoreApplication.translate("Widget", u"72", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Km/h", None))
        self.TitleHV.setText(QCoreApplication.translate("Widget", u"High Voltage", None))
        self.VoltsHV.setText(QCoreApplication.translate("Widget", u"72.4 V", None))
        self.CelsiusHV.setText(QCoreApplication.translate("Widget", u"36 \u00baC", None))
        self.AmperesHV.setText(QCoreApplication.translate("Widget", u"104 A", None))
        self.TitleLV.setText(QCoreApplication.translate("Widget", u"Low Voltage", None))
        self.VoltslV.setText(QCoreApplication.translate("Widget", u"12 V", None))
        self.CelsiusLV.setText(QCoreApplication.translate("Widget", u"36 \u00baC", None))
        self.TitleSystem.setText(QCoreApplication.translate("Widget", u"System", None))
        self.StatusTitle.setText(QCoreApplication.translate("Widget", u"Ready to Drive", None))
        self.TitleMotor.setText(QCoreApplication.translate("Widget", u"Motor", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"36 \u00baC", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"4500", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"RPM", None))
    # retranslateUi

