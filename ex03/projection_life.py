from matplotlib.pyplot import tight_layout, subplots, savefig
from pandas import DataFrame


def convert_to_int(value):
    """ Convert a string with a suffix like 'M' (million) or 'K' (thousand) \
    to an integer. """
    if not value:
        return 0
    if isinstance(value, int):
        return value

    value = value.strip().upper()
    if value.endswith('M'):
        return int(float(value[:-1]) * 1000000)
    elif value.endswith('K'):
        return int(float(value[:-1]) * 1000)
    elif value.endswith('B'):
        return int(float(value[:-1]) * 1000000000)
    else:
        return int(float(value))


def get_values(df: DataFrame, keyword: str) -> list:

    """Search for a keyword in the entire DataFrame"""
    try:
        isinstance(df, DataFrame)

        # df.loc[:, index] means select all rows. index means select
        # the columns labeled as index.
        values = df.loc[:, int(convert_to_int(keyword) - 1800 + 1)]

    except Exception as e:
        raise AssertionError(f"Error: {e}")
    # print("values", values[1:])
    return list(values[1:])


def display(frame_x: DataFrame, frame_y: DataFrame) -> None:

    list_x = get_values(frame_x, '1900')
    list_y = get_values(frame_y, '1900')

    nlist_x = []
    nlist_y = []
    for i, x in enumerate(list_x):
        nlist_x.insert(i, convert_to_int(x))
    for j, y in enumerate(list_y):
        nlist_y.insert(j, convert_to_int(y))

    # print("list_y", nlist_y)
    # print("list_x", nlist_x)

    # Custom positions and labels for the x-axis
    x_positions = [300, 1000, 10000]
    x_labels = ['300', '1k', '10k']

    fig, ax = subplots()

    ax.scatter(nlist_y, nlist_x)

    # Set the x-axis to logarithmic scale
    ax.set_xscale('log')

    # Set custom ticks and labels for the x-axis
    ax.set_xticks(x_positions)
    ax.set_xticklabels(x_labels)
    ax.set_xlim(300, 11000)

    ax.set_yticks(range(20, 56, 5))
    ax.set_ylim(19, 56)

    # Customize the plot
    ax.set_title("1900")
    ax.set_xlabel("Gross Domestic product")
    ax.set_ylabel("Life Expectancy")

    # Display the plot
    tight_layout()
    savefig('output', dpi=100)
