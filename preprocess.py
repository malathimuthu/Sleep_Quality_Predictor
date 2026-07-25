import pandas as pd
from sklearn.preprocessing import LabelEncoder


def load_and_preprocess_data(path):

    # Load Dataset
    df = pd.read_csv(path)

    # Remove spaces in column names
    df.columns = df.columns.str.strip()


    # Remove missing values
    df.dropna(inplace=True)


    # Store encoders
    label_encoders = {}


    categorical_columns = [
        "Gender",
        "Occupation",
        "BMI Category",
        "Blood Pressure",
        "Sleep Disorder"
    ]


    # Encode categorical values
    for col in categorical_columns:

        encoder = LabelEncoder()

        df[col] = encoder.fit_transform(
            df[col].astype(str)
        )

        label_encoders[col] = encoder



    # Encode Target

    target_encoder = LabelEncoder()

    df["Quality of Sleep"] = target_encoder.fit_transform(
        df["Quality of Sleep"]
    )


    return df, label_encoders, target_encoder



# Test

if __name__ == "__main__":

    data, encoders, target = load_and_preprocess_data(
        "dataset/sleep.csv"
    )


    print("Preprocessing Completed ✅")
    print(data.head())