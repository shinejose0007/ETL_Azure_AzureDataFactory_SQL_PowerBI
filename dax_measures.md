# Suggested DAX measures for Power BI (DailyKPIs table)

Assumes you loaded `transformed_daily_kpis.csv` into a table named 'DailyKPIs' with columns:
- OrderDate (Date)
- TotalSales (Decimal)
- UnitsSold (Int)
- AvgOrderValue (Decimal)
- Rolling7Avg (Decimal)

1) Total Sales
TotalSales = SUM('DailyKPIs'[TotalSales])

2) Units Sold
UnitsSold = SUM('DailyKPIs'[UnitsSold])

3) Average Order Value (overall)
AvgOrderValue = AVERAGE('DailyKPIs'[AvgOrderValue])

4) 7-day rolling average (context-aware)
Rolling7AvgMeasure =
CALCULATE(
    AVERAGE('DailyKPIs'[TotalSales]),
    DATESINPERIOD(
        'DailyKPIs'[OrderDate],
        LASTDATE('DailyKPIs'[OrderDate]),
        -7,
        DAY
    )
)

5) Month-to-date Sales
MTDSales =
TOTALMTD(
    SUM('DailyKPIs'[TotalSales]),
    'DailyKPIs'[OrderDate]
)

6) Year-to-date Sales
YTDSales =
TOTALYTD(
    SUM('DailyKPIs'[TotalSales]),
    'DailyKPIs'[OrderDate]
)

7) % change vs previous period (7-day)
PctChange7Days =
VAR Current = [TotalSales]
VAR Prev = 
    CALCULATE(
        [TotalSales],
        DATEADD('DailyKPIs'[OrderDate], -7, DAY)
    )
RETURN
IF(ISBLANK(Prev), BLANK(), DIVIDE(Current - Prev, Prev))

Notes:
- Replace measure references (e.g., [TotalSales]) with the exact measure names you create.
- For visuals that use time intelligence, mark 'OrderDate' as a Date table or create a Date dimension and mark it as Date Table in Power BI.
- If you import the detailed `synapse_load.csv`, you can create Product / Region level measures by creating relationships and using SUMX over transactional table.
