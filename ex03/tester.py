from projection_life import display
from load_csv import load


def main():
    display(load("../life_expectancy_years.csv"),
            load("../income_per_person_gdppercapita\
_ppp_inflation_adjusted.csv"))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
