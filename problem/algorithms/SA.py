# Simulated Annealing


from .utils.base import Base
from .utils.path import Path


class SA(Base):
    """
    ...
    """

    def __init__(self) -> None:
        """..."""

        pass

    def run(self, points: list[tuple[int]], name: str = None) -> Path:
        """..."""

        return Path(indx=[], leng=-1.0, name=name)


if __name__ == "__main__":
    pass
