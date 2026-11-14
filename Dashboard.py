
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ============================================
# 1. KONFIGURASI DASHBOARD
# ============================================

st.set_page_config(
    page_title="Bike Sharing Analysis Dashboard",
    page_icon="🚲",
    layout="wide"
)

sns.set_theme(style="whitegrid")

# ============================================
# 2. MEMUAT DATASET
# ============================================

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "main_data.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("File main_data.csv tidak ditemukan. Pastikan file berada di folder dashboard.")
    st.stop()

# ============================================
# 3. JUDUL DASHBOARD
# ============================================

st.title("🚲 Bike Sharing Analysis Dashboard")

st.markdown("""
Dashboard ini menyajikan hasil analisis pola penyewaan sepeda
berdasarkan waktu, kondisi cuaca, dan karakteristik pengguna
selama periode Januari 2011 hingga Desember 2012.
""")

st.divider()

# ============================================
# 4. FILTER DATA
# ============================================

st.sidebar.header("Filter Data")

min_date = df['dteday'].min().date()
max_date = df['dteday'].max().date()

selected_date = st.sidebar.date_input(
    "Pilih Rentang Tanggal",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if isinstance(selected_date, (tuple, list)) and len(selected_date) == 2:
    start_date, end_date = selected_date
else:
    start_date, end_date = min_date, max_date

filtered_df = df[
    (df['dteday'].dt.date >= start_date) &
    (df['dteday'].dt.date <= end_date)
].copy()

if filtered_df.empty:
    st.warning("Tidak ada data pada rentang tanggal yang dipilih.")
    st.stop()

# ============================================
# 5. METRIK UTAMA
# ============================================

st.subheader("Ringkasan Penyewaan Sepeda")

total_rentals = filtered_df['cnt'].sum()
average_rentals = filtered_df['cnt'].mean()
total_casual = filtered_df['casual'].sum()
total_registered = filtered_df['registered'].sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Penyewaan",
    f"{total_rentals:,.0f}"
)

col2.metric(
    "Rata-rata Penyewaan",
    f"{average_rentals:,.0f}"
)

col3.metric(
    "Pengguna Casual",
    f"{total_casual:,.0f}"
)

col4.metric(
    "Pengguna Registered",
    f"{total_registered:,.0f}"
)

st.divider()

# ============================================
# 6. ANALISIS POLA PENYEWAAN BERDASARKAN JAM
# ============================================

st.subheader("1. Pola Penyewaan Sepeda Berdasarkan Jam")

hourly_data = (
    filtered_df.groupby('hr')['cnt']
    .mean()
    .reset_index()
    .sort_values('hr')
)

fig1, ax1 = plt.subplots(figsize=(12, 5))

sns.lineplot(
    data=hourly_data,
    x='hr',
    y='cnt',
    marker='o',
    ax=ax1
)

ax1.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Jam")
ax1.set_xlabel("Jam")
ax1.set_ylabel("Rata-rata Jumlah Penyewaan")
ax1.set_xticks(range(24))

st.pyplot(fig1)
plt.close(fig1)

peak_hour = hourly_data.loc[hourly_data['cnt'].idxmax()]
lowest_hour = hourly_data.loc[hourly_data['cnt'].idxmin()]

st.markdown(f"""
**Insight:**
- Jam dengan rata-rata penyewaan tertinggi adalah pukul
  **{int(peak_hour['hr']):02d}.00** dengan rata-rata
  **{peak_hour['cnt']:.2f} sepeda**.
- Jam dengan rata-rata penyewaan terendah adalah pukul
  **{int(lowest_hour['hr']):02d}.00** dengan rata-rata
  **{lowest_hour['cnt']:.2f} sepeda**.
""")

st.divider()

# ============================================
# 7. ANALISIS BERDASARKAN KONDISI CUACA
# ============================================

st.subheader("2. Pola Penyewaan Berdasarkan Kondisi Cuaca")

weather_data = (
    filtered_df.groupby('weather_label')['cnt']
    .mean()
    .reset_index()
    .sort_values('cnt', ascending=False)
)

fig2, ax2 = plt.subplots(figsize=(12, 5))

sns.barplot(
    data=weather_data,
    x='weather_label',
    y='cnt',
    ax=ax2
)

ax2.set_title("Rata-rata Penyewaan Berdasarkan Kondisi Cuaca")
ax2.set_xlabel("Kondisi Cuaca")
ax2.set_ylabel("Rata-rata Jumlah Penyewaan")
ax2.tick_params(axis='x', rotation=15)

st.pyplot(fig2)
plt.close(fig2)

if not weather_data.empty:
    best_weather = weather_data.iloc[0]
    worst_weather = weather_data.iloc[-1]

    st.markdown(f"""
    **Insight:**
    - Rata-rata penyewaan tertinggi terjadi pada kondisi
      **{best_weather['weather_label']}** sebesar
      **{best_weather['cnt']:.2f} sepeda**.
    - Rata-rata penyewaan terendah terjadi pada kondisi
      **{worst_weather['weather_label']}** sebesar
      **{worst_weather['cnt']:.2f} sepeda**.
    """)

st.divider()


# ============================================
# 8. ANALISIS KARAKTERISTIK PENGGUNA
# ============================================

st.subheader("3. Perbandingan Jenis Pengguna")

user_data = pd.DataFrame({
    'Jenis Pengguna': ['Casual', 'Registered'],
    'Jumlah Penyewaan': [
        filtered_df['casual'].sum(),
        filtered_df['registered'].sum()
    ]
})

fig3, ax3 = plt.subplots(figsize=(8, 5))

sns.barplot(
    data=user_data,
    x='Jenis Pengguna',
    y='Jumlah Penyewaan',
    ax=ax3
)

ax3.set_title("Total Penyewaan Berdasarkan Jenis Pengguna")
ax3.set_xlabel("Jenis Pengguna")
ax3.set_ylabel("Total Penyewaan")

st.pyplot(fig3)
plt.close(fig3)

# Menghitung jumlah dan persentase pengguna
total_casual = user_data.loc[
    user_data['Jenis Pengguna'] == 'Casual',
    'Jumlah Penyewaan'
].iloc[0]

total_registered = user_data.loc[
    user_data['Jenis Pengguna'] == 'Registered',
    'Jumlah Penyewaan'
].iloc[0]

total_user = total_casual + total_registered

casual_percentage = (total_casual / total_user) * 100
registered_percentage = (total_registered / total_user) * 100

# Menampilkan insight otomatis
st.markdown("**Insight:**")

st.write(
    f"- Total penyewaan oleh pengguna Casual mencapai "
    f"**{total_casual:,.0f} penyewaan** "
    f"({casual_percentage:.2f}%)."
)

st.write(
    f"- Total penyewaan oleh pengguna Registered mencapai "
    f"**{total_registered:,.0f} penyewaan** "
    f"({registered_percentage:.2f}%)."
)

if total_registered > total_casual:
    st.write(
        "- Pengguna Registered mendominasi aktivitas penyewaan "
        "sepeda dibandingkan pengguna Casual."
    )
else:
    st.write(
        "- Pengguna Casual mendominasi aktivitas penyewaan "
        "sepeda dibandingkan pengguna Registered."
    )

st.divider()



# ============================================
# 9. ANALISIS BERDASARKAN KATEGORI WAKTU
# ============================================

st.subheader("4. Penyewaan Berdasarkan Kategori Waktu")

time_data = (
    filtered_df.groupby('time_category')['cnt']
    .mean()
    .reset_index()
    .sort_values('cnt', ascending=False)
)

fig4, ax4 = plt.subplots(figsize=(10, 5))

sns.barplot(
    data=time_data,
    x='time_category',
    y='cnt',
    ax=ax4
)

ax4.set_title("Rata-rata Penyewaan Berdasarkan Kategori Waktu")
ax4.set_xlabel("Kategori Waktu")
ax4.set_ylabel("Rata-rata Jumlah Penyewaan")

st.pyplot(fig4)
plt.close(fig4)

# Mengidentifikasi kategori tertinggi dan terendah
highest_time = time_data.loc[time_data['cnt'].idxmax()]
lowest_time = time_data.loc[time_data['cnt'].idxmin()]

difference = highest_time['cnt'] - lowest_time['cnt']

# Menampilkan insight otomatis
st.markdown("**Insight:**")

st.write(
    f"- Kategori waktu dengan rata-rata penyewaan tertinggi "
    f"adalah **{highest_time['time_category']}**, "
    f"yaitu sebesar **{highest_time['cnt']:.2f} penyewaan**."
)

st.write(
    f"- Kategori waktu dengan rata-rata penyewaan terendah "
    f"adalah **{lowest_time['time_category']}**, "
    f"yaitu sebesar **{lowest_time['cnt']:.2f} penyewaan**."
)

st.write(
    f"- Selisih rata-rata penyewaan antara kedua kategori "
    f"tersebut adalah **{difference:.2f} penyewaan**."
)

st.divider()

# ============================================
# 10. TABEL DATA
# ============================================

st.subheader("5. Data Penyewaan Sepeda")

st.dataframe(
    filtered_df,
    use_container_width=True
)


# ============================================
# FITUR DOWNLOAD DATA
# ============================================

st.markdown("### Download Data Hasil Filter")

csv_data = filtered_df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="📥 Download Data CSV",
    data=csv_data,
    file_name="bike_sharing_filtered.csv",
    mime="text/csv"
)

st.caption(
    "Unduh data penyewaan sepeda berdasarkan rentang tanggal "
    "yang telah dipilih."
)

st.caption(
    "Sumber: Bike Sharing Dataset, periode Januari 2011–Desember 2012."
)