from projection_life import display_graph
import sys


def main():
    if len(sys.argv) > 2:
        print("Too much arguments")
        return 1
    year = sys.argv[1] if len(sys.argv) > 1 else "1900"
    try:
        display_graph(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv",
            "life_expectancy_years.csv", year)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
