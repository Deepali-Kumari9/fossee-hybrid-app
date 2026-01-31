import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QLineEdit,
    QTableWidget, QTableWidgetItem,
    QScrollArea, QFileDialog, QMessageBox
)
from PyQt5.QtCore import Qt

from api import (
    login, get_summary, get_equipment_list,
    upload_csv, download_pdf_report
)
from charts import PieChart, BarChart, LineChart


# ================= LOGIN WINDOW =================
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.resize(300, 200)

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Username"))
        self.username = QLineEdit()
        layout.addWidget(self.username)

        layout.addWidget(QLabel("Password"))
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password)

        btn = QPushButton("Login")
        btn.clicked.connect(self.handle_login)
        layout.addWidget(btn)

    def handle_login(self):
        if login(self.username.text(), self.password.text()):
            self.dashboard = Dashboard()
            self.dashboard.show()
            self.close()
        else:
            QMessageBox.critical(self, "Error", "Invalid credentials")


# ================= DASHBOARD =================
class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Equipment Parameter Visualizer")
        self.resize(1200, 800)

        root_layout = QVBoxLayout(self)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        root_layout.addWidget(scroll)

        self.content = QWidget()
        scroll.setWidget(self.content)

        self.layout = QVBoxLayout(self.content)
        self.layout.setSpacing(25)

        title = QLabel("Chemical Equipment Parameter Visualizer")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size:22px;font-weight:bold;")
        self.layout.addWidget(title)

        # Buttons
        btn_layout = QHBoxLayout()

        upload_btn = QPushButton("📂 Upload CSV")
        upload_btn.clicked.connect(self.upload_csv_file)

        refresh_btn = QPushButton("🔄 Refresh Data")
        refresh_btn.clicked.connect(self.load_data)

        pdf_btn = QPushButton("📄 Download PDF Report")
        pdf_btn.clicked.connect(self.handle_pdf_download)

        btn_layout.addWidget(upload_btn)
        btn_layout.addWidget(refresh_btn)
        btn_layout.addWidget(pdf_btn)
        btn_layout.addStretch()

        self.layout.addLayout(btn_layout)

        self.summary_label = QLabel()
        self.layout.addWidget(self.summary_label)

        self.charts_layout = QHBoxLayout()
        self.layout.addLayout(self.charts_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["Name", "Type", "Temperature", "Pressure", "Flowrate"]
        )
        self.layout.addWidget(self.table)

        footer = QLabel("Powered by Django REST API")
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("color: gray;")
        self.layout.addWidget(footer)

        self.load_data()

    # ================= LOAD DATA =================
    def load_data(self):
        equipment = get_equipment_list()
        summary = get_summary()

        if summary:
            self.populate_summary(summary)
        if equipment:
            self.populate_table(equipment)
            self.populate_charts(equipment)

    # ================= SUMMARY =================
    def populate_summary(self, s):
        text = (
            f"Total Equipment: {s['total_equipment']}   |   "
            f"Avg Temp: {s['average_temperature']}   |   "
            f"Avg Pressure: {s['average_pressure']}   |   "
            f"Avg Flowrate: {s['average_flowrate']}"
        )
        self.summary_label.setText(text)

    # ================= TABLE =================
    def populate_table(self, data):
        self.table.setRowCount(len(data))
        for row, eq in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(eq["name"]))
            self.table.setItem(row, 1, QTableWidgetItem(eq["type"]))
            self.table.setItem(row, 2, QTableWidgetItem(str(eq["temperature"])))
            self.table.setItem(row, 3, QTableWidgetItem(str(eq["pressure"])))
            self.table.setItem(row, 4, QTableWidgetItem(str(eq["flowrate"])))
        self.table.resizeColumnsToContents()

    # ================= CHARTS =================
    def populate_charts(self, data):
        for i in reversed(range(self.charts_layout.count())):
            self.charts_layout.itemAt(i).widget().setParent(None)

        type_count = {}
        temps, flows, pressures = [], [], []

        for eq in data:
            type_count[eq["type"]] = type_count.get(eq["type"], 0) + 1
            temps.append(eq["temperature"])
            flows.append(eq["flowrate"])
            pressures.append(eq["pressure"])

        self.charts_layout.addWidget(PieChart(type_count, "Equipment Type Distribution"))
        self.charts_layout.addWidget(BarChart(temps, flows))
        self.charts_layout.addWidget(LineChart(pressures))

    # ================= CSV UPLOAD =================
    def upload_csv_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select CSV File", "", "CSV Files (*.csv)"
        )

        if not file_path:
            return

        success = upload_csv(file_path)

        if success:
            QMessageBox.information(
                self,
                "Success",
                "CSV uploaded successfully to Django server 🚀"
            )
            self.load_data()
        else:
            QMessageBox.critical(
                self,
                "Error",
                "CSV upload failed. Check Django terminal for error."
            )

    # ================= PDF DOWNLOAD =================
    def handle_pdf_download(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save PDF Report", "equipment_report.pdf", "PDF Files (*.pdf)"
        )
        if file_path:
            success = download_pdf_report(file_path)
            if success:
                QMessageBox.information(self, "Success", "PDF downloaded successfully!")
            else:
                QMessageBox.critical(self, "Error", "Failed to download PDF report.")


# ================= RUN APP =================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
