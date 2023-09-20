# Genetic Algorithm


from random import random, shuffle, sample
from .utils.base import Base
from .utils.path import Path


class GA(Base):
    """
    Genetic algorithm is a metaheuristic inspired by the process of natural selection
    that belongs to the larger class of evolutionary algorithms.\n
    -----
     `population: int` THE NUMBER OF INDIVIDUALS\n
    The total number of individuals involved in one iteration.\n
    -----
     `iter: int` THE NUMBER OF ITERATIONS\n
    The maximum number of iterations of the algorithm.\n
    -----
     `s: float` SELECTION COEFFICIENT\n
    Determines how many of the best individuals will make it to the next population.\n
    -----
     `m: float` MUTATION COEFFICIENT\n
    Determines how often individuals in a population mutate.\n
    """

    def __init__(self, population: int, iter: int, s: float, m: float) -> None:
        """Initializes the hyperparameters for the algorithm."""

        self.population = population
        self.iter = iter
        self.s = s
        self.m = m

    @staticmethod
    def __fitness_sort(dm: list[list[float]], individuals: list[list[int]]) -> None:
        """Sorts the individuals of a given population by fit."""

        individuals.sort(key=lambda i: GA._calculate_dist(dm, i))

    def __initialization(self, l: int) -> list[list[int]]:
        """Initializes the first population of individuals."""

        base = list(range(l))
        individuals = []
        for _ in range(self.population):
            shuffle(base)
            individuals.append(base + [base[0]])
        return individuals

    def __selection(self, individuals: list[list[int]]) -> None:
        """Selects the best individuals of a given population."""

        del individuals[int(self.population * self.s) :]

    def __crossover(self, individuals: list[list[int]]) -> None:
        """Crossbreeding some individuals of a given population."""

        childs = []
        w_size = len(individuals[0]) // 2
        for _ in range(len(individuals), self.population):
            p1, p2 = sample(individuals, 2)
            childs.append(
                p1[: w_size - 1]
                + [i for i in p2[:-1] if i not in p1[: w_size - 1]]
                + [p1[0]]
            )
        individuals += childs

    def __mutation(self, individuals: list[list[int]]) -> None:
        """Mutates some individuals of a given population."""

        sampling = list(range(1, len(individuals[0]) - 1))
        for item in individuals:
            if random() < self.m:
                i, j = sample(sampling, 2)
                item[i], item[j] = item[j], item[i]

    def run(self, points: list[tuple[int]], name: str = None) -> Path:
        """Runs the algorithm for the given 2D points."""

        l = len(points)
        dm = GA._distance_matrix(points)
        individuals = self.__initialization(l)
        for _ in range(self.iter):
            GA.__fitness_sort(dm, individuals)
            self.__selection(individuals)
            self.__crossover(individuals)
            self.__mutation(individuals)
        GA.__fitness_sort(dm, individuals)
        return Path(indx=individuals[0], leng=GA._calculate_dist(dm, individuals[0]), name=name)


if __name__ == "__main__":
    pass
