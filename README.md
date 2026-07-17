# Customer Churn Prediction

## Deskripsi
Aplikasi ini digunakan untuk memprediksi apakah seorang pelanggan berpotensi melakukan **Customer Churn** menggunakan algoritma **Random Forest** yang telah dioptimasi menggunakan **Hyperparameter Tuning**. Aplikasi dikembangkan menggunakan **Streamlit** sehingga pengguna dapat melakukan prediksi secara interaktif melalui web.

## Dataset
IBM Telco Customer Churn Dataset

Target:
- Churn (Yes / No)

Input Features:
- Age
- Tenure
- Monthly Charge
- Satisfaction Score
- Gender
- Married
- Internet Service
- Contract Type

## Algoritma
Model yang diuji:
- Logistic Regression
- Decision Tree
- Random Forest (Best Model)

## Performa Model Terbaik
- Accuracy : **95.10%**
- ROC-AUC : **97.80%**

## Teknologi
- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib

## Cara Menjalankan

1. Clone repository

```bash
git clone https://github.com/alzieren/Telco-Churn-App.git
```

2. Install dependency

```bash
pip install -r requirements.txt
```

3. Jalankan aplikasi

```bash
streamlit run app.py
```

## Struktur Folder

```
Telco-Churn-App/
│
├── app.py
├── model_churn.pkl
├── feature_names.pkl
├── telco_clean.csv
├── requirements.txt
└── README.md
```

## Demo Aplikasi

Streamlit Cloud:
https://telco-churn-app-putrinabilah.streamlit.app

## Author

**Putri Nabilah A**  
Universitas Dian Nuswantoro