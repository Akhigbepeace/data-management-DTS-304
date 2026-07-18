CREATE DATABASE retail_business;

USE retail_business;

CREATE TABLE purchases (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    purchase_date DATE NOT NULL,
    product_id VARCHAR(20) NOT NULL,
    product_category VARCHAR(50) NOT NULL,
    amount DECIMAL(10,2) NOT NULL
);

CREATE INDEX idx_product_category
ON purchases(product_category);

CREATE INDEX idx_purchase_date
ON purchases(purchase_date);

SELECT *
FROM purchases
WHERE purchase_date BETWEEN '2026-06-01' AND '2026-06-03';

SELECT *
FROM purchases
WHERE product_category = 'Electronics';