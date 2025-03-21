import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

def load_data():
    day_df = pd.read_csv("Cleaned_day.csv")
    hour_df = pd.read_csv("Cleaned_hour.csv")
    return day_df, hour_df

def save_plot_as_image(fig, filename):
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    return buf

# Load dataset
day_df, hour_df = load_data()

st.title("Dashboard Analisis Penyewaan Sepeda")
st.sidebar.header("Pengaturan")

data_option = st.sidebar.radio("Pilih Dataset", ("Day Data", "Hour Data"))
df = day_df if data_option == "Day Data" else hour_df

st.subheader("Statistik Ringkasan")
st.write(df.describe())

# Visualisasi Heatmap
st.subheader("Heatmap Korelasi")
corr_columns = ["temp", "atemp", "hum", "windspeed", "casual", "registered", "cnt"]
corr_matrix = df[corr_columns].corr()
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
st.pyplot(fig)

# Simpan heatmap sebagai gambar
image_buf = save_plot_as_image(fig, "heatmap.png")
st.download_button("Unduh Heatmap", image_buf, file_name="heatmap.png", mime="image/png")

# Scatter Plot Interaktif
st.subheader("Scatter Plot: Temperatur vs Jumlah Penyewaan Sepeda")
fig_scatter = px.scatter(df, x="temp", y="cnt", trendline="ols", title="Hubungan Suhu dan Penyewaan")
st.plotly_chart(fig_scatter)

# Unduh dataset
csv_data = df.to_csv(index=False).encode('utf-8')
st.download_button("Unduh Data", csv_data, file_name="data.csv", mime="text/csv")

st.write("Dashboard ini menampilkan analisis data penyewaan sepeda berdasarkan dataset yang tersedia.")
