import pandas

# For full pandas documentation: [ https://pandas.pydata.org/docs/ ]


def main():
    get_version()


def get_version():
    print("pandas version: ", pandas.__version__)

# ||-------------------------------------------------------------------------------------------------------------------||

# PANDAS: data || machine learning
# pandas provide high performance, easy-to-use data structures and data analysis tools for Python.
# pandas allow you to work with a lot larger datasets (Big Data).

# ||-------------------------------------------------------------------------------------------------------------------||


def loading_data():

    data = pandas.read_csv('./Data/pokemon_data.csv')
    print("Data from CSV:\n", data)


if __name__ == "__main__":
    main()
