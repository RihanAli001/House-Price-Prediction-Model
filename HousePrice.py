# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HousePrice.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("web_hi_res_512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setStyleSheet("background:rgb(0, 0, 0)")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setToolTip("")
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 777, 767))
        self.scrollAreaWidgetContents.setStyleSheet("QLabel{\n"
"    color:rgb(255, 255, 255);\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QLineEdit{\n"
"    color:rgb(255, 255, 255);\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"    padding:10px;\n"
"}\n"
"QComboBox{\n"
"    color:rgb(255, 255, 255);\n"
"    border:1px solid white;\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"    padding:10px;\n"
"}\n"
"QPushButton{\n"
"    color:rgb(255, 255, 255);\n"
"    border:2px solid white;\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QSpinBox{\n"
"    color:rgb(255, 255, 255);\n"
"    border:1px solid white;\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"    padding:10px;\n"
"}")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setObjectName("formLayout")
        self.noOfBathroom = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.noOfBathroom.setObjectName("noOfBathroom")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.noOfBathroom)
        self.noOfBathroomSpinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.noOfBathroomSpinBox.setMinimumSize(QtCore.QSize(0, 40))
        self.noOfBathroomSpinBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.noOfBathroomSpinBox.setObjectName("noOfBathroomSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.noOfBathroomSpinBox)
        self.flatArea = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.flatArea.setObjectName("flatArea")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.flatArea)
        self.flatAreaLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.flatAreaLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.flatAreaLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.flatAreaLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.flatAreaLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.flatAreaLineEdit.setObjectName("flatAreaLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.flatAreaLineEdit)
        self.lotArea = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lotArea.setObjectName("lotArea")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lotArea)
        self.lotAreaLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lotAreaLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.lotAreaLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lotAreaLineEdit.setObjectName("lotAreaLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lotAreaLineEdit)
        self.noOfTimesVisited = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.noOfTimesVisited.setObjectName("noOfTimesVisited")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.noOfTimesVisited)
        self.noOfTimesVisitedLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.noOfTimesVisitedLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.noOfTimesVisitedLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.noOfTimesVisitedLineEdit.setObjectName("noOfTimesVisitedLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.noOfTimesVisitedLineEdit)
        self.overallGrade = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.overallGrade.setObjectName("overallGrade")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.overallGrade)
        self.overallGradeLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.overallGradeLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.overallGradeLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.overallGradeLineEdit.setObjectName("overallGradeLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.overallGradeLineEdit)
        self.basementArea = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.basementArea.setObjectName("basementArea")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.basementArea)
        self.basementAreaLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.basementAreaLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.basementAreaLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.basementAreaLineEdit.setObjectName("basementAreaLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.basementAreaLineEdit)
        self.ageOfHouseLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.ageOfHouseLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.ageOfHouseLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.ageOfHouseLineEdit.setObjectName("ageOfHouseLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.ageOfHouseLineEdit)
        self.latitude = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.latitude.setObjectName("latitude")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.latitude)
        self.latitudeLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.latitudeLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.latitudeLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.latitudeLineEdit.setObjectName("latitudeLineEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.latitudeLineEdit)
        self.longitude = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.longitude.setObjectName("longitude")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.longitude)
        self.longitudeLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.longitudeLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.longitudeLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.longitudeLineEdit.setObjectName("longitudeLineEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.longitudeLineEdit)
        self.livingAreaAfterRenovation = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.livingAreaAfterRenovation.setObjectName("livingAreaAfterRenovation")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.livingAreaAfterRenovation)
        self.livingAreaAfterRenovationLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.livingAreaAfterRenovationLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.livingAreaAfterRenovationLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.livingAreaAfterRenovationLineEdit.setObjectName("livingAreaAfterRenovationLineEdit")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.livingAreaAfterRenovationLineEdit)
        self.yearsSinceRenovation = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.yearsSinceRenovation.setObjectName("yearsSinceRenovation")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.yearsSinceRenovation)
        self.yearsSinceRenovationLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.yearsSinceRenovationLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.yearsSinceRenovationLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.yearsSinceRenovationLineEdit.setObjectName("yearsSinceRenovationLineEdit")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.yearsSinceRenovationLineEdit)
        self.condition = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.condition.setStyleSheet("")
        self.condition.setObjectName("condition")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.condition)
        self.conditionComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.conditionComboBox.setMinimumSize(QtCore.QSize(0, 40))
        self.conditionComboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.conditionComboBox.setObjectName("conditionComboBox")
        self.conditionComboBox.addItem("")
        self.conditionComboBox.addItem("")
        self.conditionComboBox.addItem("")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.conditionComboBox)
        self.waterfronView = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.waterfronView.setObjectName("waterfronView")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.waterfronView)
        self.waterfrontViewComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.waterfrontViewComboBox.setMinimumSize(QtCore.QSize(0, 40))
        self.waterfrontViewComboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.waterfrontViewComboBox.setObjectName("waterfrontViewComboBox")
        self.waterfrontViewComboBox.addItem("")
        self.waterfrontViewComboBox.addItem("")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.waterfrontViewComboBox)
        self.everRenovate = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.everRenovate.setObjectName("everRenovate")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.everRenovate)
        self.everRenovateComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.everRenovateComboBox.setMinimumSize(QtCore.QSize(0, 40))
        self.everRenovateComboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.everRenovateComboBox.setObjectName("everRenovateComboBox")
        self.everRenovateComboBox.addItem("")
        self.everRenovateComboBox.addItem("")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.everRenovateComboBox)
        self.zipcodeGroup = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.zipcodeGroup.setObjectName("zipcodeGroup")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.zipcodeGroup)
        self.zipcodeGroupComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.zipcodeGroupComboBox.setMinimumSize(QtCore.QSize(0, 40))
        self.zipcodeGroupComboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.zipcodeGroupComboBox.setObjectName("zipcodeGroupComboBox")
        self.zipcodeGroupComboBox.addItem("")
        self.zipcodeGroupComboBox.addItem("")
        self.zipcodeGroupComboBox.addItem("")
        self.zipcodeGroupComboBox.addItem("")
        self.zipcodeGroupComboBox.addItem("")
        self.zipcodeGroupComboBox.addItem("")
        self.zipcodeGroupComboBox.addItem("")
        self.zipcodeGroupComboBox.addItem("")
        self.zipcodeGroupComboBox.addItem("")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.zipcodeGroupComboBox)
        self.predictBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.predictBtn.setMinimumSize(QtCore.QSize(150, 40))
        self.predictBtn.setObjectName("predictBtn")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.predictBtn)
        self.resultPriceLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.resultPriceLabel.setMaximumSize(QtCore.QSize(200, 16777215))
        self.resultPriceLabel.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.resultPriceLabel.setObjectName("resultPriceLabel")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.resultPriceLabel)
        self.ageOfHouse = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ageOfHouse.setObjectName("ageOfHouse")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.ageOfHouse)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RHouse Price Prediction"))
        self.noOfBathroom.setText(_translate("MainWindow", "No of Bathrooms"))
        self.noOfBathroomSpinBox.setToolTip(_translate("MainWindow", "Set count"))
        self.flatArea.setText(_translate("MainWindow", "Flat Area (in Sqft)"))
        self.flatAreaLineEdit.setToolTip(_translate("MainWindow", "Numeric data only"))
        self.lotArea.setText(_translate("MainWindow", "Lot Area (in Sqft)"))
        self.lotAreaLineEdit.setToolTip(_translate("MainWindow", "Numeric data only"))
        self.noOfTimesVisited.setText(_translate("MainWindow", "No of Times Visited"))
        self.noOfTimesVisitedLineEdit.setToolTip(_translate("MainWindow", "Numeric data only"))
        self.overallGrade.setText(_translate("MainWindow", "Overall Grade"))
        self.overallGradeLineEdit.setToolTip(_translate("MainWindow", "Numeric data only"))
        self.basementArea.setText(_translate("MainWindow", "Basement Area (in Sqft)"))
        self.basementAreaLineEdit.setToolTip(_translate("MainWindow", "Numeric data only"))
        self.ageOfHouseLineEdit.setToolTip(_translate("MainWindow", "Numeric data only"))
        self.latitude.setText(_translate("MainWindow", "Latitude"))
        self.latitudeLineEdit.setToolTip(_translate("MainWindow", "Numeric data only"))
        self.longitude.setText(_translate("MainWindow", "Longitude"))
        self.longitudeLineEdit.setToolTip(_translate("MainWindow", "Numeric data only"))
        self.livingAreaAfterRenovation.setText(_translate("MainWindow", "Living Area after Renovation (in Sqft)"))
        self.livingAreaAfterRenovationLineEdit.setToolTip(_translate("MainWindow", "Numeric data only"))
        self.yearsSinceRenovation.setText(_translate("MainWindow", "Years since Renovation"))
        self.yearsSinceRenovationLineEdit.setToolTip(_translate("MainWindow", "Numeric data only"))
        self.condition.setText(_translate("MainWindow", "Condition"))
        self.conditionComboBox.setToolTip(_translate("MainWindow", "Select any one option"))
        self.conditionComboBox.setItemText(0, _translate("MainWindow", "Excellent"))
        self.conditionComboBox.setItemText(1, _translate("MainWindow", "Good"))
        self.conditionComboBox.setItemText(2, _translate("MainWindow", "Fair"))
        self.waterfronView.setText(_translate("MainWindow", "Waterfront View"))
        self.waterfrontViewComboBox.setToolTip(_translate("MainWindow", "Select any one option"))
        self.waterfrontViewComboBox.setItemText(0, _translate("MainWindow", "Yes"))
        self.waterfrontViewComboBox.setItemText(1, _translate("MainWindow", "No"))
        self.everRenovate.setText(_translate("MainWindow", "Ever Renovate"))
        self.everRenovateComboBox.setToolTip(_translate("MainWindow", "Select any one option"))
        self.everRenovateComboBox.setItemText(0, _translate("MainWindow", "Yes"))
        self.everRenovateComboBox.setItemText(1, _translate("MainWindow", "No"))
        self.zipcodeGroup.setText(_translate("MainWindow", "Zipcode Group"))
        self.zipcodeGroupComboBox.setToolTip(_translate("MainWindow", "Select any one option"))
        self.zipcodeGroupComboBox.setItemText(0, _translate("MainWindow", "Group 1"))
        self.zipcodeGroupComboBox.setItemText(1, _translate("MainWindow", "Group 2"))
        self.zipcodeGroupComboBox.setItemText(2, _translate("MainWindow", "Group 3"))
        self.zipcodeGroupComboBox.setItemText(3, _translate("MainWindow", "Group 4"))
        self.zipcodeGroupComboBox.setItemText(4, _translate("MainWindow", "Group 5"))
        self.zipcodeGroupComboBox.setItemText(5, _translate("MainWindow", "Group 6"))
        self.zipcodeGroupComboBox.setItemText(6, _translate("MainWindow", "Group 7"))
        self.zipcodeGroupComboBox.setItemText(7, _translate("MainWindow", "Group 8"))
        self.zipcodeGroupComboBox.setItemText(8, _translate("MainWindow", "Group 9"))
        self.predictBtn.setToolTip(_translate("MainWindow", "Click to predict price"))
        self.predictBtn.setText(_translate("MainWindow", "Predict"))
        self.resultPriceLabel.setToolTip(_translate("MainWindow", "Predicted Price"))
        self.resultPriceLabel.setText(_translate("MainWindow", "Rs. 0.0"))
        self.ageOfHouse.setText(_translate("MainWindow", "Age of House (in Years)"))
