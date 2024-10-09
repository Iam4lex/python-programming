
population = 30000

print("{0:20} {1}".format("Year", "Population"))

for year in range(2010, 2020):
    print("{0:<20d} {1: ,d}".format(year, round(population)))
    population += 0.03 * population