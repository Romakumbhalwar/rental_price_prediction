Rental Price Prediction Model

This project predicts the rent price of residential properties using a 
Linear Regression model trained on a dataset of housing features. 
It uses scikit-learn for model training and one-hot encoding for categorical features.

Features Used
- City
- Area
- Location
- Zone
- Propery_Type
- Size_In_Sqft
- Carpet_Area_Sqft
- Bedrooms
- Bathrooms
- Balcony
- Frurnishing_Status
- Number_Of_Amenities
- Security_Deposite
- Property_Age
- Brokerage
- Floor_No
- Total_floors_In_Building
- Maintenance_Charge

Target variable: Rent_Price

Model Details

- Model: LinearRegression
- Encoding: One-hot encoding for categorical variables
- Evaluation: Split into training and test sets (80/20)
- Output:
  - Trained model: best_rent_model.pkl
  - Test data: X_test.csv and y_test.csv

