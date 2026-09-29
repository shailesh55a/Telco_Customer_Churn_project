import pandas as pd

def clean_data(df):
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce')
    df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median()) 
    df.drop_duplicates(inplace=True)

    if "customerID" in df.columns:
        df.drop("customerID", axis=1, inplace=True)

    return df
