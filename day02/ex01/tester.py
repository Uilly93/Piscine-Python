from aff_life import display_graph


def main():
    try:
        display_graph("life_expectancy_years.csv")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
