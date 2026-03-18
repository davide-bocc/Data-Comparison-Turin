import os
import pandas as pd
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_imprese_ict():
    df = pd.read_csv(os.path.join(BASE, 'file', 'ATECO_J.csv'), sep=';', encoding='utf-8-sig')
    row = df[df['Settore Ateco 2007'] == 'J'].copy()
    date_cols = [col for col in row.columns if col not in ['Territorio', 'Settore Ateco 2007']]
    serie = row[date_cols].iloc[0]
    serie.index = pd.to_datetime(serie.index, format='%d/%m/%Y')
    serie = pd.to_numeric(serie, errors='coerce')
    return serie.groupby(serie.index.year).mean()

if __name__ == '__main__':
    serie = get_imprese_ict()
    plt.figure(figsize=(14, 5))
    plt.plot(serie.index, serie.values, '-o', markersize=2, color='steelblue')
    plt.xlabel('Anno')
    plt.ylabel('Imprese attive')
    plt.title('Imprese ATECO J (ICT/Informatica) – Torino (2009–2025)')
    plt.tight_layout()
    plt.show()