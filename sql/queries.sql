SELECT
    scheme_name,
    aum
FROM fact_performance
ORDER BY aum DESC
LIMIT 5;

SELECT
    strftime('%Y-%m', nav_date) AS month,
    AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

SELECT
    strftime('%Y', transaction_date) AS year,
    SUM(amount) AS total_sip
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;

SELECT
    state,
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

SELECT
    scheme_name,
    expense_ratio
FROM fact_performance
WHERE expense_ratio < 1;

SELECT
    scheme_name,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

SELECT
    d.category,
    AVG(f.annual_return) AS avg_return
FROM fact_performance f
JOIN dim_fund d
ON f.amfi_code = d.amfi_code
GROUP BY d.category;

SELECT
    scheme_name,
    sharpe_ratio
FROM fact_performance
WHERE sharpe_ratio < 0;

SELECT
    nav_date,
    nav
FROM fact_nav
WHERE amfi_code = '120503'
ORDER BY nav_date;

SELECT
    SUM(amount) AS total_redemption
FROM fact_transactions
WHERE transaction_type = 'Redemption';