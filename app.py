import streamlit as st
import numpy as np
import pickle

# ================== Load Model Files ==================
model = pickle.load(open("crop_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
le = pickle.load(open("label_encoder.pkl", "rb"))

# ================== Page Configuration ==================
st.set_page_config(
    page_title="🌾 Crop Recommendation System",
    page_icon="🌱",
    layout="centered"
)

# ================== Custom Header ==================
st.markdown("""
    <h1 style='text-align:center; color:#2E7D32;'>🌱 Crop Recommendation System</h1>
    <p style='text-align:center; color:gray;'>
    Intelligent ML-based system for smart agriculture
    </p>
""", unsafe_allow_html=True)

st.markdown("---")

# ================== Input Section ==================
st.subheader("🧪 Soil & Climate Parameters")

col1, col2 = st.columns(2)

with col1:
    N = st.slider("Nitrogen (N)", 0, 150, 50)
    P = st.slider("Phosphorus (P)", 0, 150, 50)
    K = st.slider("Potassium (K)", 0, 150, 50)
    ph = st.slider("pH Value", 0.0, 14.0, 6.5)

with col2:
    temperature = st.slider("Temperature (°C)", 0.0, 50.0, 25.0)
    humidity = st.slider("Humidity (%)", 0.0, 100.0, 60.0)
    rainfall = st.slider("Rainfall (mm)", 0.0, 400.0, 100.0)

st.markdown("---")

# ================== Prediction Section ==================
if st.button("🌾 Recommend Best Crop", use_container_width=True):

    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    scaled_data = scaler.transform(input_data)

    prediction = model.predict(scaled_data)
    crop = le.inverse_transform(prediction)

    st.success(f"🌿 **Recommended Crop:** {crop[0]}")

    # ================== Explanation ==================
    st.info(
        "ℹ️ This recommendation is generated using a trained Machine Learning model "
        "based on soil nutrients and climatic conditions."
    )

    # ================== Debug (Optional) ==================
    with st.expander("🔍 Technical Details"):
        st.write("Input Values:", input_data)
        st.write("Scaled Values:", scaled_data)
        st.write("Model Prediction Index:", prediction)

# ================== Footer ==================
st.markdown("---")
st.markdown("""
    <p style='text-align:center; color:gray;'>
    Developed using Machine Learning & Streamlit
    </p>
""", unsafe_allow_html=True)
