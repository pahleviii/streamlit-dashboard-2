import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    day_df = pd.read_csv("Cleaned_day.csv")
    hour_df = pd.read_csv("Cleaned_hour.csv")
    return day_df, hour_df

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

# Scatter Plot Interaktif
st.subheader("Scatter Plot: Temperatur vs Jumlah Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8, 6))
sns.regplot(x=df["temp"], y=df["cnt"], scatter_kws={"alpha": 0.5}, line_kws={"color": "red"}, ax=ax)
st.pyplot(fig)

# Fitur interaktif: Filter data berdasarkan musim
st.sidebar.subheader("Filter Data")
season_option = st.sidebar.selectbox("Pilih Musim", df["season"].unique())
filtered_df = df[df["season"] == season_option]

st.subheader(f"Data Penyewaan Sepeda untuk Musim {season_option}")
st.write(filtered_df.head())

# Unduh dataset
csv_data = df.to_csv(index=False).encode('utf-8')
st.download_button("Unduh Data", csv_data, file_name="data.csv", mime="text/csv")

st.write("Dashboard ini menampilkan analisis data penyewaan sepeda berdasarkan dataset yang tersedia.")
