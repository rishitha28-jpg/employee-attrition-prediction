import pandas as pd
from sklearn.preprocessing import LabelEncoder


def load_and_preprocess_data(csv_path):

    df = pd.read_csv(csv_path)

    # -----------------------------
    # CREATE TARGET COLUMN
    # -----------------------------
    df['target'] = df.apply(
        lambda row: 1 if (
            str(row['last_new_job']) in ['0', '1'] or
            row['training_hours'] < 30 or
            row['relevent_experience'] == 'No relevent experience'
        ) else 0,
        axis=1
    )

    # -----------------------------
    # FEATURES
    # -----------------------------
    features = [
        'city',
        'city_development_index',
        'gender',
        'relevent_experience',
        'enrolled_university',
        'education_level',
        'experience',
        'company_size',
        'last_new_job',
        'training_hours'
    ]

    df = df[features + ['target']].dropna()

    encoders = {}

    # -----------------------------
    # ENCODE CATEGORICAL FEATURES
    # -----------------------------
    for col in df.columns:

        if df[col].dtype == object:

            le = LabelEncoder()

            df[col] = le.fit_transform(df[col])

            encoders[col] = le

    X = df[features]
    y = df['target']

    return X, y, df, encoders


# -----------------------------
# SAFE USER INPUT ENCODING
# -----------------------------
def encode_user_input(input_df, encoders):

    df = input_df.copy()

    for col, encoder in encoders.items():

        if col in df.columns:

            df[col] = df[col].apply(
                lambda x: encoder.transform([x])[0] if x in encoder.classes_ else -1
            )

    return df