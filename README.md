# Sleep Quality Predictor 🌙

## Project Overview

Sleep Quality Predictor is a Machine Learning based web application that predicts a person's sleep quality based on health, lifestyle, and daily activity factors.

The system analyzes user inputs such as sleep duration, stress level, physical activity, BMI, heart rate, daily steps, screen time, caffeine intake, mood, and sleep habits to predict sleep quality and provide personalized recommendations.

---

## Objectives

* Predict sleep quality using Machine Learning algorithms
* Analyze lifestyle factors affecting sleep
* Provide personalized sleep improvement suggestions
* Help users monitor and improve their sleep habits

---

## Features

✅ Sleep quality prediction
✅ User-friendly prediction form
✅ Machine Learning based classification
✅ Personalized sleep recommendations
✅ Prediction history tracking
✅ Dashboard with charts and analysis
✅ Responsive web interface
✅ Download prediction history as CSV

---

## Technologies Used

### Programming Language

* Python

### Web Framework

* Flask

### Machine Learning Libraries

* Scikit-learn
* Pandas
* NumPy
* Joblib

### Data Visualization

* Matplotlib
* Seaborn
* Chart.js

### Frontend

* HTML
* CSS
* JavaScript
* Bootstrap

---

## Machine Learning Algorithm

The project uses supervised machine learning techniques.

Algorithms:

* Random Forest Classifier
* Logistic Regression
* Decision Tree
* Support Vector Machine (SVM)

---

## Dataset

Dataset Used:

**Sleep Health and Lifestyle Dataset**

Features include:

* Gender
* Age
* Occupation
* Sleep Duration
* Physical Activity Level
* Stress Level
* BMI Category
* Blood Pressure
* Heart Rate
* Daily Steps
* Sleep Disorder

---

## Project Structure

```
Sleep_Quality_Predictor

│── app.py
│── train_model.py
│── preprocess.py
│── recommendation.py
│── visualization.py
│── helper.py
│── requirements.txt
│── README.md

│── dataset
│     └── sleep.csv

│── model
│     ├── sleep_model.pkl
│     ├── scaler.pkl
│     ├── label_encoder.pkl
│     └── target_encoder.pkl

│── templates
│     ├── index.html
│     ├── predict.html
│     ├── result.html
│     ├── dashboard.html
│     └── history.html

│── static
      ├── css
      ├── js
      └── images
```

---

## Installation

Install required libraries:

```
pip install -r requirements.txt
```

---

## How to Run Project

Step 1:

Open project folder in terminal.

Step 2:

Run Flask application:

```
python app.py
```

Step 3:

Open browser:

```
http://127.0.0.1:5000/
```

---

## Working Process

1. User enters sleep and lifestyle details.
2. Input data is preprocessed.
3. Machine Learning model analyzes the data.
4. System predicts sleep quality.
5. User receives recommendation tips.
6. Prediction details are stored in history.

---

## Output

The system provides:

* Predicted Sleep Quality
* Sleep Improvement Suggestions
* Prediction History
* Dashboard Analytics

---

## Future Enhancements

* Mobile application development
* Real-time sleep monitoring using wearable devices
* Deep Learning based prediction
* AI chatbot for sleep guidance

---

## Conclusion

Sleep Quality Predictor helps users understand the factors affecting their sleep and provides useful recommendations to improve sleep habits using Machine Learning and data analytics.
