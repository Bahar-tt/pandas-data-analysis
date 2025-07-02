<<<<<<< HEAD
# 🐼 Pandas Real-World Data Analysis Project

This repository contains a complete practical training in **Pandas** — a powerful data analysis library in Python — structured as a 10-day hands-on journey, from beginner to real-world project level. It simulates the type of analytical tasks performed by data professionals in industries, including retail analytics, time-series analysis, and reporting.

---

## 📌 Overview

- 💼 **Target**: Preparing for real-world data analyst / AI engineer roles (Germany-focused use case)
- 📚 **Tools Used**: Python, Pandas, Jupyter/VSCode, Excel (for export)
- 📁 **Dataset**: Simulated `sales_data.csv` created manually to replicate business sales behavior
- 🧪 **Result**: Multiple step-by-step tasks that demonstrate mastery over all core Pandas features

---

## 📅 Project Roadmap (10 Days)

| Day | Topic | Key Skills Practiced |
|-----|-------|----------------------|
| 1 | Intro to Pandas | DataFrame, Series, indexing, filtering |
| 2 | Structure Operations | `set_index`, `sort_values`, `drop`, `rename` |
| 3 | Statistical Methods | `sum`, `mean`, `describe`, `groupby` |
| 4 | Missing Data | `isnull`, `fillna`, `dropna`, `interpolate` |
| 5 | Data Merging | `merge`, `join`, `concat` |
| 6 | Reshaping Data | `melt`, `pivot`, `pivot_table`, `stack`, `unstack` |
| 7 | Datetime Handling | `to_datetime`, `dt`, `resample`, `day_name` |
| 8 | File I/O | `read_csv`, `to_csv`, `read_excel`, `to_excel` |
| 9 | Combined Exercises | Mixed operations across a real dataset |
| 10 | Final Project | Realistic multi-step business analysis scenario |

---

## 📊 Final Project Summary

### 🔹 Dataset Fields:
- `order_id`, `order_date`, `shipping_date`, `customer_name`, `country`, `category`, `quantity`, `unit_price`, `total_price`

### 🔸 Tasks:
- Convert and manipulate `datetime` columns
- Calculate total sales (`total_price`)
- Group sales by `country`, `month`, and `category`
- Analyze shipping delays
- Build pivot tables: `customer_name x category`
- Save filtered results to CSV and Excel

---

## 💡 Example Analysis Snippets

```python
# Total sales per month per country
df.groupby([df['country'], df['order_date'].dt.month_name()])['total_price'].sum()

# Pivot: Monthly sales by category
df.pivot_table(index='month', columns='category', values='total_price', aggfunc='sum')

# Shipping delay in days
df['shipping_delay'] = (df['shipping_date'] - df['order_date']).dt.days


📁 Outputs
final_sales_data.csv – filtered transactional dataset

pivot_sales_report.xlsx – category-based monthly pivot table

germany_sales.csv – filtered sales data for Germany

category_sales.xlsx – category-level analysis

📍 Author
🧑‍💻 Bahar Nasehi – AI Intern & Future Data Professional in Germany 🇩🇪
🌱 Learning Path: Python → Pandas → Matplotlib + Seaborn → Machine Learning

✅ What’s Next?
👉 From here, I’ll continue to:

Explore Matplotlib & Seaborn for professional data visualization

Prepare dashboard-style reports

Integrate with real datasets (e.g., from Kaggle or open-data portals)
=======
# pandas-data-analysis
“Real-world data analysis projects using Pandas”
>>>>>>> 04d747e3bc2bbf5b31c69e57de33dfa59189b6e8
