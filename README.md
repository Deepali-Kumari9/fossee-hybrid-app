# 🧪 Chemical Equipment Parameter Visualizer

### Hybrid Web + Desktop Application (Django + React + PyQt5)

This project is developed as part of the **FOSSEE Internship Screening Task**. It demonstrates a **hybrid architecture** where a single Django REST backend is consumed by both a React Web Application and a PyQt5 Desktop Application to perform data visualization and analytics for chemical equipment parameters.

---

## 📌 Project Overview

The system allows users to upload a CSV file containing chemical equipment data with the following columns:

* Equipment Name
* Equipment Type
* Temperature
* Pressure
* Flowrate

The Django backend processes the data using **Pandas**, stores recent datasets in **SQLite**, and exposes summary analytics via REST APIs. Both the Web and Desktop applications consume the same APIs to present tables, charts, summaries, dataset history, and PDF reports.

---

## 🧱 Technology Stack

| Layer            | Technology                     | Purpose                        |
| ---------------- | ------------------------------ | ------------------------------ |
| Backend          | Django + Django REST Framework | API and data processing        |
| Data Analysis    | Pandas                         | CSV parsing and analytics      |
| Database         | SQLite                         | Store last 5 uploaded datasets |
| Web Frontend     | React.js + Chart.js            | Visualization in browser       |
| Desktop Frontend | PyQt5 + Matplotlib             | Visualization in desktop       |
| PDF Generation   | ReportLab                      | Analytical report              |
| Version Control  | Git & GitHub                   | Project submission             |

---

## ✨ Features

* CSV upload from both Web and Desktop applications
* Summary statistics (total count, averages, equipment type distribution)
* Equipment Type Distribution chart
* Flowrate vs Temperature chart
* Pressure trend visualization
* Tabular data representation
* Dataset history (last 5 uploads stored in database)
* PDF report generation
* Basic authentication (login system)
* **Refresh Data button to reload latest dataset without re-uploading**
* Single Django backend serving two different frontends

---

## 📁 Project Structure

```
FOSSEE_INTERNSHIP/
│
├── backend/                     # Django REST API
├── web-frontend/                # React Web Application
├── desktop-app/                 # PyQt5 Desktop Application
├── Screenshots/                 # Output screenshots
├── demo-video.mp4               # Project demo video
├── sample_equipment_data.csv    # Sample CSV for testing
└── README.md
```

---

## ⚙️ How to Run the Project (Important Order)

> This project uses **two separate virtual environments**: one for backend and one for desktop app.

### 🟢 Step 1 — Run Backend Server

Open Terminal 1:

```
cd backend
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Backend runs at:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

### 🟢 Step 2 — Run Desktop Application

Open Terminal 2:

```
cd desktop-app
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

---

### 🟢 Step 3 — Run Web Application 

Open Terminal 3:

```
cd web-frontend
npm install
npm run dev
```

Web app runs at:
[http://localhost:5173/](http://localhost:5173/)

---

## 🔐 Demo Login Credentials

```
Username: demo
Password: democheck123
```

---

## 📊 Sample CSV for Testing

Use the file:

```
sample_equipment_data.csv
```

Upload this file from Web or Desktop to view analytics, charts, dataset history, and generate PDF report.

---

## 📸 Screenshots

All output screenshots of the project are available inside the **Screenshots/** folder.

---

## 🎥 Demo Video

A complete working demonstration of the project is provided in:

```
demo-video.mp4
```

---

## 📄 PDF Report

After uploading data, a PDF report containing summary statistics can be downloaded from both Web and Desktop interfaces.

---

## 👩‍💻 Developer

**Deepali Kumari**


