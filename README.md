# 🛡️ Sentinel — AI-Based Personnel Stress & Welfare Monitoring System

**Smart India Hackathon 2024 | Problem Statement 26186**

A privacy-first, AI-powered platform to proactively detect early signs of stress and burnout among uniformed personnel (CRPF, BSF, CISF, Army, etc.) and trigger timely welfare support — before crisis strikes.

---

## 📌 Problem Statement

Uniformed personnel face chronic occupational stress from long deployments, hazardous duty, and family separation. Current systems are **reactive**, relying on self-reporting (avoided due to stigma) or subjective officer observation. There is no proactive, data-driven, privacy-safe system to detect stress early.

**PS ID:** 26186
**Category:** Software
**Theme:** Miscellaneous / Defence

---

## 💡 Our Solution

A multi-layered AI platform combining passive HR data analysis, voluntary self-assessment, and explainable machine learning to flag at-risk personnel — without compromising individual privacy or dignity.

### Core Components

| Component | Purpose |
|---|---|
| 🔮 Predictive Analytics Engine | Detects stress patterns from HR data |
| 📱 Mobile Wellness App | Voluntary self-assessment by personnel |
| 📊 Risk Dashboard | For welfare officers & commanders |
| 🩺 Intervention Recommender | Suggests counseling, leave, workload rebalancing |
| 🔐 Role-Based Access Control | Ensures only authorized people see data |
| 🕶️ Privacy & Anonymization Layer | Protects individual dignity |

### What Makes It Different

- **Privacy-first by design** — individual data never shown to commanding officers; only anonymized trends
- **Welfare, not surveillance** — flags trigger counselor outreach, not disciplinary action
- **Culturally adapted** — multilingual (Hindi + English), built for Indian paramilitary workflows
- **On-premise / federated** — sensitive data never leaves the force's own servers
- **Explainable AI** — welfare officers see *why* someone is flagged, not just a score

---

## 🏗️ System Architecture

```
Mobile App ──► API Gateway ──► Anonymizer ──► PostgreSQL
                                    │
                              InfluxDB (biometrics)
                                    │
                             Feature Extractor
                                    │
                          ML Inference Engine (Celery)
                                    │
                            Risk Score Written to DB
                                    │
                    Threshold crossed? ──► WebSocket Alert
                                              │
                                    Welfare Officer Dashboard
```

### Three-Layer Approach

1. **Passive Data Collection** — Pulls from existing HRMS (leave frequency, transfers, duty hours, deployment duration); flags anomalies automatically, zero burden on personnel.
2. **Voluntary Engagement** — Weekly 2-minute wellness check-in via mobile app (mood, sleep, stress scale), anonymous peer reporting, optional wearable sync.
3. **AI Prediction Engine** — Ensemble model (XGBoost + LSTM + NLP) outputs a Green / Amber / Red risk classification with SHAP-based explainability.

---

## 🛠️ Tech Stack

### Frontend
- **Mobile App:** React Native
- **Web Dashboard:** React.js + TypeScript
- **UI:** Tailwind CSS + shadcn/ui
- **Charts:** Recharts / D3.js
- **State Management:** Redux Toolkit

### Backend
- **Primary API:** FastAPI (Python)
- **Secondary API:** Node.js + Express
- **Auth:** JWT + OAuth 2.0
- **Real-time Alerts:** WebSockets (Socket.io)
- **Task Queue:** Celery + Redis

### AI / ML
- **Model Building:** Scikit-learn, XGBoost
- **Deep Learning:** PyTorch (LSTM for time-series trends)
- **NLP:** HuggingFace Transformers — MuRIL (multilingual Indian languages)
- **Explainability:** SHAP
- **Model Serving & Tracking:** MLflow

### Database
- **Primary DB:** PostgreSQL
- **Cache:** Redis
- **Time-Series:** InfluxDB (wearable/biometric streams)
- **Vector DB:** Pinecone / pgvector (NLP embeddings)
- **Object Storage:** MinIO

### Infrastructure & Security
- **Deployment:** Docker + Kubernetes
- **Encryption:** AES-256 (at rest), TLS 1.3 (in transit)
- **Secrets Management:** HashiCorp Vault
- **Monitoring:** Prometheus + Grafana
- **CI/CD:** GitHub Actions

---

## 🧠 ML Model Design

**Ensemble Risk Scoring:**

```
final_score = (
    0.45 * xgboost_score +
    0.35 * lstm_trajectory_score +
    0.20 * nlp_distress_score
)

Risk Label:
  >= 0.75  → 🔴 HIGH   (Immediate welfare contact)
  >= 0.45  → 🟡 AMBER  (Monitor + optional check-in)
  <  0.45  → 🟢 LOW    (Routine wellness)
```

**Feature Categories:**
- **HR Signals** (passive): deployment duration, transfer frequency, leave utilization, consecutive duty days, overtime, night shifts
- **Self-Report Signals** (voluntary): PHQ-9, GAD-7, PSS scores, sleep quality, mood score
- **NLP Signals**: sentiment analysis, distress/hopelessness language detection from free-text entries

Every prediction includes a SHAP-based breakdown of the top contributing factors, shown only to authorized welfare officers.

---

## 🔐 Privacy Architecture

| Layer | Access |
|---|---|
| Real Identity (name, service number) | Encrypted vault only — most restricted |
| Anonymized Layer (anon_id, hashed) | System internal use |
| Analytics Layer (risk scores, trends) | Welfare officers & commanders |

- Welfare officers see: risk score + SHAP reasons + recommendations
- Commanding officers see: **only** unit-level aggregates (% of unit at risk)
- No one sees: raw self-report text or individual biometric values
- De-identification is irreversible at the analytics layer

---

## 👥 Team

| Member | Role |
|---|---|
| Member 1 | Team Lead & Backend Developer |
| Member 2 | ML Engineer |
| Member 3 | Frontend Developer (Dashboard) |
| Member 4 | Mobile App Developer |
| Member 5 | Database & Security Developer |
| Member 6 | UI/UX Designer & Presenter |

---

## 🚀 Getting Started

### Prerequisites
- Docker & Docker Compose
- Node.js 18+
- Python 3.10+
- PostgreSQL 14+

### Setup

```bash
# Clone the repository
git clone https://github.com/<your-org>/sentinel-sih26186.git
cd sentinel-sih26186

# Spin up local services (Postgres, Redis, InfluxDB)
docker-compose up -d

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend dashboard setup
cd frontend
npm install
npm run dev

# Mobile app setup
cd mobile
npm install
npx expo start
```

### Environment Variables

Create a `.env` file in `backend/` based on `.env.example`:

```
DATABASE_URL=postgresql://user:password@localhost:5432/sentinel
REDIS_URL=redis://localhost:6379
JWT_SECRET=your_jwt_secret
```

---

## 📅 Development Roadmap

- [x] Problem research & solution design
- [x] Tech stack & architecture finalization
- [ ] Database schema + anonymization layer
- [ ] Core backend APIs + auth
- [ ] XGBoost model (baseline)
- [ ] Web dashboard (welfare officer view)
- [ ] Mobile app (wellness check-in)
- [ ] LSTM + NLP model integration
- [ ] SHAP explainability
- [ ] Alert system (WebSockets)
- [ ] Integration testing
- [ ] Demo video & pitch deck

---

## 📄 License

This project was built for Smart India Hackathon 2024 (Problem Statement 26186). License TBD.

---

## 🙏 Acknowledgements

- Smart India Hackathon & Ministry of Home Affairs for the problem statement
- iCall, NIMHANS, and existing mental health helplines for reference research
