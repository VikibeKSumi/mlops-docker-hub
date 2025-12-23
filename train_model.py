# train_model.py
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# 1. Prepare dummy data
# X = Years of Experience (must be 2D array)
X = np.array([[1], [2], [3], [4], [5], [6], [8], [10]])
# y = Salary in Thousands (e.g., 40k, 50k...)
y = np.array([40, 50, 60, 70, 80, 90, 110, 130])

# 2. Train the model
print("Training the model...")
model = LinearRegression()
model.fit(X, y)

# 3. Save the "Brain" to a file
model_filename = "salary_model.joblib"
joblib.dump(model, model_filename)

print(f"Success! Model saved to {model_filename}")
print("Test prediction (5 years):", model.predict([[5]]))
