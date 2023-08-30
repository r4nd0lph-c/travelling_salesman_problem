from TSP import generate_problem, TSP


def main() -> None:
    """..."""

    points = generate_problem(10)
    print(points)
    tsp = TSP(points=points, paths=None)


if __name__ == "__main__":
    main()
