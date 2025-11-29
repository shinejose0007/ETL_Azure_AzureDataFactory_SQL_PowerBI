# Power BI Page Mockups & Step-by-step assembly

Overview page
1. Import 'transformed_daily_kpis.csv' as 'DailyKPIs'.
2. Create measures (use dax_measures.md).
3. Add Card visuals for YTDSales, MTDSales, UnitsSold.
4. Add a Line chart:
   - Axis: OrderDate (continuous)
   - Values: TotalSales
   - Secondary Values: Rolling7AvgMeasure
   - Analytics -> Forecast: add 14-day forecast
5. Add slicers: Date range, Region (if available).
6. Format visuals and save report as Demo_Sales_Report.pbix

Sales by Region & Product
1. Use SalesTransactions if available; create aggregations if needed.
2. Add Stacked Bar: Region vs TotalSales
3. Add Matrix: Product x Region with TotalSales and UnitsSold

Transactions
1. Table visual: include OrderID, OrderDate, Product, Quantity, UnitPrice, Total, Salesperson, Region, Channel
2. Add Date slicer and filters.

Forecast & Anomalies
1. Line chart with forecast (30 days)
2. Create AnomalyFlag = IF(TotalSales > Rolling7Avg * 1.5, 1, 0)
3. Visualize anomalies with conditional formatting or scatter overlay.
