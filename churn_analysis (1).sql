-- Customer Churn Analysis
-- SQL analysis in Google BigQuery
-- Table used: telco_churn

-- 1. Total customers and churned customers
SELECT
  COUNT(*) AS total_customers,
  COUNTIF(Churn = 'Yes') AS churned_customers
FROM `telco_churn`;


-- 2. Overall churn rate
SELECT
  ROUND(COUNTIF(Churn = 'Yes') * 100.0 / COUNT(*), 2) AS churn_rate
FROM `telco_churn`;


-- 3. Churn by contract type
SELECT
  Contract,
  COUNT(*) AS customers,
  COUNTIF(Churn = 'Yes') AS churned_customers,
  ROUND(COUNTIF(Churn = 'Yes') * 100.0 / COUNT(*), 2) AS churn_rate
FROM `telco_churn`
GROUP BY Contract
ORDER BY churn_rate DESC;


-- 4. Churn by tenure group
SELECT
  CASE
    WHEN tenure <= 12 THEN '0-12 months'
    WHEN tenure <= 24 THEN '13-24 months'
    ELSE '25+ months'
  END AS tenure_group,
  COUNT(*) AS customers,
  COUNTIF(Churn = 'Yes') AS churned_customers,
  ROUND(COUNTIF(Churn = 'Yes') * 100.0 / COUNT(*), 2) AS churn_rate
FROM `telco_churn`
GROUP BY tenure_group
ORDER BY churn_rate DESC;


-- 5. Average monthly charges by churn status
SELECT
  Churn,
  COUNT(*) AS customers,
  ROUND(AVG(MonthlyCharges), 2) AS average_monthly_charges
FROM `telco_churn`
GROUP BY Churn
ORDER BY Churn;


-- 6. Churn by internet service
SELECT
  InternetService,
  COUNT(*) AS customers,
  COUNTIF(Churn = 'Yes') AS churned_customers,
  ROUND(COUNTIF(Churn = 'Yes') * 100.0 / COUNT(*), 2) AS churn_rate
FROM `telco_churn`
GROUP BY InternetService
ORDER BY churn_rate DESC;


-- 7. Churn by payment method
SELECT
  PaymentMethod,
  COUNT(*) AS customers,
  COUNTIF(Churn = 'Yes') AS churned_customers,
  ROUND(COUNTIF(Churn = 'Yes') * 100.0 / COUNT(*), 2) AS churn_rate
FROM `telco_churn`
GROUP BY PaymentMethod
ORDER BY churn_rate DESC;


-- 8. Customer count by churn status
SELECT
  Churn,
  COUNT(*) AS customer_count
FROM `telco_churn`
GROUP BY Churn
ORDER BY customer_count DESC;
