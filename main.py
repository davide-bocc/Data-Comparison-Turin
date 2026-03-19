from data.Remuneration import get_remuneration
from data.Population import get_population
from data.ATECO import get_ict_companies
from data.BikeLanes import get_bike_lanes
from charts import plot_singolo, plot_normalizzato

remuneration = get_remuneration()
population = get_population()
ict_companies = get_ict_companies()
bike_lanes = get_bike_lanes()

shared_years = sorted(set(remuneration.index) & set(population.index)
                      & set(ict_companies.index) & set(bike_lanes.index))

plot_normalizzato({
    'Population':    population.loc[shared_years],
    'Remuneration':  remuneration.loc[shared_years],
    'ICT companies': ict_companies.loc[shared_years],
    'Bike lanes':    bike_lanes.loc[shared_years]
})