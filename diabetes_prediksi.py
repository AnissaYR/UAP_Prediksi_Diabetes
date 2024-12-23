import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

# Mengatur tema terang di Streamlit
st.set_page_config(page_title="Prediksi Diabetes", page_icon=":guardsman:", layout="wide", initial_sidebar_state="expanded")

# Memuat model dari folder 'UAP'
model_xgb = joblib.load('UAP/xgboost_model.pkl')
model_RF = joblib.load('UAP/random_forest_model.sav')

# Fungsi untuk encode kolom kategorikal
def encode_input_data(df):
    label_encoder = LabelEncoder()
    categorical_columns = ['gender', 'smoking_history']  # Sesuaikan dengan kolom kategorikal di dataset
    for column in categorical_columns:
        df[column] = label_encoder.fit_transform(df[column])
    return df

# Judul aplikasi
st.title("Prediksi Diabetes")

# Deskripsi aplikasi
st.write("""
Aplikasi ini menggunakan model Random Forest atau XGBoost untuk memprediksi kemungkinan seseorang menderita diabetes.
Silakan pilih model dan masukkan data di bawah untuk melakukan prediksi.
""")

# Pilihan model yang ingin digunakan
model_choice = st.selectbox('Pilih Model untuk Prediksi:', ['Random Forest', 'XGBoost'])

# Input data pengguna
gender = st.selectbox('Jenis Kelamin', ['Female', 'Male'])
age = st.slider('Usia', min_value=1, max_value=100, value=25)
hypertension = st.selectbox('Apakah Anda menderita hipertensi?', [0, 1])
heart_disease = st.selectbox('Apakah Anda memiliki penyakit jantung?', [0, 1])
smoking_history = st.selectbox('Riwayat Merokok', ['No Info', 'never', 'ever', 'former', 'current', 'not current'])
bmi = st.slider('BMI', min_value=10.0, max_value=50.0, value=25.0)
hba1c_level = st.slider('Level HbA1c', min_value=4.0, max_value=10.0, value=5.0)
blood_glucose_level = st.slider('Tingkat Glukosa Darah', min_value=50, max_value=300, value=100)

# Mengubah input menjadi format yang sesuai dengan model
input_data = {
    'gender': [gender],
    'age': [age],
    'hypertension': [hypertension],
    'heart_disease': [heart_disease],
    'smoking_history': [smoking_history],
    'bmi': [bmi],
    'HbA1c_level': [hba1c_level],
    'blood_glucose_level': [blood_glucose_level]
}

input_df = pd.DataFrame(input_data)

# Melakukan encoding pada input data
input_df_encoded = encode_input_data(input_df)

# Menambahkan Progress Bar atau Spinner
with st.spinner('Melakukan prediksi...'):
    # Melakukan prediksi
    if st.button('Prediksi'):
        # Memilih model yang akan digunakan
        if model_choice == 'XGBoost':
            model = model_xgb
        else:
            model = model_RF
        
        # Melakukan prediksi dengan model yang dipilih
        prediction = model.predict(input_df_encoded)
        
        # Mengambil nilai prediksi dari array
        prediction_value = prediction[0]  # Mengambil nilai pertama dari array
        
        # Menampilkan hasil prediksi secara langsung tanpa visualisasi grafik
        if prediction_value == 1:
            st.write("Hasil Prediksi: **Diabetes Negatif**")
            st.image('https://student-activity.binus.ac.id/tfi/wp-content/uploads/sites/41/2021/05/MENJAGA-POLA-HIDUP-SEHAT-DI-MASA-PANDEMI-COVID-19.jpg', caption="Gambar Ilustrasi Kesehatan")
        else:
            st.write("Hasil Prediksi: **Diabetes Positif**")
            st.image('https://i0.wp.com/www.rhesusnegative.net/staynegative/wp-content/uploads/2015/01/Figure1diabetes.jpg', caption="Gambar Ilustrasi Diabetes")
            
