# Travelling Salesman Problem


from dataclasses import dataclass
from random import randint
from numpy import array
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D


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

    CLR_POINT = "#eb343a"
    CLR_PATH = [
        "#eb343a",
        "#db34eb",
        "#5b34eb",
        "#34b4eb",
        "#34eb4c",
        "#ebe534",
        "#eb9234",
    ]

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

    def __draw_points(self) -> None:
        """..."""

        self.__ax.scatter(
            *array(self.__points).T,
            zorder=1,
            color=TSP.CLR_POINT,
            label=f"Points ({len(self.__points)})",
        )
        for i, p in enumerate(self.__points):
            plt.annotate(
                i + 1,
                p,
                ha="center",
                textcoords="offset points",
                xytext=(0, 4),
                fontsize=8,
            )
            plt.annotate(
                f"({p[0]}; {p[1]})",
                p,
                ha="center",
                va="top",
                textcoords="offset points",
                xytext=(0, -4),
                fontsize=6,
            )

    def __draw_paths(self) -> list[Line2D]:
        """..."""

        lines = []
        if self.__paths:
            for i, path in enumerate(self.__paths):
                points = [self.__points[i] for i in path.indx]
                (l,) = plt.plot(
                    *array(points).T,
                    ls="--",
                    zorder=0,
                    color=TSP.CLR_PATH[i % len(TSP.CLR_PATH)],
                    label=f"{path.name} ({path.leng:.2f})",
                )
                lines.append(l)
        return lines

    def __show(self) -> None:
        """..."""

        self.__draw_points()
        self.__draw_paths()
        plt.show()


if __name__ == "__main__":
    pass
