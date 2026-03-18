import os
import pandas as pd

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_retribuzione():
    df = pd.read_excel(os.path.join(BASE, 'file', 'Retribuzione.xlsx'),
                       sheet_name='Indicatori_per_provincia_sesso')
    row = df[
        (df['DOMINIO'] == 'Benessere economico') &
        (df['INDICATORE'] == 'Retribuzione media annua dei lavoratori dipendenti') &
        (df['SESSO'] == 'Totale') &
        (df['TERRITORIO'] == 'Torino')
    ].copy()
    anni = [col for col in row.columns if col.startswith('V')]
    serie = row[anni].iloc[0]
    serie.index = [int(col.replace('V', '')) for col in serie.index]
    serie = serie.astype(str).str.replace(',', '.', regex=False)
    return pd.to_numeric(serie, errors='coerce')
