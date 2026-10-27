# Data Cleaning & Reporting Automation

This internship project automates data cleaning and summary reporting using Python and Pandas.

## Features
- Removes duplicate records
- Cleans extra spaces
- Standardizes categories and order status
- Converts sales values to numeric format
- Handles missing sales using the median
- Detects invalid/missing dates and fills them
- Generates a cleaned CSV
- Generates an automated cleaning report

## Files
- `data_cleaning_automation.py` - Main Python program
- `sales_dirty.csv` - Sample raw dataset
- `requirements.txt` - Dependencies
- `README.md` - Documentation

## Run
```bash
pip install -r requirements.txt
python data_cleaning_automation.py
```

The program creates `cleaned_sales.csv` and `cleaning_report.csv`.
