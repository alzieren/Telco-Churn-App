import streamlit as st
import pandas as pd
import joblib

# Konfigurasi halaman
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# Sidebar
st.sidebar.title("📊 Customer Churn Prediction")
st.sidebar.markdown("---")

st.sidebar.write("**Model:** Random Forest (Hyperparameter Tuned)")
st.sidebar.write("**Accuracy:** 95.10%")
st.sidebar.write("**AUC:** 97.80%")

st.sidebar.markdown("---")

st.sidebar.info(
    """
    **Cara menggunakan:**
    1. Isi data pelanggan.
    2. Klik **Prediksi Churn**.
    3. Lihat hasil prediksi beserta probabilitasnya.
    """
)

st.sidebar.markdown("---")
st.sidebar.caption("UAS Pembelajaran Mesin - UDINUS")

st.title("📊 Customer Churn Prediction")
st.markdown(
    """
    Prediksi kemungkinan seorang pelanggan akan **melakukan churn** menggunakan
    model **Random Forest** yang telah dioptimasi dengan **Hyperparameter Tuning**.
    """
)

# Load model dan nama fitur
model = joblib.load("model_churn.pkl")
feature_names = joblib.load("feature_names.pkl")

st.divider()

st.subheader("Input Data Pelanggan")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 18, 100, 30)
    tenure = st.number_input("Tenure in Months", 0, 100, 12)
    monthly_charge = st.number_input("Monthly Charge", 0.0, 500.0, 50.0)
    satisfaction = st.slider("Satisfaction Score", 1, 5, 3)

with col2:
    gender = st.selectbox("Gender", ["Female", "Male"])
    married = st.selectbox("Married", ["No", "Yes"])
    internet = st.selectbox("Internet Service", ["No", "Yes"])
    contract = st.selectbox("Contract", ["Month-to-Month", "One Year", "Two Year"])
    
if st.button("🔍 Prediksi Churn"):

    input_data = pd.DataFrame(0, index=[0], columns=feature_names)

    input_data["Age"] = age
    input_data["Tenure in Months"] = tenure
    input_data["Monthly Charge"] = monthly_charge
    input_data["Satisfaction Score"] = satisfaction

    # Encoding Gender
    if gender == "Male":
        input_data["Gender_Male"] = 1

    # Encoding Married
    if married == "Yes":
        input_data["Married_Yes"] = 1

    # Encoding Internet Service
    if internet == "Yes":
        input_data["Internet Service_Yes"] = 1

    # Encoding Contract
    if contract == "One Year":
        input_data["Contract_One Year"] = 1
    elif contract == "Two Year":
        input_data["Contract_Two Year"] = 1

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    if prediction == 1:
        st.error("🚨 Hasil Prediksi: Customer berpotensi melakukan Churn")
        st.metric(
            label="Tingkat Risiko Churn",
            value=f"{probability[1]*100:.2f}%"
        )
    else:
        st.success("🎉 Hasil Prediksi: Customer diprediksi Tidak Churn")
        st.metric(
            label="Peluang Tetap Berlangganan",
            value=f"{probability[0]*100:.2f}%"
        )
    
