# Genetic Algorithm


from random import shuffle
from .utils.base import Base
from .utils.path import Path


class GA(Base):
    """
    ...
    """

    def __init__(self, population: int, iter: int) -> None:
        """..."""

        self.__population = population
        self.iter = iter

    def __create_individuals(self, l: int) -> list[list[int]]:
        """..."""

        base = list(range(l))
        individuals = []
        for _ in range(self.__population):
            shuffle(base)
            individuals.append(base + [base[0]])
        return individuals

    def run(self, points: list[tuple[int]], name: str = None) -> Path:
        """..."""

        l = len(points)
        individuals = self.__create_individuals(l)
        return Path(indx=[], leng=-1.0, name=name)


if __name__ == "__main__":
    pass
