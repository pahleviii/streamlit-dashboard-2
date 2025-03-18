# Dashboard Analisis Data E-commerce

## Deskripsi
Dashboard ini dibuat menggunakan **Streamlit** untuk menganalisis data e-commerce dari dataset Olist. Dashboard ini memungkinkan pengguna untuk menjelajahi data pelanggan, pesanan, produk, dan penjual dengan berbagai opsi visualisasi interaktif.

## Fitur
- **Filter Data**: Memilih kota pelanggan dan negara bagian penjual dari sidebar.
- **Visualisasi Data**: Beberapa pilihan visualisasi yang dapat dipilih pengguna:
  - **Top 10 Kota dengan Jumlah Pesanan Terbanyak**
  - **Distribusi Penjual Berdasarkan Negara Bagian (Top 10)**
  - **Distribusi Produk Berdasarkan Kategori (Top 10)**
  - **Distribusi Waktu Pemesanan**
- **Interaksi Dinamis**: Visualisasi dan tabel data berubah berdasarkan filter yang dipilih.

## Instalasi dan Menjalankan Dashboard
### 1. Instalasi Dependensi
Pastikan Anda memiliki Python dan pip terinstal. Kemudian, instal dependensi berikut:

```sh
pip install streamlit pandas matplotlib seaborn
```

### 2. Menjalankan Dashboard
Jalankan perintah berikut di terminal atau command prompt:

```sh
streamlit run nama_file.py
```

Gantilah `nama_file.py` dengan nama file yang berisi kode Streamlit Anda.

## Struktur Data
Dataset yang digunakan dalam dashboard ini terdiri dari beberapa file CSV:
- **olist_customers_dataset.csv**: Informasi pelanggan
- **olist_orders_dataset.csv**: Informasi pesanan
- **olist_sellers_dataset.csv**: Informasi penjual
- **olist_products_dataset.csv**: Informasi produk

## Penjelasan Kode
1. **Memuat Dataset**
   - Menggunakan `@st.cache_data` agar proses pemuatan lebih cepat.
2. **Sidebar Interaktif**
   - Memungkinkan pengguna memilih kota pelanggan dan negara bagian penjual.
3. **Menampilkan Data**
   - Menampilkan tabel data pelanggan dan penjual berdasarkan filter.
4. **Visualisasi Data**
   - Menggunakan **matplotlib** dan **seaborn** untuk membuat grafik interaktif berdasarkan pilihan pengguna.
