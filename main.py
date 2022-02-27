from joblib import load
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from HousePrice import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator


# Prediction class for predicting the house prices
class Prediction:
    def __init__(self):
        self.model = load('Parvej Ali House Pricing.joblib')  # Load the house price model
        # All fields(columns) for predicting the house price
        self.col = ['No of Bathrooms', 'Flat Area (in Sqft)', 'Lot Area (in Sqft)',
                    'No of Times Visited', 'Overall Grade', 'Basement Area (in Sqft)',
                    'Age of House (in Years)', 'Latitude', 'Longitude',
                    'Living Area after Renovation (in Sqft)', 'Years since Renovation',
                    'Condition_of_the_House_Excellent', 'Condition_of_the_House_Fair',
                    'Condition_of_the_House_Good', 'Waterfront_View_Yes',
                    'Ever_Renovate_Yes', 'Zipcode_Group_Zipcode_Group_1',
                    'Zipcode_Group_Zipcode_Group_2', 'Zipcode_Group_Zipcode_Group_3',
                    'Zipcode_Group_Zipcode_Group_4', 'Zipcode_Group_Zipcode_Group_5',
                    'Zipcode_Group_Zipcode_Group_6', 'Zipcode_Group_Zipcode_Group_7',
                    'Zipcode_Group_Zipcode_Group_8', 'Zipcode_Group_Zipcode_Group_9']
        self.data = pd.read_csv("Raw_Housing_Prices_5.csv")  # Read CSV file "Raw_Housing_Prices_5.csv" for scaling data
        self.data.drop(columns=['Sale_Price'], inplace=True)  # Drop "Sale_Price" field from the csv data
        self.scalar = StandardScaler()  # Create the StandardScaler data


# Gui class for showing house price window to interact with user
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        # Create housePrice model object for predicting the prices
        self.houseModel = Prediction()
        validate = QRegExpValidator(QRegExp(r'[0-9]*\.[0-9]*'))
        sign_validate = QRegExpValidator(QRegExp(r'[+,\-][0-9]*\.[0-9]*'))
        self.flatAreaLineEdit.setValidator(validate)
        self.lotAreaLineEdit.setValidator(validate)
        self.noOfTimesVisitedLineEdit.setValidator(validate)
        self.overallGradeLineEdit.setValidator(validate)
        self.basementAreaLineEdit.setValidator(validate)
        self.ageOfHouseLineEdit.setValidator(validate)
        self.latitudeLineEdit.setValidator(sign_validate)
        self.longitudeLineEdit.setValidator(sign_validate)
        self.livingAreaAfterRenovationLineEdit.setValidator(validate)
        self.yearsSinceRenovationLineEdit.setValidator(validate)
        self.predictBtn.clicked.connect(self.predict_price)

    def predict_price(self):
        self.resultPriceLabel.setText("Wait for a while")
        # Sample data for testing model
        t1 = self.is_null(self.noOfBathroomSpinBox.text())
        t2 = self.is_null(self.flatAreaLineEdit.text())
        t3 = self.is_null(self.lotAreaLineEdit.text())
        t4 = self.is_null(self.noOfTimesVisitedLineEdit.text())
        t5 = self.is_null(self.overallGradeLineEdit.text())
        t6 = self.is_null(self.basementAreaLineEdit.text())
        t7 = self.is_null(self.ageOfHouseLineEdit.text())
        t8 = self.is_null(self.latitudeLineEdit.text())
        t9 = self.is_null(self.longitudeLineEdit.text())
        t10 = self.is_null(self.livingAreaAfterRenovationLineEdit.text())
        t11 = self.is_null(self.yearsSinceRenovationLineEdit.text())
        condition_text = self.conditionComboBox.currentText()
        t12 = 0
        t13 = 0
        t14 = 0
        if condition_text == "Excellent":
            t12 = 1
        elif condition_text == "Fair":
            t13 = 1
        else:
            t14 = 1
        waterfront_view = self.waterfrontViewComboBox.currentText()
        t15 = 0
        if waterfront_view == "Yes":
            t15 = 1
        ever_renovated = self.everRenovateComboBox.currentText()
        t16 = 0
        if ever_renovated == "Yes":
            t16 = 1
        zipcode_group_text = self.zipcodeGroupComboBox.currentText()
        t17 = 0
        t18 = 0
        t19 = 0
        t20 = 0
        t21 = 0
        t22 = 0
        t23 = 0
        t24 = 0
        t25 = 0
        if zipcode_group_text == "Group 1":
            t17 = 1
        elif zipcode_group_text == "Group 2":
            t18 = 1
        elif zipcode_group_text == "Group 3":
            t19 = 1
        elif zipcode_group_text == "Group 4":
            t20 = 1
        elif zipcode_group_text == "Group 5":
            t21 = 1
        elif zipcode_group_text == "Group 6":
            t22 = 1
        elif zipcode_group_text == "Group 7":
            t23 = 1
        elif zipcode_group_text == "Group 8":
            t24 = 1
        else:
            t25 = 1
        # data_set = np.array([[3.0, 1960.0, 5000.0, 0, 7, 910, 53, 47.5208, -122.393, 1360.0,
        #                       0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]])
        data_set = np.array([[t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14,
                              t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25]])
        result = self.houseModel.data.append(
            pd.DataFrame(data=data_set, columns=self.houseModel.col), ignore_index=True)
        result = self.houseModel.scalar.fit_transform(result)
        result = pd.DataFrame(data=result, columns=self.houseModel.data.columns)
        price = self.houseModel.model.predict(result.tail(1))
        self.resultPriceLabel.setText("Rs. " + str(price[0]))
        print("Rs. " + str(price[0]))

    # is_null function for converting string number input to float data type
    @staticmethod
    def is_null(text):
        if text == "":
            return 0
        else:
            if text[0] == "+":
                return MyMainWindow.is_null(text[1:])
            elif text[0] == "-":
                return -(MyMainWindow.is_null(text[1:]))
            return float(text)


# Main class execution
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
