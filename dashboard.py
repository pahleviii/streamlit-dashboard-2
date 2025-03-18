import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title("Dashboard Analisis Data E-commerce")

# Memuat dataset (pastikan path sesuai)
@st.cache_data
def load_data():
    customers_df = pd.read_csv("olist_customers_dataset.csv")
    orders_df = pd.read_csv("olist_orders_dataset.csv")
    sellers_df = pd.read_csv("olist_sellers_dataset.csv")
    products_df = pd.read_csv("olist_products_dataset.csv")
    return customers_df, orders_df, sellers_df, products_df

customers_df, orders_df, sellers_df, products_df = load_data()

# Sidebar untuk Filter
st.sidebar.header("Filter Data")
selected_city = st.sidebar.selectbox("Pilih Kota", customers_df["customer_city"].unique())
selected_state = st.sidebar.selectbox("Pilih Negara Bagian", sellers_df["seller_state"].unique())

# Pilihan Visualisasi
st.sidebar.header("Pilih Visualisasi")
visualization_options = [
    "Top 10 Kota dengan Jumlah Pesanan Terbanyak",
    "Distribusi Penjual Berdasarkan Negara Bagian (Top 10)",
    "Distribusi Produk Berdasarkan Kategori (Top 10)",
    "Distribusi Waktu Pemesanan"
]
selected_visualization = st.sidebar.radio("Pilih Visualisasi", visualization_options)

# Menampilkan data berdasarkan filter
filtered_customers = customers_df[customers_df["customer_city"] == selected_city]
st.write(f"### Data Pelanggan di {selected_city}")
st.dataframe(filtered_customers)

filtered_sellers = sellers_df[sellers_df["seller_state"] == selected_state]
st.write(f"### Data Penjual di {selected_state}")
st.dataframe(filtered_sellers)

# Menampilkan visualisasi sesuai pilihan
if selected_visualization == "Top 10 Kota dengan Jumlah Pesanan Terbanyak":
    st.write("### Top 10 Kota dengan Jumlah Pesanan Terbanyak")
    orders_by_city = orders_df.merge(customers_df, on="customer_id")["customer_city"].value_counts().head(10)
    fig, ax = plt.subplots()
    sns.barplot(x=orders_by_city.index, y=orders_by_city.values, palette="Blues", ax=ax)
    plt.xticks(rotation=45)
    plt.xlabel("Kota")
    plt.ylabel("Jumlah Pesanan")
    st.pyplot(fig)

elif selected_visualization == "Distribusi Penjual Berdasarkan Negara Bagian (Top 10)":
    st.write("### Distribusi Penjual Berdasarkan Negara Bagian (Top 10)")
    sellers_by_state = sellers_df["seller_state"].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=sellers_by_state.index, y=sellers_by_state.values, palette="Reds", ax=ax)
    plt.xlabel("Negara Bagian")
    plt.ylabel("Jumlah Penjual")
    plt.xticks(rotation=45)
    st.pyplot(fig)

elif selected_visualization == "Distribusi Produk Berdasarkan Kategori (Top 10)":
    st.write("### Distribusi Produk Berdasarkan Kategori (Top 10)")
    products_by_category = products_df["product_category_name"].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=products_by_category.index, y=products_by_category.values, palette="Greens", ax=ax)
    plt.xlabel("Kategori Produk")
    plt.ylabel("Jumlah Produk")
    plt.xticks(rotation=45)
    st.pyplot(fig)

elif selected_visualization == "Distribusi Waktu Pemesanan":
    st.write("### Distribusi Waktu Pemesanan")
    orders_df["order_purchase_timestamp"] = pd.to_datetime(orders_df["order_purchase_timestamp"])
    orders_df["order_month"] = orders_df["order_purchase_timestamp"].dt.to_period("M")
    orders_by_month = orders_df["order_month"].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x=orders_by_month.index.astype(str), y=orders_by_month.values, marker="o", color="purple", ax=ax)
    plt.xlabel("Bulan")
    plt.ylabel("Jumlah Pesanan")
    plt.xticks(rotation=45)
    st.pyplot(fig)