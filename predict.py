import joblib
import pandas as pd

# ==========================
# Load Saved Files
# ==========================

model = joblib.load("model/sleep_model.pkl")
scaler = joblib.load("model/scaler.pkl")
label_encoders = joblib.load("model/label_encoder.pkl")
target_encoder = joblib.load("model/target_encoder.pkl")
feature_columns = joblib.load("model/feature_columns.pkl")


# ==========================
# Prediction Function
# ==========================

def predict_sleep_quality(user_data):

    data = pd.DataFrame([user_data])

    # Encode categorical values
    categorical_columns = [
    "Gender",
    "Occupation",
    "BMI Category",
    "Blood Pressure",
    "Sleep Disorder",
    "Caffeine Intake",
    "Mood",
    "Bedtime",
    "Wake Time"
]

    for col in categorical_columns:
        data[col] = label_encoders[col].transform(data[col])

    # Arrange columns
    data = data[feature_columns]

    # Scale
    data = scaler.transform(data)

    # Predict
    prediction = model.predict(data)

    # Convert back to original label
    result = target_encoder.inverse_transform(prediction)

    return result[0]


# ==========================
# Test Prediction
# ==========================

if __name__ == "__main__":

    sample = {
    "Gender": "Male",
    "Age": 30,
    "Occupation": "Engineer",
    "Sleep Duration": 7.5,
    "Physical Activity Level": 40,
    "Stress Level": 3,
    "BMI Category": "Normal",
    "Blood Pressure": "120/80",
    "Heart Rate": 70,
    "Daily Steps": 8000,
    "Sleep Disorder": "None",
    
    "Screen Time": 60,
    "Caffeine Intake": "Low",
    "Mood": "Happy",
    "Bedtime": "22:30",
    "Wake Time": "06:30"
}

    print("=" * 50)
    print("Prediction :", predict_sleep_quality(sample))
    print("=" * 50)