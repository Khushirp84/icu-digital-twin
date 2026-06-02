# 🏥 Cloud-Edge Digital Twin Framework for ICU Simulation and Clinical Decision Support

## 📌 Project Overview

This project implements a Cloud-Edge Digital Twin Framework for ICU Simulation and Clinical Decision Support using synthetic patient monitoring data.

The system creates a Digital Twin (virtual representation) of ICU patients by continuously monitoring vital signs and providing real-time health insights through an interactive dashboard.

The solution is containerized using Docker, version-controlled using GitHub, and deployed on the cloud using Render.

---

## 🚀 Live Demo

Dashboard URL:

https://icu-digital-twin.onrender.com

---

## 🎯 Objectives

- Develop a Digital Twin for ICU patients.
- Simulate ICU monitoring using synthetic healthcare data.
- Provide real-time visualization of patient vitals.
- Generate clinical alerts for abnormal conditions.
- Monitor ICU risk scores.
- Deploy the system using cloud technologies.

---

## 🧠 What is a Digital Twin?

A Digital Twin is a virtual model of a real-world entity.

In this project:

- Each patient has a virtual representation.
- Patient vitals are continuously monitored.
- The dashboard reflects the latest patient state.
- Clinical alerts are generated automatically.
- Risk assessment is performed using ICU risk scores.

Thus, every patient selected in the dashboard acts as a Digital Twin of an ICU patient.

---

## 🏗️ System Architecture

```text
+----------------------+
| Synthetic ICU Data   |
+----------+-----------+
           |
           v
+----------------------+
| Patient Digital Twin |
+----------+-----------+
           |
           v
+----------------------+
| Clinical Decision    |
| Support System       |
+----------+-----------+
           |
           v
+----------------------+
| Streamlit Dashboard  |
+----------+-----------+
           |
           v
+----------------------+
| Docker Container     |
+----------+-----------+
           |
           v
+----------------------+
| Cloud Deployment     |
| (Render)             |
+----------------------+
```

---

## ⚙️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Backend Development |
| Pandas | Data Processing |
| Streamlit | Dashboard Development |
| Docker | Containerization |
| Git & GitHub | Version Control |
| Render | Cloud Deployment |
| CSV Dataset | Synthetic ICU Data |

---

## 📊 Features

### 👤 Patient Digital Twin

Displays:

- Patient ID
- Heart Rate
- Blood Pressure
- SpO₂
- Temperature
- Respiratory Rate
- Glucose Level
- ICU Risk Score

### 🚨 Clinical Decision Support

Detects:

- Tachycardia
- Hypoxia
- Fever
- High ICU Risk
- Critical Patient Alerts

### 📈 Dashboard Analytics

Shows:

- Total Patients
- Average Heart Rate
- Average SpO₂
- Average ICU Risk
- Individual Patient Monitoring

### 🔍 Data Drift Monitoring

Tracks:

- Normal Data
- Warning Drift
- Critical Drift

---

## 📂 Project Structure

```text
icu-digital-twin/
│
├── dashboard/
│   ├── dashboard.py
│   ├── patient_monitoring_with_drift.csv
│   ├── requirements.txt
│   └── Dockerfile
│
├── k8s/
│   ├── orion-deployment.yaml
│   └── simulator-deployment.yaml
│
├── docker-compose.yml
│
└── README.md
```

---

## 🖥️ Running Locally

### Clone Repository

```bash
git clone https://github.com/Khushirp84/icu-digital-twin.git

cd icu-digital-twin/dashboard
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Dashboard

```bash
streamlit run dashboard.py
```

Open:

```text
http://localhost:8501
```

---

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t icu-dashboard .
```

### Run Container

```bash
docker run -p 8501:8501 icu-dashboard
```

Open:

```text
http://localhost:8501
```

---

## 🐙 Git Commands Used

### Initialize Repository

```bash
git init
```

### Add Files

```bash
git add .
```

### Commit Changes

```bash
git commit -m "ICU Digital Twin Dashboard"
```

### Connect GitHub

```bash
git remote add origin https://github.com/Khushirp84/icu-digital-twin.git
```

### Push Code

```bash
git branch -M main

git push -u origin main
```

---

## ☁️ Cloud Deployment

### Platform

Render

### Deployment Method

- GitHub Integration
- Docker Deployment
- Automatic Build & Deploy

### Live URL

https://icu-digital-twin.onrender.com

---

## 📋 Results

The developed framework successfully:

✅ Creates Digital Twins for ICU patients

✅ Simulates ICU monitoring using synthetic data

✅ Generates clinical alerts

✅ Displays patient health information

✅ Performs ICU risk assessment

✅ Detects data drift

✅ Runs in Docker containers

✅ Deploys successfully on cloud infrastructure

---

## 🔮 Future Scope (Phase 2)

### Edge Layer

- FIWARE Orion Context Broker
- MQTT Integration
- IoT Device Connectivity

### AI Layer

- Machine Learning Risk Prediction
- Early Warning Score Prediction
- Patient Deterioration Forecasting

### Cloud Layer

- Multi-Hospital Monitoring
- Real-Time Data Streaming
- Historical Patient Analytics

### Clinical Decision Support

- AI-Based Recommendations
- Predictive Alerts
- Automated Notification System

---

## 🎓 Academic Relevance

This project demonstrates concepts from:

- Digital Twin Technology
- Cloud Computing
- Edge Computing
- Healthcare Analytics
- Clinical Decision Support Systems
- Data Monitoring and Visualization
- Containerization using Docker

---

## 👩‍💻 Author

**Khushi R Patel**

Computer Science & Engineering

GitHub: https://github.com/Khushirp84

---

## 📜 License

This project is developed for academic and educational purposes.