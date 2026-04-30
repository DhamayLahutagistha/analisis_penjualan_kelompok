📊 Laporan Proyek Analisis Data Penjualan E-commerce
Tugas Kelompok Praktikum - Optimasi Strategi Pemasaran
Nama: Dhamay Lahutagistha Pramu Putri
Kelas: XI RPL 1
No Absen: 14

📋 Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis performa penjualan e-commerce pakaian wanita guna mengidentifikasi efisiensi produk, segmentasi pelanggan, dan pengaruh variabel harga terhadap total pendapatan menggunakan teknik analisis data tingkat lanjut.
🚀 Metodologi Analisis
Analisis ini mencakup empat tahapan krusial sesuai standar modul praktikum:
- Data Wrangling: Pembersihan data dari nilai missing, perbaikan tipe data tanggal, dan penanganan anomali harga.
- Identifikasi Underperformer: Menggunakan analisis sebaran (Scatter Plot) untuk menemukan produk "beban" stok.
- Analisis RFM (Recency, Frequency, Monetary): Segmentasi pelanggan berbasis perilaku belanja dengan sistem scoring 1-5.
- Analisis Prediktif: Implementasi Regresi Linear untuk memprediksi tren pendapatan berdasarkan variabel harga.
📊 Hasil Analisis & Jawaban Modul
1. Produk Underperformer (Halaman 4)
   Analisis: Berdasarkan grafik Scatter Plot antara Harga Satuan dan Kuantitas, kami menemukan titik-titik produk di kuadran kanan bawah.
   - Insight: Produk ini memiliki harga tinggi namun volume penjualan rendah, sehingga menghambat perputaran arus kas.
   - Rekomendasi: Disarankan strategi promo bundling atau diskon musiman untuk mempercepat likuidasi stok pada kategori ini.
2. Segmentasi Pelanggan (RFM Scoring) (Halaman 5)
   Sistem penilaian dilakukan dengan membagi pelanggan ke dalam 5 tingkatan (quintiles):
   - Champions (Skor 555): Pelanggan paling berharga. Strategi: Berikan akses eksklusif produk baru dan voucher loyalitas.
   - At Risk (Skor 111): Pelanggan yang sudah lama tidak kembali. Strategi: Kirimkan kampanye email re-engagement atau diskon khusus "Kami Merindukanmu".
3. Analisis Prediktif: Regresi Linear (Halaman 6)
   Melalui model Machine Learning (Scikit-Learn), diperoleh parameter sebagai berikut:
   - Model Equation: $y = \beta_0 + \beta_1x$
   - R2 Score: (Masukkan angka R2 dari terminal kamu, misal: 0.82)
   - Interpretasi: Nilai R2 menunjukkan seberapa kuat harga dapat menjelaskan variasi total penjualan. Koefisien positif menunjukkan bahwa strategi harga saat ini masih selaras dengan peningkatan total nilai transaksi.
🛠️ Teknologi & Library
- Bahasa: Python 3.13
- Library Utama:
  - Pandas: Manipulasi dan pembersihan data.
  - Matplotlib & Seaborn: Visualisasi data (Scatter, Bar, Line).
  - Scikit-Learn: Pemodelan Regresi Linear.
📁 Struktur Repositori
- women_clothing_ecommerce_sales.csv: Dataset utama transaksi.
- analisis_individu.py: Skrip untuk eksplorasi tren bulanan dan heatmap.
- analisis_kelompok.py: Skrip analisis komprehensif (RFM, Underperformer, Regresi).
- README.md: Dokumentasi proyek (File ini).

OUTPUT :

=== MEMULAI TUGAS KELOMPOK ===

[1] Menghitung Skor RFM...
Tabel Hasil Segmentasi (5 baris pertama):
          Recency  Frequency  Monetary RFM_Segment
order_id                                          
1              32          3       754         355
2              32          2       473         322
3              32          2       542         323
4              32          2       542         323
5              31          2       542         323
d:\kka\Analisis Penjualan\analisis_kelompok.py:66: FutureWarning: 

Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.

  sns.countplot(x='M_Score', data=rfm, palette='Greens')

[2] Menjalankan Analisis Regresi...
Koefisien (Beta): 0.99
Akurasi Model (R2 Score): 0.9612

=== TUGAS KELOMPOK SELESAI ===
