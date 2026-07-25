from flask import Flask, render_template, request, send_file
import pandas as pd
import joblib
import os
from datetime import datetime

app = Flask(__name__)

# ==========================================
# Load Machine Learning Files
# ==========================================

model = joblib.load("model/sleep_model.pkl")
scaler = joblib.load("model/scaler.pkl")
label_encoders = joblib.load("model/label_encoders.pkl")
target_encoder = joblib.load("model/target_encoder.pkl")
feature_columns = joblib.load("model/feature_columns.pkl")

# ==========================================
# History File
# ==========================================

HISTORY_FILE = "history.csv"

if not os.path.exists(HISTORY_FILE):
    history = pd.DataFrame(columns=[
        "Date",
        "Sleep Duration",
        "Prediction"
    ])
    history.to_csv(HISTORY_FILE, index=False)

# ==========================================
# Home Page
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")

# ==========================================
# About Page
# ==========================================

@app.route("/about")
def about():
    return render_template("about.html")

# ==========================================
# Contact Page
# ==========================================

@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "POST":

        gender = request.form["gender"]
        age = int(request.form["age"])
        occupation = request.form["occupation"]
        sleep_duration = float(request.form["sleep_duration"])
        physical_activity = int(request.form["physical_activity"])
        stress_level = int(request.form["stress_level"])
        bmi = request.form["bmi"]
        blood_pressure = request.form["blood_pressure"]
        heart_rate = int(request.form["heart_rate"])
        daily_steps = int(request.form["daily_steps"])
        sleep_disorder = request.form["sleep_disorder"]

        screen_time = int(request.form.get("screen_time",0))
        caffeine = request.form.get("caffeine","None")
        mood = request.form.get("mood","Neutral")
        bedtime = request.form.get("bedtime","22:00")
        wake_time = request.form.get("wake_time","06:00")

        user_data = pd.DataFrame([{
            "Gender": gender,
            "Age": age,
            "Occupation": occupation,
            "Sleep Duration": sleep_duration,
            "Physical Activity Level": physical_activity,
            "Stress Level": stress_level,
            "BMI Category": bmi,
            "Blood Pressure": blood_pressure,
            "Heart Rate": heart_rate,
            "Daily Steps": daily_steps,
            "Sleep Disorder": sleep_disorder
        }])

        categorical_columns = [
            "Gender",
            "Occupation",
            "BMI Category",
            "Blood Pressure",
            "Sleep Disorder"
        ]

        # Encode categorical columns
        for col in categorical_columns:
            value = str(user_data[col].iloc[0]).strip()
            encoder = label_encoders[col]

            classes = [str(x).strip() for x in encoder.classes_]

            if value not in classes:
                value = classes[0]

            user_data[col] = encoder.transform([value])[0]

        # Arrange feature columns
        user_data = user_data[feature_columns]

        # Scale data
        user_data = scaler.transform(user_data)

        # Predict
        prediction = model.predict(user_data)

        try:
            quality = target_encoder.inverse_transform(prediction)[0]
        except:
            quality = prediction[0]

        recommendation = ""

        if str(quality).lower() in ["excellent", "good"]:
            recommendation = "Good sleep quality. Maintain your healthy routine."

        elif str(quality).lower() == "average":
            recommendation = "Try reducing stress and maintain a fixed sleep schedule."

        else:
            recommendation = "Poor sleep quality. Sleep 7–8 hours daily."


        # Extra Feature Based Tips

        if screen_time > 90:
            recommendation += " Reduce screen time before bed."

        if caffeine.lower() in ["high", "moderate"]:
            recommendation += " Avoid caffeine before sleeping."

        if mood.lower() in ["sad", "anxious"]:
            recommendation += " Try relaxation activities before sleep."
        # Save History
        history = pd.read_csv(HISTORY_FILE)

        new_row = pd.DataFrame([{
            "Date": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "Sleep Duration": sleep_duration,
            "Prediction": quality
        }])

        history = pd.concat([history, new_row], ignore_index=True)
        history.to_csv(HISTORY_FILE, index=False)

        return render_template(
            "result.html",
            prediction=quality,
            recommendation=recommendation,
            screen_time=screen_time,
            caffeine=caffeine,
            mood=mood,
            bedtime=bedtime,
            wake_time=wake_time
        )

    return render_template("predict.html")
@app.route("/dashboard")
def dashboard():

    history = pd.read_csv(HISTORY_FILE)
    recent = history.tail(5).iloc[::-1].to_dict(orient="records")

    total = len(history)

    if total > 0:
        average = round(history["Prediction"].mean(), 2)
        highest = history["Prediction"].max()
        lowest = history["Prediction"].min()
        progress = average * 10

        excellent = len(history[history["Prediction"] >= 8])
        good = len(history[(history["Prediction"] >= 6) & (history["Prediction"] < 8)])
        poor = len(history[history["Prediction"] < 6])

    else:
        average = 0
        highest = 0
        lowest = 0
        progress = 0
        excellent = 0
        good = 0
        poor = 0

    return render_template(
        "dashboard.html",
        total=total,
        average=average,
        highest=highest,
        lowest=lowest,
        progress=progress,
        recent=recent,
        excellent=excellent,
        good=good,
        poor=poor
    )
# ==========================================
# History
# ==========================================

@app.route("/history")
def history():

    history = pd.read_csv(HISTORY_FILE)

    records = history.to_dict(orient="records")

    return render_template(
        "history.html",
        records=records
    )
@app.route("/download")
def download():

    return send_file(
        HISTORY_FILE,
        as_attachment=True
    )
@app.route("/clear_history")
def clear_history():

    history = pd.DataFrame(columns=[
        "Date",
        "Sleep Duration",
        "Prediction"
    ])

    history.to_csv(HISTORY_FILE, index=False)

    return dashboard()


# ==========================================
# Run Flask
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)