import { useEffect, useState } from "react";

export default function DatasetHistory({ token }) {
  const [datasets, setDatasets] = useState([]);

  useEffect(() => {
    if (!token) return;

    fetch("http://127.0.0.1:8000/api/datasets/", {
      headers: {
        Authorization: `Token ${token}`,
      },
    })
      .then((res) => res.json())
      .then((data) => {
        setDatasets(data.datasets || []);
      })
      .catch((err) => console.error(err));
  }, [token]);

  return (
    <div>
      <h2>Dataset History (Last 5 uploads)</h2>

      {datasets.length === 0 ? (
        <p>No datasets uploaded yet</p>
      ) : (
        <ul>
          {datasets.map((ds) => (
            <li key={ds.id}>
              <b>{ds.name}</b> — {ds.equipment_count} rows —{" "}
              {new Date(ds.uploaded_at).toLocaleString()}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
