import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from detector import AnomalyDetector

st.set_page_config(layout="wide")
st.title("🛡️ Network Anomaly Detection Dashboard")

# 🔹 Mode selection
mode = st.radio("Select Mode", ["Pretrained Model", "Dynamic Training"])

uploaded_file = st.file_uploader("Upload Dataset", type=["csv"])

if uploaded_file is not None:

    # Step 1: Load data
    data = pd.read_csv(uploaded_file)

    # Step 2: Clean column names
    data.columns = data.columns.str.strip()

    st.subheader("📊 Dataset Preview")
    st.dataframe(data.head())

    # Step 3: Detect numeric columns
    numeric_cols = data.select_dtypes(include=['number']).columns.tolist()

    # Step 4: Feature selection (for dynamic mode)
    selected_features = st.multiselect(
        "Select features",
        numeric_cols,
        default=numeric_cols[:min(4, len(numeric_cols))]
    )

    detector = AnomalyDetector()

    # ===============================
    # 🔹 PRETRAINED MODE
    # ===============================
    if mode == "Pretrained Model":

        st.info("Using pretrained model (fixed features required)")

        # ⚠️ CHANGE THIS according to your trained model
        pretrained_features = ['dst_port', 'packet_size', 'src_port']

        # Check if dataset matches
        if not all(col in data.columns for col in pretrained_features):
            st.error("❌ Dataset does not match pretrained model features")
            st.write("Required:", pretrained_features)
            st.write("Available:", list(data.columns))
            st.stop()

        detector.load_model()

        data['Predicted'] = detector.predict_pretrained(
            data[pretrained_features]
        )

    # ===============================
    # 🔹 DYNAMIC MODE
    # ===============================
    else:

        st.info("Dynamic training mode (works with any dataset)")

        if len(selected_features) < 2:
            st.warning("Select at least 2 features")
            st.stop()

        detector.train_model()

        data['Predicted'] = detector.predict_dynamic(
            data[selected_features]
        )

    # ===============================
    # 📊 RESULTS
    # ===============================
    st.subheader("📈 Results")

    total = len(data)
    anomalies = data['Predicted'].sum()

    col1, col2 = st.columns(2)
    col1.metric("Total Records", total)
    col2.metric("Anomalies Detected", int(anomalies))

    st.subheader("🔍 Data with Predictions")
    st.dataframe(data)

    # ===============================
    # 📊 VISUALIZATION
    # ===============================
    st.subheader("📊 Visualization")

    if len(selected_features) >= 2:
        fig, ax = plt.subplots()
        ax.scatter(
            data[selected_features[0]],
            data[selected_features[1]],
            c=data['Predicted']
        )
        ax.set_xlabel(selected_features[0])
        ax.set_ylabel(selected_features[1])
        st.pyplot(fig)

else:
    st.info("👆 Upload a dataset to begin")