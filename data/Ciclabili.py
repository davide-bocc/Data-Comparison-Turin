import os
import pandas as pd

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_piste_ciclabili():
    df = pd.read_excel(
        os.path.join(BASE, 'file', 'Piste_ciclabili.xlsx'),
        sheet_name='A BILANESKM',
        header=None
    )

    anni   = df.iloc[4, 1:].tolist()
    valori = df.iloc[6, 1:].tolist()

    coppie = [(int(a), v) for a, v in zip(anni, valori) if pd.notna(a)]

    serie = pd.Series(
        [v for _, v in coppie],
        index=[a for a, _ in coppie]
    )
    serie.index = serie.index.astype(int)
    serie = pd.to_numeric(serie, errors='coerce')
    return serie.loc[2004:2023]
