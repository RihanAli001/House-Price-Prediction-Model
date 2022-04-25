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
        MainWindow.resize(997, 629)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("web_hi_res_512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setStyleSheet("background-color: rgb(104, 0, 104);")
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
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 995, 627))
        self.scrollAreaWidgetContents.setStyleSheet("QLabel{\n"
"font: 10pt \"Times New Roman\";\n"
"}\n"
"QLineEdit, QComboBox{\n"
"border: 1px solid black;\n"
"}")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMaximumSize(QtCore.QSize(1000, 600))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding:10px;\n"
"margin: 10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.noOfBathroom = QtWidgets.QLabel(self.frame)
        self.noOfBathroom.setObjectName("noOfBathroom")
        self.gridLayout.addWidget(self.noOfBathroom, 0, 0, 1, 1)
        self.noOfBathroomSpinBox = QtWidgets.QSpinBox(self.frame)
        self.noOfBathroomSpinBox.setMinimumSize(QtCore.QSize(0, 40))
        self.noOfBathroomSpinBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.noOfBathroomSpinBox.setStyleSheet("")
        self.noOfBathroomSpinBox.setObjectName("noOfBathroomSpinBox")
        self.gridLayout.addWidget(self.noOfBathroomSpinBox, 0, 1, 1, 1)
        self.everRenovate = QtWidgets.QLabel(self.frame)
        self.everRenovate.setObjectName("everRenovate")
        self.gridLayout.addWidget(self.everRenovate, 0, 2, 1, 1)
        self.everRenovateComboBox = QtWidgets.QComboBox(self.frame)
        self.everRenovateComboBox.setMinimumSize(QtCore.QSize(0, 40))
        self.everRenovateComboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.everRenovateComboBox.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.everRenovateComboBox.setObjectName("everRenovateComboBox")
        self.everRenovateComboBox.addItem("")
        self.everRenovateComboBox.addItem("")
        self.gridLayout.addWidget(self.everRenovateComboBox, 0, 3, 1, 1)
        self.flatArea = QtWidgets.QLabel(self.frame)
        self.flatArea.setObjectName("flatArea")
        self.gridLayout.addWidget(self.flatArea, 1, 0, 1, 1)
        self.flatAreaLineEdit = QtWidgets.QLineEdit(self.frame)
        self.flatAreaLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.flatAreaLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.flatAreaLineEdit.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.flatAreaLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.flatAreaLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.flatAreaLineEdit.setObjectName("flatAreaLineEdit")
        self.gridLayout.addWidget(self.flatAreaLineEdit, 1, 1, 1, 1)
        self.latitude = QtWidgets.QLabel(self.frame)
        self.latitude.setObjectName("latitude")
        self.gridLayout.addWidget(self.latitude, 1, 2, 1, 1)
        self.latitudeLineEdit = QtWidgets.QLineEdit(self.frame)
        self.latitudeLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.latitudeLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.latitudeLineEdit.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.latitudeLineEdit.setObjectName("latitudeLineEdit")
        self.gridLayout.addWidget(self.latitudeLineEdit, 1, 3, 1, 1)
        self.lotArea = QtWidgets.QLabel(self.frame)
        self.lotArea.setObjectName("lotArea")
        self.gridLayout.addWidget(self.lotArea, 2, 0, 1, 1)
        self.lotAreaLineEdit = QtWidgets.QLineEdit(self.frame)
        self.lotAreaLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.lotAreaLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lotAreaLineEdit.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.lotAreaLineEdit.setObjectName("lotAreaLineEdit")
        self.gridLayout.addWidget(self.lotAreaLineEdit, 2, 1, 1, 1)
        self.longitude = QtWidgets.QLabel(self.frame)
        self.longitude.setObjectName("longitude")
        self.gridLayout.addWidget(self.longitude, 2, 2, 1, 1)
        self.longitudeLineEdit = QtWidgets.QLineEdit(self.frame)
        self.longitudeLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.longitudeLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.longitudeLineEdit.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.longitudeLineEdit.setObjectName("longitudeLineEdit")
        self.gridLayout.addWidget(self.longitudeLineEdit, 2, 3, 1, 1)
        self.noOfTimesVisited = QtWidgets.QLabel(self.frame)
        self.noOfTimesVisited.setObjectName("noOfTimesVisited")
        self.gridLayout.addWidget(self.noOfTimesVisited, 3, 0, 1, 1)
        self.noOfTimesVisitedLineEdit = QtWidgets.QLineEdit(self.frame)
        self.noOfTimesVisitedLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.noOfTimesVisitedLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.noOfTimesVisitedLineEdit.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.noOfTimesVisitedLineEdit.setObjectName("noOfTimesVisitedLineEdit")
        self.gridLayout.addWidget(self.noOfTimesVisitedLineEdit, 3, 1, 1, 1)
        self.livingAreaAfterRenovation = QtWidgets.QLabel(self.frame)
        self.livingAreaAfterRenovation.setObjectName("livingAreaAfterRenovation")
        self.gridLayout.addWidget(self.livingAreaAfterRenovation, 3, 2, 1, 1)
        self.livingAreaAfterRenovationLineEdit = QtWidgets.QLineEdit(self.frame)
        self.livingAreaAfterRenovationLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.livingAreaAfterRenovationLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.livingAreaAfterRenovationLineEdit.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.livingAreaAfterRenovationLineEdit.setObjectName("livingAreaAfterRenovationLineEdit")
        self.gridLayout.addWidget(self.livingAreaAfterRenovationLineEdit, 3, 3, 1, 1)
        self.overallGrade = QtWidgets.QLabel(self.frame)
        self.overallGrade.setObjectName("overallGrade")
        self.gridLayout.addWidget(self.overallGrade, 4, 0, 1, 1)
        self.overallGradeLineEdit = QtWidgets.QLineEdit(self.frame)
        self.overallGradeLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.overallGradeLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.overallGradeLineEdit.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.overallGradeLineEdit.setObjectName("overallGradeLineEdit")
        self.gridLayout.addWidget(self.overallGradeLineEdit, 4, 1, 1, 1)
        self.yearsSinceRenovation = QtWidgets.QLabel(self.frame)
        self.yearsSinceRenovation.setObjectName("yearsSinceRenovation")
        self.gridLayout.addWidget(self.yearsSinceRenovation, 4, 2, 1, 1)
        self.yearsSinceRenovationLineEdit = QtWidgets.QLineEdit(self.frame)
        self.yearsSinceRenovationLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.yearsSinceRenovationLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.yearsSinceRenovationLineEdit.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.yearsSinceRenovationLineEdit.setObjectName("yearsSinceRenovationLineEdit")
        self.gridLayout.addWidget(self.yearsSinceRenovationLineEdit, 4, 3, 1, 1)
        self.basementArea = QtWidgets.QLabel(self.frame)
        self.basementArea.setObjectName("basementArea")
        self.gridLayout.addWidget(self.basementArea, 5, 0, 1, 1)
        self.basementAreaLineEdit = QtWidgets.QLineEdit(self.frame)
        self.basementAreaLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.basementAreaLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.basementAreaLineEdit.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.basementAreaLineEdit.setObjectName("basementAreaLineEdit")
        self.gridLayout.addWidget(self.basementAreaLineEdit, 5, 1, 1, 1)
        self.waterfronView = QtWidgets.QLabel(self.frame)
        self.waterfronView.setObjectName("waterfronView")
        self.gridLayout.addWidget(self.waterfronView, 5, 2, 1, 1)
        self.waterfrontViewComboBox = QtWidgets.QComboBox(self.frame)
        self.waterfrontViewComboBox.setMinimumSize(QtCore.QSize(0, 40))
        self.waterfrontViewComboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.waterfrontViewComboBox.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.waterfrontViewComboBox.setObjectName("waterfrontViewComboBox")
        self.waterfrontViewComboBox.addItem("")
        self.waterfrontViewComboBox.addItem("")
        self.gridLayout.addWidget(self.waterfrontViewComboBox, 5, 3, 1, 1)
        self.ageOfHouse = QtWidgets.QLabel(self.frame)
        self.ageOfHouse.setObjectName("ageOfHouse")
        self.gridLayout.addWidget(self.ageOfHouse, 6, 0, 1, 1)
        self.ageOfHouseLineEdit = QtWidgets.QLineEdit(self.frame)
        self.ageOfHouseLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.ageOfHouseLineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.ageOfHouseLineEdit.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.ageOfHouseLineEdit.setObjectName("ageOfHouseLineEdit")
        self.gridLayout.addWidget(self.ageOfHouseLineEdit, 6, 1, 1, 1)
        self.zipcodeGroup = QtWidgets.QLabel(self.frame)
        self.zipcodeGroup.setObjectName("zipcodeGroup")
        self.gridLayout.addWidget(self.zipcodeGroup, 6, 2, 1, 1)
        self.zipcodeGroupComboBox = QtWidgets.QComboBox(self.frame)
        self.zipcodeGroupComboBox.setMinimumSize(QtCore.QSize(0, 40))
        self.zipcodeGroupComboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.zipcodeGroupComboBox.setStyleSheet("background-color: rgb(198, 198, 198);")
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
        self.gridLayout.addWidget(self.zipcodeGroupComboBox, 6, 3, 1, 1)
        self.condition = QtWidgets.QLabel(self.frame)
        self.condition.setStyleSheet("")
        self.condition.setObjectName("condition")
        self.gridLayout.addWidget(self.condition, 7, 0, 1, 1)
        self.conditionComboBox = QtWidgets.QComboBox(self.frame)
        self.conditionComboBox.setMinimumSize(QtCore.QSize(0, 40))
        self.conditionComboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.conditionComboBox.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.conditionComboBox.setObjectName("conditionComboBox")
        self.conditionComboBox.addItem("")
        self.conditionComboBox.addItem("")
        self.conditionComboBox.addItem("")
        self.gridLayout.addWidget(self.conditionComboBox, 7, 1, 1, 1)
        self.predictBtn = QtWidgets.QPushButton(self.frame)
        self.predictBtn.setMinimumSize(QtCore.QSize(150, 40))
        self.predictBtn.setStyleSheet("background-color: #0083ce;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Times New Roman\";")
        self.predictBtn.setObjectName("predictBtn")
        self.gridLayout.addWidget(self.predictBtn, 7, 2, 1, 1)
        self.resultPriceLabel = QtWidgets.QLabel(self.frame)
        self.resultPriceLabel.setMaximumSize(QtCore.QSize(200, 16777215))
        self.resultPriceLabel.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.resultPriceLabel.setObjectName("resultPriceLabel")
        self.gridLayout.addWidget(self.resultPriceLabel, 7, 3, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame)
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
        self.everRenovate.setText(_translate("MainWindow", "Ever Renovate"))
        self.everRenovateComboBox.setToolTip(_translate("MainWindow", "Select any one option"))
        self.everRenovateComboBox.setItemText(0, _translate("MainWindow", "Yes"))
        self.everRenovateComboBox.setItemText(1, _translate("MainWindow", "No"))
        self.flatArea.setText(_translate("MainWindow", "Flat Area (in Sqft)"))
        self.flatAreaLineEdit.setToolTip(_translate("MainWindow", "Numeric data only"))
        self.latitude.setText(_translate("MainWindow", "Latitude"))
        self.latitudeLineEdit.setToolTip(_translate("MainWindow", "Numeric data only"))
        self.lotArea.setText(_translate("MainWindow", "Lot Area (in Sqft)"))
        self.lotAreaLineEdit.setToolTip(_translate("MainWindow", "Numeric data only"))
        self.longitude.setText(_translate("MainWindow", "Longitude"))
        self.longitudeLineEdit.setToolTip(_translate("MainWindow", "Numeric data only"))
        self.noOfTimesVisited.setText(_translate("MainWindow", "No of Times Visited"))
        self.noOfTimesVisitedLineEdit.setToolTip(_translate("MainWindow", "Numeric data only"))
        self.livingAreaAfterRenovation.setText(_translate("MainWindow", "Living Area after Renovation (in Sqft)"))
        self.livingAreaAfterRenovationLineEdit.setToolTip(_translate("MainWindow", "Numeric data only"))
        self.overallGrade.setText(_translate("MainWindow", "Overall Grade"))
        self.overallGradeLineEdit.setToolTip(_translate("MainWindow", "Numeric data only"))
        self.yearsSinceRenovation.setText(_translate("MainWindow", "Years since Renovation"))
        self.yearsSinceRenovationLineEdit.setToolTip(_translate("MainWindow", "Numeric data only"))
        self.basementArea.setText(_translate("MainWindow", "Basement Area (in Sqft)"))
        self.basementAreaLineEdit.setToolTip(_translate("MainWindow", "Numeric data only"))
        self.waterfronView.setText(_translate("MainWindow", "Waterfront View"))
        self.waterfrontViewComboBox.setToolTip(_translate("MainWindow", "Select any one option"))
        self.waterfrontViewComboBox.setItemText(0, _translate("MainWindow", "Yes"))
        self.waterfrontViewComboBox.setItemText(1, _translate("MainWindow", "No"))
        self.ageOfHouse.setText(_translate("MainWindow", "Age of House (in Years)"))
        self.ageOfHouseLineEdit.setToolTip(_translate("MainWindow", "Numeric data only"))
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
        self.condition.setText(_translate("MainWindow", "Condition"))
        self.conditionComboBox.setToolTip(_translate("MainWindow", "Select any one option"))
        self.conditionComboBox.setItemText(0, _translate("MainWindow", "Excellent"))
        self.conditionComboBox.setItemText(1, _translate("MainWindow", "Good"))
        self.conditionComboBox.setItemText(2, _translate("MainWindow", "Fair"))
        self.predictBtn.setToolTip(_translate("MainWindow", "Click to predict price"))
        self.predictBtn.setText(_translate("MainWindow", "Predict"))
        self.resultPriceLabel.setToolTip(_translate("MainWindow", "Predicted Price"))
        self.resultPriceLabel.setText(_translate("MainWindow", "Rs. 0.0"))
