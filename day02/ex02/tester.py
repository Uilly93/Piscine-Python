from aff_pop import display_graph


def main():
    try:
        display_graph("population_total.csv")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
