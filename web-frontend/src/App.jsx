import { useEffect, useState } from "react";
import History from "./components/DatasetHistory";
import Charts from "./components/Charts";
import EquipmentTable from "./components/EquipmentTable";
import Login from "./Login";
import "./App.css";

function App() {
  const [summary, setSummary] = useState(null);
  const [file, setFile] = useState(null);
  const [token, setToken] = useState(localStorage.getItem("token"));

  // ================= FETCH SUMMARY =================
  const fetchSummary = async () => {
    if (!token) return;

    const res = await fetch("https://fossee-backend-deepali.onrender.com/api/summary/", {
      headers: { Authorization: `Token ${token}` },
    });

    const data = await res.json();
    setSummary(data);
  };

  useEffect(() => {
    fetchSummary();
  }, [token]);

  // ================= CSV UPLOAD  =================
  const handleUpload = async () => {
    if (!file) {
      alert("Please select a CSV file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("https://fossee-backend-deepali.onrender.com/api/upload/", {
        method: "POST",
        headers: {
          Authorization: `Token ${token}`,
        },
        body: formData,
      });

      if (response.ok) {
        alert("CSV uploaded successfully 🚀");
        fetchSummary();
      } else {
        const err = await response.text();
        alert("Upload failed: " + err);
      }
    } catch (error) {
      console.error(error);
    }
  };

  // ================= PDF DOWNLOAD =================
  const handleDownloadPDF = () => {
    fetch("https://fossee-backend-deepali.onrender.com/api/download-report/", {
      headers: { Authorization: `Token ${token}` },
    })
      .then((res) => res.blob())
      .then((blob) => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "Chemical_Equipment_Report.pdf";
        a.click();
      });
  };

  // ================= LOGOUT =================
  const handleLogout = () => {
    localStorage.removeItem("token");
    setToken(null);
  };

  // ================= LOGIN SCREEN =================
  if (!token) {
    return <Login setToken={setToken} />;
  }

  return (
    <div style={{ width: "100vw", minHeight: "100vh" }}>
      <div className="container">
        <div className="header">
          <h2>Chemical Equipment Parameter Visualizer</h2>
          <button className="button" onClick={handleLogout}>
            Logout
          </button>
        </div>

        <div className="section">
          <h3>📂 Upload CSV Dataset</h3>
          <input type="file" onChange={(e) => setFile(e.target.files[0])} />
          <br />
          <button className="button" onClick={handleUpload}>
            Upload CSV
          </button>
        </div>

        {summary && (
          <div className="section">
            <h3>📊 Summary Statistics</h3>
            <div className="summary-cards">
              <div className="card">Total Equipment<br />{summary.total_equipment}</div>
              <div className="card">Avg Temperature<br />{Number(summary.average_temperature).toFixed(2)}</div>
              <div className="card">Avg Pressure<br />{Number(summary.average_pressure).toFixed(2)}</div>
              <div className="card">Avg Flowrate<br />{Number(summary.average_flowrate).toFixed(2)}</div>
            </div>
          </div>
        )}

        <div className="section">
          <h3>📈 Visualization Charts</h3>
          <Charts summary={summary} />
        </div>

        <div className="section">
          <h3>🕒 Dataset History</h3>
          <History token={token} />
        </div>

        <div className="section">
          <h3>📋 Equipment Table</h3>
          <EquipmentTable token={token} />
        </div>

        <div className="section">
          <h3>📄 Generate PDF Report</h3>
          <button className="button" onClick={handleDownloadPDF}>
            Download PDF Report
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
