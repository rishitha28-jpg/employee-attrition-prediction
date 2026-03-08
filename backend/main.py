from fastapi import FastAPI
import pandas as pd

from model import load_model, predict
from preprocessing import encode_user_input
from schema import Employee


app = FastAPI(
    title="Employee Attrition Prediction API",
    version="1.0"
)


# -----------------------------
# LOAD MODEL
# -----------------------------
model, encoders = load_model()


# -----------------------------
# HOME ENDPOINT
# -----------------------------
@app.get("/")
def home():

    return {"message": "Attrition API Running"}


# -----------------------------
# HEALTH CHECK (Production API)
# -----------------------------
@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "service": "Employee Attrition Prediction API"
    }


# -----------------------------
# MODEL INFORMATION
# -----------------------------
@app.get("/model-info")
def model_info():

    return {
        "model_name": "Employee Attrition Classifier",
        "algorithm": "RandomForestClassifier",
        "version": "1.0",
        "features": [
            "city",
            "city_development_index",
            "gender",
            "relevent_experience",
            "enrolled_university",
            "education_level",
            "experience",
            "company_size",
            "last_new_job",
            "training_hours"
        ]
    }


# -----------------------------
# PREDICTION ENDPOINT
# -----------------------------
@app.post("/predict")
def predict_attrition(employee: Employee):

    data = employee.dict()

    df = pd.DataFrame([data])

    encoded = encode_user_input(df, encoders)

    pred, prob = predict(model, encoded)

    return {
        "prediction": int(pred),
        "probability": float(prob)
    }