# Usage Examples


from TSP import generate_problem, TSP
from ACO import ACO


def main() -> None:
    """..."""

    points = generate_problem(50)
    aco = ACO(c=100, i=20, a=1.5, b=1.2, p=0.9, q=10)
    path = aco.run(points=points, name="ACO #1")
    paths = [path]
    TSP(points=points, paths=paths)


if __name__ == "__main__":
    main()
