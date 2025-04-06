import pandas as pd
import streamlit as st

st.set_page_config(page_title="Retail Sales Report", layout="wide")
st.title("🛍️ Retail Sales Cleanup & Trend Report")

# Upload file
uploaded_file = st.file_uploader("📂 Upload your cleaned sales data (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # --- Data Preview ---
    st.subheader("📋 Raw Data Preview")
    if st.checkbox("Show raw data"):
        st.write(df.head(10))

    # --- Preprocessing ---
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M').astype(str)

    # --- Monthly Revenue by Category ---
    st.subheader("📈 Monthly Revenue by Category")
    monthly_rev = df.groupby(['Month', 'Category'])['Revenue'].sum().unstack().fillna(0)
    st.bar_chart(monthly_rev)

    # --- Top Products by Revenue ---
    st.subheader("🏆 Top 5 Products by Revenue (Per Month)")
    top_products = df.groupby(['Month', 'Product_Name'])['Revenue'].sum().reset_index()
    top_products = top_products.sort_values(['Month', 'Revenue'], ascending=[True, False])
    top_5 = top_products.groupby('Month').head(5)

    st.dataframe(top_5)

    # --- Download Cleaned Data ---
    st.subheader("💾 Download Cleaned Data")
    st.download_button(
        label="Download as CSV",
        data=df.to_csv(index=False),
        file_name="cleaned_sales_data.csv",
        mime="text/csv"
    )

else:
    st.info("👆 Please upload a CSV file to begin.")
