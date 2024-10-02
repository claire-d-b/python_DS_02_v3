from aff_pop import display
import sys
import os
# print(os.getcwd())  # This will print your current working directory
# Get the path to the parent directory (project_directory)

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from ex00 import load  # Using relative import

def main():

    display(load("../population_total.csv"), "Belgium", "France")
    # x2, y2 = get_line(load("../population_total.csv"), "Belgium")
    # display_graph(x1, y1, x2, y2, "France", "Belgium")
    # x2, y2 = get_line(load("../wrong_file.csv"), "France")
    # display_graph(x1, y1, x2, y2, "France", "Belgium")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")


