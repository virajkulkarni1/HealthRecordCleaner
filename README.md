# HealthRecordCleaner

A reproducible pipeline for cleaning, standardizing, and visualizing healthcare patient records. Built for the NORP Data Integration theme, this project demonstrates how to handle missing values, standardize medical condition names using a mini-ontology, and visualize data distributions before and after cleaning.

## Project Structure

```
HealthRecordCleaner/
├── data/
│   ├── raw_patients.csv              # 100 patient records with issues
│   └── cleaned_patients.csv          # Cleaned and standardized data
├── src/
│   ├── cleaner.py                    # Cleans data using JSON ontology
│   ├── visualizer.py                 # Generates bar plots of condition counts
│   └── ontology_map.json             # Maps raw condition names to standard ones
├── notebook/
│   └── analysis.ipynb                # Jupyter demo to run cleaner + visualizer
├── requirements.txt                  # Lists dependencies (pandas, matplotlib)
└── README.md                         # Describes usage and setup
```

## How to Use



1 **Run the cleaning script:**
   python3 src/cleaner.py
   This will read `data/raw_patients.csv`, clean and standardize it, and write the result to `data/cleaned_patients.csv`.

2 **Visualize the data:**
   python3 src/visualizer.py
   This will generate before/after bar plots of condition counts.

3. **Explore in Jupyter Notebook:**
   Open `notebook/analysis.ipynb` to see the full pipeline, outputs, and visualizations interactively.

## About
- Cleans missing values (e.g., age, gender, condition)
- Standardizes condition names using a JSON ontology
- Visualizes distributions before and after cleaning
- Ready for ML or LLM prompt generation


NORP Project - Viraj Kulkarni 
June 8 2025