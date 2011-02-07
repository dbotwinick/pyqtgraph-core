# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProtocolTemplate.ui'
#
# Created: Sun Feb 06 20:53:08 2011
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(825, 338)
        self.gridLayout_4 = QtGui.QGridLayout(Form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.cameraCombo = QtGui.QComboBox(Form)
        self.cameraCombo.setObjectName("cameraCombo")
        self.gridLayout_2.addWidget(self.cameraCombo, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.laserCombo = QtGui.QComboBox(Form)
        self.laserCombo.setObjectName("laserCombo")
        self.gridLayout_2.addWidget(self.laserCombo, 1, 1, 1, 1)
        self.displayCheck = QtGui.QCheckBox(Form)
        self.displayCheck.setChecked(True)
        self.displayCheck.setObjectName("displayCheck")
        self.gridLayout_2.addWidget(self.displayCheck, 3, 0, 1, 2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.minTimeSpin = QtGui.QDoubleSpinBox(Form)
        self.minTimeSpin.setDecimals(3)
        self.minTimeSpin.setMaximum(1000000.0)
        self.minTimeSpin.setObjectName("minTimeSpin")
        self.gridLayout.addWidget(self.minTimeSpin, 0, 0, 1, 1)
        self.minDistSpin = QtGui.QDoubleSpinBox(Form)
        self.minDistSpin.setMaximum(1000000.0)
        self.minDistSpin.setObjectName("minDistSpin")
        self.gridLayout.addWidget(self.minDistSpin, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.packingSpin = QtGui.QDoubleSpinBox(Form)
        self.packingSpin.setMinimum(0.1)
        self.packingSpin.setMaximum(1000.0)
        self.packingSpin.setSingleStep(0.1)
        self.packingSpin.setProperty("value", QtCore.QVariant(1.0))
        self.packingSpin.setObjectName("packingSpin")
        self.gridLayout.addWidget(self.packingSpin, 2, 0, 1, 1)
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 0, 1, 2)
        self.addPointBtn = QtGui.QPushButton(Form)
        self.addPointBtn.setObjectName("addPointBtn")
        self.gridLayout_2.addWidget(self.addPointBtn, 5, 0, 1, 1)
        self.addOcclusionBtn = QtGui.QPushButton(Form)
        self.addOcclusionBtn.setObjectName("addOcclusionBtn")
        self.gridLayout_2.addWidget(self.addOcclusionBtn, 5, 1, 1, 1)
        self.addGridBtn = QtGui.QPushButton(Form)
        self.addGridBtn.setObjectName("addGridBtn")
        self.gridLayout_2.addWidget(self.addGridBtn, 6, 0, 1, 1)
        self.addProgramBtn = QtGui.QPushButton(Form)
        self.addProgramBtn.setObjectName("addProgramBtn")
        self.gridLayout_2.addWidget(self.addProgramBtn, 6, 1, 1, 1)
        self.deleteBtn = QtGui.QPushButton(Form)
        self.deleteBtn.setObjectName("deleteBtn")
        self.gridLayout_2.addWidget(self.deleteBtn, 7, 0, 1, 1)
        self.deleteAllBtn = QtGui.QPushButton(Form)
        self.deleteAllBtn.setObjectName("deleteAllBtn")
        self.gridLayout_2.addWidget(self.deleteAllBtn, 7, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 8, 0, 1, 1)
        self.recomputeBtn = QtGui.QPushButton(Form)
        self.recomputeBtn.setObjectName("recomputeBtn")
        self.gridLayout_2.addWidget(self.recomputeBtn, 9, 0, 1, 1)
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 9, 1, 1, 1)
        self.timeLabel = QtGui.QLabel(Form)
        self.timeLabel.setObjectName("timeLabel")
        self.gridLayout_2.addWidget(self.timeLabel, 10, 0, 1, 1)
        self.simulateShutterCheck = QtGui.QCheckBox(Form)
        self.simulateShutterCheck.setObjectName("simulateShutterCheck")
        self.gridLayout_2.addWidget(self.simulateShutterCheck, 2, 0, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 2, 1)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 2, 1, 1)
        self.programControlsLayout = QtGui.QVBoxLayout()
        self.programControlsLayout.setObjectName("programControlsLayout")
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.programControlsLayout.addWidget(self.label_8)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.addLineScanBtn = QtGui.QPushButton(Form)
        self.addLineScanBtn.setObjectName("addLineScanBtn")
        self.verticalLayout.addWidget(self.addLineScanBtn)
        self.addCircleScanBtn = QtGui.QPushButton(Form)
        self.addCircleScanBtn.setObjectName("addCircleScanBtn")
        self.verticalLayout.addWidget(self.addCircleScanBtn)
        self.addSpiralScanBtn = QtGui.QPushButton(Form)
        self.addSpiralScanBtn.setObjectName("addSpiralScanBtn")
        self.verticalLayout.addWidget(self.addSpiralScanBtn)
        self.deleteStepBtn = QtGui.QPushButton(Form)
        self.deleteStepBtn.setObjectName("deleteStepBtn")
        self.verticalLayout.addWidget(self.deleteStepBtn)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.previewBtn = QtGui.QPushButton(Form)
        self.previewBtn.setObjectName("previewBtn")
        self.verticalLayout.addWidget(self.previewBtn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.programControlsLayout.addLayout(self.horizontalLayout)
        self.gridLayout_3.addLayout(self.programControlsLayout, 0, 3, 2, 1)
        self.itemList = QtGui.QListWidget(Form)
        self.itemList.setObjectName("itemList")
        self.gridLayout_3.addWidget(self.itemList, 1, 1, 1, 1)
        self.targetList = QtGui.QListWidget(Form)
        self.targetList.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.targetList.setObjectName("targetList")
        self.gridLayout_3.addWidget(self.targetList, 1, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 4, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Camera Module:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Laser Device:", None, QtGui.QApplication.UnicodeUTF8))
        self.displayCheck.setText(QtGui.QApplication.translate("Form", "Display controls", None, QtGui.QApplication.UnicodeUTF8))
        self.minTimeSpin.setSuffix(QtGui.QApplication.translate("Form", "sec", None, QtGui.QApplication.UnicodeUTF8))
        self.minDistSpin.setSuffix(QtGui.QApplication.translate("Form", "µm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Minimum distance", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Minimum time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Point Spacing", None, QtGui.QApplication.UnicodeUTF8))
        self.addPointBtn.setText(QtGui.QApplication.translate("Form", "Add Point", None, QtGui.QApplication.UnicodeUTF8))
        self.addOcclusionBtn.setText(QtGui.QApplication.translate("Form", "Add Occlusion", None, QtGui.QApplication.UnicodeUTF8))
        self.addGridBtn.setText(QtGui.QApplication.translate("Form", "Add Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.addProgramBtn.setText(QtGui.QApplication.translate("Form", "Add Program", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteBtn.setText(QtGui.QApplication.translate("Form", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteAllBtn.setText(QtGui.QApplication.translate("Form", "Delete All", None, QtGui.QApplication.UnicodeUTF8))
        self.recomputeBtn.setText(QtGui.QApplication.translate("Form", "Recompute", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Form", "Auto recompute", None, QtGui.QApplication.UnicodeUTF8))
        self.timeLabel.setText(QtGui.QApplication.translate("Form", "Total Time:", None, QtGui.QApplication.UnicodeUTF8))
        self.simulateShutterCheck.setText(QtGui.QApplication.translate("Form", "Simulate Shutter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Items", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Targets", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Program Controls:", None, QtGui.QApplication.UnicodeUTF8))
        self.addLineScanBtn.setText(QtGui.QApplication.translate("Form", "Add Line Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.addCircleScanBtn.setText(QtGui.QApplication.translate("Form", "Add Circle Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.addSpiralScanBtn.setText(QtGui.QApplication.translate("Form", "Add Spiral Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteStepBtn.setText(QtGui.QApplication.translate("Form", "Delete Step", None, QtGui.QApplication.UnicodeUTF8))
        self.previewBtn.setText(QtGui.QApplication.translate("Form", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setSortingEnabled(True)

