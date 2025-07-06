import pandas as pd
import os

CLEANED_PATH = os.path.join('data', 'cleaned_patients.csv')
SUMMARY_PATH = os.path.join('data', 'summary_report.txt')

def generate_summary():
    """
    Computes and prints key statistics from the cleaned patient data:
    - Average age
    - Gender distribution (counts)
    - Top 5 most common conditions
    Also saves the summary to a text file.
    """
    df = pd.read_csv(CLEANED_PATH)
    summary_lines = []

    # Average age
    avg_age = df['age'].mean()
    summary_lines.append(f"Average Age: {avg_age:.2f}")

    # Gender distribution
    gender_counts = df['gender'].value_counts()
    summary_lines.append("\nGender Distribution:")
    for gender, count in gender_counts.items():
        summary_lines.append(f"  {gender}: {count}")

    # Top 5 most common conditions
    condition_counts = df['condition'].value_counts().head(5)
    summary_lines.append("\nTop 5 Most Common Conditions:")
    for cond, count in condition_counts.items():
        summary_lines.append(f"  {cond}: {count}")

    # Print summary
    print("\n".join(summary_lines))

    # Save to file
    with open(SUMMARY_PATH, 'w') as f:
        f.write("\n".join(summary_lines))
        f.write("\n")
    print(f"\nSummary saved to {SUMMARY_PATH}")

if __name__ == '__main__':
    generate_summary() 