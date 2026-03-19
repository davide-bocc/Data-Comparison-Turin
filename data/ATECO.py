import os
import pandas as pd
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_ict_companies():
    # File ‘ATECO_J.csv’: list of active companies by ATECO code
    # Section J = ‘Information and communication services’ (ICT companies)
    # sep=‘;’ -> the CSV uses a semicolon as the separator (ISTAT standard)
    # encoding=‘utf-8-sig’ -> handles the BOM (Byte Order Mark) in ISTAT files
    try:
        df = pd.read_csv(
            os.path.join(BASE, 'file', 'ATECO_J.csv'),
            sep=';',
            encoding='utf-8-sig'
        )
    except FileNotFoundError:
        raise FileNotFoundError("File 'ATECO_J.csv' not found in the 'file' folder")
    except Exception as e:
        raise RuntimeError(f"Error while reading 'ATECO_J.csv': {e}")

    try:
        row = df[df['Settore Ateco 2007'] == 'J'].copy()

        if row.empty:
            raise ValueError("No rows found for ATECO section J — check the file content")

        date_cols = [col for col in row.columns if col not in ['Territorio', 'Settore Ateco 2007']]
        serie = row[date_cols].iloc[0]
        serie.index = pd.to_datetime(serie.index, format='%d/%m/%Y')
        serie = pd.to_numeric(serie, errors='coerce')
        return serie.groupby(serie.index.year).mean()

    except ValueError as e:
        raise
    except Exception as e:
        raise RuntimeError(f"Error while processing ICT companies data: {e}")

if __name__ == '__main__':
    serie = get_ict_companies()
    plt.figure(figsize=(14, 5))
    plt.plot(serie.index, serie.values, '-o', markersize=2, color='steelblue')
    plt.xlabel('Years')
    plt.ylabel('Active Companies')
    plt.title('Companies ATECO J (ICT) – Torino (2009–2025)')
    plt.tight_layout()
    plt.show()