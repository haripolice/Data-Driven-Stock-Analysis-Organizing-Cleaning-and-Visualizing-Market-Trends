import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yaml
import glob
import os

st.title('📊 Stock Analysis Dashboard')
st.markdown("---")  # Horizontal divider

# ✅ List of folders to scan for YAML files
stk_data_list = [
    '2023-10','2023-11','2023-12',
    '2024-01','2024-02','2024-03','2024-04','2024-05',
    '2024-06','2024-07','2024-08','2024-09','2024-10','2024-11'
]

# ✅ Master list for all data
all_dfs = []

# ✅ Load and combine YAML data
st.subheader("🔄 Loading stock data...")

for i in stk_data_list:
    folder_path = fr"C:\Users\KRHA1002\OneDrive - Nielsen IQ\Profile\GUVI\Project 2\data\{i}"
    yaml_files = glob.glob(os.path.join(folder_path, "*.yaml"))

    st.write(f"📁 Processing {i}: Found {len(yaml_files)} YAML files")

    file_dfs = []
    for j in yaml_files:
        try:
            with open(j, 'r') as file:
                yaml_data = yaml.safe_load(file)
            df = pd.DataFrame(yaml_data)
            file_dfs.append(df)
        except Exception as e:
            st.warning(f"⚠️ Error reading {j}: {e}")

    if file_dfs:
        month_df = pd.concat(file_dfs, ignore_index=True)
        all_dfs.append(month_df)
    else:
        st.warning(f"⚠️ No valid YAML files found in {folder_path}")

# ✅ Stop execution if no data found
if not all_dfs:
    st.error("❌ No YAML data found in any folder. Please check the file paths and try again.")
    st.stop()

# ✅ Combine all monthly data
final_df = pd.concat(all_dfs, ignore_index=True)
st.success(f"✅ Combined {len(final_df)} total records successfully!")

# ✅ Optional: Save for reference
output_path = r'C:\Users\KRHA1002\OneDrive - Nielsen IQ\Profile\GUVI\Project 2\data\final.csv'
final_df.to_csv(output_path, index=False)
st.write(f"💾 Combined data saved to: `{output_path}`")

# ----------------------------- #
# 📈 CALCULATIONS
# ----------------------------- #

Tickers = list(final_df['Ticker'].unique())
returns = []
start_prices = []
close_prices = []
avg_prices = []
avg_volumes = []
std_devs = []
cum_returns = []
clo_pct_df = pd.DataFrame()

for Tic in Tickers:
    data = final_df[final_df['Ticker'] == Tic].reset_index(drop=True)

    # Skip if empty
    if data.empty:
        continue

    clo_pct_df[Tic] = data['close'].pct_change()
    start_price = data.iloc[0]['open']
    close_price = data.iloc[-1]['close']
    yearly_return = (close_price / start_price) - 1
    avg_price = data['close'].mean().round(2)
    avg_volume = data['volume'].mean()

    daily_rets = data['close'].pct_change().dropna()
    cum_returns.append(daily_rets.sum())
    std_dev = daily_rets.std()

    std_devs.append(std_dev)
    start_prices.append(start_price)
    close_prices.append(close_price)
    returns.append(yearly_return)
    avg_prices.append(avg_price)
    avg_volumes.append(avg_volume)

yearly_return_df = pd.DataFrame({
    'Tickers': Tickers,
    'Annual_returns': returns,
    'start_prices': start_prices,
    'close_prices': close_prices,
    'avg_prices': avg_prices,
    'avg_volumes': avg_volumes,
    'std_devs': std_devs,
    'cum_returns': cum_returns
})

# ----------------------------- #
# 📊 STREAMLIT NAVIGATION
# ----------------------------- #
r = st.sidebar.radio('Navigation', [
    'Key Metrics',
    '1.Volatility Analysis',
    '2.Cumulative Return Over Time',
    '3.Sector-wise Performance',
    '4.Stock Price Correlation',
    '5.Top 5 Gainers and Losers'
])

# ----------------------------- #
# 1️⃣ KEY METRICS
# ----------------------------- #
if r == 'Key Metrics':
    st.header('🟢 Top 10 Gainers')
    st.markdown("---")
    top_10_green_stocks = yearly_return_df.sort_values(by='Annual_returns', ascending=False)
    st.dataframe(top_10_green_stocks.head(10))

    st.header('🔴 Top 10 Decliners')
    st.markdown("---")
    top_10_loss_stocks = yearly_return_df.sort_values(by='Annual_returns', ascending=True)
    st.dataframe(top_10_loss_stocks.head(10))

    st.header('📦 Quick Market Snapshot')
    st.markdown("---")

    col1, col2, col3 = st.columns(3, gap="small")
    green_stocks = (yearly_return_df['Annual_returns'] > 0).sum()
    red_stocks = (yearly_return_df['Annual_returns'] < 0).sum()

    col1.subheader('⚖️ Green vs Red Breakdown')
    col1.write(f"Total Green Stocks: {green_stocks}")
    col1.write(f"Total Red Stocks: {red_stocks}")

    col2.subheader('💰 Average Price (All Stocks)')
    col2.dataframe(yearly_return_df[['Tickers', 'avg_prices']])

    col3.subheader('📊 Average Daily Volume')
    col3.dataframe(yearly_return_df[['Tickers', 'avg_volumes']])

# ----------------------------- #
# 2️⃣ VOLATILITY ANALYSIS
# ----------------------------- #
if r == '1.Volatility Analysis':
    top_10_most_vol_df = yearly_return_df.sort_values(['std_devs'], ascending=False).head(10)
    st.dataframe(top_10_most_vol_df)

    plt.figure(figsize=(8, 4))
    plt.bar(top_10_most_vol_df['Tickers'], top_10_most_vol_df['std_devs'])
    plt.xlabel('Stock Tickers')
    plt.ylabel('Standard Deviation')
    plt.title('Top 10 Most Volatile Stocks')
    plt.xticks(rotation=75)
    st.pyplot(plt)

# ----------------------------- #
# 3️⃣ CUMULATIVE RETURN
# ----------------------------- #
if r == '2.Cumulative Return Over Time':
    top_5_cum = yearly_return_df.sort_values(['cum_returns'], ascending=False).head(5)
    st.dataframe(top_5_cum)
    plt.figure(figsize=(8, 4))
    plt.plot(top_5_cum['Tickers'], top_5_cum['cum_returns'], marker='o', linestyle='--', color='blue')
    plt.xlabel('Stock Ticker')
    plt.ylabel('Cumulative Return')
    plt.title('Cumulative Return by Ticker')
    plt.xticks(rotation=45)
    plt.grid(True)
    st.pyplot(plt)

# ----------------------------- #
# 4️⃣ SECTOR-WISE PERFORMANCE
# ----------------------------- #
if r == '3.Sector-wise Performance':
    try:
        sectors_df = pd.read_csv(r'C:\Users\kanna\Desktop\GUVI\5.Project\2.Data-Driven Stock Analysis\Sector_data - Sheet1.csv')
        sectors_df['tic_symbol'] = sectors_df['Symbol'].str.split(':').str[1]
        yearly_return_df['Tickers'] = yearly_return_df['Tickers'].str.strip()
        sectors_df['tic_symbol'] = sectors_df['tic_symbol'].str.strip()

        sector_map = dict(zip(sectors_df['tic_symbol'], sectors_df['sector']))
        yearly_return_df['sector'] = yearly_return_df['Tickers'].map(sector_map)
        yearly_return_df.loc[yearly_return_df['Tickers'] == 'TATACONSUM', 'sector'] = 'FMCG'

        manual_map = {'BHARTIARTL': 'TELECOM', 'ADANIENT': 'MISCELLANEOUS', 'BRITANNIA': 'FMCG'}
        yearly_return_df['sector'] = yearly_return_df['Tickers'].map(manual_map).fillna(yearly_return_df['sector'])

        sectors = list(yearly_return_df['sector'].unique())
        sec_annual_returns = [yearly_return_df[yearly_return_df['sector'] == sec]['Annual_returns'].mean() for sec in sectors]

        secwise_returns = pd.DataFrame({'sectors': sectors, 'Avg_yearly_return': sec_annual_returns}).sort_values('Avg_yearly_return', ascending=False)
        st.dataframe(secwise_returns)

        plt.figure(figsize=(8, 4))
        plt.bar(secwise_returns['sectors'], secwise_returns['Avg_yearly_return'])
        plt.xlabel('Sectors')
        plt.ylabel('Avg Yearly Return')
        plt.title('Sector-wise Average Yearly Return')
        plt.xticks(rotation=90)
        st.pyplot(plt)
    except Exception as e:
        st.error(f"Error loading sector data: {e}")

# ----------------------------- #
# 5️⃣ STOCK PRICE CORRELATION
# ----------------------------- #
if r == '4.Stock Price Correlation':
    if clo_pct_df.empty:
        st.error("No stock data to calculate correlation.")
    else:
        plt.figure(figsize=(56, 40))
        sns.heatmap(
            clo_pct_df.corr(),
            annot=True,
            fmt=".2f",
            cmap='coolwarm',
            linewidths=0.5,
            square=True,
            annot_kws={"size": 18},
            cbar_kws={"label": "Correlation", "shrink": 0.8}
        )
        plt.title("Stock Correlation Matrix", fontsize=28)
        plt.xticks(rotation=45, ha='right', fontsize=18)
        plt.yticks(rotation=0, fontsize=18)
        plt.tight_layout()
        st.pyplot(plt)

# ----------------------------- #
# 6️⃣ TOP 5 GAINERS AND LOSERS (MONTHLY)
# ----------------------------- #
if r == '5.Top 5 Gainers and Losers':
    stocks = list(final_df['Ticker'].unique())
    tickers, months, months_open, months_close = [], [], [], []

    for stock in stocks:
        infos = final_df[final_df['Ticker'] == stock].reset_index(drop=True)
        if infos.empty:
            continue
        grouped_data = infos.groupby(['month'])
        for a, b in grouped_data:
            months.append(b.iloc[0]['month'])
            tickers.append(stock)
            months_open.append(b.iloc[0]['open'])
            months_close.append(b.iloc[-1]['close'])

    monthly_return = pd.DataFrame({
        'tickers': tickers,
        'months': months,
        'months_open': months_open,
        'months_close': months_close
    })
    monthly_return['month_return'] = (monthly_return['months_close'] - monthly_return['months_open']) / monthly_return['months_open']

    periods = sorted(monthly_return['months'].unique())
    for period in periods:
        temp = monthly_return[monthly_return['months'] == period]
        if temp.empty:
            continue
        top5 = temp.sort_values(by='month_return', ascending=False).head(5)
        bottom5 = temp[temp['month_return'] < 0].sort_values(by='month_return').head(5)
        combined = pd.concat([top5, bottom5])

        plt.figure(figsize=(10, 6))
        bars = plt.bar(combined['tickers'], combined['month_return'],
                       color=combined['month_return'].apply(lambda x: 'green' if x > 0 else 'red'))

        plt.title(f'Top 5 Gainers and Losers – {pd.to_datetime(period).strftime("%B %Y")}')
        plt.ylabel('Monthly Return (%)')
        plt.xticks(rotation=75)
        plt.axhline(0, color='black', linewidth=0.8)
        plt.grid(axis='y', linestyle='--', linewidth=0.5)

        for bar in bars:
            height = bar.get_height()
            plt.annotate(f'{height:.2%}', xy=(bar.get_x() + bar.get_width()/2, height),
                         xytext=(0, 3 if height >= 0 else -15),
                         textcoords="offset points", ha='center', fontsize=8)

        plt.tight_layout()
        st.pyplot(plt)
