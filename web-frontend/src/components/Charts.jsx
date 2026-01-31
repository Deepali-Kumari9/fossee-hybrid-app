import { Bar, Pie } from "react-chartjs-2";
import {
  Chart as ChartJS,
  BarElement,
  ArcElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  BarElement,
  ArcElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend
);

export default function Charts({ summary }) {
  if (!summary) return null;

  const values = [
    Number(summary.average_temperature),
    Number(summary.average_pressure),
    Number(summary.average_flowrate),
  ];

  const labels = ["Temperature", "Pressure", "Flowrate"];

  const barData = {
    labels: labels,
    datasets: [
      {
        label: "Average Values",
        data: values,
        backgroundColor: ["#4f46e5", "#16a34a", "#f97316"],
        borderRadius: 6,
      },
    ],
  };

  const pieData = {
    labels: labels,
    datasets: [
      {
        data: values,
        backgroundColor: ["#4f46e5", "#16a34a", "#f97316"],
        borderWidth: 1,
      },
    ],
  };

  const commonOptions = {
    responsive: true,
    maintainAspectRatio: false,
  };

  return (
    <div className="charts">
      <div className="chart-box">
        <h4>Bar Chart</h4>
        <div style={{ height: "300px" }}>
          <Bar data={barData} options={commonOptions} />
        </div>
      </div>

      <div className="chart-box">
        <h4>Pie Chart</h4>
        <div style={{ height: "300px" }}>
          <Pie data={pieData} options={commonOptions} />
        </div>
      </div>
    </div>
  );
}
