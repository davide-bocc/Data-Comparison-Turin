# 🏙️ Torino – Urban Transformation Analysis

> A data-driven exploration of Turin's shift from an industrial city to a sustainable, tech-oriented metropolitan area.

![Torino Full-scale comparison](https://raw.githubusercontent.com/davide-bocc/Data-Comparison-Turin/main/docs/Figure_1.png)

---

## 📌 Overview

This project analyzes **four key urban indicators** for the city of Turin (Italy) over a ~15-year period, combining open public datasets to tell a coherent story about the city's ongoing transformation:

| Indicator | Source | Period |
|---|---|---|
| 🧍 Resident population | ISTAT / OpenData Torino | 2009–2023 |
| 💶 Average annual salary (employees) | ISTAT | 2009–2023 |
| 💻 ICT companies registered | ISTAT / ATECO J | 2009–2023 |
| 🚲 Bike lane network length (km) | OpenData Torino | 2009–2023 |

The central question: **Is Turin leaving its FIAT-era identity behind and reinventing itself as a tech and sustainability hub?**

---

## 📊 Output

The main visualization is a **multi-axis time series chart** that plots all four indicators on a shared timeline, each on its own scale, making trends and correlations immediately visible.

![Torino Full-scale comparison](https://raw.githubusercontent.com/davide-bocc/Data-Comparison-Turin/main/docs/Figure_1.png)

**Key findings:**

- 📉 **Population** has declined steadily (~890k → ~851k), consistent with post-industrial demographic shifts
- 💶 **Salaries** grew slowly until 2019, dropped sharply during COVID, then recovered — reflecting national trends
- 📈 **ICT companies** grew almost without interruption, signaling a structural shift toward the digital economy
- 🚲 **Bike lanes** nearly doubled (120 km → 250 km), accelerating after 2020 thanks to post-COVID urban mobility funding

---

## 🗂️ Project Structure

```
Data-Comparison-Turin/
│
├── main.py                  # Entry point — loads data, computes common years, renders chart
│
├── data/
│   ├── Population.py        # Population data loader
│   ├── Remuneration.py      # Salary data loader
│   ├── ATECO.py             # ICT companies data loader
│   └── BikeLanes.py         # Bike lane data loader
│
├── charts.py                # Plotting functions (single series + multi-axis normalized)
│
├── file/                    # Raw data files (Excel / CSV)
│   ├── Popolazione_residenti.xlsx
│   ├── Retribuzione.xlsx
│   ├── ATECO_J.csv
│   └── Piste_ciclabili.xlsx
│
├── output/                  # Generated charts (gitignored)
│
└── docs/
    └── Figure_1.png         # Exported chart
```

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/davide-bocc/Data-Comparison-Turin.git
cd Data-Comparison-Turin

# Create and activate a virtual environment (optional but recommended)
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python main.py
```

This will load all datasets, compute the intersection of available years, and display the multi-axis comparison chart.

---

## 📦 Requirements

```
pandas>=2.0
matplotlib>=3.7
openpyxl>=3.1
numpy>=1.24
```

Or install directly:

```bash
pip install pandas matplotlib openpyxl numpy
```

---

## 🧠 Skills Demonstrated

- **Real-world data wrangling** — heterogeneous sources (Excel, CSV), inconsistent headers, missing values, type mismatches
- **Multi-source data alignment** — computing year intersections across independently structured datasets
- **Data storytelling** — translating raw numbers into a coherent urban narrative
- **Custom visualization** — multi-axis matplotlib charts with independent scales and shared x-axis
- **Modular code design** — each data source isolated in its own loader module for maintainability

---

## 📁 Data Sources

- [ISTAT – Indicatori territoriali per le politiche di sviluppo](https://www.istat.it)
- [OpenData Torino – Piste ciclabili](https://esploradati.istat.it/databrowser/#/)
- [ISTAT – Registro Statistico delle Imprese Attive (ASIA)](https://www.istat.it)

> ⚠️ **Note:** The original dataset filenames have been renamed for clarity and consistency.
> Original filenames are preserved in the comments at the top of each loader in `/data/`.
---

## 🔭 Possible Extensions

- [ ] Add more cities for cross-comparison (Milano, Genova, Bologna)
- [ ] Include university enrollment data to quantify the student/tech ecosystem
- [ ] Add an interactive version using Plotly or Streamlit
- [ ] Automate data refresh via public APIs

---

## 📄 License

MIT — free to use, modify and distribute with attribution.

---

*Built with Python · Open data · Curiosity about cities*
