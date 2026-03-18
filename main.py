from data.Retribuzione import get_retribuzione
from data.Popolazione import get_popolazione
from data.ATECO import get_imprese_ict
from data.Ciclabili import get_piste_ciclabili
from grafici import plot_singolo, plot_normalizzato

ret = get_retribuzione()
pop = get_popolazione()
ict = get_imprese_ict()
bike = get_piste_ciclabili()

anni_comuni = sorted(set(ret.index) & set(pop.index) & set(ict.index) & set(bike.index))

plot_normalizzato({
    'Population':  pop.loc[anni_comuni],
    'Remuneration': ret.loc[anni_comuni],
    'ICT companies':  ict.loc[anni_comuni],
    'Bike lanes': bike.loc[anni_comuni]
})