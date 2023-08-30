# Travelling Salesman Problem


from dataclasses import dataclass
from random import randint
from matplotlib import pyplot as plt


def generate_problem(count: int, canvas_size: int = 1000) -> list[tuple[int]]:
    """..."""

    return [(randint(0, canvas_size), randint(0, canvas_size)) for _ in range(count)]


@dataclass
class Path:
    """
    ...
    """

    indx: list[int]
    leng: float
    name: str


class TSP:
    """
    ...
    """

    def __init__(self, points: list[tuple[int]], paths: list[Path] = None) -> None:
        """..."""

        self.__points = points
        self.__paths = paths
        self.__fig, self.__ax = plt.subplots(num=f"Travelling Salesman Problem")
        self.__show()

    def get_points(self) -> list[tuple[int]]:
        """..."""

        return self.__points

    def get_paths(self) -> list[Path]:
        """..."""

        return self.__paths

    def __show(self) -> None:
        """..."""

        plt.show()


if __name__ == "__main__":
    pass
