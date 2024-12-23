# ✨ Prediksi Penderita Diabetes ✨
## Klasifikasi Otomatis Penderita Diabetes dengan Random Forest dan XGBoost

![Ilustrasi Diabetes](https://scontent.fsub9-1.fna.fbcdn.net/v/t39.30808-6/465067656_9238603872836297_8013902093878392409_n.png?_nc_cat=111&ccb=1-7&_nc_sid=0b6b33&_nc_ohc=omryABp_dPcQ7kNvgEq3XsP&_nc_zt=23&_nc_ht=scontent.fsub9-1.fna&_nc_gid=Aah5DLKnOJmtXSeq-spc8gx&oh=00_AYDuuv0afqybxcQnbEibT0SiLNll7Pl-vhz7VryzZ13shA&oe=676DBF18)

Diabetes adalah penyakit kronis yang sering berkembang secara diam-diam namun memiliki dampak besar pada kesehatan. Penyakit ini terjadi ketika tubuh tidak mampu mengatur kadar gula darah dengan baik, yang dapat memicu berbagai komplikasi serius seperti penyakit jantung, kerusakan ginjal, gangguan penglihatan, hingga masalah saraf. Gejalanya sering kali muncul perlahan, seperti sering merasa haus, mudah lelah, sering buang air kecil, dan luka yang sulit sembuh. Hal ini menjadikan diabetes sebagai tantangan besar dalam dunia kesehatan, terutama karena gaya hidup modern yang semakin meningkatkan risiko penyakit ini.

Namun, kemajuan teknologi kini memungkinkan deteksi dini diabetes dengan bantuan prediksi berbasis kecerdasan buatan. Dengan memanfaatkan data medis dan demografi seperti usia, BMI, riwayat kesehatan, serta kadar gula darah, model pembelajaran mesin seperti Random Forest dan XGBoost dapat digunakan untuk memprediksi apakah seseorang berisiko terkena diabetes atau tidak. Solusi ini memudahkan tenaga medis dan individu untuk mengambil langkah pencegahan lebih awal, sehingga risiko komplikasi dapat diminimalkan dan kualitas hidup tetap terjaga.✨

### ✨Overview Dataset✨
Proyek ini menggunakan dataset Diabetes Prediction Dataset yang diambil dari platform Kaggle [Diabetes Prediction Dataset - Kaggle](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset). Dataset ini berisi sekitar 100.000 data medis dan demografi pasien, mencakup informasi penting seperti usia, jenis kelamin, indeks massa tubuh (BMI), riwayat hipertensi, penyakit jantung, kebiasaan merokok, kadar HbA1c, dan kadar glukosa darah, serta status diabetes pasien (positif atau negatif). Dataset ini dapat digunakan untuk membangun model pembelajaran mesin yang dapat memprediksi kemungkinan seseorang mengidap diabetes berdasarkan riwayat medis dan informasi demografis mereka. Dengan demikian, dataset ini memiliki potensi besar untuk mendukung pencegahan dini serta perencanaan perawatan yang lebih tepat dan personal.

### ✨Algorirtma Classification✨
- *Random Forest Classification*
  
![Random Forest](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*ZFuMI_HrI3jt2Wlay73IUQ.png)

Random Forest Classification adalah metode pembelajaran mesin yang digunakan untuk mengklasifikasikan data dengan cara membangun sejumlah pohon keputusan (decision trees) yang saling independen, kemudian menggabungkan hasil prediksi dari masing-masing pohon untuk menghasilkan keputusan akhir. Tujuan utamanya adalah untuk meningkatkan akurasi dan mengurangi risiko overfitting, yang sering terjadi pada pohon keputusan tunggal. Prosesnya dimulai dengan membangun banyak pohon keputusan dengan menggunakan sampel acak dari data pelatihan, dan setiap pohon memberikan prediksi berdasarkan fitur yang relevan. Hasil dari semua pohon ini kemudian digabungkan untuk memberikan prediksi yang lebih stabil dan akurat, menjadikan Random Forest sangat efektif untuk menangani dataset besar dengan banyak variabel.

- *XGBoost Classification*

![XGBoost](https://lh3.googleusercontent.com/4svO7UdzXj-JxFwU-_SyrMWMqxp8Al3pVpQYr5A-nzCDXdEqVL_CHeqbeVVW8Kivsq76q5sozAKwGsQuy5qnk5wVYfqWb5LHxhknBm9DSLBjg0ViSRTVjZ3gFQPwiGxJ8wP2usOH)

XGBoost Classification adalah salah satu algoritma pembelajaran mesin paling kuat dan efisien yang digunakan untuk tugas klasifikasi. Dengan menggabungkan kekuatan beberapa model lemah (pohon keputusan) melalui teknik boosting, XGBoost berfokus pada perbaikan kesalahan yang dibuat oleh model sebelumnya, sehingga menghasilkan prediksi yang lebih akurat. Setiap pohon yang ditambahkan bekerja untuk mengoreksi kesalahan dari pohon sebelumnya, membuat model semakin kuat. Keunggulan XGBoost terletak pada kemampuannya untuk menangani data besar dengan cepat dan akurat, serta kemampuannya menghindari overfitting melalui regularisasi. Berkat kinerjanya yang luar biasa, XGBoost sering menjadi pilihan utama dalam kompetisi machine learning dan aplikasi dunia nyata.

### ✨Preprocessing, EDA, dan Train-split✨

![Perbandingan](assets/images/Perbandingan_Penderita_Diabetes.png)

Distribusi data menunjukkan ketimpangan yang signifikan, dengan 91.500 individu tanpa diabetes dibandingkan hanya 8.500 dengan diabetes. Hal ini mengindikasikan bahwa prediksi dalam proyek ini kemungkinan besar akan lebih sulit untuk mendeteksi kasus positif diabetes secara akurat karena dominasi data non-diabetes, walaupun meskipun model prediksi mungkin mencapai akurasi tinggi.

#### *Random Forest Classification*
- Sebelum SMOTE
  
![RR_SBS](assets/images/Random_Forest_Sebelum_SMOTE.png)

Dengan pembagian data train-test 80:20, hasil classification report sebelum SMOTE menunjukkan akurasi sebesar 97%.

- Sesudah SMOTE
  
![RR_SBS](assets/images/Random_Forest_Sebelum_SMOTE.png)

Hasil classification report setelah SMOTE menunjukkan akurasi tetap sebesar 97%, dengan peningkatan keseimbangan dalam mendeteksi kelas 1 (positif diabetes) meskipun recall mencapai 71%."

Kesimpulannya, penerapan SMOTE membantu model lebih seimbang dalam mendeteksi kasus positif diabetes tanpa mengorbankan akurasi keseluruhan.

#### ✨Confusion Matrix Random Forest✨
![CMRF](assets/images/Confusion_Matrix_Random_Forest_Sebelum_SMOTE.png)
![CMRF](assets/images/Confusion_Matrix_Random_Forest_Sesudah_SMOTE.png)



  
