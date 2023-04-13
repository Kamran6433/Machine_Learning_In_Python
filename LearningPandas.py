import pandas

# For full pandas documentation: [ https://pandas.pydata.org/docs/ ]


def main():
    get_version()
    loading_and_reading_data()


def get_version():
    print("pandas version: ", pandas.__version__)

# ||-------------------------------------------------------------------------------------------------------------------||

# PANDAS: data || machine learning
# pandas provide high performance, easy-to-use data structures and data analysis tools for Python.
# pandas allow you to work with a lot larger datasets (Big Data).

# ||-------------------------------------------------------------------------------------------------------------------||


def loading_and_reading_data():
    print("\n||-------------------------------------------LOADING----------------------------------------------||\n")

    # data_txt = pandas.read_csv('/Users/kamran/Projects/Machine_Learning_In_Python/Data/pokemon_data.txt', delimiter='\t')
    # data_csv = pandas.read_csv('/Users/kamran/Projects/Machine_Learning_In_Python/Data/pokemon_data.csv')
    data_xlsx = pandas.read_excel('/Users/kamran/Projects/Machine_Learning_In_Python/Data/pokemon_data.xlsx')
    # print(data_txt.to_string())
    # print(data_csv.to_string())
    print("Excel data:\n", data_xlsx.to_string())  # Don't actually do this. This is only to display the data

    print("\n||-------------------------------------------READING----------------------------------------------||\n")

    # Reading the headers:
    headers_data_xlsx = data_xlsx.columns
    print("Headers of the data:\n", headers_data_xlsx)

    # Reading each column:
    print("Reading a specific column:\n", data_xlsx['Name'][0:5])  # This prints out the Name column and the indexes can be specified
    # print("Reading a specific column:\n", data_xlsx[['Name', 'Type 1', 'HP']][0:5])
    # print(data_xlsx.Name)  You can also do this


if __name__ == "__main__":
    main()
