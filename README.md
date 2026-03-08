# Employee Attrition Prediction System

An end-to-end **Machine Learning application** that predicts the probability of employee attrition using structured HR data.  
The system exposes a **REST API built with FastAPI**, deployed on **Railway**, and integrated with a **Streamlit dashboard**.

This project demonstrates a **production-style ML inference pipeline**, including model serving, API validation, monitoring endpoints, and cloud deployment.

---

# Project Overview

Employee attrition is a major challenge for organizations. Losing skilled employees leads to increased hiring costs, productivity loss, and operational disruption.

This system predicts whether an employee is likely to leave the company based on HR-related features such as:

- City
- City development index
- Gender
- Relevant experience
- Education level
- Company size
- Training hours
- Previous job changes

The model outputs:

- **Prediction** → Whether the employee may leave
- **Probability Score** → Confidence of the prediction

This allows HR teams to **identify high-risk employees and improve retention strategies.**

---

# Live API

Base API URL

https://employee-attrition-prediction-production.up.railway.app

Swagger API Documentation

https://employee-attrition-prediction-production.up.railway.app/docs

Health Check Endpoint

https://employee-attrition-prediction-production.up.railway.app/health

---

# System Architecture

User  
↓  
Streamlit Dashboard  
↓  
FastAPI REST API  
↓  
Preprocessing Pipeline  
↓  
RandomForest ML Model  
↓  
Prediction Response  

Deployment pipeline

GitHub → Railway → FastAPI API → ML Model

---

# Tech Stack

Machine Learning

- Python
- Scikit-learn
- Pandas
- NumPy

Backend

- FastAPI
- Pydantic
- Uvicorn

Frontend

- Streamlit

Deployment

- Railway
- GitHub

---

# Project Structure

```
employee-attrition-prediction
│
├── backend
│   ├── main.py
│   ├── model.py
│   ├── preprocessing.py
│   ├── schema.py
│   ├── train.py
│   ├── saved_model.pkl
│   └── requirements.txt
│
├── frontend
│   └── streamlit_app.py
│
├── data
│   └── aug_test.csv
│
├── README.md
└── .gitignore
```

---

# API Endpoints

## Health Check

GET /health

Response

```
{
  "status": "healthy",
  "service": "Employee Attrition Prediction API"
}
```

---

## Predict Attrition

POST /predict

Example Request

```
{
  "city": "city_103",
  "city_development_index": 0.65,
  "gender": "Male",
  "relevent_experience": "Has relevent experience",
  "enrolled_university": "no_enrollment",
  "education_level": "Graduate",
  "experience": "5",
  "company_size": "50-99",
  "last_new_job": "1",
  "training_hours": 80
}
```

Example Response

```
{
  "prediction": 1,
  "probability": 0.84
}
```

Where:

- prediction = 1 → Employee likely to leave
- prediction = 0 → Employee likely to stay

---

# Running the Project Locally

Clone the repository

```
git clone https://github.com/rishitha28-jpg/employee-attrition-prediction.git
cd employee-attrition-prediction
```

Install dependencies

```
pip install -r backend/requirements.txt
```

Run the FastAPI server

```
cd backend
uvicorn main:app --reload
```

Open API documentation

```
http://127.0.0.1:8000/docs
```

Run the Streamlit dashboard

```
cd frontend
streamlit run streamlit_app.py
```

---

# Model Details

Algorithm used

RandomForestClassifier

Features used

- city
- city_development_index
- gender
- relevent_experience
- enrolled_university
- education_level
- experience
- company_size
- last_new_job
- training_hours

Output

- Binary classification
- Probability score

---

# Deployment

The backend API is deployed on **Railway cloud platform**.

Deployment workflow

1. Push project to GitHub
2. Connect GitHub repository to Railway
3. Set root directory as backend
4. Configure start command

```
uvicorn main:app --host 0.0.0.0 --port $PORT
```

5. Generate public domain

---

# Future Improvements

Potential production enhancements:

- Prediction logging
- Model monitoring
- Data drift detection
- Docker containerization
- CI/CD pipelines
- Authentication for API endpoints
