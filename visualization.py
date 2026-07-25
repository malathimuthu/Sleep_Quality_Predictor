# ==========================================
# Sleep Quality Predictor
# Data Visualization Module
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Create folder for graphs

os.makedirs("static/images", exist_ok=True)



# Load Dataset

df = pd.read_csv("dataset/sleep.csv")

df.columns = df.columns.str.strip()



# ==========================================
# Sleep Quality Distribution
# ==========================================

plt.figure(figsize=(7,5))

sns.countplot(
    data=df,
    x="Quality of Sleep"
)

plt.title("Sleep Quality Distribution")

plt.xlabel("Sleep Quality")

plt.ylabel("Count")

plt.savefig(
    "static/images/sleep_quality_distribution.png"
)

plt.close()



# ==========================================
# Stress vs Sleep Quality
# ==========================================

plt.figure(figsize=(7,5))

sns.barplot(
    data=df,
    x="Stress Level",
    y="Quality of Sleep"
)

plt.title(
    "Stress Level vs Sleep Quality"
)

plt.savefig(
    "static/images/stress_sleep.png"
)

plt.close()



# ==========================================
# Sleep Duration Analysis
# ==========================================

plt.figure(figsize=(7,5))

sns.scatterplot(
    data=df,
    x="Sleep Duration",
    y="Quality of Sleep"
)

plt.title(
    "Sleep Duration vs Quality"
)

plt.savefig(
    "static/images/sleep_duration.png"
)

plt.close()



# ==========================================
# Correlation Heatmap
# ==========================================

numeric_df = df.select_dtypes(
    include="number"
)


plt.figure(figsize=(10,6))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)


plt.title(
    "Feature Correlation Heatmap"
)


plt.savefig(
    "static/images/correlation_heatmap.png"
)

plt.close()



print("Visualization Completed Successfully ✅")