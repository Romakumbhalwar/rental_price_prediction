import pandas as pd
import pickle
from sklearn.metrics import mean_squared_error, r2_score

# Load saved model and feature names
with open("best_rent_model.pkl", "rb") as f:
    model_package = pickle.load(f)

model = model_package['model']
feature_names = model_package['feature_names']

# Load saved test data
X_test = pd.read_csv("X_test.csv")
y_test = pd.read_csv("y_test.csv")

# Ensure test data has the correct columns
X_test = X_test[feature_names]

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("✅ Model Evaluation Complete")
print(f"Mean Squared Error: {mse}")
print(f"R² Score: {r2}")
