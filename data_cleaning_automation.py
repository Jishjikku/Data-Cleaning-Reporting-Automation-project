import pandas as pd
from pathlib import Path

INPUT_FILE = Path("sales_dirty.csv")
CLEANED_FILE = Path("cleaned_sales.csv")
REPORT_FILE = Path("cleaning_report.csv")

def clean_data(df):
    df = df.copy()
    text_cols = df.select_dtypes(include="object").columns
    for col in text_cols:
        df[col] = df[col].astype("string").str.strip()
    df["Category"] = df["Category"].str.title()
    df["Status"] = df["Status"].str.title()
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce", dayfirst=True)
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
    df["Sales"] = df["Sales"].fillna(df["Sales"].median())
    if df["Order_Date"].isna().any():
        df["Order_Date"] = df["Order_Date"].fillna(df["Order_Date"].dropna().mode().iloc[0])
    return df.drop_duplicates()

def main():
    original = pd.read_csv(INPUT_FILE)
    cleaned = clean_data(original)
    cleaned.to_csv(CLEANED_FILE, index=False)
    invalid_dates = pd.to_datetime(original["Order_Date"], errors="coerce", dayfirst=True).isna().sum()
    report = pd.DataFrame({
        "Metric": ["Original Rows","Cleaned Rows","Duplicate Rows Removed",
                   "Missing Sales Before Cleaning","Invalid/Missing Dates Before Cleaning",
                   "Total Sales After Cleaning","Completed Orders","Pending Orders","Cancelled Orders"],
        "Value": [len(original),len(cleaned),len(original)-len(cleaned),
                  original["Sales"].isna().sum(),invalid_dates,
                  round(cleaned["Sales"].sum(),2),
                  (cleaned["Status"]=="Completed").sum(),
                  (cleaned["Status"]=="Pending").sum(),
                  (cleaned["Status"]=="Cancelled").sum()]
    })
    report.to_csv(REPORT_FILE, index=False)
    print("Data Cleaning & Reporting Automation completed successfully.")
    print(f"Original rows: {len(original)}")
    print(f"Cleaned rows: {len(cleaned)}")
    print(f"Duplicates removed: {len(original)-len(cleaned)}")
    print(f"Total sales: {cleaned['Sales'].sum():.2f}")
    print(f"Created: {CLEANED_FILE} and {REPORT_FILE}")

if __name__ == "__main__":
    main()
