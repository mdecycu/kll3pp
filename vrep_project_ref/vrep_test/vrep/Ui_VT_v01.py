# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Y:\tmp\vrep_project\vrep_test\vrep\VT_v01.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Daci(object):
    def setupUi(self, Daci):
        Daci.setObjectName("Daci")
        Daci.resize(480, 410)
        Daci.setMinimumSize(QtCore.QSize(480, 410))
        Daci.setMaximumSize(QtCore.QSize(480, 410))
        self.horizontalLayoutWidget = QtWidgets.QWidget(Daci)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 601, 823))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_output = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.text_output.setMaximumSize(QtCore.QSize(100, 14))
        font = QtGui.QFont()
        font.setFamily("新細明體")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.text_output.setFont(font)
        self.text_output.setObjectName("text_output")
        self.verticalLayout.addWidget(self.text_output)
        self.print_output = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.print_output.setMinimumSize(QtCore.QSize(245, 384))
        self.print_output.setMaximumSize(QtCore.QSize(245, 384))
        self.print_output.setObjectName("print_output")
        self.verticalLayout.addWidget(self.print_output)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
        self.verticalTabWidget = QtWidgets.QTabWidget(self.horizontalLayoutWidget)
        self.verticalTabWidget.setMinimumSize(QtCore.QSize(225, 403))
        self.verticalTabWidget.setMaximumSize(QtCore.QSize(225, 403))
        self.verticalTabWidget.setMouseTracking(False)
        self.verticalTabWidget.setTabletTracking(False)
        self.verticalTabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.verticalTabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.verticalTabWidget.setAccessibleName("")
        self.verticalTabWidget.setAutoFillBackground(True)
        self.verticalTabWidget.setObjectName("verticalTabWidget")
        self.verticalTabWidgetPage1 = QtWidgets.QWidget()
        self.verticalTabWidgetPage1.setObjectName("verticalTabWidgetPage1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalTabWidgetPage1)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.text_name1 = QtWidgets.QLabel(self.verticalTabWidgetPage1)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_name1.setFont(font)
        self.text_name1.setObjectName("text_name1")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.text_name1)
        self.text_return1 = QtWidgets.QLabel(self.verticalTabWidgetPage1)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_return1.setFont(font)
        self.text_return1.setObjectName("text_return1")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.text_return1)
        self.click_return = QtWidgets.QPushButton(self.verticalTabWidgetPage1)
        self.click_return.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.click_return.setFont(font)
        self.click_return.setObjectName("click_return")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.click_return)
        self.edit_name1 = QtWidgets.QLineEdit(self.verticalTabWidgetPage1)
        self.edit_name1.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.edit_name1.setFont(font)
        self.edit_name1.setInputMask("")
        self.edit_name1.setMaxLength(16)
        self.edit_name1.setPlaceholderText("")
        self.edit_name1.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.edit_name1.setClearButtonEnabled(True)
        self.edit_name1.setObjectName("edit_name1")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edit_name1)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.formLayout_6)
        self.line_2 = QtWidgets.QFrame(self.verticalTabWidgetPage1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_2)
        self.form_3d = QtWidgets.QFormLayout()
        self.form_3d.setObjectName("form_3d")
        self.text_3d = QtWidgets.QLabel(self.verticalTabWidgetPage1)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_3d.setFont(font)
        self.text_3d.setObjectName("text_3d")
        self.form_3d.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.text_3d)
        self.click_start1 = QtWidgets.QPushButton(self.verticalTabWidgetPage1)
        self.click_start1.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.click_start1.setFont(font)
        self.click_start1.setObjectName("click_start1")
        self.form_3d.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.click_start1)
        self.value_x = QtWidgets.QDoubleSpinBox(self.verticalTabWidgetPage1)
        self.value_x.setMinimumSize(QtCore.QSize(80, 0))
        self.value_x.setMaximumSize(QtCore.QSize(100, 16777215))
        self.value_x.setSizeIncrement(QtCore.QSize(-24288, 0))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.value_x.setFont(font)
        self.value_x.setSuffix("")
        self.value_x.setDecimals(1)
        self.value_x.setMinimum(-1000.0)
        self.value_x.setMaximum(1000.0)
        self.value_x.setSingleStep(10.0)
        self.value_x.setObjectName("value_x")
        self.form_3d.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.value_x)
        self.value_y = QtWidgets.QDoubleSpinBox(self.verticalTabWidgetPage1)
        self.value_y.setMinimumSize(QtCore.QSize(80, 0))
        self.value_y.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.value_y.setFont(font)
        self.value_y.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.value_y.setMouseTracking(False)
        self.value_y.setTabletTracking(False)
        self.value_y.setAcceptDrops(False)
        self.value_y.setAutoFillBackground(False)
        self.value_y.setWrapping(False)
        self.value_y.setAccelerated(False)
        self.value_y.setProperty("showGroupSeparator", False)
        self.value_y.setPrefix("")
        self.value_y.setSuffix("")
        self.value_y.setDecimals(1)
        self.value_y.setMinimum(-1000.0)
        self.value_y.setMaximum(1000.0)
        self.value_y.setSingleStep(10.0)
        self.value_y.setObjectName("value_y")
        self.form_3d.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.value_y)
        self.value_z = QtWidgets.QDoubleSpinBox(self.verticalTabWidgetPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.value_z.sizePolicy().hasHeightForWidth())
        self.value_z.setSizePolicy(sizePolicy)
        self.value_z.setMinimumSize(QtCore.QSize(80, 0))
        self.value_z.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.value_z.setFont(font)
        self.value_z.setPrefix("")
        self.value_z.setSuffix("")
        self.value_z.setDecimals(1)
        self.value_z.setMinimum(-1000.0)
        self.value_z.setMaximum(1000.0)
        self.value_z.setSingleStep(10.0)
        self.value_z.setProperty("value", 0.0)
        self.value_z.setObjectName("value_z")
        self.form_3d.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.value_z)
        self.test_3d_x = QtWidgets.QLabel(self.verticalTabWidgetPage1)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.test_3d_x.setFont(font)
        self.test_3d_x.setObjectName("test_3d_x")
        self.form_3d.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.test_3d_x)
        self.test_3d_y = QtWidgets.QLabel(self.verticalTabWidgetPage1)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.test_3d_y.setFont(font)
        self.test_3d_y.setObjectName("test_3d_y")
        self.form_3d.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.test_3d_y)
        self.test_3d_z = QtWidgets.QLabel(self.verticalTabWidgetPage1)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.test_3d_z.setFont(font)
        self.test_3d_z.setObjectName("test_3d_z")
        self.form_3d.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.test_3d_z)
        self.formLayout_3.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.form_3d)
        self.line = QtWidgets.QFrame(self.verticalTabWidgetPage1)
        self.line.setMinimumSize(QtCore.QSize(0, 0))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.click_y_up = QtWidgets.QPushButton(self.verticalTabWidgetPage1)
        self.click_y_up.setMinimumSize(QtCore.QSize(40, 25))
        self.click_y_up.setMaximumSize(QtCore.QSize(40, 25))
        self.click_y_up.setMouseTracking(False)
        self.click_y_up.setAutoRepeat(True)
        self.click_y_up.setObjectName("click_y_up")
        self.gridLayout.addWidget(self.click_y_up, 1, 1, 1, 2)
        self.click_x_down = QtWidgets.QPushButton(self.verticalTabWidgetPage1)
        self.click_x_down.setMinimumSize(QtCore.QSize(40, 25))
        self.click_x_down.setMaximumSize(QtCore.QSize(40, 25))
        self.click_x_down.setAutoRepeat(True)
        self.click_x_down.setObjectName("click_x_down")
        self.gridLayout.addWidget(self.click_x_down, 2, 0, 1, 1)
        self.click_y_down = QtWidgets.QPushButton(self.verticalTabWidgetPage1)
        self.click_y_down.setMinimumSize(QtCore.QSize(40, 25))
        self.click_y_down.setMaximumSize(QtCore.QSize(40, 25))
        self.click_y_down.setAutoRepeat(True)
        self.click_y_down.setObjectName("click_y_down")
        self.gridLayout.addWidget(self.click_y_down, 3, 1, 1, 1)
        self.click_z_down = QtWidgets.QPushButton(self.verticalTabWidgetPage1)
        self.click_z_down.setMinimumSize(QtCore.QSize(40, 25))
        self.click_z_down.setMaximumSize(QtCore.QSize(40, 25))
        self.click_z_down.setAutoRepeat(True)
        self.click_z_down.setObjectName("click_z_down")
        self.gridLayout.addWidget(self.click_z_down, 3, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.click_x_up = QtWidgets.QPushButton(self.verticalTabWidgetPage1)
        self.click_x_up.setMinimumSize(QtCore.QSize(40, 25))
        self.click_x_up.setMaximumSize(QtCore.QSize(40, 25))
        self.click_x_up.setAutoRepeat(True)
        self.click_x_up.setObjectName("click_x_up")
        self.gridLayout.addWidget(self.click_x_up, 2, 2, 1, 1)
        self.text_control = QtWidgets.QLabel(self.verticalTabWidgetPage1)
        self.text_control.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_control.setFont(font)
        self.text_control.setObjectName("text_control")
        self.gridLayout.addWidget(self.text_control, 0, 0, 1, 3)
        self.click_z_up = QtWidgets.QPushButton(self.verticalTabWidgetPage1)
        self.click_z_up.setMinimumSize(QtCore.QSize(40, 25))
        self.click_z_up.setMaximumSize(QtCore.QSize(40, 25))
        self.click_z_up.setAutoRepeat(True)
        self.click_z_up.setAutoExclusive(False)
        self.click_z_up.setObjectName("click_z_up")
        self.gridLayout.addWidget(self.click_z_up, 1, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(5, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(15, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 3, 1, 1)
        self.formLayout_3.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.gridLayout)
        self.verticalLayout_2.addLayout(self.formLayout_3)
        self.verticalTabWidget.addTab(self.verticalTabWidgetPage1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 279, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setObjectName("formLayout_8")
        self.text_open = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_open.setFont(font)
        self.text_open.setObjectName("text_open")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.text_open)
        self.click_open = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.click_open.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.click_open.setFont(font)
        self.click_open.setObjectName("click_open")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.click_open)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setMaximumSize(QtCore.QSize(190, 20))
        self.listWidget.setAlternatingRowColors(False)
        self.listWidget.setObjectName("listWidget")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.listWidget)
        self.text_name2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_name2.setFont(font)
        self.text_name2.setObjectName("text_name2")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.text_name2)
        self.edit_name2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_name2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.edit_name2.setFont(font)
        self.edit_name2.setInputMask("")
        self.edit_name2.setMaxLength(16)
        self.edit_name2.setPlaceholderText("")
        self.edit_name2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.edit_name2.setClearButtonEnabled(True)
        self.edit_name2.setObjectName("edit_name2")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.edit_name2)
        self.text_name3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_name3.setFont(font)
        self.text_name3.setObjectName("text_name3")
        self.formLayout_8.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.text_name3)
        self.edit_name3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_name3.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.edit_name3.setFont(font)
        self.edit_name3.setInputMask("")
        self.edit_name3.setMaxLength(16)
        self.edit_name3.setPlaceholderText("")
        self.edit_name3.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.edit_name3.setClearButtonEnabled(True)
        self.edit_name3.setObjectName("edit_name3")
        self.formLayout_8.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.edit_name3)
        self.text_run = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_run.setFont(font)
        self.text_run.setObjectName("text_run")
        self.formLayout_8.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.text_run)
        self.click_start2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.click_start2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.click_start2.setFont(font)
        self.click_start2.setObjectName("click_start2")
        self.formLayout_8.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.click_start2)
        self.verticalLayout_3.addLayout(self.formLayout_8)
        self.verticalTabWidget.addTab(self.tab_2, "")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.verticalTabWidget)
        self.horizontalLayout.addLayout(self.formLayout_2)

        self.retranslateUi(Daci)
        self.verticalTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Daci)

    def retranslateUi(self, Daci):
        _translate = QtCore.QCoreApplication.translate
        Daci.setWindowTitle(_translate("Daci", "Daci"))
        self.text_output.setText(_translate("Daci", "輸出結果"))
        self.text_name1.setText(_translate("Daci", "物件名稱 :   "))
        self.text_return1.setText(_translate("Daci", "原點復歸 :"))
        self.click_return.setText(_translate("Daci", "Return"))
        self.click_return.setShortcut(_translate("Daci", "Ctrl+R"))
        self.edit_name1.setText(_translate("Daci", "box"))
        self.text_3d.setText(_translate("Daci", "參數控制 :   "))
        self.click_start1.setText(_translate("Daci", "Start"))
        self.click_start1.setShortcut(_translate("Daci", "Ctrl+G"))
        self.value_z.setToolTip(_translate("Daci", "x"))
        self.test_3d_x.setText(_translate("Daci", "         X (mm)"))
        self.test_3d_y.setText(_translate("Daci", "         Y (mm)"))
        self.test_3d_z.setText(_translate("Daci", "         Z (mm)"))
        self.click_y_up.setText(_translate("Daci", "+ Y"))
        self.click_y_up.setShortcut(_translate("Daci", "Y, +"))
        self.click_x_down.setText(_translate("Daci", "- X"))
        self.click_x_down.setShortcut(_translate("Daci", "X, -"))
        self.click_y_down.setText(_translate("Daci", "- Y"))
        self.click_y_down.setShortcut(_translate("Daci", "Y, -"))
        self.click_z_down.setText(_translate("Daci", "- Z"))
        self.click_z_down.setShortcut(_translate("Daci", "Z, -"))
        self.click_x_up.setText(_translate("Daci", "+ X"))
        self.click_x_up.setShortcut(_translate("Daci", "X, +"))
        self.text_control.setText(_translate("Daci", "按鍵控制 :"))
        self.click_z_up.setText(_translate("Daci", "+ Z"))
        self.click_z_up.setShortcut(_translate("Daci", "Z, +"))
        self.verticalTabWidget.setTabText(self.verticalTabWidget.indexOf(self.verticalTabWidgetPage1), _translate("Daci", "控制"))
        self.text_open.setText(_translate("Daci", "開啟檔案 : "))
        self.click_open.setText(_translate("Daci", "Open"))
        self.click_open.setShortcut(_translate("Daci", "Ctrl+O"))
        self.listWidget.setSortingEnabled(False)
        self.text_name2.setText(_translate("Daci", "物件噴嘴 :   "))
        self.edit_name2.setText(_translate("Daci", "nozzle"))
        self.text_name3.setText(_translate("Daci", "物件平台 :   "))
        self.edit_name3.setText(_translate("Daci", "platform"))
        self.text_run.setText(_translate("Daci", "執行模擬 : "))
        self.click_start2.setText(_translate("Daci", "Start"))
        self.click_start2.setShortcut(_translate("Daci", "Ctrl+Alt+G"))
        self.verticalTabWidget.setTabText(self.verticalTabWidget.indexOf(self.tab_2), _translate("Daci", "模擬"))

