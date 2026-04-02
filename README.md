# NetworkAnomalyDetection


# 🛡️ Network Anomaly Detection Dashboard

A machine learning-based cybersecurity dashboard that detects anomalies in network traffic using real-time and batch data analysis.

---

## 🚀 Features

* 🔍 Detect anomalies in network traffic using **Isolation Forest**
* ⚡ Real-time + batch processing support
* 🔄 Dual mode:

  * **Pretrained Model Mode** (fast, fixed features)
  * **Dynamic Training Mode** (flexible, works with any dataset)
* 📊 Interactive dashboard using Streamlit
* 📈 Visualizations for traffic analysis
* 🧠 Automatic feature selection for unknown datasets

---

## 🧠 Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Matplotlib
* Joblib

---

## 📁 Project Structure

```
cyber-anomaly-dashboard/
│── app.py              # Main Streamlit app
│── detector.py         # ML model logic
│── requirements.txt    # Dependencies
│── anomaly_model.pkl   # (Optional) Saved model
│── scaler.pkl          # (Optional) Saved scaler
│── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/network-anomaly-detection.git
cd network-anomaly-detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📊 Usage

1. Upload a CSV dataset
2. Select mode:

   * **Pretrained Model** → requires specific features
   * **Dynamic Training** → works with any numeric dataset
3. Select features (for dynamic mode)
4. View:

   * Anomaly predictions
   * Metrics
   * Visualizations

---

## ⚠️ Notes

* Pretrained model requires specific feature names (e.g., `src_port`, `dst_port`, `packet_size`)
* Dynamic mode is recommended for unknown datasets
* Dataset must contain **numeric columns** for analysis

---

## 📈 Output

* `0` → Normal traffic
* `1` → Anomaly detected

---

## 💡 Future Improvements

* 🌍 IP geolocation mapping
* 🔐 Real-time packet capture using Scapy
* 📊 Advanced dashboards (Plotly, heatmaps)
* 🎯 Attack classification (DoS, Probe, etc.)
* 📡 API deployment (FastAPI)

---

## 🧪 Development Workflow

* Model training and experimentation done in Google Colab
* Deployment and dashboard built using Streamlit in VS Code

---

## 🤝 Contributing

Feel free to fork this repository and improve the project!

---

## ⭐ Acknowledgment

This project demonstrates practical implementation of machine learning in cybersecurity for anomaly detection.

---
