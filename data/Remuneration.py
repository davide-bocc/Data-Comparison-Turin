import os
import pandas as pd

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_remuneration():
    # ‘Indicatori_per_provincia_sesso’ (‘Indicators_by_province_and_gender’)
    # sheet: contains indicators for multiple domains,
    # territori e categorie (regions, and categories) — you must filter for the specific row of interest.
    # Select:
    #   DOMINIO (DOMAIN) -> ‘Economic well-being’ (excludes other domains such as education, health, etc.)
    #   INDICATORE (INDICATOR) -> average annual income (excludes other economic indicators)
    #   SESSO (GENDER) -> ‘Total’ (excludes data broken down by men/women)
    #   TERRITORIO (TERRITORY) -> ‘Turin’ (excludes other provinces)
    try:
        df = pd.read_excel(
            os.path.join(BASE, 'file', 'Retribuzione.xlsx'),
            sheet_name='Indicatori_per_provincia_sesso'
        )
    except FileNotFoundError:
        raise FileNotFoundError("File ‘Retribuzione.xlsx’ not found in the ‘file/’ folder'")
    except Exception as e:
        raise RuntimeError(f"Error while reading 'Retribuzione.xlsx'': {e}")

    try:
        row = df[
            (df['DOMINIO'] == 'Benessere economico') &
            (df['INDICATORE'] == 'Retribuzione media annua dei lavoratori dipendenti') &
            (df['SESSO'] == 'Totale') &
            (df['TERRITORIO'] == 'Torino')
            ].copy()

        if row.empty:
            raise ValueError("No rows found for Turin — check the filters or the file contents")

        anni = [col for col in row.columns if col.startswith('V')]
        serie = row[anni].iloc[0]
        serie.index = [int(col.replace('V', '')) for col in serie.index]
        serie = serie.astype(str).str.replace(',', '.', regex=False)
        return pd.to_numeric(serie, errors='coerce')

    except ValueError as e:
        raise
    except Exception as e:
        raise RuntimeError(f"Error while processing payroll data: {e}")
