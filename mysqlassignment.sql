use ecommerce_dbs
show tables;
select * from ecommerce_data

/* check1 */

SELECT 
     COUNT(*) As null_count
	FROM
       ecommerce_data
WHERE 
    TransactionID IS NULL 
    OR ProductID IS NULL 
    OR ProductCategory IS NULL 
    OR ProductSubcategory IS NULL 
    OR ProductPrice IS NULL 
    OR QuantitySold IS NULL 
    OR TransactionDate IS NULL 
    OR CustomerID IS NULL 
    OR CustomerLocation IS NULL 
    OR PaymentMethod IS NULL;

SELECT 
    COUNT(*) AS duplicate_count
FROM 
  ecommerce_data
GROUP BY 
    TransactionID, ProductID, ProductCategory, ProductSubcategory, ProductPrice, QuantitySold, TransactionDate, CustomerID, CustomerLocation, PaymentMethod
HAVING 
    COUNT(*) > 1;

SELECT 
    COUNT(*) AS invalid_date_count
FROM 
    ecommerce_data
WHERE 
    TransactionDate < '1900-01-01' 
    OR TransactionDate > CURDATE();
    
    SELECT 
    COUNT(*) AS invalid_price_count
FROM 
    ecommerce_data
WHERE 
    ProductPrice < 0;
    
    
SELECT 
    COUNT(*) AS invalid_quantity_count
FROM 
    ecommerce_data
WHERE 
    QuantitySold < 0;
    
    