"""
etl.py - simple ETL script for the demo repo
Run: python etl.py
Creates:
 - transformed.csv (aggregated daily KPIs)
 - synapse_load.csv (simulated table load file)
"""
import pandas as pd

def main():
    df = pd.read_csv("data_sample_sales.csv", parse_dates=["OrderDate"])
    # Basic cleaning
    df = df.dropna(subset=["OrderDate","Product","Quantity","UnitPrice"])
    df["Total"] = df["Quantity"] * df["UnitPrice"]
    # Convert types
    df["Quantity"] = df["Quantity"].astype(int)
    # Aggregate daily KPIs
    daily = df.groupby("OrderDate").agg(
        TotalSales = ("Total","sum"),
        UnitsSold = ("Quantity","sum"),
        AvgOrderValue = ("Total","mean")
    ).reset_index()
    daily = daily.sort_values("OrderDate")
    # Create rolling 7-day average as a simple forecast baseline
    daily["Rolling7Avg"] = daily["TotalSales"].rolling(window=7,min_periods=1).mean()
    # Save transformed data
    daily.to_csv("transformed_daily_kpis.csv", index=False)
    # Simulate load file for Synapse (full detail rows)
    df.to_csv("synapse_load.csv", index=False)
    print("ETL complete. Outputs: transformed_daily_kpis.csv, synapse_load.csv")

if __name__ == "__main__":
    main()
