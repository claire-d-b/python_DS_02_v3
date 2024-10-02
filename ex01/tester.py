from aff_life import display
import sys
import os
# print(os.getcwd())  # This will print your current working directory
# Get the path to the parent directory (project_directory)

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from ex00 import load  # Using relative import

def main():
    print(display(load("../life_expectancy_years.csv")))
    # print(load("Wrong path"))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")