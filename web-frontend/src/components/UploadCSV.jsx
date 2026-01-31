import { useState } from "react";
import { uploadCSV } from "../services/api";

export default function UploadCSV({ refresh }) {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
  if (!file) {
    alert("Please select a CSV file");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  try {
    const res = await uploadCSV(formData);
    console.log("UPLOAD RESPONSE:", res.data);
    alert("CSV uploaded successfully 🚀");
    refresh();
  } catch (error) {
    console.error("UPLOAD ERROR:", error);
    alert("Upload failed ❌ (check console)");
  }
};


  return (
    <div style={{ marginBottom: 20 }}>
      <h3>Upload CSV</h3>
      <input
        type="file"
        accept=".csv"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <br /><br />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
}
