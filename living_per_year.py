def f1(population):
    living_per_year = {}
    for birth, death in population:
        for year in range(birth, death):
            if year in living_per_year:
                living_per_year[year] += 1
            else:
                living_per_year[year] = 1
    return living_per_year


if __name__ == "__main__":
    p = [(1, 10)]
    print(f1(p))
