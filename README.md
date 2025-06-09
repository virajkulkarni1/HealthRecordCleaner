# HealthRecordCleaner


A repeatable process for cleanup, normalization and visualization of patient records from healthcare. This follows the NORP Data Integration theme, and the main point of the analysis below is to show how to treat missing values, how to standardize medical condition names into a mini-ontology, and visualising data distributions before and after cleaning. 

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

3 **Explore in Jupyter Notebook:**
   Open `notebook/analysis.ipynb` to see the full pipeline, outputs, and visualizations interactively.

## About
- Cleans missing values 
- Standardizes condition names using a JSON ontology
- Visualizes distributions before and after cleaning
- Ready for ML or LLM prompt generation along with next steps of this project


NORP Project - Viraj Kulkarni 
June 8 2025