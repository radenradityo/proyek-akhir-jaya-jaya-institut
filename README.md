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

Dashboard dibuat dalam lingkungan lokal menggunakan Metabase **Metabase v0.46.4**. File konfigurasi database Metabase untuk kebutuhan submission disertakan dalam repository melalui file `metabase.db.mv.db`.

Dashboard dapat dipulihkan menggunakan file application database
`metabase.db.mv.db` yang disertakan dalam repository.

- Jalankan container Metabase
```bash
docker run -d --name metabase -p 3000:3000 metabase/metabase:v0.46.4
```

Perintah tersebut membuat container Metabase dengan nama metabase dan membuka port 3000.

- Tunggu hingga Metabase selesai melakukan proses startup  untuk melihat proses startup, jalankan:
```bash
docker logs -f metabase
```
Tunggu sampai proses startup selesai.

Tekan Ctrl + C untuk keluar dari tampilan log tanpa menghentikan container.

- Hentikan container sementara

Sebelum mengganti application database dengan file backup, hentikan container:
```bash
docker stop metabase
```

- Copy file `metabase.db.mv.db` ke dalam container

File `metabase.db.mv.db` yang disertakan dalam repository digunakan sebagai application database Metabase.

Jalankan perintah berikut dari folder tempat file tersebut berada:
```bash
docker cp metabase.db.mv.db metabase:/metabase.db/metabase.db.mv.db
```
Lokasi database tersebut sesuai dengan lokasi default H2 application database pada container Metabase.

- Jalankan kembali container
docker start metabase

Kemudian pantau proses startup:
```bash
docker logs -f metabase
```
Tunggu sampai Metabase selesai melakukan startup.

- Buka dashboard

Setelah container berhasil berjalan, buka browser dan akses:

http://localhost:3000

Dashboard Metabase kemudian dapat digunakan untuk melihat hasil monitoring Student Performance.

Kredensial login Metabase:

- **Email:** ``
- **Password:** ``

## Menjalankan Sistem Machine Learning

Model machine learning dibuat untuk membantu melakukan deteksi dini terhadap status mahasiswa.

Model utama yang digunakan adalah **Logistic Regression** dengan preprocessing menggunakan:

- One-Hot Encoding untuk fitur kategorikal.
- StandardScaler untuk fitur ordinal dan numerik.

Model menggunakan informasi yang tersedia hingga **akhir semester pertama**, sehingga fitur semester kedua tidak digunakan dalam model utama. Pendekatan ini dipilih agar prediksi dapat digunakan lebih awal untuk mendukung intervensi terhadap mahasiswa yang berpotensi mengalami dropout.

Pada proses modeling, mahasiswa dengan status **Enrolled** tidak digunakan sebagai target training karena status tersebut belum merupakan hasil akhir studi. Data yang digunakan untuk training hanya terdiri dari mahasiswa dengan status **Graduate** dan **Dropout**.

Target yang digunakan dalam model:

- `Graduate` = 0
- `Dropout` = 1

Sebanyak **3.630 data** digunakan untuk modeling, yang terdiri dari:

- 2.209 mahasiswa Graduate
- 1.421 mahasiswa Dropout

Sementara itu, sebanyak **794 mahasiswa Enrolled** dipisahkan untuk kemungkinan digunakan dalam prediksi status akhir di masa mendatang.

### Fitur yang digunakan

Beberapa kelompok fitur yang digunakan antara lain:

- Informasi pendaftaran.
- Informasi pendidikan sebelumnya.
- Informasi administratif.
- Karakteristik mahasiswa.
- Performa akademik semester pertama.
- Informasi kondisi ekonomi makro.

### Model Pembanding

Selain Logistic Regression, **Random Forest** juga digunakan sebagai model pembanding.

Hasil evaluasi kedua model:

| Model | Accuracy | Precision Dropout | Recall Dropout | F1-Score Dropout |
|---|---:|---:|---:|---:|
| Logistic Regression | 90,08% | 86,81% | 88,03% | 87,41% |
| Random Forest | 90,22% | 89,30% | 85,21% | 87,21% |

### Hasil Evaluasi Model

Model Logistic Regression menghasilkan:

| Metric | Score |
|---|---:|
| Accuracy | 90,08% |
| Precision Dropout | 86,81% |
| Recall Dropout | 88,03% |
| F1-Score Dropout | 87,41% |

Classification report:

| Status | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| Graduate | 0,92 | 0,91 | 0,92 |
| Dropout | 0,87 | 0,88 | 0,87 |

Confusion matrix Logistic Regression:

| Actual \ Predicted | Graduate | Dropout |
| --- | ---: | ---: |
| Graduate |  404 | 38 |
| Dropout | 34 | 250 |


Hasil evaluasi menunjukkan bahwa model berhasil mengidentifikasi **250 dari 284 mahasiswa Dropout** pada data testing.

Logistic Regression digunakan sebagai model pada prototype Streamlit karena memiliki **Recall Dropout sebesar 88,03%**, lebih tinggi dibandingkan Random Forest sebesar **85,21%**. Recall menjadi salah satu metrik yang diperhatikan karena sistem ditujukan sebagai early warning untuk membantu mengidentifikasi mahasiswa yang berpotensi mengalami dropout.

### Interpretasi Fitur

Hasil interpretasi model menunjukkan bahwa beberapa fitur yang memiliki kontribusi penting terhadap prediksi antara lain:

| No. | Fitur | Keterangan |
|---:|---|---|
| 1 | `Curricular_units_1st_sem_approved` | Jumlah mata kuliah Semester 1 yang berhasil diselesaikan |
| 2 | `Curricular_units_1st_sem_grade` | Nilai Semester 1 |
| 3 | `Curricular_units_1st_sem_enrolled` | Jumlah mata kuliah Semester 1 yang diambil |
| 4 | `Tuition_fees_up_to_date` | Status pembayaran tuition fee |
| 5 | `Curricular_units_1st_sem_evaluations` | Jumlah evaluasi Semester 1 |
| 6 | `Age_at_enrollment` | Usia mahasiswa saat pendaftaran |
| 7 | `Admission_grade` | Nilai penerimaan mahasiswa |

Pada Logistic Regression, `Curricular_units_1st_sem_approved` memiliki koefisien dengan nilai absolut terbesar.

Sementara pada Random Forest, `Curricular_units_1st_sem_approved` dan `Curricular_units_1st_sem_grade` merupakan fitur dengan feature importance tertinggi.

> Nilai koefisien dan feature importance digunakan untuk melihat kontribusi fitur terhadap prediksi model dan tidak menunjukkan hubungan sebab-akibat.

### Menjalankan Prototype

Pastikan virtual environment sudah aktif dan dependencies telah ter-install.

Jalankan Streamlit dengan:

```bash
streamlit run app.py
```



Prototype menerima informasi mahasiswa dan menghasilkan prediksi status:

- Dropout
- Graduate

Prototype juga menampilkan probabilitas prediksi untuk masing-masing status.

**Akses prototype Streamlit:**  
`https://proyek-akhir-jaya-jaya-institut-aeljf9majxps4lecsgbkdm.streamlit.app/`

## Conclusion

Berdasarkan hasil exploratory data analysis dan pemodelan machine learning, status mahasiswa memiliki keterkaitan dengan beberapa faktor akademik, administratif, finansial, demografi, dan program studi.

Performa akademik pada semester pertama merupakan salah satu faktor yang paling penting dalam model, terutama jumlah mata kuliah yang berhasil diselesaikan dan nilai semester pertama. Status pembayaran tuition fee juga menunjukkan pola yang berbeda terhadap status mahasiswa. Selain itu, jumlah mata kuliah yang diambil, jumlah evaluasi semester pertama, usia saat pendaftaran, dan course turut memberikan kontribusi terhadap prediksi model.

Berdasarkan hasil exploratory data analysis, secara umum mahasiswa yang cenderung berada pada kelompok **Dropout** memiliki beberapa karakteristik sebagai berikut:

- Memiliki jumlah mata kuliah Semester 1 yang berhasil diselesaikan (`Curricular_units_1st_sem_approved`) relatif lebih rendah.
- Memiliki nilai Semester 1 (`Curricular_units_1st_sem_grade`) yang relatif lebih rendah.
- Lebih banyak ditemukan pada mahasiswa yang memiliki unit Semester 1 tanpa evaluasi.
- Lebih banyak ditemukan pada mahasiswa yang tuition fee-nya belum up to date.
- Proporsi Dropout lebih tinggi pada mahasiswa yang memiliki status debtor.
- Kelompok usia yang lebih tinggi, khususnya mahasiswa berusia di atas 25 tahun, menunjukkan jumlah dan proporsi Dropout yang lebih tinggi.
- Beberapa program studi menunjukkan dropout rate yang lebih tinggi dibandingkan program studi lainnya.

Karakteristik tersebut merupakan pola yang ditemukan pada dataset dan **tidak berarti bahwa mahasiswa dengan karakteristik tersebut pasti akan mengalami dropout**. Faktor-faktor tersebut dapat digunakan sebagai indikator untuk membantu proses monitoring dan early warning.

Pada proses pemodelan, mahasiswa dengan status **Enrolled** tidak digunakan sebagai target training karena status tersebut belum merupakan hasil akhir studi. Model dilatih menggunakan mahasiswa dengan status **Graduate** dan **Dropout**, dengan informasi yang tersedia hingga akhir semester pertama.

Model Logistic Regression menghasilkan **accuracy sebesar 90,08%**, **precision Dropout sebesar 86,81%**, **recall Dropout sebesar 88,03%**, dan **F1-score Dropout sebesar 87,41%**. Model ini kemudian digunakan sebagai prototype untuk membantu melakukan deteksi dini terhadap mahasiswa yang berpotensi mengalami dropout.

Dashboard Metabase melengkapi sistem dengan menyediakan monitoring dan visualisasi kondisi mahasiswa berdasarkan berbagai faktor akademik, administratif, finansial, demografi, dan program studi. Dengan kombinasi dashboard dan prototype machine learning, institusi dapat memperoleh informasi yang lebih terstruktur untuk mendukung proses monitoring dan memberikan intervensi kepada mahasiswa yang membutuhkan perhatian lebih lanjut.

> Hasil analisis dan prediksi model digunakan sebagai alat bantu early warning dan tidak dimaksudkan sebagai satu-satunya dasar dalam pengambilan keputusan terhadap mahasiswa.

### Rekomendasi Action Items

Beberapa action items yang dapat dilakukan Jaya Jaya Institut adalah:

- Melakukan intervensi akademik setelah semester pertama terhadap mahasiswa dengan jumlah mata kuliah yang berhasil diselesaikan rendah.
- Memberikan pendampingan akademik kepada mahasiswa yang menunjukkan performa atau nilai semester pertama yang rendah.
- Melakukan monitoring terhadap mahasiswa yang memiliki status pembayaran tuition fee belum up to date dan menghubungkannya dengan layanan administrasi atau pendampingan yang sesuai.
- Melakukan monitoring dropout berdasarkan course untuk mengidentifikasi program yang membutuhkan evaluasi atau dukungan lebih lanjut.
- Menggunakan dashboard secara berkala untuk memantau perubahan kondisi mahasiswa.
- Menggunakan prototype machine learning sebagai alat bantu deteksi dini, bukan sebagai satu-satunya dasar pengambilan keputusan.
- Melakukan evaluasi model secara berkala apabila tersedia data mahasiswa baru agar performa prediksi tetap relevan.
