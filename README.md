# Azure Data Factory → Synapse → Power BI - Demo Repo

This small repository is designed as a hands-on demo you can complete in ~1–2 hours.
It provides:
- sample data: `data_sample_sales.csv`
- ETL script: `etl.py` (creates `transformed_daily_kpis.csv` and `synapse_load.csv`)
- Synapse SQL script: `create_table.sql`
- Azure Data Factory pipeline template: `data_factory_pipeline_example.json`
- README with step-by-step instructions (this file)
- `pbix_readme.txt`: 3-sentence description for the Power BI artifact

## Quick summary (what you will build)
1. Run the ETL locally to clean and produce daily KPIs.
2. (Optional) Simulate loading full rows into Azure Synapse using `create_table.sql` and `synapse_load.csv`.
3. Import `transformed_daily_kpis.csv` into Power BI Desktop and create a dashboard showing KPIs, trends and a simple forecast.

## Step 1 — Inspect sample data
File: `data_sample_sales.csv`  
Columns: OrderID, OrderDate, Region, Product, Quantity, UnitPrice, Salesperson, Channel

## Step 2 — Run ETL (local)
Requirements: Python 3.8+, pandas installed.
1. Open a terminal in the repo folder.
2. Run: `python etl.py`
3. Outputs:
   - `transformed_daily_kpis.csv` (daily KPIs ready for BI)
   - `synapse_load.csv` (detailed rows to load into Synapse)

## Step 3 — Load data into Synapse (optional)
This is a high-level guide; use the Azure Portal / Synapse Studio:
1. Create a database / dedicated SQL pool or use serverless SQL pool.
2. Run `create_table.sql` in Synapse Studio to create tables.
3. Use Azure Data Factory or Synapse Copy Data tool to copy `synapse_load.csv` from your Blob Storage into `dbo.SalesTransactions`. The `data_factory_pipeline_example.json` is a starting template for an ADF pipeline (replace dataset and linked service names).

## Step 4 — Azure Data Factory (optional)
1. In Azure Data Factory, create Linked Services:
   - Blob Storage (where `synapse_load.csv` is uploaded)
   - Azure Synapse Analytics (destination)
2. Create Datasets:
   - DelimitedText dataset pointing to the CSV in Blob Storage
   - Azure SQL dataset pointing to the Synapse table
3. Import the pipeline JSON (`data_factory_pipeline_example.json`) as a template, or create a Copy activity that reads the CSV and writes to the Synapse table.

## Step 5 — Build Power BI Dashboard (local)
1. Open Power BI Desktop.
2. Get Data → Text/CSV → choose `transformed_daily_kpis.csv`.
3. In Power Query: ensure `OrderDate` is Date type; set locale if needed.
4. Close & Apply.
5. Create visuals:
   - Card visual: TotalSales (measure: SUM(TotalSales))
   - Line chart: OrderDate vs TotalSales (add Rolling7Avg as a second series)
   - Bar chart: UnitsSold by OrderDate (or by Region if you load transactions)
   - Table: Top Products (if loading detailed `synapse_load.csv` data)
   - Forecast: select the line chart, use Analytics pane → Forecast to add a basic forecast.
6. Save your report as `Demo_Sales_Report.pbix`.

## PBIX README (3-sentence description)
See `pbix_readme.txt`.

## Tips & Next steps (high leverage)
- Turn the local ETL into an Azure Function or Data Factory pipeline that runs on a schedule.
- Replace CSV storage with Azure Blob Storage and point Data Factory to the storage.
- Create a Synapse SQL view that aggregates KPIs for Power BI for better performance.
