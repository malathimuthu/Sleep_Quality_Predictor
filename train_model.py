import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# ==========================================
# Load Dataset
# ==========================================

print("=" * 50)
print("Loading Dataset...")
print("=" * 50)

df = pd.read_csv("dataset/sleep.csv")
df.columns = df.columns.str.strip()

print("Dataset Loaded Successfully!")
print("Total Rows :", len(df))
print("Total Columns :", len(df.columns))

# ==========================================
# Remove Missing Values
# ==========================================

df.dropna(inplace=True)

print("\nMissing Values Removed!")

# ==========================================
# Encode Categorical Columns
# ==========================================

label_encoders = {}

categorical_columns = [
    "Gender",
    "Occupation",
    "BMI Category",
    "Blood Pressure",
    "Sleep Disorder"
]

for column in categorical_columns:
    encoder = LabelEncoder()
    df[column] = encoder.fit_transform(df[column].astype(str))
    label_encoders[column] = encoder

# Encode Target Column

target_encoder = LabelEncoder()
df["Quality of Sleep"] = target_encoder.fit_transform(df["Quality of Sleep"])

# ==========================================
# Features & Target
# ==========================================

X = df.drop(["Person ID", "Quality of Sleep"], axis=1)
y = df["Quality of Sleep"]

# Save Feature Names

feature_columns = list(X.columns)

# ==========================================
# Feature Scaling
# ==========================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# ==========================================
# Train Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ==========================================
# Train Model
# ==========================================

print("\nTraining Random Forest Model...")

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# ==========================================
# Model Evaluation
# ==========================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Trained Successfully!")
print(f"Accuracy : {accuracy * 100:.2f}%")

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# ==========================================
# Save Model Files
# ==========================================

os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/sleep_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")
joblib.dump(label_encoders, "model/label_encoder.pkl")
joblib.dump(target_encoder, "model/target_encoder.pkl")
joblib.dump(feature_columns, "model/feature_columns.pkl")

# ==========================================
# Completed
# ==========================================

print("\n" + "=" * 50)
print("All Files Saved Successfully!")
print("=" * 50)

print("✔ sleep_model.pkl")
print("✔ scaler.pkl")
print("✔ label_encoder.pkl")
print("✔ target_encoder.pkl")
print("✔ feature_columns.pkl")

print("\nTraining Completed Successfully!")