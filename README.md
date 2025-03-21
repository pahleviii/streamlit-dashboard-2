Deskripsi

Dashboard ini dibuat menggunakan Streamlit untuk menganalisis faktor-faktor yang mempengaruhi jumlah penyewaan sepeda. Dengan menggunakan dataset day_df dan hour_df, dashboard ini menjawab dua pertanyaan utama:

Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda per hari?

Faktor apa yang paling berpengaruh terhadap jumlah penyewaan sepeda?

Fitur Utama

Visualisasi Data: Menampilkan dua grafik utama yang mendukung analisis kedua pertanyaan.

Fitur Interaktif: Pengguna dapat memilih dataset (harian atau per jam) serta menyaring data berdasarkan musim.

Statistik Ringkasan: Menyediakan ringkasan statistik dari dataset yang dipilih.

Download Data & Visualisasi: Pengguna dapat mengunduh dataset dan gambar hasil visualisasi.

Teknologi yang Digunakan

Python

Streamlit untuk dashboard interaktif

Matplotlib & Seaborn untuk visualisasi data

Pandas untuk manipulasi data

Cara Menjalankan

Pastikan telah menginstal dependensi yang diperlukan:

pip install streamlit pandas matplotlib seaborn

Jalankan aplikasi Streamlit:

streamlit run dashboard.py

Buka browser dan akses http://localhost:8501 untuk melihat dashboard.

Struktur File

.
├── dashboard.py  # Kode utama Streamlit
├── day_df.csv     # Dataset harian
├── hour_df.csv    # Dataset per jam
├── README.md      # Dokumentasi ini

Penjelasan Analisis

Pengaruh Cuaca: Visualisasi heatmap korelasi menunjukkan bahwa suhu dan kelembaban memiliki pengaruh signifikan terhadap jumlah penyewaan sepeda.

Faktor Paling Berpengaruh: Scatter plot menunjukkan hubungan antara temperatur dan jumlah penyewaan, dengan tren yang menunjukkan peningkatan seiring dengan kenaikan suhu.
