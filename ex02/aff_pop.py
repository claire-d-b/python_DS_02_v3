from matplotlib.pyplot import figure, plot, xlim, xticks, yticks, title, \
                              xlabel, ylabel, legend, tight_layout, savefig
from pandas import DataFrame


def convert_to_int(value):
    """Convert a string with a suffix like 'M' (million) or 'K' (thousand)
    to an integer"""
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


def get_line(df: DataFrame, keyword: str) -> tuple:
    """Search for two keyword in the entire DataFrame, then compare
    the two keywords (countries) data"""
    try:
        isinstance(df, DataFrame)
        # Search for a keyword in the entire DataFrame

        # lambda function sets all char to lowercase do we
        # talk about case-insensititvity then it searches for the
        # keyword in all lowercase words
        # axis=1 means "row-wise"
        # Finally, df[...] filters the rows where the condition is True.
        # In other words, it selects the rows where the keyword was found
        # in at least one of the columns.

        # To reindex a boolean Series so that it matches a DataFrame's
        # index, you can use the .reindex() method in pandas.
        # This method adjusts the index of the boolean Series to match the
        # DataFrame’s index, filling any missing values with False
        # (or another value of your choice) to ensure proper alignment.
        data_col = df[df.map(lambda x: keyword.lower() in str(x).lower())
                      .any(axis=0).reindex(df.index, fill_value=False)]
        data_row = df[df.map(lambda x: keyword.lower() in str(x).lower())
                      .any(axis=1)]

        vlist = []
        klist = []

        rows = data_row.values
        cols = data_col.values

        flat_rows = [item for sublist in rows for item in sublist][1:-1]
        flat_cols = [item for sublist in cols for item in sublist][1:-1]
        # flat_example= []
        # for sublist in rows:
        #     for item in sublist:
        #         flat_example.append(item)
        # flat_res = flat_example[1:-1]

        for i, row in enumerate(flat_rows):
            if i != len(flat_rows):
                vlist.insert(i, float(convert_to_int(row)))
        for i, col in enumerate(flat_cols):
            if i != len(flat_cols):
                klist.insert(i, float(convert_to_int(col)))

    except Exception as e:
        raise AssertionError(f"Error: {e}")

    return (klist, vlist)


def display(dataset: DataFrame, keyword_one: str, keyword_two: str) -> None:
    """Display custom figure"""
    figure(figsize=(8, 5))
    x_one, y_one = get_line(dataset, keyword_one)
    # print("xone", x_one[:-50])
    # print("yone", y_one[:-50])
    plot(x_one[:-50], y_one[:-50], label=keyword_one)
    x_two, y_two = get_line(dataset, keyword_two)
    plot(x_two[:-50], y_two[:-50], color='green', label=keyword_two)
    title('Population Total')
    xlabel('Year')
    ylabel('Population')
    xticks(range(1800, 2050, 40))
    xlim(1790, 2060)
    yticks([20000000, 40000000, 60000000], ['20M', '40M', '60M'])
    legend(loc='lower right')
    tight_layout()
    savefig('output', dpi=100)
