# Streamlit Dashboard untuk Analisis Penyewaan Sepeda

## 📌 Deskripsi
Dashboard ini dibuat menggunakan **Streamlit** untuk menganalisis data penyewaan sepeda berdasarkan dataset harian (*day_df*) dan per jam (*hour_df*). Dashboard ini menyajikan berbagai visualisasi interaktif dan fitur eksplorasi data.

## 📂 Fitur
✅ **Pilih Dataset**: Pengguna dapat memilih antara dataset harian atau per jam.
✅ **Statistik Ringkasan**: Menampilkan statistik deskriptif dari dataset yang dipilih.
✅ **Heatmap Korelasi**: Menampilkan hubungan antar variabel menggunakan **seaborn heatmap**.
✅ **Scatter Plot Interaktif**: Menunjukkan hubungan antara suhu dan jumlah penyewaan sepeda dengan **Plotly**.
✅ **Unduh Data**: Dataset yang dipilih dapat diunduh dalam format CSV.
✅ **Unduh Visualisasi**: Heatmap dapat disimpan dalam bentuk gambar PNG.

## 📥 Instalasi
1. **Clone repository (jika ada)**
   ```bash
   git clone https://github.com/username/repo-name.git
   cd repo-name
   ```
2. **Buat virtual environment (opsional)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Mac/Linux
   venv\Scripts\activate  # Untuk Windows
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Menjalankan Aplikasi
Jalankan perintah berikut untuk memulai dashboard:
```bash
streamlit run app.py
```

## 📊 Struktur Kode
- `Dashboard.py`: Script utama yang menjalankan dashboard.
- `Cleaned_day.csv` & `Cleaned_hour.csv`: Dataset yang digunakan.
- `requirements.txt`: File dependencies yang dibutuhkan.

## 🛠️ Teknologi yang Digunakan
- **Python** (Pandas, Matplotlib, Seaborn, Streamlit, Plotly)
- **Streamlit**: Untuk membangun UI interaktif.
- **Seaborn & Matplotlib**: Untuk visualisasi data statis.


