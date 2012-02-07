# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './lib/util/pyqtgraph/imageview/ImageViewTemplate.ui'
#
# Created: Mon Feb  6 23:48:27 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(726, 588)
        self.gridLayout_3 = QtGui.QGridLayout(Form)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.graphicsView = GraphicsView(self.layoutWidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 2, 1)
        self.histogram = HistogramLUTWidget(self.layoutWidget)
        self.histogram.setObjectName(_fromUtf8("histogram"))
        self.gridLayout.addWidget(self.histogram, 0, 1, 1, 2)
        self.roiBtn = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.roiBtn.sizePolicy().hasHeightForWidth())
        self.roiBtn.setSizePolicy(sizePolicy)
        self.roiBtn.setCheckable(True)
        self.roiBtn.setObjectName(_fromUtf8("roiBtn"))
        self.gridLayout.addWidget(self.roiBtn, 1, 1, 1, 1)
        self.normBtn = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.normBtn.sizePolicy().hasHeightForWidth())
        self.normBtn.setSizePolicy(sizePolicy)
        self.normBtn.setCheckable(True)
        self.normBtn.setObjectName(_fromUtf8("normBtn"))
        self.gridLayout.addWidget(self.normBtn, 1, 2, 1, 1)
        self.roiPlot = PlotWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roiPlot.sizePolicy().hasHeightForWidth())
        self.roiPlot.setSizePolicy(sizePolicy)
        self.roiPlot.setMinimumSize(QtCore.QSize(0, 40))
        self.roiPlot.setObjectName(_fromUtf8("roiPlot"))
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)
        self.normGroup = QtGui.QGroupBox(Form)
        self.normGroup.setObjectName(_fromUtf8("normGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.normGroup)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.normSubtractRadio = QtGui.QRadioButton(self.normGroup)
        self.normSubtractRadio.setObjectName(_fromUtf8("normSubtractRadio"))
        self.gridLayout_2.addWidget(self.normSubtractRadio, 0, 2, 1, 1)
        self.normDivideRadio = QtGui.QRadioButton(self.normGroup)
        self.normDivideRadio.setChecked(False)
        self.normDivideRadio.setObjectName(_fromUtf8("normDivideRadio"))
        self.gridLayout_2.addWidget(self.normDivideRadio, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.normGroup)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.normGroup)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.normGroup)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.normROICheck = QtGui.QCheckBox(self.normGroup)
        self.normROICheck.setObjectName(_fromUtf8("normROICheck"))
        self.gridLayout_2.addWidget(self.normROICheck, 1, 1, 1, 1)
        self.normXBlurSpin = QtGui.QDoubleSpinBox(self.normGroup)
        self.normXBlurSpin.setObjectName(_fromUtf8("normXBlurSpin"))
        self.gridLayout_2.addWidget(self.normXBlurSpin, 2, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.normGroup)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 2, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.normGroup)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 2, 3, 1, 1)
        self.normYBlurSpin = QtGui.QDoubleSpinBox(self.normGroup)
        self.normYBlurSpin.setObjectName(_fromUtf8("normYBlurSpin"))
        self.gridLayout_2.addWidget(self.normYBlurSpin, 2, 4, 1, 1)
        self.label_10 = QtGui.QLabel(self.normGroup)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 2, 5, 1, 1)
        self.normOffRadio = QtGui.QRadioButton(self.normGroup)
        self.normOffRadio.setChecked(True)
        self.normOffRadio.setObjectName(_fromUtf8("normOffRadio"))
        self.gridLayout_2.addWidget(self.normOffRadio, 0, 3, 1, 1)
        self.normTimeRangeCheck = QtGui.QCheckBox(self.normGroup)
        self.normTimeRangeCheck.setObjectName(_fromUtf8("normTimeRangeCheck"))
        self.gridLayout_2.addWidget(self.normTimeRangeCheck, 1, 3, 1, 1)
        self.normFrameCheck = QtGui.QCheckBox(self.normGroup)
        self.normFrameCheck.setObjectName(_fromUtf8("normFrameCheck"))
        self.gridLayout_2.addWidget(self.normFrameCheck, 1, 2, 1, 1)
        self.normTBlurSpin = QtGui.QDoubleSpinBox(self.normGroup)
        self.normTBlurSpin.setObjectName(_fromUtf8("normTBlurSpin"))
        self.gridLayout_2.addWidget(self.normTBlurSpin, 2, 6, 1, 1)
        self.gridLayout_3.addWidget(self.normGroup, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.roiBtn.setText(QtGui.QApplication.translate("Form", "ROI", None, QtGui.QApplication.UnicodeUTF8))
        self.normBtn.setText(QtGui.QApplication.translate("Form", "Norm", None, QtGui.QApplication.UnicodeUTF8))
        self.normGroup.setTitle(QtGui.QApplication.translate("Form", "Normalization", None, QtGui.QApplication.UnicodeUTF8))
        self.normSubtractRadio.setText(QtGui.QApplication.translate("Form", "Subtract", None, QtGui.QApplication.UnicodeUTF8))
        self.normDivideRadio.setText(QtGui.QApplication.translate("Form", "Divide", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Operation:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Mean:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Blur:", None, QtGui.QApplication.UnicodeUTF8))
        self.normROICheck.setText(QtGui.QApplication.translate("Form", "ROI", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Form", "T", None, QtGui.QApplication.UnicodeUTF8))
        self.normOffRadio.setText(QtGui.QApplication.translate("Form", "Off", None, QtGui.QApplication.UnicodeUTF8))
        self.normTimeRangeCheck.setText(QtGui.QApplication.translate("Form", "Time range", None, QtGui.QApplication.UnicodeUTF8))
        self.normFrameCheck.setText(QtGui.QApplication.translate("Form", "Frame", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph.widgets.GraphicsView import GraphicsView
from pyqtgraph.widgets.PlotWidget import PlotWidget
from pyqtgraph.widgets.HistogramLUTWidget import HistogramLUTWidget
