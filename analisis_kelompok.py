import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Load Dataset
file_path = 'Analisis Penjualan/women_clothing_ecommerce_sales.csv'
df = pd.read_csv(file_path)

# --- DETEKSI KOLOM OTOMATIS ---
cols = df.columns.tolist()
date_col = next((c for c in cols if 'date' in c.lower()), None)
price_col = next((c for c in cols if 'price' in c.lower() or 'unit' in c.lower()), None)
qty_col = next((c for c in cols if 'quant' in c.lower() or 'qty' in c.lower()), None)
cat_col = next((c for c in cols if 'cat' in c.lower()), None)
user_col = next((c for c in cols if 'id' in c.lower() or 'customer' in c.lower()), None)

# 2. Data Cleaning
df = df.dropna(subset=[date_col, price_col, qty_col])
df[date_col] = pd.to_datetime(df[date_col])
df['Total_Sales'] = df[qty_col] * df[price_col]

print("=== MEMULAI TUGAS KELOMPOK ===")

# --- [TUGAS 1] SCATTER PLOT: IDENTIFIKASI UNDERPERFORMER ---
# Mencari produk harga tinggi tapi penjualan rendah
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x=price_col, y=qty_col, hue=cat_col, alpha=0.7)
plt.axvline(df[price_col].mean(), color='red', linestyle='--', label='Rerata Harga')
plt.axhline(df[qty_col].mean(), color='blue', linestyle='--', label='Rerata Kuantitas')
plt.title('Identifikasi Produk Underperformer (Harga vs Kuantitas)')
plt.xlabel('Harga Satuan')
plt.ylabel('Kuantitas Terjual')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# --- [TUGAS 2] SEGMENTASI RFM DENGAN SCORING 1-5 ---
print("\n[1] Menghitung Skor RFM...")
snapshot_date = df[date_col].max() + dt.timedelta(days=1)

# Agregasi data pelanggan
rfm = df.groupby(user_col if user_col else df.index).agg({
    date_col: lambda x: (snapshot_date - x.max()).days, # Recency
    qty_col: 'sum',                                    # Frequency (sebagai jumlah barang)
    'Total_Sales': 'sum'                               # Monetary
})
rfm.columns = ['Recency', 'Frequency', 'Monetary']

# Scoring 1-5 (5 adalah yang terbaik)
# Menggunakan rank(method='first') agar tidak error jika banyak data bernilai sama
rfm['R_Score'] = pd.qcut(rfm['Recency'].rank(method='first'), 5, labels=[5, 4, 3, 2, 1])
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])
rfm['M_Score'] = pd.qcut(rfm['Monetary'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])

# Gabungkan skor untuk melihat segmen
rfm['RFM_Segment'] = rfm.R_Score.astype(str) + rfm.F_Score.astype(str) + rfm.M_Score.astype(str)

print("Tabel Hasil Segmentasi (5 baris pertama):")
print(rfm[['Recency', 'Frequency', 'Monetary', 'RFM_Segment']].head())

# Visualisasi Distribusi Skor Monetary
plt.figure(figsize=(8, 5))
sns.countplot(x='M_Score', data=rfm, palette='Greens')
plt.title('Distribusi Skor Monetary Pelanggan (1-5)')
plt.show()

# --- [TUGAS 3] ANALISIS PREDIKTIF: REGRESI LINEAR ---
print("\n[2] Menjalankan Analisis Regresi...")
# Variabel Independen (Harga) dan Dependen (Total Sales)
X = df[[price_col]]
y = df['Total_Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

print(f"Koefisien (Beta): {model.coef_[0]:.2f}")
print(f"Akurasi Model (R2 Score): {model.score(X_test, y_test):.4f}")

# Visualisasi Garis Regresi
plt.figure(figsize=(8, 5))
plt.scatter(X_test, y_test, color='gray', alpha=0.5, label='Data Asli')
plt.plot(X_test, model.predict(X_test), color='red', linewidth=2, label='Garis Prediksi')
plt.title('Analisis Regresi: Harga terhadap Total Penjualan')
plt.xlabel('Harga Satuan')
plt.ylabel('Total Penjualan')
plt.legend()
plt.show()

print("\n=== TUGAS KELOMPOK SELESAI ===")