from TSP import generate_problem, Path, TSP


def main() -> None:
    """..."""

    points = generate_problem(5)
    paths = [
        Path(indx=[0, 1, 2, 3, 4, 0], leng=128.0, name="Path #1"),
        Path(indx=[0, 2, 4, 1, 3, 0], leng=256.0, name="Path #2"),
    ]
    tsp = TSP(points=points, paths=paths)


if __name__ == "__main__":
    main()
