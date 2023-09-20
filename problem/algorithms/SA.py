# Simulated Annealing


# from math import exp
from numpy import exp
from random import sample, random
from .utils.base import Base
from .utils.path import Path


class SA(Base):
    """
    ...
    """

    def __init__(self, iter: int, t: int, g: float) -> None:
        """..."""

        self.iter = iter
        self.t = t
        self.g = g

    def __is_acceptable(self, prb_leng: float, tmp_leng: float) -> bool:
        """..."""

        prob = min(1, exp(-(prb_leng - tmp_leng) / self.t))
        if prob > random():
            return True
        return False

    def run(self, points: list[tuple[int]], name: str = None) -> Path:
        """..."""

        l = len(points)
        dm = SA._distance_matrix(points)
        tmp_indx = [i for i in range(l)] + [0]
        tmp_leng = SA._calculate_dist(dm, tmp_indx)
        res_indx = tmp_indx.copy()
        res_leng = tmp_leng
        for _ in range(self.iter):
            i, j = sample(range(1, l), 2)
            prb_indx = tmp_indx.copy()
            prb_indx[i], prb_indx[j] = prb_indx[j], prb_indx[i]
            prb_leng = SA._calculate_dist(dm, prb_indx)
            if self.__is_acceptable(prb_leng, tmp_leng):
                tmp_indx = prb_indx
                tmp_leng = prb_leng
            if tmp_leng < res_leng:
                res_indx = tmp_indx
                res_leng = tmp_leng
            self.t *= self.g
        return Path(indx=res_indx, leng=res_leng, name=name)


if __name__ == "__main__":
    pass
