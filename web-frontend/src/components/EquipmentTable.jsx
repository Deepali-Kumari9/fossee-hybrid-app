import { useEffect, useState } from "react";

export default function EquipmentTable({ token }) {
  const [equipment, setEquipment] = useState([]);

  useEffect(() => {
    if (!token) return;

    fetch("http://127.0.0.1:8000/api/equipment/", {
      headers: {
        Authorization: `Token ${token}`,
      },
    })
      .then((res) => res.json())
      .then((data) => {
        if (Array.isArray(data)) {
          setEquipment(data);
        } else if (Array.isArray(data.equipment)) {
          setEquipment(data.equipment);
        } else {
          setEquipment([]);
        }
      })
      .catch((err) => {
        console.error(err);
        setEquipment([]);
      });
  }, [token]);

  return (
    <div style={{ marginTop: "50px" }}>
      <h2>Equipment Table</h2>

      <table className="table"
        border="1"
        cellPadding="10"
        style={{ width: "100%", borderCollapse: "collapse" }}
      >
        <thead style={{ background: "#f2f2f2" }}>
          <tr>
            <th>Name</th>
            <th>Temperature</th>
            <th>Pressure</th>
            <th>Flowrate</th>
          </tr>
        </thead>

        <tbody>
          {equipment.length === 0 ? (
            <tr>
              <td colSpan="4" style={{ textAlign: "center" }}>
                No data available
              </td>
            </tr>
          ) : (
            equipment.map((item) => (
              <tr key={item.id}>
                <td>{item.name}</td>
                <td>{item.temperature}</td>
                <td>{item.pressure}</td>
                <td>{item.flowrate}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}
