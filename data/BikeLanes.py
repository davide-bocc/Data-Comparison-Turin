import os
import pandas as pd

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_bike_lanes():
    try:
        df = pd.read_excel(
            os.path.join(BASE, 'file', 'Piste_ciclabili.xlsx'),
            sheet_name='A BILANESKM',
            header=None
        )
    except FileNotFoundError:
        raise FileNotFoundError("File ‘Piste_ciclabili.xlsx’ not found in the ‘file’ folder")
    except Exception as e:
        raise RuntimeError(f"Error while reading 'Piste_ciclabili.xlsx: {e}")

    try:
        anni   = df.iloc[4, 1:].tolist()   # Line 4 lists the years
        valori = df.iloc[6, 1:].tolist()   # Line 6 contains the values

        coppie = [(int(a), v) for a, v in zip(anni, valori) if pd.notna(a)]

        serie = pd.Series(
            [v for _, v in coppie],
            index=[a for a, _ in coppie]
        )
        serie.index = serie.index.astype(int)
        serie = pd.to_numeric(serie, errors='coerce')
        return serie.loc[2004:2023]

    except ValueError as e:
        raise
    except Exception as e:
        raise RuntimeError(f"Error while processing data on the length of bike lanes: {e}")

