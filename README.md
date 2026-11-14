# Bike Sharing Analysis Dashboard 🚲

## 1. Project Overview

Proyek ini merupakan analisis data penyewaan sepeda menggunakan Bike Sharing Dataset yang mencakup periode Januari 2011 hingga Desember 2012.

Proyek ini bertujuan untuk memahami pola penyewaan sepeda berdasarkan waktu, kondisi cuaca, dan karakteristik pengguna. Hasil analisis disajikan dalam bentuk visualisasi interaktif menggunakan Streamlit sehingga informasi dapat dipahami dengan lebih mudah dan dapat digunakan sebagai pendukung pengambilan keputusan.

## 2. Business Questions

Analisis ini berfokus pada dua pertanyaan bisnis utama:

1. Bagaimana pola rata-rata jumlah penyewaan sepeda berdasarkan jam dalam sehari selama periode Januari 2011 hingga Desember 2012, dan pada jam berapa permintaan penyewaan sepeda mencapai puncaknya?

2. Bagaimana perbedaan rata-rata jumlah penyewaan sepeda berdasarkan kondisi cuaca selama periode Januari 2011 hingga Desember 2012, dan kondisi cuaca mana yang menunjukkan tingkat penyewaan sepeda tertinggi?

## 3. Dataset

Dataset yang digunakan adalah Bike Sharing Dataset yang terdiri dari dua file utama:

- `day.csv`: Dataset penyewaan sepeda berdasarkan hari, dengan 731 baris dan 16 kolom.
- `hour.csv`: Dataset penyewaan sepeda berdasarkan jam, dengan 17.379 baris dan 17 kolom.

Dataset mencakup periode Januari 2011 hingga Desember 2012.

Dalam proyek ini, `hour.csv` digunakan sebagai dataset utama untuk menganalisis pola penyewaan berdasarkan jam, sedangkan `day.csv` digunakan sebagai dataset pendukung untuk analisis harian.

## 4. Data Analysis Process

Tahapan analisis yang dilakukan dalam proyek ini meliputi:

### A. Gathering Data

Mengumpulkan dan memuat dataset Bike Sharing yang terdiri dari data harian (`day.csv`) dan data per jam (`hour.csv`).

### B. Assessing Data

Melakukan pemeriksaan kualitas data yang mencakup:

- Memeriksa tipe data setiap kolom.
- Memeriksa missing values.
- Memeriksa data duplikat.
- Memeriksa konsistensi jumlah penyewaan.
- Mengidentifikasi nilai outlier menggunakan metode Interquartile Range (IQR).

### C. Data Cleaning

Melakukan perbaikan dan validasi data, yaitu:

- Mengubah tipe data kolom `dteday` menjadi datetime.
- Memeriksa kembali missing values dan duplikasi.
- Memvalidasi kesesuaian jumlah penyewaan antara pengguna Casual, Registered, dan total penyewaan.
- Mempertahankan nilai outlier yang masih valid dan tidak menunjukkan kesalahan pencatatan.

### D. Exploratory Data Analysis (EDA)

Melakukan eksplorasi data untuk memahami karakteristik penyewaan sepeda melalui:

- Statistik deskriptif jumlah penyewaan.
- Analisis pola penyewaan berdasarkan jam.
- Analisis penyewaan berdasarkan kondisi cuaca.
- Perbandingan pengguna Casual dan Registered.
- Analisis penyewaan berdasarkan kategori waktu.

### E. Data Visualization

Menyajikan hasil eksplorasi data dalam bentuk grafik agar pola dan perbedaan jumlah penyewaan lebih mudah dipahami.

### F. Advanced Analysis

Melakukan analisis lanjutan melalui pengelompokan kategori waktu dan pembagian rata-rata penyewaan berdasarkan kategori rendah, sedang, dan tinggi menggunakan metode binning.

### G. Dashboard Development

Mengembangkan dashboard interaktif menggunakan Streamlit untuk menampilkan hasil analisis, visualisasi, ringkasan data, filter tanggal, dan fitur pengunduhan data.

## 5. Analysis Results

### A. Pola Penyewaan Berdasarkan Jam

Hasil analisis menunjukkan bahwa rata-rata penyewaan sepeda tertinggi terjadi pada pukul 17.00 dengan rata-rata sebesar 461,45 penyewaan.

Sementara itu, rata-rata penyewaan terendah terjadi pada pukul 04.00 dengan rata-rata sebesar 6,35 penyewaan.

Pola tersebut menunjukkan bahwa aktivitas penyewaan meningkat pada pagi hari dan mencapai puncak pada sore hari, khususnya sekitar pukul 16.00 hingga 18.00.

### B. Pola Penyewaan Berdasarkan Kondisi Cuaca

Berdasarkan hasil analisis, kondisi Cerah / Sedikit Berawan menunjukkan rata-rata penyewaan tertinggi sebesar 204,87 penyewaan.

Sebaliknya, kondisi Cuaca Buruk menunjukkan rata-rata penyewaan terendah sebesar 74,33 penyewaan.

Hasil ini menunjukkan adanya perbedaan tingkat penyewaan sepeda berdasarkan kondisi cuaca.

### C. Karakteristik Pengguna

Analisis karakteristik pengguna dilakukan dengan membandingkan jumlah penyewaan dari dua kelompok pengguna, yaitu Casual dan Registered.

Berdasarkan hasil dashboard, total penyewaan pengguna Casual mencapai 620.017, sedangkan pengguna Registered mencapai 2.672.662.

Hal ini menunjukkan bahwa pengguna Registered memberikan kontribusi lebih besar terhadap total aktivitas penyewaan sepeda.

### D. Analisis Kategori Waktu

Analisis kategori waktu dilakukan dengan mengelompokkan aktivitas penyewaan ke dalam lima kategori, yaitu:

- Dini Hari
- Pagi
- Siang
- Sore
- Malam

Pengelompokan ini digunakan untuk mengetahui perbedaan rata-rata penyewaan sepeda pada setiap periode waktu.

### E. Advanced Analysis dengan Binning

Analisis lanjutan dilakukan dengan membagi rata-rata penyewaan berdasarkan jam ke dalam tiga kategori:

- Low: rata-rata 39,00 penyewaan.
- Medium: rata-rata 197,98 penyewaan.
- High: rata-rata 328,46 penyewaan.

Setiap kategori terdiri dari delapan observasi jam. Hasil ini memperlihatkan adanya perbedaan tingkat permintaan penyewaan sepeda sepanjang hari.

## 6. Conclusion and Recommendations

### Conclusion

Berdasarkan hasil analisis, dapat disimpulkan bahwa pola penyewaan sepeda memiliki perbedaan berdasarkan waktu dan kondisi cuaca.

Penyewaan tertinggi terjadi pada pukul 17.00, sedangkan penyewaan terendah terjadi pada pukul 04.00. Selain itu, kondisi Cerah / Sedikit Berawan menunjukkan rata-rata penyewaan lebih tinggi dibandingkan kondisi Cuaca Buruk.

Dari karakteristik pengguna, kelompok Registered memiliki jumlah penyewaan yang lebih besar dibandingkan Casual.

### Recommendations

Berdasarkan hasil analisis, beberapa rekomendasi yang dapat diberikan adalah:

1. Meningkatkan ketersediaan sepeda pada jam-jam dengan permintaan tinggi, terutama sore hari.
2. Mengatur distribusi sepeda berdasarkan pola permintaan pada waktu tertentu.
3. Mempertimbangkan kondisi cuaca dalam perencanaan operasional penyewaan sepeda.
4. Mengembangkan strategi untuk mempertahankan pengguna Registered serta meningkatkan ketertarikan pengguna Casual.
5. Melakukan pemantauan pola penyewaan secara berkala untuk mendukung pengambilan keputusan operasional.

## 7. Dashboard Features

Dashboard dikembangkan menggunakan Streamlit dan menyediakan beberapa fitur utama:

- Filter data berdasarkan rentang tanggal.
- Ringkasan total dan rata-rata penyewaan sepeda.
- Visualisasi penyewaan berdasarkan jam.
- Visualisasi penyewaan berdasarkan kondisi cuaca.
- Perbandingan jumlah penyewaan pengguna Casual dan Registered.
- Visualisasi penyewaan berdasarkan kategori waktu.
- Insight otomatis berdasarkan hasil visualisasi.
- Tabel data penyewaan.
- Fitur download data hasil filter dalam format CSV.

## 8. Setup Environment - Anaconda

Jika menggunakan Anaconda, jalankan perintah berikut pada Anaconda Prompt atau terminal:

```bash
conda create --name bike-sharing python=3.11
conda activate bike-sharing
pip install -r requirements.txt
```

## 9. Setup Environment - Shell/Terminal

Jika menggunakan Shell atau Terminal pada Visual Studio Code, ikuti langkah berikut.

### A. Membuat dan Masuk ke Folder Proyek

```bash
mkdir Submission
cd Submission
```

### B. Membuat Virtual Environment

```bash
python -m venv .venv
```

### C. Mengaktifkan Virtual Environment

Untuk Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Jika terjadi kendala Execution Policy, jalankan:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Kemudian aktifkan kembali virtual environment.

### D. Menginstal Dependencies

```bash
pip install -r requirements.txt
```

## 10. Run Streamlit App

Setelah seluruh dependencies berhasil diinstal dan virtual environment aktif, jalankan aplikasi dengan perintah:

```bash
python -m streamlit run Dashboard/Dashboard.py
```

Setelah berhasil dijalankan, Streamlit akan menampilkan alamat lokal pada terminal.

Buka alamat berikut melalui browser:

```text
http://localhost:8501
```

## 11. Technologies Used

Teknologi dan library yang digunakan dalam proyek ini meliputi:

- Python: Bahasa pemrograman utama.
- Pandas: Pengolahan dan analisis data.
- NumPy: Operasi numerik.
- Matplotlib: Visualisasi data.
- Seaborn: Visualisasi statistik.
- Plotly: Library visualisasi interaktif yang disiapkan dalam environment.
- Streamlit: Pengembangan dashboard interaktif.
- Google Colab: Lingkungan pengerjaan analisis data.
- Visual Studio Code: Pengembangan dan pengelolaan proyek.

## 12. Project Structure

Struktur folder proyek yang digunakan adalah sebagai berikut:

```text
Submission/
│
├── Dashboard/
│   ├── Dashboard.py
│   └── main_data.csv
│
├── data/
│   ├── day.csv
│   └── hour.csv
│
├── README.md
└── requirements.txt
```