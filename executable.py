# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(844, 481)
        Widget.setStyleSheet("QWidget{\n"
"    background-color: rgb(44, 44, 44);\n"
"}")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(27, 380, 751, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BrakeButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BrakeButton.sizePolicy().hasHeightForWidth())
        self.BrakeButton.setSizePolicy(sizePolicy)
        self.BrakeButton.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"color: white;\n"
"\n"
"")
        self.BrakeButton.setObjectName("BrakeButton")
        self.horizontalLayout.addWidget(self.BrakeButton)
        self.AccelerationButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AccelerationButton.sizePolicy().hasHeightForWidth())
        self.AccelerationButton.setSizePolicy(sizePolicy)
        self.AccelerationButton.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"color: white;\n"
"\n"
"")
        self.AccelerationButton.setObjectName("AccelerationButton")
        self.horizontalLayout.addWidget(self.AccelerationButton)
        self.AutocrossButon = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AutocrossButon.sizePolicy().hasHeightForWidth())
        self.AutocrossButon.setSizePolicy(sizePolicy)
        self.AutocrossButon.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"color: white;\n"
"\n"
"")
        self.AutocrossButon.setObjectName("AutocrossButon")
        self.horizontalLayout.addWidget(self.AutocrossButon)
        self.SkidpadButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SkidpadButton.sizePolicy().hasHeightForWidth())
        self.SkidpadButton.setSizePolicy(sizePolicy)
        self.SkidpadButton.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"color: white;\n"
"\n"
"")
        self.SkidpadButton.setObjectName("SkidpadButton")
        self.horizontalLayout.addWidget(self.SkidpadButton)
        self.EnduranceButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EnduranceButton.sizePolicy().hasHeightForWidth())
        self.EnduranceButton.setSizePolicy(sizePolicy)
        self.EnduranceButton.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"color: white;\n"
"\n"
"")
        self.EnduranceButton.setObjectName("EnduranceButton")
        self.horizontalLayout.addWidget(self.EnduranceButton)
        self.Odometro = QtWidgets.QFrame(Widget)
        self.Odometro.setGeometry(QtCore.QRect(260, 30, 300, 300))
        self.Odometro.setStyleSheet("QFrame{\n"
"    border: none;\n"
"}")
        self.Odometro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Odometro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Odometro.setObjectName("Odometro")
        self.CircularPB = QtWidgets.QFrame(self.Odometro)
        self.CircularPB.setGeometry(QtCore.QRect(50, 50, 200, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CircularPB.sizePolicy().hasHeightForWidth())
        self.CircularPB.setSizePolicy(sizePolicy)
        self.CircularPB.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CircularPB.setStyleSheet("QFrame{\n"
"    border-radius: 100px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:240, stop:0.4 rgba(210, 22, 116, 0), stop:1 rgba(23, 165, 0, 255));\n"
"}")
        self.CircularPB.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CircularPB.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CircularPB.setObjectName("CircularPB")
        self.CircularBg = QtWidgets.QFrame(self.Odometro)
        self.CircularBg.setGeometry(QtCore.QRect(50, 50, 200, 200))
        self.CircularBg.setStyleSheet("QFrame{\n"
"    border: none;\n"
"    border-radius: 100px;\n"
"    background-color:  rgba(108, 108, 108, 120);\n"
"}")
        self.CircularBg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CircularBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CircularBg.setObjectName("CircularBg")
        self.container = QtWidgets.QFrame(self.Odometro)
        self.container.setGeometry(QtCore.QRect(60, 60, 180, 180))
        self.container.setStyleSheet("QFrame{\n"
"    border-radius: 90px;\n"
"    background-color: rgb(44, 44, 44);\n"
"}")
        self.container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.label = QtWidgets.QLabel(self.container)
        self.label.setGeometry(QtCore.QRect(30, 40, 121, 80))
        self.label.setStyleSheet("font-size: 80px;\n"
"color: white;")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.container)
        self.label_2.setGeometry(QtCore.QRect(55, 120, 67, 17))
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.outsideCircle = QtWidgets.QFrame(self.Odometro)
        self.outsideCircle.setGeometry(QtCore.QRect(40, 40, 220, 220))
        self.outsideCircle.setStyleSheet("QFrame{\n"
"    border: none;\n"
"    border-radius: 110px;\n"
"    background-color: rgb(44, 44, 44);\n"
"}")
        self.outsideCircle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.outsideCircle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outsideCircle.setObjectName("outsideCircle")
        self.outsideCircle.raise_()
        self.CircularBg.raise_()
        self.CircularPB.raise_()
        self.container.raise_()
        self.BrakeStatus = QtWidgets.QFrame(Widget)
        self.BrakeStatus.setGeometry(QtCore.QRect(77, 440, 45, 5))
        self.BrakeStatus.setStyleSheet("QFrame{\n"
"    border: none;\n"
"    border-radius: 2px;\n"
"    background-color: rgb(108, 108, 108);\n"
"}\n"
"\n"
"QFrame::hover{\n"
"    background-color: rgb(23, 165, 0);\n"
"}")
        self.BrakeStatus.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BrakeStatus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BrakeStatus.setObjectName("BrakeStatus")
        self.AutocrossStatus = QtWidgets.QFrame(Widget)
        self.AutocrossStatus.setGeometry(QtCore.QRect(379, 440, 45, 5))
        self.AutocrossStatus.setStyleSheet("QFrame{\n"
"    border: none;\n"
"    border-radius: 2px;\n"
"    background-color: rgb(108, 108, 108);\n"
"}")
        self.AutocrossStatus.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AutocrossStatus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AutocrossStatus.setObjectName("AutocrossStatus")
        self.AccelerationStatus = QtWidgets.QFrame(Widget)
        self.AccelerationStatus.setGeometry(QtCore.QRect(228, 440, 45, 5))
        self.AccelerationStatus.setStyleSheet("QFrame{\n"
"    border: none;\n"
"    border-radius: 2px;\n"
"    background-color: rgb(108, 108, 108);\n"
"}")
        self.AccelerationStatus.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AccelerationStatus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AccelerationStatus.setObjectName("AccelerationStatus")
        self.EnduranceStatus = QtWidgets.QFrame(Widget)
        self.EnduranceStatus.setGeometry(QtCore.QRect(681, 440, 45, 5))
        self.EnduranceStatus.setStyleSheet("QFrame{\n"
"    border: none;\n"
"    border-radius: 2px;\n"
"    background-color: rgb(108, 108, 108);\n"
"}")
        self.EnduranceStatus.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.EnduranceStatus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EnduranceStatus.setObjectName("EnduranceStatus")
        self.SkidpadStatus = QtWidgets.QFrame(Widget)
        self.SkidpadStatus.setGeometry(QtCore.QRect(530, 440, 45, 5))
        self.SkidpadStatus.setStyleSheet("QFrame{\n"
"    border: none;\n"
"    border-radius: 2px;\n"
"    background-color: rgb(108, 108, 108);\n"
"}")
        self.SkidpadStatus.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SkidpadStatus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SkidpadStatus.setObjectName("SkidpadStatus")
        self.HighVoltage = QtWidgets.QFrame(Widget)
        self.HighVoltage.setGeometry(QtCore.QRect(30, 50, 221, 151))
        self.HighVoltage.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"color: white;")
        self.HighVoltage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HighVoltage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.HighVoltage.setObjectName("HighVoltage")
        self.BatteryLevelHV = QtWidgets.QProgressBar(self.HighVoltage)
        self.BatteryLevelHV.setGeometry(QtCore.QRect(27, 50, 161, 23))
        self.BatteryLevelHV.setStyleSheet("QProgressBar {\n"
"     border: none;\n"
"     background-color: rgb(44, 44, 44);\n"
"      text-align: center;\n"
" }\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(23, 165, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.BatteryLevelHV.setProperty("value", 24)
        self.BatteryLevelHV.setObjectName("BatteryLevelHV")
        self.TitleHV = QtWidgets.QLabel(self.HighVoltage)
        self.TitleHV.setGeometry(QtCore.QRect(70, 10, 101, 31))
        self.TitleHV.setObjectName("TitleHV")
        self.VoltsHV = QtWidgets.QLabel(self.HighVoltage)
        self.VoltsHV.setGeometry(QtCore.QRect(30, 110, 51, 16))
        self.VoltsHV.setObjectName("VoltsHV")
        self.CelsiusHV = QtWidgets.QLabel(self.HighVoltage)
        self.CelsiusHV.setGeometry(QtCore.QRect(95, 110, 41, 16))
        self.CelsiusHV.setObjectName("CelsiusHV")
        self.AmperesHV = QtWidgets.QLabel(self.HighVoltage)
        self.AmperesHV.setGeometry(QtCore.QRect(160, 110, 41, 16))
        self.AmperesHV.setObjectName("AmperesHV")
        self.LowVoltage = QtWidgets.QFrame(Widget)
        self.LowVoltage.setGeometry(QtCore.QRect(30, 230, 221, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LowVoltage.sizePolicy().hasHeightForWidth())
        self.LowVoltage.setSizePolicy(sizePolicy)
        self.LowVoltage.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"color: white;")
        self.LowVoltage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LowVoltage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LowVoltage.setObjectName("LowVoltage")
        self.TitleLV = QtWidgets.QLabel(self.LowVoltage)
        self.TitleLV.setGeometry(QtCore.QRect(70, 10, 111, 21))
        self.TitleLV.setObjectName("TitleLV")
        self.BatteryLevelLV = QtWidgets.QProgressBar(self.LowVoltage)
        self.BatteryLevelLV.setGeometry(QtCore.QRect(27, 40, 161, 23))
        self.BatteryLevelLV.setStyleSheet("QProgressBar {\n"
"     border: none;\n"
"     background-color: rgb(44, 44, 44);\n"
"    text-align: center;\n"
" }\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(23, 165, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.BatteryLevelLV.setProperty("value", 24)
        self.BatteryLevelLV.setObjectName("BatteryLevelLV")
        self.VoltslV = QtWidgets.QLabel(self.LowVoltage)
        self.VoltslV.setGeometry(QtCore.QRect(40, 90, 41, 21))
        self.VoltslV.setObjectName("VoltslV")
        self.CelsiusLV = QtWidgets.QLabel(self.LowVoltage)
        self.CelsiusLV.setGeometry(QtCore.QRect(120, 90, 41, 21))
        self.CelsiusLV.setObjectName("CelsiusLV")
        self.frame = QtWidgets.QFrame(Widget)
        self.frame.setGeometry(QtCore.QRect(550, 220, 221, 141))
        self.frame.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"color: white;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.TitleSystem = QtWidgets.QLabel(self.frame)
        self.TitleSystem.setGeometry(QtCore.QRect(90, 10, 51, 21))
        self.TitleSystem.setObjectName("TitleSystem")
        self.StatusTitle = QtWidgets.QLabel(self.frame)
        self.StatusTitle.setGeometry(QtCore.QRect(80, 60, 111, 21))
        self.StatusTitle.setObjectName("StatusTitle")
        self.CarStatus = QtWidgets.QFrame(self.frame)
        self.CarStatus.setGeometry(QtCore.QRect(40, 55, 31, 31))
        self.CarStatus.setStyleSheet("border: none;\n"
"border-radius: 15px;\n"
"background-color: rgb(23, 165, 0);")
        self.CarStatus.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CarStatus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CarStatus.setObjectName("CarStatus")
        self.Motor = QtWidgets.QFrame(Widget)
        self.Motor.setGeometry(QtCore.QRect(550, 50, 221, 141))
        self.Motor.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"color: white;")
        self.Motor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Motor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Motor.setObjectName("Motor")
        self.TitleMotor = QtWidgets.QLabel(self.Motor)
        self.TitleMotor.setGeometry(QtCore.QRect(90, 10, 41, 16))
        self.TitleMotor.setObjectName("TitleMotor")
        self.label_3 = QtWidgets.QLabel(self.Motor)
        self.label_3.setGeometry(QtCore.QRect(160, 50, 51, 16))
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(self.Motor)
        self.progressBar.setGeometry(QtCore.QRect(10, 110, 201, 23))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"     border: none;\n"
"     background-color: rgb(44, 44, 44);\n"
"    text-align: center;\n"
" }\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(23, 165, 0);\n"
"    border-radius: 10px;\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.OdometroMotor = QtWidgets.QFrame(self.Motor)
        self.OdometroMotor.setGeometry(QtCore.QRect(40, 30, 70, 70))
        self.OdometroMotor.setStyleSheet("QFrame{\n"
"    border-radius: 35px;\n"
"    background-color: rgb(44, 44, 44);\n"
"}")
        self.OdometroMotor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.OdometroMotor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OdometroMotor.setObjectName("OdometroMotor")
        self.CircularPBMotor = QtWidgets.QFrame(self.OdometroMotor)
        self.CircularPBMotor.setGeometry(QtCore.QRect(5, 5, 60, 60))
        self.CircularPBMotor.setStyleSheet("QFrame{\n"
"    border-radius: 30px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:240, stop:0.4 rgba(210, 22, 116, 0), stop:1 rgba(23, 165, 0, 255));\n"
"}")
        self.CircularPBMotor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CircularPBMotor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CircularPBMotor.setObjectName("CircularPBMotor")
        self.CircularBg_3 = QtWidgets.QFrame(self.CircularPBMotor)
        self.CircularBg_3.setGeometry(QtCore.QRect(0, 0, 60, 60))
        self.CircularBg_3.setStyleSheet("QFrame{\n"
"    border-radius: 30px;\n"
"    background-color: rgba(44, 44, 44, 120);\n"
"}")
        self.CircularBg_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CircularBg_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CircularBg_3.setObjectName("CircularBg_3")
        self.frame_2 = QtWidgets.QFrame(self.CircularBg_3)
        self.frame_2.setGeometry(QtCore.QRect(4, 4, 50, 50))
        self.frame_2.setStyleSheet("QFrame{\n"
"    border: none;\n"
"    border-radius: 25px;\n"
"    background-color: rgb(44, 44, 44);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 41, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(12, 25, 31, 16))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.BrakeButton.setText(_translate("Widget", "Brake"))
        self.AccelerationButton.setText(_translate("Widget", "Acceleration"))
        self.AutocrossButon.setText(_translate("Widget", "Autocross"))
        self.SkidpadButton.setText(_translate("Widget", "Skidpad"))
        self.EnduranceButton.setText(_translate("Widget", "Endurance"))
        self.label.setText(_translate("Widget", "72"))
        self.label_2.setText(_translate("Widget", "Km/h"))
        self.TitleHV.setText(_translate("Widget", "High Voltage"))
        self.VoltsHV.setText(_translate("Widget", "72.4 V"))
        self.CelsiusHV.setText(_translate("Widget", "36 ºC"))
        self.AmperesHV.setText(_translate("Widget", "104 A"))
        self.TitleLV.setText(_translate("Widget", "Low Voltage"))
        self.VoltslV.setText(_translate("Widget", "12 V"))
        self.CelsiusLV.setText(_translate("Widget", "36 ºC"))
        self.TitleSystem.setText(_translate("Widget", "System"))
        self.StatusTitle.setText(_translate("Widget", "Ready to Drive"))
        self.TitleMotor.setText(_translate("Widget", "Motor"))
        self.label_3.setText(_translate("Widget", "36 ºC"))
        self.label_6.setText(_translate("Widget", "4500"))
        self.label_7.setText(_translate("Widget", "RPM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
