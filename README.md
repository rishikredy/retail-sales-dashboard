# report
# 🛍️ Retail Sales Cleanup & Trend Report

A simple Streamlit dashboard to clean, analyze, and visualize retail sales data.  
Upload your sales CSV file, and get powerful monthly insights — no Excel formulas needed!

---

## 🔧 Tech Stack

- Python
- Pandas
- Streamlit

---

## 💡 Features

✅ Upload retail sales data (CSV)  
✅ Clean and format the data (Date, Revenue, etc.)  
✅ View raw data sample  
✅ See monthly revenue trends by category  
✅ View top 5 products (monthly)  
✅ Download cleaned dataset

---

## 📊 Sample Dataset Format

Your CSV should include columns like:

| Date       | Product_Name     | Category     | Units_Sold | Price | Revenue |
|------------|------------------|--------------|------------|-------|---------|
| 2023-01-01 | Wireless Mouse   | Electronics  | 100        | 10    | 1000    |
| 2023-01-02 | T-Shirt - Black  | Clothing     | 50         | 20    | 1000    |

---

## 🚀 How to Run Locally

```bash
# 1. Clone this repo
git clone https://github.com/your-username/retail-sales-dashboard.git
cd retail-sales-dashboard

# 2. (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate

# 3. Install requirements
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run frontend.py
