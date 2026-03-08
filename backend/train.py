import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from preprocessing import load_and_preprocess_data


DATA_PATH = "../data/aug_test.csv"


def train():

    X, y, df, encoders = load_and_preprocess_data(DATA_PATH)

    X_train, X_test, y_train, y_test = train_test_split(

        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(

        n_estimators=150,
        max_depth=6,
        min_samples_split=10,
        random_state=42
    )

    model.fit(X_train, y_train)

    joblib.dump((model, encoders), "saved_model.pkl")

    print("Model saved successfully")


if __name__ == "__main__":

    train()