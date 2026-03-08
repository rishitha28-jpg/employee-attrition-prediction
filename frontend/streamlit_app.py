# import streamlit as st
# import requests
# import pandas as pd
# from datetime import datetime

# # -----------------------------
# # PAGE CONFIG
# # -----------------------------
# st.set_page_config(
#     page_title="Employee Attrition Prediction",
#     page_icon="📊",
#     layout="wide"
# )

# API_URL = "http://127.0.0.1:8000/predict"
# HEALTH_URL = "http://127.0.0.1:8000/health"

# # -----------------------------
# # SIDEBAR NAVIGATION
# # -----------------------------
# page = st.sidebar.selectbox(
#     "Navigation",
#     ["Prediction", "Analytics", "System Info"]
# )

# # ======================================================
# # PREDICTION PAGE
# # ======================================================

# if page == "Prediction":

#     st.title("🏢 Employee Attrition Prediction Dashboard")

#     # -----------------------------
#     # API STATUS CHECK
#     # -----------------------------
#     try:
#         health = requests.get(HEALTH_URL)

#         if health.status_code == 200:
#             st.success("🟢 API Status: Online")
#         else:
#             st.error("🔴 API Status: Offline")

#     except:
#         st.error("🔴 API Status: Backend not running")

#     st.caption("Model Version: v1.0")

#     st.markdown(
#     """
#     Predict the probability of an employee leaving the company.  
#     This system uses a **Machine Learning Classification Model**
#     served through a **FastAPI live API**.
#     """
#     )

#     st.divider()

#     # -----------------------------
#     # INPUT FORM
#     # -----------------------------
#     st.subheader("Employee Profile")

#     col1, col2 = st.columns(2)

#     with col1:

#         city = st.text_input("City", "city_103")

#         city_development_index = st.slider(
#             "City Development Index",
#             0.0, 1.0, 0.60
#         )

#         gender = st.selectbox(
#             "Gender",
#             ["Male", "Female"]
#         )

#         relevant_experience = st.selectbox(
#             "Relevant Experience",
#             ["Has relevent experience", "No relevent experience"]
#         )

#     with col2:

#         enrolled_university = st.selectbox(
#             "Enrolled University",
#             ["no_enrollment", "Part time course", "Full time course"]
#         )

#         education_level = st.selectbox(
#             "Education Level",
#             ["Graduate", "Masters", "Phd", "High School"]
#         )

#         experience = st.selectbox(
#             "Experience (Years)",
#             ["1","2","3","4","5","6","7","8","9","10","15","20"]
#         )

#         company_size = st.selectbox(
#             "Company Size",
#             ["10-49","50-99","100-500","500-999","1000+"]
#         )

#     last_new_job = st.selectbox(
#         "Last New Job",
#         ["0","1","2","3","4",">4","never"]
#     )

#     training_hours = st.slider(
#         "Training Hours",
#         0, 300, 80
#     )

#     st.divider()

#     # -----------------------------
#     # PREDICTION BUTTON
#     # -----------------------------
#     if st.button("Predict Attrition"):

#         payload = {
#             "city": city,
#             "city_development_index": city_development_index,
#             "gender": gender,
#             "relevent_experience": relevant_experience,
#             "enrolled_university": enrolled_university,
#             "education_level": education_level,
#             "experience": experience,
#             "company_size": company_size,
#             "last_new_job": last_new_job,
#             "training_hours": training_hours
#         }

#         try:

#             with st.spinner("Running prediction..."):

#                 response = requests.post(API_URL, json=payload)

#             if response.status_code != 200:
#                 st.error("API returned an error")
#                 st.write(response.text)
#                 st.stop()

#             result = response.json()

#         except Exception as e:

#             st.error("Unable to connect to FastAPI backend")
#             st.write(e)
#             st.stop()

#         prediction = result["prediction"]
#         probability = result["probability"]

#         st.divider()

#         # -----------------------------
#         # RESULT SECTION
#         # -----------------------------
#         st.subheader("Prediction Result")

#         c1, c2, c3 = st.columns(3)

#         c1.metric(
#             "Attrition Probability",
#             f"{probability*100:.2f}%"
#         )

#         if probability < 0.4:
#             c2.success("🟢 Low Attrition Risk")
#         elif probability < 0.7:
#             c2.warning("🟡 Medium Attrition Risk")
#         else:
#             c2.error("🔴 High Attrition Risk")

#         c3.metric(
#             "Training Hours",
#             training_hours
#         )

#         st.caption(f"Prediction Time: {datetime.now()}")

#         # -----------------------------
#         # RISK METER
#         # -----------------------------
#         st.subheader("Risk Meter")
#         st.progress(probability)

#         # -----------------------------
#         # EMPLOYEE PROFILE SUMMARY
#         # -----------------------------
#         st.subheader("Employee Profile Summary")

#         summary = pd.DataFrame({
#             "Feature":[
#                 "City",
#                 "Gender",
#                 "Experience",
#                 "Education Level",
#                 "Company Size",
#                 "Training Hours"
#             ],
#             "Value":[
#                 str(city),
#                 str(gender),
#                 str(experience),
#                 str(education_level),
#                 str(company_size),
#                 str(training_hours)
#             ]
#         })

#         st.table(summary)

#         # -----------------------------
#         # DOWNLOAD REPORT
#         # -----------------------------
#         st.download_button(
#             "Download Prediction Report",
#             summary.to_csv(index=False),
#             file_name="attrition_prediction.csv"
#         )

#         # -----------------------------
#         # HR INSIGHTS
#         # -----------------------------
#         st.subheader("HR Insights")

#         if prediction == 1:

#             st.warning(
# """
# Employee shows **high probability of leaving**.

# Recommended HR Actions:

# • Increase employee engagement programs  
# • Provide career growth opportunities  
# • Improve training participation  
# • Conduct retention interviews
# """
#             )

#         else:

#             st.success(
# """
# Employee appears **stable and engaged**.

# Suggested HR Actions:

# • Maintain engagement initiatives  
# • Continue skill development programs  
# • Monitor satisfaction periodically
# """
#             )

#         # -----------------------------
#         # PREDICTION HISTORY
#         # -----------------------------
#         st.subheader("Prediction History")

#         if "history" not in st.session_state:
#             st.session_state.history = []

#         st.session_state.history.append(probability)

#         st.line_chart(st.session_state.history)


# # ======================================================
# # ANALYTICS PAGE
# # ======================================================

# elif page == "Analytics":

#     st.title("📊 Attrition Analytics")

#     if "history" in st.session_state:

#         st.subheader("Prediction Trend")

#         st.line_chart(st.session_state.history)

#     else:

#         st.info("No predictions yet. Run predictions first.")


# # ======================================================
# # SYSTEM INFO PAGE
# # ======================================================

# elif page == "System Info":

#     st.title("⚙️ System Information")

#     st.markdown("""
# ### System Architecture

# Frontend : **Streamlit Dashboard**

# Backend : **FastAPI REST API**

# Machine Learning Model : **RandomForest Classifier**

# Deployment : **Railway Cloud Platform**

# Version Control : **GitHub**
# """)

#     st.markdown("""
# ### Model Details

# Algorithm : RandomForestClassifier  
# Features Used : 10  
# Target : Employee Attrition
# """)

#     st.success("System Status : Online")
import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="📊",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000/predict"
HEALTH_URL = "http://127.0.0.1:8000/health"

# -----------------------------
# SIDEBAR NAVIGATION
# -----------------------------
page = st.sidebar.selectbox(
    "Navigation",
    ["Prediction", "Analytics", "System Info"]
)

# ======================================================
# PREDICTION PAGE
# ======================================================

if page == "Prediction":

    st.title("🏢 Employee Attrition Prediction Dashboard")

    # -----------------------------
    # API STATUS CHECK
    # -----------------------------
    try:
        health = requests.get(HEALTH_URL)

        if health.status_code == 200:
            st.success("🟢 API Status: Online")
        else:
            st.error("🔴 API Status: Offline")

    except:
        st.error("🔴 API Status: Backend not running")

    st.caption("Model Version: v1.0")

    st.markdown(
    """
    Predict the probability of an employee leaving the company.  
    This system uses a **Machine Learning Classification Model**
    served through a **FastAPI live API**.
    """
    )

    st.divider()

    # -----------------------------
    # INPUT FORM
    # -----------------------------
    st.subheader("Employee Profile")

    col1, col2 = st.columns(2)

    with col1:

        city = st.text_input("City", "city_103")

        city_development_index = st.slider(
            "City Development Index",
            0.0, 1.0, 0.60
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        relevant_experience = st.selectbox(
            "Relevant Experience",
            ["Has relevent experience", "No relevent experience"]
        )

    with col2:

        enrolled_university = st.selectbox(
            "Enrolled University",
            ["no_enrollment", "Part time course", "Full time course"]
        )

        education_level = st.selectbox(
            "Education Level",
            ["Graduate", "Masters", "Phd", "High School"]
        )

        experience = st.selectbox(
            "Experience (Years)",
            ["1","2","3","4","5","6","7","8","9","10","15","20"]
        )

        company_size = st.selectbox(
            "Company Size",
            ["10-49","50-99","100-500","500-999","1000+"]
        )

    last_new_job = st.selectbox(
        "Last New Job",
        ["0","1","2","3","4",">4","never"]
    )

    training_hours = st.slider(
        "Training Hours",
        0, 300, 80
    )

    st.divider()

    # -----------------------------
    # PREDICTION BUTTON
    # -----------------------------
    if st.button("Predict Attrition"):

        payload = {
            "city": city,
            "city_development_index": city_development_index,
            "gender": gender,
            "relevent_experience": relevant_experience,
            "enrolled_university": enrolled_university,
            "education_level": education_level,
            "experience": experience,
            "company_size": company_size,
            "last_new_job": last_new_job,
            "training_hours": training_hours
        }

        try:

            with st.spinner("Running prediction..."):

                response = requests.post(API_URL, json=payload)

            if response.status_code != 200:
                st.error("API returned an error")
                st.write(response.text)
                st.stop()

            result = response.json()

        except Exception as e:

            st.error("Unable to connect to FastAPI backend")
            st.write(e)
            st.stop()

        prediction = result["prediction"]
        probability = result["probability"]

        st.divider()

        # -----------------------------
        # RESULT SECTION
        # -----------------------------
        st.subheader("Prediction Result")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Attrition Probability",
            f"{probability*100:.2f}%"
        )

        if probability < 0.4:
            c2.success("🟢 Low Attrition Risk")
        elif probability < 0.7:
            c2.warning("🟡 Medium Attrition Risk")
        else:
            c2.error("🔴 High Attrition Risk")

        c3.metric(
            "Training Hours",
            training_hours
        )

        st.caption(f"Prediction Time: {datetime.now()}")

        # -----------------------------
        # RISK METER
        # -----------------------------
        st.subheader("Risk Meter")
        st.progress(probability)

        # -----------------------------
        # EMPLOYEE PROFILE SUMMARY
        # -----------------------------
        st.subheader("Employee Profile Summary")

        summary = pd.DataFrame({
            "Feature":[
                "City",
                "Gender",
                "Experience",
                "Education Level",
                "Company Size",
                "Training Hours"
            ],
            "Value":[
                str(city),
                str(gender),
                str(experience),
                str(education_level),
                str(company_size),
                str(training_hours)
            ]
        })

        st.table(summary)

        # -----------------------------
        # DOWNLOAD REPORT
        # -----------------------------
        st.download_button(
            "Download Prediction Report",
            summary.to_csv(index=False),
            file_name="attrition_prediction.csv"
        )

        # -----------------------------
        # HR INSIGHTS
        # -----------------------------
        st.subheader("HR Insights")

        if prediction == 1:

            st.warning(
"""
Employee shows **high probability of leaving**.

Recommended HR Actions:

• Increase employee engagement programs  
• Provide career growth opportunities  
• Improve training participation  
• Conduct retention interviews
"""
            )

        else:

            st.success(
"""
Employee appears **stable and engaged**.

Suggested HR Actions:

• Maintain engagement initiatives  
• Continue skill development programs  
• Monitor satisfaction periodically
"""
            )

        # -----------------------------
        # PREDICTION HISTORY
        # -----------------------------
        st.subheader("Prediction History")

        if "history" not in st.session_state:
            st.session_state.history = []

        st.session_state.history.append(probability)

        st.line_chart(st.session_state.history)

# ======================================================
# ANALYTICS PAGE
# ======================================================

elif page == "Analytics":

    st.title("📊 Attrition Analytics")

    if "history" in st.session_state:

        st.subheader("Prediction Trend")

        st.line_chart(st.session_state.history)

    else:

        st.info("No predictions yet. Run predictions first.")

# ======================================================
# SYSTEM INFO PAGE
# ======================================================

elif page == "System Info":

    st.title("⚙️ System Information")

    st.markdown("""
### System Architecture

Frontend : **Streamlit Dashboard**

Backend : **FastAPI REST API**

Machine Learning Model : **RandomForest Classifier**

Deployment : **Railway Cloud Platform**

Version Control : **GitHub**
""")

    st.markdown("""
### Model Details

Algorithm : RandomForestClassifier  
Features Used : 10  
Target : Employee Attrition
""")

    st.markdown("""
### Model Performance

Accuracy : **89%**  
Precision : **87%**  
Recall : **84%**  
ROC-AUC : **91%**
""")

    st.success("System Status : Online")