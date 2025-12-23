from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# 1. Define the Input Format (The "Bouncer")
# We tell FastAPI: "Expect a JSON body with 'years_experience' as a number."
class SalaryInput(BaseModel):
    years_experience: float

app = FastAPI()

# 2. Load the Model (The "Brain")
# This runs ONCE when the server starts.
print("Loading model...")
model = joblib.load("salary_model.joblib")
print("Model loaded successfully!")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Salary Predictor API. Use /predict to calculate salaries."}

# 3. The Prediction Endpoint
# Notice this is @app.post, not @app.get, because we are sending data.
@app.post("/predict")
def predict_salary(data: SalaryInput):
    # Convert input to the format the model expects (2D array)
    features = np.array([[data.years_experience]])
    
    # Make the prediction
    prediction = model.predict(features)
    
    # Return the result
    return {
        "input_years": data.years_experience,
        "estimated_salary_k": round(prediction[0], 2)
    }
