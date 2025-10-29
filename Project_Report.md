# 🧾 Project Report: Data-Driven Stock Analysis — Organizing, Cleaning, and Visualizing Market Trends

## 📘 Project Overview
The **Stock Performance Dashboard** provides a comprehensive visualization and analysis of the **Nifty 50** stocks' performance over the past year.  
It analyzes daily stock data (Open, Close, High, Low, Volume) to generate insights and visualize market behavior.  
This helps investors, analysts, and enthusiasts make informed decisions based on stock performance trends.

---

## 🎯 Objectives
- Extract and organize stock data provided in **YAML format**.  
- Clean, validate, and transform the data into structured **CSV** files.  
- Analyze and visualize stock performance metrics using **Python, Streamlit, and Power BI**.  
- Identify top-performing and underperforming stocks, analyze volatility, and evaluate sector performance.  

---

## 🧩 Business Use Cases
1. **Stock Performance Ranking:** Identify top 10 best and worst performing stocks over the year.  
2. **Market Overview:** Show average performance, price, and volume trends.  
3. **Volatility Analysis:** Determine risk and price fluctuations for each stock.  
4. **Investment Insights:** Highlight consistent gainers or decliners.  
5. **Decision Support:** Enable retail and institutional investors to track trends easily.

---

## 🧮 Approach & Methodology

### 🔹 1. Data Extraction and Transformation
- Source data: YAML files organized month-wise (e.g., `data/2023-10`, `data/2023-11`, etc.).  
- Each YAML file contains daily trading data.  
- Python scripts combine all monthly YAMLs into a consolidated **final.csv** file.  
- The script ensures all records are clean, consistent, and formatted properly for analysis.

### 🔹 2. Data Cleaning
- Missing values handled through interpolation or removal.  
- Non-numeric entries in price/volume columns corrected.  
- Date formats standardized for time-series analysis.

### 🔹 3. Data Analysis (Metrics Computed)
| Metric | Formula | Description |
|--------|----------|-------------|
| **Daily Return** | (Close - Prev Close) / Prev Close | Daily stock movement |
| **Annual Return** | (Last Close / First Open) - 1 | Overall performance |
| **Volatility** | Standard deviation of daily returns | Risk measurement |
| **Cumulative Return** | Sum of daily returns | Growth trend |
| **Average Volume** | Mean of daily volumes | Trading activity indicator |

---

## 📊 Visualizations (Streamlit Dashboard)

### 1️⃣ **Key Metrics**
- Top 10 gainers and losers displayed in tables.  
- Quick market overview (average returns, prices, volumes).  

### 2️⃣ **Volatility Analysis**
- Standard deviation of daily returns calculated.  
- Bar chart shows **Top 10 most volatile stocks** — higher = more risk.

### 3️⃣ **Cumulative Return Over Time**
- Line chart showing cumulative return for top 5 performing stocks.  
- Helps visualize long-term growth and trends.

### 4️⃣ **Sector-Wise Performance**
- Merges yearly returns with **sector data (CSV)**.  
- Bar chart shows **average yearly return by sector**.  

### 5️⃣ **Stock Price Correlation**
- Computes **correlation matrix** between stock closing prices.  
- Heatmap visualizes stock relationships (positive/negative correlations).  

### 6️⃣ **Top 5 Gainers & Losers (Month-Wise)**
- Groups data by month, calculates monthly returns.  
- Displays 12 mini bar charts showing each month's top and bottom 5 performers.

---

## ⚙️ Tools and Technologies
| Category | Tools |
|-----------|-------|
| **Programming Language** | Python |
| **Visualization Tools** | Streamlit, Power BI |
| **Libraries** | Pandas, NumPy, PyYAML, Matplotlib, Seaborn |
| **Database (optional)** | MySQL / PostgreSQL (SQLAlchemy) |
| **Version Control** | GitHub |

---

## 🧾 Results & Insights
- Identified **Top 10 gainers and losers** based on annual returns.  
- Visualized **volatility and sector performance** trends.  
- Displayed **correlation heatmaps** showing inter-stock relationships.  
- Provided **interactive dashboards** for investors and analysts.  
- Power BI dashboard offers **executive-level summaries** and cross-filtering capabilities.

---

## 🧠 Learnings and Takeaways
- Efficient handling of structured and semi-structured data (YAML → CSV).  
- Integration of **data engineering, analysis, and visualization** in one workflow.  
- Application of **financial analytics metrics** using Python.  
- Creating interactive web dashboards with **Streamlit**.

---

## 📁 Deliverables
- ✅ `Stock_app.py` — Streamlit dashboard code  
- ✅ `final.csv` — Consolidated cleaned data  
- ✅ `Sector_data - Sheet1.csv` — Sector mapping file  
- ✅ `Stock_market.pbix` — Power BI dashboard  
- ✅ `requirements.txt` — Dependency list  
- ✅ `Project_Report.md` — Documentation (this file)  

---

## 🧪 Evaluation Readiness
- All 5 visualization modules fully implemented.  
- Data pipeline verified and validated.  
- GitHub repository is public and organized.  
- README and project report completed.  
- Ready for final submission and live demo.
