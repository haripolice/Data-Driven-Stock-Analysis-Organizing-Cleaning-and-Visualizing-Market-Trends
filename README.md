# 📊 Data-Driven Stock Analysis: Organizing, Cleaning, and Visualizing Market Trends  

### 🚀 Overview
This project builds a complete **Stock Performance Dashboard** that analyzes and visualizes **Nifty 50** stock data.  
Using **Python**, **Streamlit**, and **Power BI**, the project cleans YAML-formatted stock data, transforms it into structured CSVs, and provides interactive insights such as performance rankings, volatility, sector-wise returns, and correlations.

---

## 🎯 Objectives
- Organize and clean daily stock data.  
- Analyze performance and volatility across all Nifty 50 stocks.  
- Build interactive dashboards in **Streamlit** and **Power BI**.  
- Enable investors and analysts to quickly identify trends and opportunities.

---

## 🧠 Skills Demonstrated
`Python` • `Pandas` • `NumPy` • `Matplotlib` • `Seaborn` • `Streamlit` • `YAML` • `SQLAlchemy` • `Power BI` • `Data Cleaning` • `Data Visualization`

---

## 📂 Project Structure
```
📁 Data-Driven-Stock-Analysis/
│
├── Stock_app.py                     # Main Streamlit dashboard
├── Sector_data - Sheet1.csv         # Sector classification data
├── data/
│   ├── 2023-10/ ... 2024-11/        # Daily YAML files (monthly folders)
│   ├── final.csv                    # Cleaned, consolidated dataset
│
├── Stock_market.pbix                # Power BI visualization
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

---

## 🧩 Features Implemented

### 1️⃣ **Key Metrics Dashboard**
- Displays **Top 10 Gainers** and **Top 10 Losers** based on annual returns.  
- Provides a quick **market snapshot** including average price, volume, and return ratios.

### 2️⃣ **Volatility Analysis**
- Computes **daily returns** and **standard deviation** per stock.  
- Shows the **Top 10 most volatile stocks** with a bar chart for risk assessment.

### 3️⃣ **Cumulative Return Over Time**
- Calculates **cumulative returns** from start to end of the year.  
- Plots line charts for the **Top 5 performing stocks** over time.

### 4️⃣ **Sector-Wise Performance**
- Merges with sector CSV to group stocks by industry.  
- Displays a **bar chart of average yearly returns** for each sector.

### 5️⃣ **Stock Price Correlation**
- Computes pairwise **correlation coefficients** between stock prices.  
- Visualizes them with a **heatmap** to show co-movement patterns.

### 6️⃣ **Top 5 Gainers and Losers (Month-Wise)**
- Calculates **monthly returns**.  
- Shows **Top 5 gainers and losers per month** using dynamic bar charts.

---

## ⚙️ Installation & Setup

### 🔧 Prerequisites
- Python 3.9 +  
- Git installed  

### 📦 Install dependencies
```bash
pip install -r requirements.txt
```

### ▶️ Run the Streamlit app
```bash
streamlit run Stock_app.py
```

### 💡 View Dashboard
Once started, open the link displayed in the terminal (usually `http://localhost:8501`).

---

## 🧰 Tools & Technologies
| Category | Tools |
|-----------|-------|
| **Programming Language** | Python |
| **Visualization** | Streamlit, Power BI |
| **Data Handling** | Pandas, NumPy, PyYAML |
| **Database (Optional)** | MySQL / PostgreSQL (via SQLAlchemy) |
| **Libraries** | Matplotlib, Seaborn |

---

## 📈 Results & Insights
- **Top-performing** and **worst-performing** stocks are automatically ranked.  
- Interactive visualizations reveal **market volatility**, **sector performance**, and **price correlations**.  
- Power BI dashboard provides advanced exploration and business insights.

---

## 🧪 Evaluation Readiness
✅ All project deliverables completed:
- YAML → CSV transformation  
- 5 visualization modules implemented  
- Streamlit & Power BI dashboards ready  
- Public GitHub repository maintained  