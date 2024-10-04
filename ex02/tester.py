from aff_pop import display
from load_csv import load


def main():
    display(load("../population_total.csv"), "Belgium", "France")
    # print(load("../population_total.csv"))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
