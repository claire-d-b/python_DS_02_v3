from pandas import DataFrame
from matplotlib.pyplot import figure, plot, title, xticks, savefig, \
     tight_layout
from torch.utils.data import Dataset


def display(df: DataFrame) -> Dataset:
    try:
        isinstance(df, DataFrame)
        # Search for a keyword in the entire DataFrame
        keyword = "France"

        # lambda function sets all char to lowercase do we talk about
        # case-insensititvity then it searches for the keyword in all
        # lowercase words
        # axis=1 means "row-wise"
        # Finally, df[...] filters the rows where the condition is True.
        # In other words, it selects the rows where the keyword was found
        # in at least one of the columns.

        # To reindex a boolean Series so that it matches a DataFrame's index,
        # you can use the .reindex() method in pandas. This method adjusts
        # the index of the boolean Series to match the DataFrame’s index,
        # filling any missing values with False (or another value of your
        # choice) to ensure proper alignment.
        data_col = df[df.map(lambda x: keyword.lower() in str(x).lower()).
                      any(axis=0).reindex(df.index, fill_value=False)]
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
                vlist.insert(i, float(row))
        for i, col in enumerate(flat_cols):
            if i != len(flat_cols):
                klist.insert(i, float(col))

        figure(figsize=(8, 5))
        # print("first list", klist) # years
        # print("second list", vlist) # life expectancy
        plot(klist, vlist)
        xticks(range(1800, 2100, 40))
        title('Life Expectancy Years')
        tight_layout()
        savefig('output', dpi=100)

    except AssertionError as e:
        print(f"An unexpected error occurred: {e}")

    return df
