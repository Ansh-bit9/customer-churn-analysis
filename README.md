# Customer Churn Analysis | Data Analytics

## Project Overview

This project analyzes telecom customer data to understand which customer groups are more likely to leave the service.

The project follows this workflow:

**Data Cleaning → Exploratory Analysis → SQL Analysis → Interactive Dashboard**

## Objectives

- Understand the overall customer churn rate
- Compare churn across contract types
- Analyze customer churn by tenure
- Compare monthly charges for churned and retained customers
- Identify customer groups with higher churn
- Present findings in an interactive dashboard

## Dataset

The project uses the public **Telco Customer Churn** dataset.

**Dataset source:** [Kaggle - Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

The dataset contains customer demographics, services, contract details, charges, and churn status.

## Tools Used

- Python
- Pandas
- SQL
- Google BigQuery
- Streamlit
- Plotly

## Analysis Performed

1. Data cleaning and basic validation
2. Exploratory analysis of customer churn
3. SQL analysis of churn by contract, tenure, services, and payment method
4. Interactive dashboard with filters and charts

## Key Questions

- What percentage of customers have churned?
- Which contract type has the highest churn?
- How does churn vary with customer tenure?
- Are higher monthly charges associated with higher churn?
- Which customer groups may need more retention attention?

## Live Dashboard

**[Open the interactive Customer Churn Dashboard](https://customer-churn-analysis-889.streamlit.app/)**

## Files

- `WA_Fn-UseC_-Telco-Customer-Churn.csv` — Dataset
- `analysis.py` — Python analysis
- `churn_analysis.sql` — SQL analysis
- `app.py` — Interactive dashboard
- `requirements.txt` — Python packages for the dashboard
- 
## Running the Dashboard

Install the required packages:

```bash
pip install -r requirements.txt

Run the dashboard:

streamlit run app.py
