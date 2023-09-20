# Ant Colony Optimization


from math import inf
from random import random, shuffle
from .utils.base import Base
from .utils.path import Path


class ACO(Base):
    """
    Ant Colony Optimization algorithm is introduced based on the foraging behavior of an ant
    for seeking a path between their colony and source food.\n
    -----
    `ants: int` THE NUMBER OF ANTS\n
    The total number of agents (ants) involved in one iteration.\n
    -----
    `iter: int` THE NUMBER OF ITERATIONS\n
    The maximum number of iterations of the algorithm.\n
    -----
    `a: float` INFORMATION ELICITATION FACTOR\n
    The information elicitation factor α, which represents the relative importance of the pheromone,
    reflects the importance of the accumulation of the pheromone with regard to the ants' path selection.\n
    -----
    `b: float` EXPECTED HEURISTIC FACTOR\n
    The expected heuristic factor β, which represents the relative importance of the visibility,
    reflects the importance of the heuristic information with regard to the ants' path selection.\n
    -----
    `p: float` PHEROMONE EVAPORATION COEFFICIENT\n
    The pheromone evaporation coefficient ρ, which represents the degree of pheromone evaporation,
    reflects the degree of mutual influence among ants. Generally, the value of  is [0, 1],
    which prevents the infinite accumulation of pheromone effectively.\n
    -----
    `q: float` PHEROMONE INTENSITY\n
    The pheromone intensity Q, which represents the total pheromone,
    affects the convergence speed of the alghoritm to a certain extent.\n
    """

    def __init__(self, ants: int, iter: int, a: float, b: float, p: float, q: float) -> None:
        """Initializes the hyperparameters for the algorithm."""

        self.ants = ants
        self.iter = iter
        self.a = a
        self.b = b
        self.p = p
        self.q = q

    @staticmethod
    def __select_i(selection: list[int]) -> int:
        """Selects a random index of the next 2D point."""

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
        """Creates a new ordering of 2D point indices based on the distance and pheromone."""

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

    def update_pm(self, pm: list[list[float]], tmp_indx: list[list[int]], tmp_leng: list[float]) -> None:
        """Updates the pheromone matrix."""

        l = len(pm)
        for i in range(l):
            for j in range(i, l):
                pm[i][j] *= 1 - self.p
                pm[j][i] *= 1 - self.p
        for i in range(self.ants):
            delta = self.q / tmp_leng[i]
            indx = tmp_indx[i]
            for j in range(l):
                pm[indx[j]][indx[j + 1]] += delta
                pm[indx[j + 1]][indx[j]] += delta

    def run(self, points: list[tuple[int]], name: str = None) -> Path:
        """Runs the algorithm for the given 2D points."""

        l = len(points)
        dm = ACO._distance_matrix(points)
        pm = [[1 for _ in range(l)] for _ in range(l)]
        res_indx = []
        res_leng = inf
        for _ in range(self.iter):
            tmp_indx = []
            tmp_leng = []
            for _ in range(self.ants):
                indx = self.__create_indx(dm, pm)
                tmp_indx.append(indx)
                tmp_leng.append(ACO._calculate_dist(dm, indx))
            self.update_pm(pm, tmp_indx, tmp_leng)
            best_leng = min(tmp_leng)
            if best_leng < res_leng:
                res_leng = best_leng
                res_indx = tmp_indx[tmp_leng.index(best_leng)]
        return Path(indx=res_indx, leng=res_leng, name=name)


if __name__ == "__main__":
    pass
