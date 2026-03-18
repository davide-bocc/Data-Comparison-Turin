import os
import pandas as pd

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_popolazione():
    df = pd.read_excel(os.path.join(BASE, 'file/Popolazione_residenti.xlsx'),
                       sheet_name='Tavola 1', header=9)
    df = df.rename(columns={df.columns[1]: 'Territorio'})
    row = df[df['Territorio'] == 'Torino'].copy()
    anni = [col for col in row.columns if str(col).startswith(('1', '2'))]
    serie = row[anni].iloc[0]
    serie.index = [int(str(a).replace('(p)', '').strip().split('.')[0]) for a in serie.index]
    return pd.to_numeric(serie, errors='coerce')