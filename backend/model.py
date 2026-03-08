import joblib
import pandas as pd

MODEL_PATH = "saved_model.pkl"


def load_model():

    model, encoders = joblib.load(MODEL_PATH)

    return model, encoders


def predict(model, df):

    pred = model.predict(df)[0]

    prob = model.predict_proba(df)[0][1]

    return pred, prob