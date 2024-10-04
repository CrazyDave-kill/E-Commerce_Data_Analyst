import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from babel.numbers import format_currency
sns.set(style='dark')
import pandas as pd

# Load datasets with only necessary columns
orders_df = pd.read_csv("orders_dataset_modified.csv", usecols=["order_id", "order_purchase_timestamp"])
order_items_df = pd.read_csv("order_items_dataset_modified.csv", usecols=["order_id", "seller_id", "price", "freight_value", "order_item_id"])
order_payments_df = pd.read_csv("order_payments_dataset_modified.csv", usecols=["order_id", "payment_type", "payment_value"])

# Convert order_purchase_timestamp to datetime
orders_df['order_purchase_timestamp'] = pd.to_datetime(orders_df['order_purchase_timestamp'])

# Merge datasets with only necessary columns
merged_df = pd.merge(orders_df, order_items_df, on="order_id")
merged_df = pd.merge(merged_df, order_payments_df, on="order_id")

# Sidebar for date range selection
min_date = merged_df["order_purchase_timestamp"].min().date()
max_date = merged_df["order_purchase_timestamp"].max().date()

with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Ensure start_date and end_date are in datetime format
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter dataframe based on date range
main_df = merged_df[(merged_df["order_purchase_timestamp"] >= start_date) & 
                    (merged_df["order_purchase_timestamp"] <= end_date)]

# Function to analyze seller performance
def analyze_seller_performance(df):
    df['total_revenue'] = df['price'] + df['freight_value']
    seller_revenue = df.groupby('seller_id').agg({
        'total_revenue': 'sum',
        'order_item_id': 'count'
    }).reset_index()
    seller_revenue.columns = ['seller_id', 'total_revenue', 'total_items']
    seller_revenue = seller_revenue.sort_values(by='total_revenue', ascending=False)
    return seller_revenue

# Function to analyze payment methods
def analyze_payment_methods(df):
    total_purchase_value = df.groupby('payment_type')['payment_value'].sum().reset_index()
    total_purchase_value.columns = ['payment_type', 'total_purchase_value']
    purchase_frequency = df['payment_type'].value_counts().reset_index()
    purchase_frequency.columns = ['payment_type', 'purchase_count']
    payment_analysis = total_purchase_value.merge(purchase_frequency, on='payment_type')
    payment_analysis = payment_analysis.sort_values(by='total_purchase_value', ascending=False)
    return payment_analysis

# Analyze seller performance
seller_performance_df = analyze_seller_performance(main_df)
payment_methods_df = analyze_payment_methods(main_df)

# Title
st.title("📊 E-Commerce Dashboard")
st.markdown("### Analyzing Seller Performance and Payment Methods")

# Daily Orders and Revenue in IDR
st.subheader('Daily Orders')

# Calculate daily orders and revenue
main_df['total_revenue'] = main_df['price'] + main_df['freight_value']
daily_orders_df = main_df.groupby(main_df['order_purchase_timestamp'].dt.date).agg({
    'order_item_id': 'count',
    'total_revenue': 'sum'
}).reset_index()
daily_orders_df.columns = ['order_date', 'order_count', 'revenue']

col1, col2 = st.columns(2)

with col1:
    total_orders = daily_orders_df['order_count'].sum()
    st.metric("Total orders", value=total_orders)

with col2:
    total_revenue = format_currency(daily_orders_df['revenue'].sum(), "IDR", locale='id_ID')
    st.metric("Total Revenue", value=total_revenue)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    daily_orders_df["order_date"],
    daily_orders_df["order_count"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)

# Seller Performance Visualization
st.subheader("Seller Performance")
fig, ax = plt.subplots(figsize=(16, 8))
colors = ['#4D4D4D' if i == 0 else '#B0B0B0' for i in range(len(seller_performance_df.head(10)))]
sns.barplot(y="total_revenue", x="seller_id", data=seller_performance_df.head(10), palette=colors, ax=ax)
ax.set_xlabel("Seller ID", fontsize=15)
ax.set_ylabel("Total Revenue", fontsize=15)
ax.set_title("Top 10 Sellers by Revenue", fontsize=20)
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Payment Methods Analysis Visualization
st.subheader("Payment Methods Analysis")
fig, ax = plt.subplots(figsize=(16, 8))
colors = ['#4D4D4D' if i == 0 else '#B0B0B0' for i in range(len(payment_methods_df))]
sns.barplot(y="total_purchase_value", x="payment_type", data=payment_methods_df, palette=colors, ax=ax)
ax.set_xlabel("Payment Type", fontsize=15)
ax.set_ylabel("Total Purchase Value", fontsize=15)
ax.set_title("Payment Methods by Total Purchase Value", fontsize=20)
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Seller Performance and Payment Methods Analysis Tables
col1, col2 = st.columns(2)

with col1:
    st.write("### Seller Performance")
    st.dataframe(seller_performance_df)

with col2:
    st.write("### Payment Methods Analysis")
    st.dataframe(payment_methods_df)

# Filtered Data
st.write("### Filtered Data")
st.dataframe(main_df)
