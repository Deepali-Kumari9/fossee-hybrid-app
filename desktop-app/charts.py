from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


# ---------------- PIE CHART ----------------
class PieChart(FigureCanvas):
    def __init__(self, data, title):
        fig = Figure(figsize=(4, 4))
        ax = fig.add_subplot(111)

        ax.pie(
            data.values(),
            labels=data.keys(),
            autopct='%1.1f%%',
            startangle=140
        )
        ax.set_title(title)

        super().__init__(fig)


# ---------------- BAR CHART ----------------
class BarChart(FigureCanvas):
    def __init__(self, temperatures, flowrates):
        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)

        ax.bar(temperatures, flowrates)
        ax.set_xlabel("Temperature")
        ax.set_ylabel("Flowrate")
        ax.set_title("Flowrate vs Temperature")

        super().__init__(fig)


# ---------------- LINE CHART ----------------
class LineChart(FigureCanvas):
    def __init__(self, pressures):
        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot(111)

        ax.plot(range(len(pressures)), pressures, marker='o')
        ax.set_xlabel("Equipment Index")
        ax.set_ylabel("Pressure")
        ax.set_title("Average Pressure Trend")

        super().__init__(fig)
