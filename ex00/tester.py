from load_csv import load


def main():
    print(load("../life_expectancy_years.csv"))
    display(df, num_rows, num_cols)
    print(load("Wrong path"))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
