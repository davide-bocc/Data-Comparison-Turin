import os
import pandas as pd

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_population():
    # Sheet ‘Table 1’: Data on the resident population of Turin
    # The first 9 lines are the header
    try:
        df = pd.read_excel(os.path.join(BASE, 'file/Popolazione_residenti.xlsx'),
                           sheet_name='Tavola 1', header=9)
        df = df.rename(columns={df.columns[1]: 'Territorio'})
    except FileNotFoundError:
        raise FileNotFoundError("File ‘Popolazione_residenti.xlsx’ not found in the ‘file’ folder")
    except Exception as e:
        raise RuntimeError(f"Error while reading 'Popolazione_residenti.xlsx: {e}")

    try:
        row = df[df['Territorio'] == 'Torino'].copy()
        anni = [col for col in row.columns if str(col).startswith(('1', '2'))]
        serie = row[anni].iloc[0]
        serie.index = [int(str(a).replace('(p)', '').strip().split('.')[0]) for a in serie.index]
        return pd.to_numeric(serie, errors='coerce')

    except ValueError as e:
        raise
    except Exception as e:
        raise RuntimeError(f"Error while processing resident data: {e}")