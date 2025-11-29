-- create_table.sql
-- SQL script to create a table in Synapse / Azure SQL dedicated SQL pool
-- Adjust schema/column types as needed before running

CREATE TABLE dbo.SalesTransactions (
    OrderID NVARCHAR(50) NOT NULL,
    OrderDate DATE NOT NULL,
    Region NVARCHAR(50),
    Product NVARCHAR(100),
    Quantity INT,
    UnitPrice DECIMAL(10,2),
    Salesperson NVARCHAR(100),
    Channel NVARCHAR(50),
    Total DECIMAL(12,2)
);
-- For the daily KPIs:
CREATE TABLE dbo.DailyKPIs (
    OrderDate DATE PRIMARY KEY,
    TotalSales DECIMAL(12,2),
    UnitsSold INT,
    AvgOrderValue DECIMAL(12,2),
    Rolling7Avg DECIMAL(12,2)
);
