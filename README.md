# 🧪 Chemical Equipment Parameter Visualizer

### Hybrid Web + Desktop Application (Django REST + React + PyQt5)

This project is developed as part of the **FOSSEE Internship Screening Task**.
It demonstrates a **hybrid architecture** where a **single Django REST backend** is consumed by both a **React Web Application** and a **PyQt5 Desktop Application** for chemical equipment data visualization and analytics.

---

## 🌐 Live Deployment Links

* 🔗 **Web Application (React)**: [https://fossee-hybrid-app.onrender.com](https://fossee-hybrid-app.onrender.com)
* 🔗 **Backend API (Django REST)**: [https://fossee-backend-deepali.onrender.com](https://fossee-backend-deepali.onrender.com)

> Both the Web and Desktop applications use the **same deployed backend API**.

---

## 📌 Project Overview

Users upload a CSV file containing chemical equipment parameters:

* Equipment Name
* Equipment Type
* Temperature
* Pressure
* Flowrate

The Django backend:

* Parses CSV using **Pandas**
* Stores last **5 datasets** in **SQLite**
* Provides **summary analytics APIs**
* Generates **PDF reports**
* Supports **authentication**

Both **Web** and **Desktop** frontends consume the same APIs and display:
tables, charts, summaries, history, and reports.

---

## 🧱 Technology Stack

| Layer            | Technology          | Purpose                   |
| ---------------- | ------------------- | ------------------------- |
| Backend          | Django + DRF        | API & data processing     |
| Data Analysis    | Pandas              | CSV analytics             |
| Database         | SQLite              | Store last 5 datasets     |
| Web Frontend     | React.js + Chart.js | Browser visualization     |
| Desktop Frontend | PyQt5 + Matplotlib  | Desktop visualization     |
| PDF Report       | ReportLab           | Generate analytics report |
| Version Control  | Git & GitHub        | Submission                |

---

## ✨ Key Features

* CSV Upload from Web and Desktop
* Summary statistics API
* Equipment type distribution chart
* Flowrate vs Temperature visualization
* Pressure trend chart
* Tabular data display
* Dataset history (last 5 uploads)
* PDF report generation
* Basic authentication system
* Refresh data without re-upload
* Single backend serving two frontends

---

## 🗂️ Project Structure

```
FOSSEE_INTERNSHIP/
│
├── backend/
├── web-frontend/
├── desktop-app/
├── Screenshots/
├── demo-video.mp4
├── sample_equipment_data.csv
└── README.md
```

---

## ⚙️ How to Run Locally (Development Setup)

### 🟢 Step 1 — Backend

```
cd backend
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Runs at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

### 🟢 Step 2 — Desktop App

```
cd desktop-app
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

---

### 🟢 Step 3 — Web App

```
cd web-frontend
npm install
npm run dev
```

Runs at: [http://localhost:5173/](http://localhost:5173/)

---

## 🔐 Demo Login Credentials

* **Username:** demo
* **Password:** democheck123

---

## 🧪 Sample CSV

Use:
`sample_equipment_data.csv`

Upload from Web or Desktop to test full functionality.

---

## 📊 Architecture 

This project follows a **Hybrid Architecture**:

```
           React Web App  ─┐
                           ├──> Django REST API (Render Deployed)
           PyQt5 Desktop ──┘
```

Both frontends consume the **same deployed API**, ensuring:

* Code reusability
* Consistent analytics
* Centralized data processing

---

## 📸 Screenshots

Available inside the `Screenshots/` folder.

---

## 🎥 Demo Video

Included as: `demo-video.mp4`

---

## 📄 PDF Report

Generated after CSV upload from both Web and Desktop interfaces.

---

## 👩‍💻 Developer

**Deepali Kumari**
