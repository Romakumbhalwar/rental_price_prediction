import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv("Property_price_dataset.csv")
df.columns = df.columns.str.strip()  # Remove whitespace from column names

# Define features and target
features = [
    'City', 'Area', 'Location', 'Zone', 'Propery_Type', 'Size_In_Sqft',
    'Carpet_Area_Sqft', 'Bedrooms', 'Bathrooms', 'Balcony',
    'Frurnishing_Status', 'Number_Of_Amenities', 'Security_Deposite',
    'Property_Age', 'Brokerage', 'Floor_No', 'Total_floors_In_Building',
    'Maintenance_Charge'
]
target = 'Rent_Price'

# Drop rows with missing values
df = df.dropna(subset=features + [target])

# Encode categorical features using one-hot encoding
df_encoded = pd.get_dummies(df[features])

# Align features in X and y
X = df_encoded
y = df[target]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# ✅ Save trained model and feature names
model_package = {
    'model': model,
    'feature_names': X.columns.tolist()
}

with open("best_rent_model.pkl", "wb") as f:
    pickle.dump(model_package, f)

print("✅ Model trained and saved as best_rent_model.pkl")

# Save test data
X_test.to_csv("X_test.csv", index=False)
y_test.to_csv("y_test.csv", index=False)
print("✅ Test data saved for evaluation.")
