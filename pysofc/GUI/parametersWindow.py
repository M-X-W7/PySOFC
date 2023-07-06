# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parameters.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ParameterManager(object):
    def setupUi(self, ParameterManager):
        ParameterManager.setObjectName("ParameterManager")
        ParameterManager.resize(972, 667)
        self.centralwidget = QtWidgets.QWidget(ParameterManager)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setFrameShape(QtWidgets.QFrame.Box)
        self.splitter.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.splitter.setLineWidth(1)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(121, 0))
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.thickness_anode_electrode = QtWidgets.QLineEdit(self.groupBox)
        self.thickness_anode_electrode.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.thickness_anode_electrode.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.thickness_anode_electrode.setClearButtonEnabled(False)
        self.thickness_anode_electrode.setObjectName("thickness_anode_electrode")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.thickness_anode_electrode)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.thickness_cathode_electrode = QtWidgets.QLineEdit(self.groupBox)
        self.thickness_cathode_electrode.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.thickness_cathode_electrode.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.thickness_cathode_electrode.setClearButtonEnabled(False)
        self.thickness_cathode_electrode.setObjectName("thickness_cathode_electrode")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.thickness_cathode_electrode)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.thickness_electrolyte = QtWidgets.QLineEdit(self.groupBox)
        self.thickness_electrolyte.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.thickness_electrolyte.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.thickness_electrolyte.setClearButtonEnabled(False)
        self.thickness_electrolyte.setObjectName("thickness_electrolyte")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.thickness_electrolyte)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.total_electroactive_area = QtWidgets.QLineEdit(self.groupBox)
        self.total_electroactive_area.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.total_electroactive_area.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.total_electroactive_area.setClearButtonEnabled(False)
        self.total_electroactive_area.setObjectName("total_electroactive_area")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.total_electroactive_area)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.channel_width = QtWidgets.QLineEdit(self.groupBox)
        self.channel_width.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.channel_width.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.channel_width.setClearButtonEnabled(False)
        self.channel_width.setObjectName("channel_width")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.channel_width)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.channel_height = QtWidgets.QLineEdit(self.groupBox)
        self.channel_height.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.channel_height.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.channel_height.setClearButtonEnabled(False)
        self.channel_height.setObjectName("channel_height")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.channel_height)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.channel_length = QtWidgets.QLineEdit(self.groupBox)
        self.channel_length.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.channel_length.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.channel_length.setClearButtonEnabled(False)
        self.channel_length.setObjectName("channel_length")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.channel_length)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setMinimumSize(QtCore.QSize(121, 0))
        self.label_15.setObjectName("label_15")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.porosity = QtWidgets.QLineEdit(self.groupBox_3)
        self.porosity.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.porosity.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.porosity.setClearButtonEnabled(False)
        self.porosity.setObjectName("porosity")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.porosity)
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.tortuosity = QtWidgets.QLineEdit(self.groupBox_3)
        self.tortuosity.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.tortuosity.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.tortuosity.setClearButtonEnabled(False)
        self.tortuosity.setObjectName("tortuosity")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tortuosity)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.pore_diameter = QtWidgets.QLineEdit(self.groupBox_3)
        self.pore_diameter.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.pore_diameter.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.pore_diameter.setClearButtonEnabled(False)
        self.pore_diameter.setObjectName("pore_diameter")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pore_diameter)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setMinimumSize(QtCore.QSize(121, 0))
        self.label_14.setTextFormat(QtCore.Qt.RichText)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.activation_energy_fuel = QtWidgets.QLineEdit(self.groupBox_2)
        self.activation_energy_fuel.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.activation_energy_fuel.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.activation_energy_fuel.setClearButtonEnabled(False)
        self.activation_energy_fuel.setObjectName("activation_energy_fuel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.activation_energy_fuel)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.activation_energy_oxygen = QtWidgets.QLineEdit(self.groupBox_2)
        self.activation_energy_oxygen.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.activation_energy_oxygen.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.activation_energy_oxygen.setClearButtonEnabled(False)
        self.activation_energy_oxygen.setObjectName("activation_energy_oxygen")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.activation_energy_oxygen)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.pre_exp_factor_fuel = QtWidgets.QLineEdit(self.groupBox_2)
        self.pre_exp_factor_fuel.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.pre_exp_factor_fuel.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.pre_exp_factor_fuel.setClearButtonEnabled(False)
        self.pre_exp_factor_fuel.setObjectName("pre_exp_factor_fuel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pre_exp_factor_fuel)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.pre_exp_factor_oxygen = QtWidgets.QLineEdit(self.groupBox_2)
        self.pre_exp_factor_oxygen.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.pre_exp_factor_oxygen.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.pre_exp_factor_oxygen.setClearButtonEnabled(False)
        self.pre_exp_factor_oxygen.setObjectName("pre_exp_factor_oxygen")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pre_exp_factor_oxygen)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_18.setMinimumSize(QtCore.QSize(251, 191))
        self.label_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("C:/Users/burak/Downloads/equation (2).png"))
        self.label_18.setScaledContents(False)
        self.label_18.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout.addWidget(self.label_18)
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 10, 5, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.groupBox_4)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setMinimumSize(QtCore.QSize(121, 0))
        self.label_16.setTextFormat(QtCore.Qt.RichText)
        self.label_16.setObjectName("label_16")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.activation_energy_electrolyte = QtWidgets.QLineEdit(self.groupBox_4)
        self.activation_energy_electrolyte.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.activation_energy_electrolyte.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.activation_energy_electrolyte.setClearButtonEnabled(False)
        self.activation_energy_electrolyte.setObjectName("activation_energy_electrolyte")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.activation_energy_electrolyte)
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setObjectName("label_12")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.pre_exp_factor_electrolyte = QtWidgets.QLineEdit(self.groupBox_4)
        self.pre_exp_factor_electrolyte.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.pre_exp_factor_electrolyte.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.pre_exp_factor_electrolyte.setClearButtonEnabled(False)
        self.pre_exp_factor_electrolyte.setObjectName("pre_exp_factor_electrolyte")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pre_exp_factor_electrolyte)
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setTextFormat(QtCore.Qt.RichText)
        self.label_17.setObjectName("label_17")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.other_ohmic_resistance = QtWidgets.QLineEdit(self.groupBox_4)
        self.other_ohmic_resistance.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.other_ohmic_resistance.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.other_ohmic_resistance.setClearButtonEnabled(False)
        self.other_ohmic_resistance.setObjectName("other_ohmic_resistance")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.other_ohmic_resistance)
        self.horizontalLayout_2.addWidget(self.groupBox_4)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("C:/Users/burak/Downloads/equation (3).png"))
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_2.addWidget(self.label_19)
        self.horizontalLayout_5.addWidget(self.splitter)
        self.rightBar = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightBar.sizePolicy().hasHeightForWidth())
        self.rightBar.setSizePolicy(sizePolicy)
        self.rightBar.setMinimumSize(QtCore.QSize(50, 0))
        self.rightBar.setObjectName("rightBar")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.rightBar)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.cell_id = QtWidgets.QLineEdit(self.rightBar)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cell_id.setFont(font)
        self.cell_id.setObjectName("cell_id")
        self.gridLayout.addWidget(self.cell_id, 2, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.rightBar)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.applyChanges = QtWidgets.QPushButton(self.rightBar)
        self.applyChanges.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.applyChanges.setFont(font)
        self.applyChanges.setObjectName("applyChanges")
        self.verticalLayout_2.addWidget(self.applyChanges)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_20 = QtWidgets.QLabel(self.rightBar)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setTextFormat(QtCore.Qt.RichText)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_4.addWidget(self.label_20)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.saveFile = QtWidgets.QPushButton(self.rightBar)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.saveFile.setFont(font)
        self.saveFile.setObjectName("saveFile")
        self.verticalLayout.addWidget(self.saveFile)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.loadFile = QtWidgets.QPushButton(self.rightBar)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.loadFile.setFont(font)
        self.loadFile.setObjectName("loadFile")
        self.verticalLayout_2.addWidget(self.loadFile)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem4)
        self.textBrowser = QtWidgets.QTextBrowser(self.rightBar)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5.addWidget(self.rightBar)
        ParameterManager.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ParameterManager)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 972, 21))
        self.menubar.setObjectName("menubar")
        ParameterManager.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ParameterManager)
        self.statusbar.setObjectName("statusbar")
        ParameterManager.setStatusBar(self.statusbar)

        self.retranslateUi(ParameterManager)
        QtCore.QMetaObject.connectSlotsByName(ParameterManager)

    def retranslateUi(self, ParameterManager):
        _translate = QtCore.QCoreApplication.translate
        ParameterManager.setWindowTitle(_translate("ParameterManager", "Cell Parameters"))
        self.groupBox.setTitle(_translate("ParameterManager", "Cell Dimensional Parameters"))
        self.label.setText(_translate("ParameterManager", "Thickness of Anode Electrode (m)"))
        self.label_2.setText(_translate("ParameterManager", "Thickness of Cathode Electrode (m)"))
        self.label_3.setText(_translate("ParameterManager", "Thickness of Electrolyte (m)"))
        self.label_7.setText(_translate("ParameterManager", "Total Electroactive Area (m<sup>2</sup>)"))
        self.label_4.setText(_translate("ParameterManager", "Channel width (m)"))
        self.label_5.setText(_translate("ParameterManager", "Channel height (m)"))
        self.label_6.setText(_translate("ParameterManager", "Channel length (m)"))
        self.groupBox_3.setTitle(_translate("ParameterManager", "Parameters for Diffusion Polarization"))
        self.label_15.setText(_translate("ParameterManager", "Porosity (average)"))
        self.label_10.setText(_translate("ParameterManager", "Tortuosity (average)"))
        self.label_11.setText(_translate("ParameterManager", "<html><head/><body><p>Average Pore Diameter (m)</p></body></html>"))
        self.groupBox_2.setTitle(_translate("ParameterManager", "Parameters for Activation Polarization"))
        self.label_14.setText(_translate("ParameterManager", "<html><head/><body><p>Activation Energy Fuel (J/mol): <span style=\" font-size:10pt; font-weight:600;\">E</span><span style=\" font-size:10pt; font-weight:600; vertical-align:sub;\">act,fuel</span></p></body></html>"))
        self.label_8.setText(_translate("ParameterManager", "<html><head/><body><p>Activation Energy Oxidant (J/mol): <span style=\" font-weight:600;\">γ</span><span style=\" font-weight:600; vertical-align:sub;\">fuel</span></p></body></html>"))
        self.label_9.setText(_translate("ParameterManager", "<html><head/><body><p>Pre-exponential Factor Fuel (A/m<span style=\" vertical-align:super;\">2</span>):<span style=\" font-weight:600;\"> E</span><span style=\" font-weight:600; vertical-align:sub;\">act,oxy</span></p></body></html>"))
        self.label_13.setText(_translate("ParameterManager", "<html><head/><body><p>Pre-exponential Factor Oxidant (A/m<span style=\" vertical-align:super;\">2</span>): <span style=\" font-weight:600;\">γ</span><span style=\" font-weight:600; vertical-align:sub;\">oxy</span><span style=\" font-weight:600;\"/></p></body></html>"))
        self.groupBox_4.setTitle(_translate("ParameterManager", "Parameters for Ohmic Polarization"))
        self.label_16.setText(_translate("ParameterManager", "<html><head/><body><p>Activation Energy Electrolyte (J/mol):<span style=\" font-weight:600;\"> E</span><span style=\" font-weight:600; vertical-align:sub;\">act,el</span></p></body></html>"))
        self.label_12.setText(_translate("ParameterManager", "<html><head/><body><p>Pre-exponential Factor Electrolyte (ohm<span style=\" vertical-align:super;\">-1</span>.m<span style=\" vertical-align:super;\">-1</span>): <span style=\" font-weight:600;\">σ</span><span style=\" font-weight:600; vertical-align:sub;\">0,el</span></p></body></html>"))
        self.label_17.setText(_translate("ParameterManager", "<html><head/><body><p>Other Ohmic Resistances (ohm.m<span style=\" vertical-align:super;\">2</span>):<span style=\" font-weight:600;\"> r</span><span style=\" font-weight:600; vertical-align:sub;\">other</span></p></body></html>"))
        self.label_22.setText(_translate("ParameterManager", "Name or ID of SOFC. Eg: julich_18_stack"))
        self.applyChanges.setText(_translate("ParameterManager", "Apply changes and return simulation"))
        self.label_20.setText(_translate("ParameterManager", "<html><head/><body><p><span style=\" color:#0055ff;\">Save parameters to JSON file</span></p></body></html>"))
        self.saveFile.setText(_translate("ParameterManager", "Save as file "))
        self.loadFile.setText(_translate("ParameterManager", "Load from existing data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ParameterManager = QtWidgets.QMainWindow()
    ui = Ui_ParameterManager()
    ui.setupUi(ParameterManager)
    ParameterManager.show()
    sys.exit(app.exec_())
