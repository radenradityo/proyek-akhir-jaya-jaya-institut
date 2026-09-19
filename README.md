# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan yang telah berdiri sejak tahun 2000 dan memiliki reputasi yang baik. Namun, institusi menghadapi permasalahan berupa tingginya jumlah mahasiswa yang mengalami dropout.

Kondisi tersebut dapat berdampak pada keberlangsungan studi mahasiswa serta menjadi tantangan bagi institusi dalam menjaga keberhasilan akademik. Oleh karena itu, diperlukan analisis data untuk memahami faktor-faktor yang berkaitan dengan status mahasiswa dan sebuah sistem yang dapat membantu melakukan deteksi dini terhadap mahasiswa yang berpotensi mengalami dropout.

Proyek ini menggunakan data performa mahasiswa untuk melakukan eksplorasi data, membangun business dashboard, serta mengembangkan model machine learning yang dapat digunakan sebagai prototype prediksi status mahasiswa berdasarkan informasi yang tersedia hingga akhir semester pertama.

### Permasalahan Bisnis

Permasalahan bisnis yang ingin diselesaikan dalam proyek ini adalah:

1. Tingginya jumlah mahasiswa yang mengalami dropout.
2. Belum adanya sistem deteksi dini yang dapat membantu mengidentifikasi mahasiswa yang berpotensi mengalami dropout.
3. Perlunya pemahaman mengenai faktor akademik, administratif, dan karakteristik mahasiswa yang berkaitan dengan status studi.
4. Perlunya dashboard untuk membantu institusi memantau kondisi dan performa mahasiswa.
5. Perlunya rekomendasi tindakan yang dapat dilakukan institusi berdasarkan hasil analisis data.

### Cakupan Proyek

Cakupan proyek meliputi:

1. Melakukan data understanding dan data cleaning pada dataset performa mahasiswa.
2. Melakukan exploratory data analysis (EDA) untuk memahami distribusi status mahasiswa dan hubungan berbagai fitur dengan status mahasiswa.
3. Menganalisis faktor akademik, administratif, dan karakteristik mahasiswa yang berkaitan dengan dropout.
4. Membuat business dashboard menggunakan Metabase untuk membantu monitoring performa mahasiswa.
5. Membangun model machine learning untuk memprediksi status mahasiswa.
6. Mengembangkan prototype machine learning menggunakan Streamlit.
7. Menyusun rekomendasi action items berdasarkan hasil analisis dan model.
8. Melakukan deployment prototype machine learning agar dapat digunakan sebagai sistem pendukung deteksi dini.

### Persiapan

**Sumber data:**

Sumber:
https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

**Tools yang digunakan:**

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit
- Metabase
- PostgreSQL / Supabase

**Setup environment:**

Proyek ini menggunakan **Python 3.13.15**.

Buat virtual environment:

```bash
python -m venv .venv
```

Aktifkan virtual environment pada Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Untuk menjalankan notebook:

```bash
jupyter notebook
```

## Business Dashboard

Business dashboard dibuat menggunakan Metabase dan terhubung dengan database PostgreSQL pada Supabase.

Dashboard digunakan untuk membantu institusi memantau kondisi mahasiswa dan melihat distribusi status studi berdasarkan beberapa faktor yang relevan.

Dashboard mencakup beberapa informasi utama, antara lain:

- Total mahasiswa: **4.424**
- Dropout: **1.421 mahasiswa**
- Graduate: **2.209 mahasiswa**
- Enrolled: **794 mahasiswa**
- Dropout rate: **32,12%**
- Distribusi status mahasiswa.
- Hubungan status pembayaran tuition fee dengan status mahasiswa.
- Hubungan debtor dengan status mahasiswa.
- Hubungan scholarship holder dengan status mahasiswa.
- Jumlah mata kuliah semester 1 yang berhasil diselesaikan.
- Kelompok nilai semester 1.
- Kelompok usia saat enrollment.
- Dropout rate berdasarkan course/program studi.
- Distribusi status berdasarkan gender.
- Distribusi status berdasarkan jumlah evaluasi semester 1.

Dashboard membantu memberikan gambaran kondisi mahasiswa sehingga institusi dapat melakukan monitoring dan menentukan area yang membutuhkan perhatian lebih lanjut.

### Akses Metabase

Dashboard dibuat dalam lingkungan lokal menggunakan Metabase. File konfigurasi database Metabase untuk kebutuhan submission disertakan dalam repository melalui file `metabase.db.mv.db`.

Dashboard dapat diakses melalui instance Metabase yang disertakan dalam file `metabase.db.mv.db`.

Kredensial login Metabase:

- **Email:** `bagoespp@gmail.com`
- **Password:** `Root123`

## Menjalankan Sistem Machine Learning

Model machine learning dibuat untuk membantu melakukan deteksi dini terhadap status mahasiswa.

Model utama yang digunakan adalah **Logistic Regression** dengan preprocessing menggunakan:

- One-Hot Encoding untuk fitur kategorikal.
- StandardScaler untuk fitur ordinal dan numerik.

Model menggunakan informasi yang tersedia hingga **akhir semester pertama**, sehingga fitur semester kedua tidak digunakan dalam model utama. Pendekatan ini dipilih agar prediksi dapat digunakan lebih awal untuk mendukung intervensi terhadap mahasiswa yang berpotensi mengalami dropout.

### Fitur yang digunakan

Beberapa kelompok fitur yang digunakan antara lain:

- Informasi pendaftaran.
- Informasi pendidikan sebelumnya.
- Informasi administratif.
- Karakteristik mahasiswa.
- Performa akademik semester pertama.
- Informasi kondisi ekonomi makro.

### Hasil Evaluasi Model

Model Logistic Regression menghasilkan:

| Metric | Score |
|---|---:|
| Accuracy | 74,92% |
| Weighted Precision | 73,27% |
| Weighted Recall | 74,92% |
| Weighted F1-Score | 73,62% |
| Macro F1-Score | 66,80% |

Classification report:

| Status | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| Dropout | 0,80 | 0,75 | 0,77 |
| Enrolled | 0,49 | 0,33 | 0,40 |
| Graduate | 0,78 | 0,90 | 0,83 |

Hasil analisis permutation importance menunjukkan bahwa beberapa fitur yang paling berkontribusi terhadap performa model adalah:

1. Jumlah mata kuliah semester 1 yang berhasil diselesaikan (`Curricular_units_1st_sem_approved`).
2. Status pembayaran tuition fee (`Tuition_fees_up_to_date`).
3. Jumlah mata kuliah semester 1 yang diambil (`Curricular_units_1st_sem_enrolled`).
4. Course.
5. Nilai semester 1 (`Curricular_units_1st_sem_grade`).

> Nilai feature importance digunakan untuk melihat kontribusi fitur terhadap prediksi model dan tidak menunjukkan hubungan sebab-akibat.

### Menjalankan Prototype

Pastikan virtual environment sudah aktif dan dependencies telah ter-install.

Jalankan Streamlit dengan:

```bash
streamlit run app.py
```



Prototype menerima informasi mahasiswa dan menghasilkan prediksi status:

- Dropout
- Enrolled
- Graduate

Prototype juga menampilkan probabilitas prediksi untuk masing-masing status.

**Akses prototype Streamlit:**  
`[ISI LINK STREAMLIT SETELAH DEPLOYMENT]`

## Conclusion

Berdasarkan hasil exploratory data analysis dan pemodelan machine learning, status mahasiswa memiliki keterkaitan dengan beberapa faktor akademik dan administratif.

Performa akademik pada semester pertama merupakan salah satu faktor yang paling penting dalam model, terutama jumlah mata kuliah yang berhasil diselesaikan. Status pembayaran tuition fee juga menunjukkan hubungan yang kuat dengan status mahasiswa. Selain itu, jumlah mata kuliah yang diambil, course, dan nilai semester pertama turut memberikan kontribusi terhadap prediksi model.

Model Logistic Regression yang dibangun menghasilkan accuracy sebesar **74,92%** dan macro F1-score sebesar **66,80%**. Model ini kemudian digunakan sebagai prototype untuk membantu melakukan deteksi dini terhadap status mahasiswa berdasarkan informasi yang tersedia hingga akhir semester pertama.

Dashboard Metabase melengkapi sistem dengan menyediakan monitoring dan visualisasi kondisi mahasiswa. Dengan kombinasi dashboard dan prototype machine learning, institusi dapat memperoleh informasi yang lebih terstruktur untuk mendukung proses monitoring dan intervensi mahasiswa.

### Rekomendasi Action Items

Beberapa action items yang dapat dilakukan Jaya Jaya Institut adalah:

- Melakukan intervensi akademik setelah semester pertama terhadap mahasiswa dengan jumlah mata kuliah yang berhasil diselesaikan rendah.
- Memberikan pendampingan akademik kepada mahasiswa yang menunjukkan performa atau nilai semester pertama yang rendah.
- Melakukan monitoring terhadap mahasiswa yang memiliki status pembayaran tuition fee belum up to date dan menghubungkannya dengan layanan administrasi atau pendampingan yang sesuai.
- Melakukan monitoring dropout berdasarkan course untuk mengidentifikasi program yang membutuhkan evaluasi atau dukungan lebih lanjut.
- Menggunakan dashboard secara berkala untuk memantau perubahan kondisi mahasiswa.
- Menggunakan prototype machine learning sebagai alat bantu deteksi dini, bukan sebagai satu-satunya dasar pengambilan keputusan.
- Melakukan evaluasi model secara berkala apabila tersedia data mahasiswa baru agar performa prediksi tetap relevan.
