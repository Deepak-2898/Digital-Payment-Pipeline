# Digital Payments Data Pipeline

## Project Description
This project demonstrates an end-to-end data engineering pipeline to process and analyze digital payments data. The pipeline handles data ingestion, transformation, storage, and visualization, showcasing core data engineering concepts and Python programming skills. It is designed to extract meaningful insights and automate data processing tasks.

## Features
- **Data Ingestion:** Robust loading of raw CSV files with error handling for missing files or invalid paths.
- **Data Transformation:** Normalizes column names, handles missing values, and derives new metrics (e.g., transactions per volume).
- **Data Storage:** Stores cleaned data in a SQLite database for efficient querying and analysis.
- **Data Visualization:** Generates time-series plots to visualize daily transaction trends using Matplotlib and Seaborn.
- **Scalability:** Modular design for integration with tools like Apache Airflow for scheduling and automation.

## Technologies Used
- **Programming Languages:** Python
- **Libraries:** Pandas, Matplotlib, Seaborn, SQLAlchemy
- **Database:** SQLite
- **Version Control:** Git, GitHub

## Pipeline Overview
1. **Data Ingestion:** Loads raw data from a CSV file.
2. **Data Transformation:** Prepares and cleans data for analysis.
3. **Data Storage:** Saves processed data into a SQLite database.
4. **Data Visualization:** Plots daily transaction trends and saves the visualization as a PNG file.

## File Structure
```
DigitalPaymentsPipeline/
├── README.md               # Project documentation
├── pipeline.py             # Main pipeline script
├── requirements.txt        # Python dependencies
├── RBI_Daily_Digital_Payments_Sample_Data.csv (Optional, small sample for demo)
├── outputs/                # Directory for outputs
│   └── daily_transactions_trend.png  # Visualization output
└── .gitignore              # Files to ignore in Git
```

## Setup Instructions
### Prerequisites
- Python 3.7+
- SQLite installed (comes pre-installed with Python)
- Git installed

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DigitalPaymentsPipeline.git
   cd DigitalPaymentsPipeline
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place your data file (`RBI_Daily_Digital_Payments_Sample_Data.csv`) in the project directory.

### Usage
1. Run the pipeline:
   ```bash
   python pipeline.py
   ```

2. Outputs:
   - Processed data stored in `digital_payments.db`.
   - Visualization saved as `outputs/daily_transactions_trend.png`.

### Example Output
![Daily Transactions Trend](outputs/daily_transactions_trend.png)

## Future Enhancements
- **Cloud Integration:** Extend pipeline to process data on cloud platforms like AWS or Google Cloud.
- **Automation:** Schedule pipeline using Apache Airflow or Prefect.
- **Big Data Integration:** Add support for processing larger datasets with Apache Spark.

## Contact
**Author:** Deepak Kumar Singh  
**Email:** deepak.singh.28021998@gmail.com
