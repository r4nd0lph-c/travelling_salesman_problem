# Ant Colony Optimization


from math import sqrt, inf
from random import random, shuffle
from TSP import Path


class ACO:
    """
    ...
    """

    def __init__(self, c: int, i: int, a: float, b: float, p: float, q: float) -> None:
        """..."""

        self.c = c
        self.i = i
        self.a = a
        self.b = b
        self.p = p
        self.q = q

    @staticmethod
    def __euclidean_dist(a: tuple[int], b: tuple[int]) -> float:
        """..."""

        return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    @staticmethod
    def __calc_dist(dm: list[list[float]], indx_order: list[int]) -> float:
        """..."""

        dist = 0
        for i in range(len(indx_order) - 1):
            dist += dm[indx_order[i]][indx_order[i + 1]]
        return dist

    @staticmethod
    def __select_i(selection: list[int]) -> int:
        """..."""

        sum_num = sum(selection)
        if sum_num == 0:
            return len(selection) - 1
        tmp_num = random()
        prob = 0
        for i in range(len(selection)):
            prob += selection[i] / sum_num
            if prob >= tmp_num:
                return i

    def __create_indx(self, dm: list[list[float]], pm: list[list[float]]) -> list[int]:
        """..."""

        l = len(dm)
        unvisited_indx = list(range(l))
        shuffle(unvisited_indx)
        visited_indx = [unvisited_indx.pop()]
        for _ in range(l - 1):
            i = visited_indx[-1]
            selection = []
            for j in unvisited_indx:
                selection.append(
                    (pm[i][j] ** self.a) * ((1 / max(dm[i][j], 10**-5)) ** self.b)
                )
            selected_i = ACO.__select_i(selection)
            visited_indx.append(unvisited_indx.pop(selected_i))
        visited_indx.append(visited_indx[0])
        return visited_indx

    def update_pm(
        self, pm: list[list[float]], tmp_indx: list[list[int]], tmp_leng: list[float]
    ) -> None:
        """..."""

        l = len(pm)
        for i in range(l):
            for j in range(i, l):
                pm[i][j] *= 1 - self.p
                pm[j][i] *= 1 - self.p
        for i in range(self.c):
            delta = self.q / tmp_leng[i]
            indx = tmp_indx[i]
            for j in range(l):
                pm[indx[j]][indx[j + 1]] += delta
                pm[indx[j + 1]][indx[j]] += delta

    def run(self, points: list[tuple[int]], name: str = None) -> Path:
        """..."""

        l = len(points)
        dm = [[ACO.__euclidean_dist(a, b) for b in points] for a in points]
        pm = [[1 for _ in range(l)] for _ in range(l)]
        res_indx = []
        res_leng = inf
        for _ in range(self.i):
            tmp_indx = []
            tmp_leng = []
            for _ in range(self.c):
                indx = self.__create_indx(dm, pm)
                tmp_indx.append(indx)
                tmp_leng.append(ACO.__calc_dist(dm, indx))
            self.update_pm(pm, tmp_indx, tmp_leng)
            best_leng = min(tmp_leng)
            if best_leng < res_leng:
                res_leng = best_leng
                res_indx = tmp_indx[tmp_leng.index(best_leng)]

        return Path(indx=res_indx, leng=res_leng, name=name)


if __name__ == "__main__":
    pass
