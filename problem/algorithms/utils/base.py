from math import sqrt


class Base:
    """
    The base class for path finding algorithms.
    Contains common functions.
    """

    @staticmethod
    def __euclidean_dist(a: tuple[int], b: tuple[int]) -> float:
        """Calculates the Euclidean distance between two 2D points."""

        return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    @staticmethod
    def _calculate_dist(dm: list[list[float]], indx: list[int]) -> float:
        """Calculates the path length based on the index list of the distance matrix."""

        dist = 0
        for i in range(len(indx) - 1):
            dist += dm[indx[i]][indx[i + 1]]
        return dist

    @staticmethod
    def _distance_matrix(points: list[tuple[int]]) -> list[list[float]]:
        """Calculates the distance matrix for the given 2D points."""

        return [[Base.__euclidean_dist(a, b) for b in points] for a in points]
