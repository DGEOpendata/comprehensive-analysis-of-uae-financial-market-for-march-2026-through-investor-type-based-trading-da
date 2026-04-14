markdown
# Trading Summary by Investor Type Analysis Tool

This repository contains a Python-based analytical tool for examining the "Trading Summary by Investor Type (March 2026, Daily Data)" dataset from the Abu Dhabi Open Data Platform. The tool is designed to help financial analysts, researchers, and policymakers extract meaningful insights from the data.

## Features
- **Data Loading and Inspection:** Load the dataset and inspect its structure.
- **Data Aggregation:** Group data by investor type and aggregate key metrics (e.g., buy and sell values, net values, volumes, and trades).
- **Visualization:** Generate bar charts and line plots to visualize trading activities and trends.
- **Daily Analysis:** Calculate and visualize daily net trading values.
- **Output:** Save aggregated data to a new Excel file for further analysis.

## Requirements
- Python 3.8+
- pandas
- matplotlib
- openpyxl

## Installation
1. Clone this repository:
   bash
   git clone https://github.com/your-repo/trading-summary-analysis.git
   

2. Navigate to the project directory:
   bash
   cd trading-summary-analysis
   

3. Install the required dependencies:
   bash
   pip install -r requirements.txt
   

## Usage
1. Place the dataset file (`Trading_Summary_by_Investor_Type_March.xlsx`) in the project directory.
2. Run the script:
   bash
   python analyze_trading_data.py
   
3. The script will output visualizations and save an aggregated summary to `Aggregated_Trading_Summary_March2026.xlsx`.

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License.

## Acknowledgments
This tool was developed based on the dataset provided by the Abu Dhabi Open Data Platform. Special thanks to the analysts and trend experts for their valuable insights.
