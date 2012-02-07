# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './lib/modules/ProtocolRunner/ProtocolRunnerTemplate.ui'
#
# Created: Mon Feb  6 23:48:24 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1089, 309)
        MainWindow.setStyleSheet(_fromUtf8(""))
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.LoaderDock = QtGui.QDockWidget(MainWindow)
        self.LoaderDock.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable|QtGui.QDockWidget.DockWidgetVerticalTitleBar)
        self.LoaderDock.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.TopDockWidgetArea)
        self.LoaderDock.setObjectName(_fromUtf8("LoaderDock"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.LoaderDock.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.LoaderDock)
        self.ProtocolDock = QtGui.QDockWidget(MainWindow)
        self.ProtocolDock.setEnabled(True)
        self.ProtocolDock.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable|QtGui.QDockWidget.DockWidgetVerticalTitleBar)
        self.ProtocolDock.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.TopDockWidgetArea)
        self.ProtocolDock.setObjectName(_fromUtf8("ProtocolDock"))
        self.dockWidgetContents_5 = QtGui.QWidget()
        self.dockWidgetContents_5.setObjectName(_fromUtf8("dockWidgetContents_5"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents_5)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.dockWidgetContents_5)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.protoContinuousCheck = QtGui.QCheckBox(self.dockWidgetContents_5)
        self.protoContinuousCheck.setEnabled(False)
        self.protoContinuousCheck.setObjectName(_fromUtf8("protoContinuousCheck"))
        self.gridLayout.addWidget(self.protoContinuousCheck, 0, 1, 1, 2)
        self.deviceList = QtGui.QListWidget(self.dockWidgetContents_5)
        self.deviceList.setObjectName(_fromUtf8("deviceList"))
        self.gridLayout.addWidget(self.deviceList, 1, 0, 5, 1)
        self.label_8 = QtGui.QLabel(self.dockWidgetContents_5)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.dockWidgetContents_5)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)
        self.protoLoopCheck = QtGui.QCheckBox(self.dockWidgetContents_5)
        self.protoLoopCheck.setObjectName(_fromUtf8("protoLoopCheck"))
        self.gridLayout.addWidget(self.protoLoopCheck, 3, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.dockWidgetContents_5)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 4, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 91, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 2, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.testSingleBtn = QtGui.QPushButton(self.dockWidgetContents_5)
        self.testSingleBtn.setEnabled(True)
        self.testSingleBtn.setObjectName(_fromUtf8("testSingleBtn"))
        self.horizontalLayout_2.addWidget(self.testSingleBtn)
        spacerItem1 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.runProtocolBtn = QtGui.QPushButton(self.dockWidgetContents_5)
        self.runProtocolBtn.setEnabled(True)
        self.runProtocolBtn.setObjectName(_fromUtf8("runProtocolBtn"))
        self.horizontalLayout_2.addWidget(self.runProtocolBtn)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.stopSingleBtn = QtGui.QPushButton(self.dockWidgetContents_5)
        self.stopSingleBtn.setObjectName(_fromUtf8("stopSingleBtn"))
        self.horizontalLayout_2.addWidget(self.stopSingleBtn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 0, 1, 4)
        self.protoDurationSpin = SpinBox(self.dockWidgetContents_5)
        self.protoDurationSpin.setMinimumSize(QtCore.QSize(60, 0))
        self.protoDurationSpin.setProperty(_fromUtf8("value"), 0.1)
        self.protoDurationSpin.setObjectName(_fromUtf8("protoDurationSpin"))
        self.gridLayout.addWidget(self.protoDurationSpin, 1, 2, 1, 2)
        self.protoLeadTimeSpin = SpinBox(self.dockWidgetContents_5)
        self.protoLeadTimeSpin.setProperty(_fromUtf8("value"), 0.01)
        self.protoLeadTimeSpin.setObjectName(_fromUtf8("protoLeadTimeSpin"))
        self.gridLayout.addWidget(self.protoLeadTimeSpin, 2, 2, 1, 2)
        self.protoCycleTimeSpin = SpinBox(self.dockWidgetContents_5)
        self.protoCycleTimeSpin.setObjectName(_fromUtf8("protoCycleTimeSpin"))
        self.gridLayout.addWidget(self.protoCycleTimeSpin, 4, 2, 1, 2)
        self.ProtocolDock.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.ProtocolDock)
        self.SequenceDock = QtGui.QDockWidget(MainWindow)
        self.SequenceDock.setEnabled(True)
        self.SequenceDock.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable|QtGui.QDockWidget.DockWidgetVerticalTitleBar)
        self.SequenceDock.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.TopDockWidgetArea)
        self.SequenceDock.setObjectName(_fromUtf8("SequenceDock"))
        self.dockWidgetContents_7 = QtGui.QWidget()
        self.dockWidgetContents_7.setObjectName(_fromUtf8("dockWidgetContents_7"))
        self.gridLayout_2 = QtGui.QGridLayout(self.dockWidgetContents_7)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_10 = QtGui.QLabel(self.dockWidgetContents_7)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_9 = QtGui.QLabel(self.dockWidgetContents_7)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout.addWidget(self.label_9)
        self.seqCycleTimeSpin = SpinBox(self.dockWidgetContents_7)
        self.seqCycleTimeSpin.setProperty(_fromUtf8("value"), 1.0)
        self.seqCycleTimeSpin.setObjectName(_fromUtf8("seqCycleTimeSpin"))
        self.verticalLayout.addWidget(self.seqCycleTimeSpin)
        self.label_11 = QtGui.QLabel(self.dockWidgetContents_7)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout.addWidget(self.label_11)
        self.seqRepetitionSpin = QtGui.QSpinBox(self.dockWidgetContents_7)
        self.seqRepetitionSpin.setMinimum(0)
        self.seqRepetitionSpin.setMaximum(1000000)
        self.seqRepetitionSpin.setObjectName(_fromUtf8("seqRepetitionSpin"))
        self.verticalLayout.addWidget(self.seqRepetitionSpin)
        spacerItem3 = QtGui.QSpacerItem(17, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_2 = QtGui.QLabel(self.dockWidgetContents_7)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.paramSpaceLabel = QtGui.QLabel(self.dockWidgetContents_7)
        self.paramSpaceLabel.setObjectName(_fromUtf8("paramSpaceLabel"))
        self.verticalLayout.addWidget(self.paramSpaceLabel)
        self.label_4 = QtGui.QLabel(self.dockWidgetContents_7)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.seqTimeLabel = QtGui.QLabel(self.dockWidgetContents_7)
        self.seqTimeLabel.setObjectName(_fromUtf8("seqTimeLabel"))
        self.verticalLayout.addWidget(self.seqTimeLabel)
        self.seqCurrentLabel = QtGui.QLabel(self.dockWidgetContents_7)
        self.seqCurrentLabel.setText(_fromUtf8(""))
        self.seqCurrentLabel.setObjectName(_fromUtf8("seqCurrentLabel"))
        self.verticalLayout.addWidget(self.seqCurrentLabel)
        spacerItem4 = QtGui.QSpacerItem(13, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 2, 1)
        self.sequenceParamList = ParamList(self.dockWidgetContents_7)
        self.sequenceParamList.setDragEnabled(True)
        self.sequenceParamList.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.sequenceParamList.setIndentation(10)
        self.sequenceParamList.setRootIsDecorated(True)
        self.sequenceParamList.setAnimated(True)
        self.sequenceParamList.setAllColumnsShowFocus(True)
        self.sequenceParamList.setObjectName(_fromUtf8("sequenceParamList"))
        self.gridLayout_2.addWidget(self.sequenceParamList, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.testSequenceBtn = QtGui.QPushButton(self.dockWidgetContents_7)
        self.testSequenceBtn.setEnabled(False)
        self.testSequenceBtn.setObjectName(_fromUtf8("testSequenceBtn"))
        self.horizontalLayout_3.addWidget(self.testSequenceBtn)
        spacerItem5 = QtGui.QSpacerItem(38, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.runSequenceBtn = QtGui.QPushButton(self.dockWidgetContents_7)
        self.runSequenceBtn.setEnabled(False)
        self.runSequenceBtn.setObjectName(_fromUtf8("runSequenceBtn"))
        self.horizontalLayout_3.addWidget(self.runSequenceBtn)
        self.pauseSequenceBtn = QtGui.QPushButton(self.dockWidgetContents_7)
        self.pauseSequenceBtn.setMinimumSize(QtCore.QSize(40, 0))
        self.pauseSequenceBtn.setCheckable(True)
        self.pauseSequenceBtn.setObjectName(_fromUtf8("pauseSequenceBtn"))
        self.horizontalLayout_3.addWidget(self.pauseSequenceBtn)
        spacerItem6 = QtGui.QSpacerItem(58, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.stopSequenceBtn = QtGui.QPushButton(self.dockWidgetContents_7)
        self.stopSequenceBtn.setObjectName(_fromUtf8("stopSequenceBtn"))
        self.horizontalLayout_3.addWidget(self.stopSequenceBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)
        self.SequenceDock.setWidget(self.dockWidgetContents_7)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.SequenceDock)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable|QtGui.QDockWidget.DockWidgetVerticalTitleBar)
        self.dockWidget.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.TopDockWidgetArea)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.dockWidgetContents_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.analysisList = QtGui.QListWidget(self.dockWidgetContents_2)
        self.analysisList.setObjectName(_fromUtf8("analysisList"))
        self.horizontalLayout_4.addWidget(self.analysisList)
        self.dockWidget.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Protocol Runner", None, QtGui.QApplication.UnicodeUTF8))
        self.LoaderDock.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Loader", None, QtGui.QApplication.UnicodeUTF8))
        self.ProtocolDock.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Protocol", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Devices", None, QtGui.QApplication.UnicodeUTF8))
        self.protoContinuousCheck.setToolTip(QtGui.QApplication.translate("MainWindow", "Protocol runs continuously without \n"
"gaps until stopped (not yet implemented).", None, QtGui.QApplication.UnicodeUTF8))
        self.protoContinuousCheck.setText(QtGui.QApplication.translate("MainWindow", "Continuous", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Duration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Lead Time", None, QtGui.QApplication.UnicodeUTF8))
        self.protoLoopCheck.setToolTip(QtGui.QApplication.translate("MainWindow", "Protocol will run repeatedly until stopped and \n"
"waits a minimum of Cycle Time between episodes.\n"
"Not the same as continuous acquisition (there \n"
"will be a time gap between each recording).", None, QtGui.QApplication.UnicodeUTF8))
        self.protoLoopCheck.setText(QtGui.QApplication.translate("MainWindow", "Loop", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Cycle Time", None, QtGui.QApplication.UnicodeUTF8))
        self.testSingleBtn.setText(QtGui.QApplication.translate("MainWindow", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.runProtocolBtn.setText(QtGui.QApplication.translate("MainWindow", "Record Single", None, QtGui.QApplication.UnicodeUTF8))
        self.stopSingleBtn.setText(QtGui.QApplication.translate("MainWindow", "Stop Single", None, QtGui.QApplication.UnicodeUTF8))
        self.protoDurationSpin.setToolTip(QtGui.QApplication.translate("MainWindow", "Duration of stimulus/acquisition in the protocol.", None, QtGui.QApplication.UnicodeUTF8))
        self.protoLeadTimeSpin.setToolTip(QtGui.QApplication.translate("MainWindow", "Duration of time to wait before acquisition starts \n"
"(the hardware is reserved so nothing else can \n"
"run during this time).", None, QtGui.QApplication.UnicodeUTF8))
        self.protoCycleTimeSpin.setToolTip(QtGui.QApplication.translate("MainWindow", "The minimum time to wait between recordings \n"
"in loop mode.", None, QtGui.QApplication.UnicodeUTF8))
        self.SequenceDock.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Sequence Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Cycle Time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Repetitions", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Parameter Space: ", None, QtGui.QApplication.UnicodeUTF8))
        self.paramSpaceLabel.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Total time:", None, QtGui.QApplication.UnicodeUTF8))
        self.seqTimeLabel.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.sequenceParamList.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "dev", None, QtGui.QApplication.UnicodeUTF8))
        self.sequenceParamList.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "param", None, QtGui.QApplication.UnicodeUTF8))
        self.sequenceParamList.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "len", None, QtGui.QApplication.UnicodeUTF8))
        self.testSequenceBtn.setText(QtGui.QApplication.translate("MainWindow", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.runSequenceBtn.setText(QtGui.QApplication.translate("MainWindow", "Record Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.pauseSequenceBtn.setText(QtGui.QApplication.translate("MainWindow", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.stopSequenceBtn.setText(QtGui.QApplication.translate("MainWindow", "Stop Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Analysis", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import SpinBox
from ParamList import ParamList
