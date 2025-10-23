from aff_pop import display_graph
import sys


def main():
    if len(sys.argv) > 3:
        print("Too much arguments")
        return 1
    c1 = sys.argv[1] if len(sys.argv) > 1 else "Belgium"
    c2 = sys.argv[2] if len(sys.argv) > 2 else "France"
    try:
        display_graph("population_total.csv", c1, c2)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
