import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="ICU Digital Twin Dashboard",
    layout="wide"
)

# Load data
df = pd.read_csv("patient_monitoring_with_drift.csv")

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Title
st.title("🏥 Cloud-Edge ICU Digital Twin Dashboard")

# Metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Patients", df["patient_id"].nunique())

col2.metric(
    "Avg Heart Rate",
    round(df["heart_rate_bpm"].mean(), 1)
)

col3.metric(
    "Avg SpO₂",
    round(df["spo2_percent"].mean(), 1)
)

col4.metric(
    "Avg ICU Risk",
    round(df["icu_risk_score"].mean(), 1)
)

st.divider()

# Patient Selection
st.subheader("👤 Patient Digital Twin")

patient = st.selectbox(
    "Select Patient",
    sorted(df["patient_id"].unique())
)

patient_df = df[df["patient_id"] == patient]
st.write("Records:", len(patient_df))

patient_df = patient_df.sort_values("timestamp")

latest = patient_df.iloc[-1]

# Latest Patient Data
st.write("### Latest Patient Status")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "❤️ Heart Rate",
    f"{latest['heart_rate_bpm']} BPM"
)

c2.metric(
    "🫁 SpO₂",
    f"{latest['spo2_percent']} %"
)

c3.metric(
    "🌡 Temperature",
    f"{latest['temperature_f']} °F"
)

c4.metric(
    "⚠ ICU Risk",
    f"{latest['icu_risk_score']}"
)

c5, c6, c7 = st.columns(3)

c5.metric(
    "🩸 Blood Pressure",
    latest["blood_pressure"]
)

c6.metric(
    "💨 Resp Rate",
    f"{latest['respiratory_rate_bpm']} BPM"
)

c7.metric(
    "🍬 Glucose",
    f"{latest['glucose_mg_dl']} mg/dL"
)
#st.subheader("🚨 Clinical Decision Support")

# Clinical Decision Support
st.subheader("🚨 Clinical Decision Support")

alerts = False

if latest["heart_rate_bpm"] > 120:
    st.error("Tachycardia Detected")
    alerts = True

if latest["spo2_percent"] < 90:
    st.error("Low Oxygen Saturation (Hypoxia)")
    alerts = True

if latest["temperature_f"] > 101:
    st.error("Fever Detected")
    alerts = True

if latest["icu_risk_score"] > 80:
    st.error("High ICU Risk")
    alerts = True

if latest["critical_alert_label"] != "NORMAL":
    st.warning(
        f"Critical Alert: {latest['critical_alert_label']}"
    )
    alerts = True

if not alerts:
    st.success("Patient Stable - No Critical Alerts")


# ==========================
# Trends
# ==========================

st.subheader("📈 Heart Rate Trend")

st.line_chart(
    patient_df.set_index("timestamp")["heart_rate_bpm"]
)

st.subheader("🫁 SpO₂ Trend")

st.line_chart(
    patient_df.set_index("timestamp")["spo2_percent"]
)

st.subheader("⚠ ICU Risk Trend")

st.line_chart(
    patient_df.set_index("timestamp")["icu_risk_score"]
)

st.subheader("🍬 Glucose Trend")

st.line_chart(
    patient_df.set_index("timestamp")["glucose_mg_dl"]
)


# ==========================
# Drift Detection
# ==========================

st.subheader("🔍 Data Drift Monitoring")

st.bar_chart(
    df["drift_status"].value_counts()
)