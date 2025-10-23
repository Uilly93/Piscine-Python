from projection_life import display_graph
# import sys


def main():
    # if len(sys.argv) > 3:
    #     print("Too much arguments")
    #     return 1
    # c1 = sys.argv[1] if len(sys.argv) > 1 else "Belgium"
    # c2 = sys.argv[2] if len(sys.argv) > 2 else "France"
    try:
        display_graph(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv", "life_expectancy_years.csv")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
