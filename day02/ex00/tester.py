from load_csv import load


def main():
    try:
        print(load("population_total.csv"))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
