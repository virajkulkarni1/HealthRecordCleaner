import pandas as pd
import os

CLEANED_PATH = os.path.join('data', 'cleaned_patients.csv')
REPORT_PATH = os.path.join('data', 'validation_report.txt')

def validate_data():
    """
    Validates the cleaned data for quality issues.
    - Checks for missing critical fields (age, condition).
    - Checks for invalid gender entries.
    - Checks for patients with unrealistic ages (<0 or >120).
    - Logs any issues found to a validation report.
    - Prints a summary of flagged rows.
    """
    df = pd.read_csv(CLEANED_PATH)
    flagged_rows = 0
    
    with open(REPORT_PATH, 'w') as report:
        report.write("Validation Report\n")
        report.write("=================\n\n")
        
        for index, row in df.iterrows():
            issues = []
            
            # Check for missing critical fields
            if pd.isna(row['age']):
                issues.append("Missing age")
            if pd.isna(row['condition']) or row['condition'] == 'Missing':
                issues.append("Missing condition")
            
            # Check for invalid gender entries
            if row['gender'] not in ['Male', 'Female', 'Other']:
                issues.append(f"Invalid gender: {row['gender']}")
                
            # Check for unrealistic ages
            if not pd.isna(row['age']):
                if not 0 <= row['age'] <= 120:
                    issues.append(f"Unrealistic age: {row['age']}")

            if issues:
                flagged_rows += 1
                report.write(f"Row {index + 2}: Patient ID {row['patient_id']}\n")
                for issue in issues:
                    report.write(f"- {issue}\n")
                report.write("\n")

    print(f"Validation complete. {flagged_rows} rows flagged.")
    print(f"Report saved to {REPORT_PATH}")

if __name__ == '__main__':
    validate_data() 