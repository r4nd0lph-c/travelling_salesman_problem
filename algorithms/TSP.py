# Travelling Salesman Problem


from random import randint


def generate_problem(count: int, canvas_size: int = 1000) -> list[tuple[int]]:
    """..."""

    return [(randint(0, canvas_size), randint(0, canvas_size)) for _ in range(count)]


class TSP:
    """
    ...
    """

    def __init__(self) -> None:
        """..."""

        pass


if __name__ == "__main__":
    pass
