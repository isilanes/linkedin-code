import collections
import random
import timeit


def generate_population(age: int, years: int, individuals: int) -> list[tuple[int, int]]:
    return [(b := random.randrange(0, years), b+age) for _ in range(individuals)]


def f1(population):
    living_per_year = {}
    for birth, death in population:
        for year in range(birth, death):
            if year in living_per_year:
                living_per_year[year] += 1
            else:
                living_per_year[year] = 1
    return living_per_year


def f2(population):
    return collections.Counter(
        year
        for birth, death in population
        for year in range(birth, death)
    )


if __name__ == "__main__":
    p = generate_population(age=250, years=10000, individuals=1000)

    assert f1(p) == f2(p)

    for fun in (f1, f2):
        t = timeit.Timer(lambda: fun(p))
        dt = t.timeit(10)/10  # seconds
        print(f"{fun.__name__}: {dt*1000:.1f} ms")
