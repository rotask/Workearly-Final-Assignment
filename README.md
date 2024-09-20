# Workearly Final Assignment

This project simulates the full workflow of a Data Analyst—from extracting data from a database, manipulating it using Python and Pandas to presenting insights through Matplotlib or Tableau.

## Project Overview

We are provided with a dataset containing liquor sales in the state of Iowa, USA, from 2012 to 2020. The objectives of this project are:

- **Identify the most popular liquor item per zipcode.**
- **Calculate the percentage of sales per store between 2016 and 2019.**

All calculations and data transformations are performed using a Python script.

## Data Visualization

The results are visualized using Tableau Public. You can view the interactive dashboard here:

[**Final Assignment Liquor Stores - Rotas**](https://public.tableau.com/app/profile/konstantinos.rotas/viz/FinalAssignmentLiquorstores-Rotas/Dashboard1)

![Dashboard Preview](https://public.tableau.com/static/images/Fi/FinalAssignmentLiquorstores-Rotas/Dashboard1/1.png)

## Technologies Used

- **Python**
- **Pandas**
- **Matplotlib** (optional)
- **Tableau Public**

## Getting Started

To run this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/rotask/Workearly-Final-Assignment.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd Workearly-Final-Assignment
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Python script:**

   ```bash
   python main.py
   ```

## Dataset

The dataset used in this project includes Iowa liquor sales records from 2012 to 2020. It contains information such as:

- Date of sale
- Store details
- Zipcode
- Item description
- Sale amount

## Project Structure

```
├── data
│   └── liquor_sales.csv
├── notebooks
│   └── data_analysis.ipynb
├── outputs
│   └── visualizations.png
├── main.py
├── requirements.txt
└── README.md
```

## Results

- **Most Popular Item per Zipcode:** Identified using sales data aggregated by item and zipcode.
- **Percentage of Sales per Store (2016-2019):** Calculated by summing sales per store and computing their percentage over total sales in that period.
