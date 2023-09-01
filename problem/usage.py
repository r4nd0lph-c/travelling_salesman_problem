# Usage Examples


from time import time
from TSP import generate_problem, TSP
from algorithms.ACO import ACO
from algorithms.GA import GA
from algorithms.SA import SA


def main() -> None:
    """..."""

    points = generate_problem(25)
    paths = []

    ts = time()
    aco = ACO(ants=100, iter=20, a=1.5, b=1.2, p=0.6, q=10)
    paths.append(aco.run(points=points, name="ACO"))
    print(f"ACO time: {time()-ts}")

    ts = time()
    ga = GA(population=1500, iter=40, s=0.2, m=0.5)
    paths.append(ga.run(points=points, name="GA"))
    print(f"GA time: {time()-ts}")

    # ts = time()
    # sa = SA()
    # paths.append(sa.run(points=points, name="SA"))
    # print(f"SA time: {time()-ts}")

    TSP(points=points, paths=paths)


if __name__ == "__main__":
    main()
