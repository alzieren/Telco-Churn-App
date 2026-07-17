# Customer Churn Prediction

## Deskripsi
Aplikasi ini digunakan untuk memprediksi apakah seorang pelanggan berpotensi melakukan **Customer Churn** menggunakan algoritma **Random Forest** yang telah dioptimasi menggunakan **Hyperparameter Tuning**.

## Dataset
IBM Telco Customer Churn Dataset

## Algoritma
- Logistic Regression
- Decision Tree
- Random Forest (Model Terbaik)

## Performa Model Terbaik
- Accuracy : 95.10%
- AUC : 97.80%

## Cara Menjalankan

1. Install dependency

```bash
pip install -r requirements.txt
```

2. Jalankan aplikasi

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

## Author

Putri Nabilah A
Universitas Dian Nuswantoro