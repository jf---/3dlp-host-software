# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manual_printer_control_dialog.ui'
#
# Created: Sun Jan 20 14:36:19 2013
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Manual_Control(object):
    def setupUi(self, Manual_Control):
        Manual_Control.setObjectName(_fromUtf8("Manual_Control"))
        Manual_Control.resize(352, 275)
        Manual_Control.setWindowTitle(QtGui.QApplication.translate("Manual_Control", "3DLP Manual Printer Control", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout_8 = QtGui.QVBoxLayout(Manual_Control)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label = QtGui.QLabel(Manual_Control)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("Manual_Control", "Manual Printer Control", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_7.addWidget(self.label)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.groupBox = QtGui.QGroupBox(Manual_Control)
        self.groupBox.setTitle(QtGui.QApplication.translate("Manual_Control", "Z Axis", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setText(QtGui.QApplication.translate("Manual_Control", "10mm", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setText(QtGui.QApplication.translate("Manual_Control", "1mm", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_3.setText(QtGui.QApplication.translate("Manual_Control", "0.1mm", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_4.setText(QtGui.QApplication.translate("Manual_Control", "0.01mm", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.verticalLayout.addWidget(self.radioButton_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.toolButton = QtGui.QToolButton(self.groupBox)
        self.toolButton.setText(QtGui.QApplication.translate("Manual_Control", "...", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/icons/nav_up_blue.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(48, 48))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.verticalLayout_2.addWidget(self.toolButton)
        self.toolButton_4 = QtGui.QToolButton(self.groupBox)
        self.toolButton_4.setText(QtGui.QApplication.translate("Manual_Control", "...", None, QtGui.QApplication.UnicodeUTF8))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/icons/nav_down_blue.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon1)
        self.toolButton_4.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.verticalLayout_2.addWidget(self.toolButton_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setMaximumSize(QtCore.QSize(15, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setText(QtGui.QApplication.translate("Manual_Control", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lcdNumber = QtGui.QLCDNumber(self.groupBox)
        self.lcdNumber.setMinimumSize(QtCore.QSize(100, 20))
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setNumDigits(8)
        self.lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.horizontalLayout_3.addWidget(self.lcdNumber)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setText(QtGui.QApplication.translate("Manual_Control", "mm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setText(QtGui.QApplication.translate("Manual_Control", "Zero Z Axis", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_5.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Manual_Control)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Manual_Control", "X Axis", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.radioButton_5 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_5.setText(QtGui.QApplication.translate("Manual_Control", "10mm", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.verticalLayout_5.addWidget(self.radioButton_5)
        self.radioButton_6 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_6.setText(QtGui.QApplication.translate("Manual_Control", "1mm", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.verticalLayout_5.addWidget(self.radioButton_6)
        self.radioButton_7 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_7.setText(QtGui.QApplication.translate("Manual_Control", "0.1mm", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))
        self.verticalLayout_5.addWidget(self.radioButton_7)
        self.radioButton_8 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_8.setText(QtGui.QApplication.translate("Manual_Control", "0.01mm", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_8.setChecked(True)
        self.radioButton_8.setObjectName(_fromUtf8("radioButton_8"))
        self.verticalLayout_5.addWidget(self.radioButton_8)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.toolButton_2 = QtGui.QToolButton(self.groupBox_2)
        self.toolButton_2.setText(QtGui.QApplication.translate("Manual_Control", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.verticalLayout_6.addWidget(self.toolButton_2)
        self.toolButton_5 = QtGui.QToolButton(self.groupBox_2)
        self.toolButton_5.setText(QtGui.QApplication.translate("Manual_Control", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_5.setIcon(icon1)
        self.toolButton_5.setIconSize(QtCore.QSize(48, 48))
        self.toolButton_5.setObjectName(_fromUtf8("toolButton_5"))
        self.verticalLayout_6.addWidget(self.toolButton_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.line_2 = QtGui.QFrame(self.groupBox_2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_4.addWidget(self.line_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setMaximumSize(QtCore.QSize(15, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setText(QtGui.QApplication.translate("Manual_Control", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lcdNumber_2 = QtGui.QLCDNumber(self.groupBox_2)
        self.lcdNumber_2.setMinimumSize(QtCore.QSize(100, 20))
        self.lcdNumber_2.setSmallDecimalPoint(False)
        self.lcdNumber_2.setNumDigits(8)
        self.lcdNumber_2.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_2.setProperty("value", 0.0)
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.horizontalLayout_4.addWidget(self.lcdNumber_2)
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setText(QtGui.QApplication.translate("Manual_Control", "mm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setText(QtGui.QApplication.translate("Manual_Control", "Zero X Axis", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.horizontalLayout_5.addWidget(self.groupBox_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.retranslateUi(Manual_Control)
        QtCore.QMetaObject.connectSlotsByName(Manual_Control)

    def retranslateUi(self, Manual_Control):
        pass

import resource_rc
