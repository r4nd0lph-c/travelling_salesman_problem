# Usage Examples


from TSP import generate_problem, TSP
from ACO import ACO


def main() -> None:
    """..."""

    points = generate_problem(50)

    aco1 = ACO(c=100, i=20, a=1.5, b=1.2, p=0.6, q=10)
    path1 = aco1.run(points=points, name="ACO #1")

    paths = [path1]
    TSP(points=points, paths=paths)


if __name__ == "__main__":
    main()
