import pandas

# For full pandas documentation: [ https://pandas.pydata.org/docs/ ]


def main():
    get_version()
    loading_and_reading_data()
    sorting_and_describing_data()
    making_changes_to_data()
    filtering_data()
    conditional_changes_in_data()
    aggregate_statistics()


def get_version():
    print("pandas version: ", pandas.__version__)


def get_csv_data(file):
    data = pandas.read_csv(file)
    data = data.convert_dtypes()
    return data


# ||-------------------------------------------------------------------------------------------------------------------||

# PANDAS: data || machine learning
# pandas provide high performance, easy-to-use data structures and data analysis tools for Python.
# pandas allow you to work with a lot larger datasets (Big Data).

# ||-------------------------------------------------------------------------------------------------------------------||


def loading_and_reading_data():
    print("\n||-------------------------------------------LOADING----------------------------------------------||\n")

    # data_txt = pandas.read_csv('/Users/kamran/Projects/Machine_Learning_In_Python/Data/pokemon_data.txt', delimiter='\t')
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

    #  Reading specific indexes:
    print("Reading specific indexes:\n", data_xlsx.iloc[3])

    # Reading a specific location:
    print("Reading specific location:\n", data_xlsx.iloc[(2, 3)])

    print("\n||-----------------------------------------------------------------------------------------||\n")

    # Reading all data:
    for index, row in data_xlsx.iterrows():
        print(index, row['Name'])  # To print all 'Name' in data

    print("\n||-----------------------------------------------------------------------------------------||\n")

    # Reading all columns that are specific to something:
    # print(data_csv.loc[data_csv['Type 1'] == 'Fire'])  I do not know why this does not work.


def sorting_and_describing_data():
    print("\n||-------------------------------------------DESCRIBING----------------------------------------------||\n")

    # data_csv = get_csv_data('/Users/kamran/Projects/Machine_Learning_In_Python/Data/pokemon_data.csv')

    # print("Describing the data:\n", data_csv.describe())

    print("\n||-------------------------------------------SORTING----------------------------------------------||\n")

    # Sorting the data specifically:
    # print("Sorting values in the data:\n", data_csv.sort_values(['Name', 'Type 1', 'HP'], ascending=False))  # ascending=[1,0]


def making_changes_to_data():
    print("\n||-------------------------------------------CHANGING----------------------------------------------||\n")

    data_csv = get_csv_data('/Users/kamran/Projects/Machine_Learning_In_Python/Data/pokemon_data.csv')

    # Adding a column:
    data_csv['Total'] = data_csv['HP'] + data_csv['Attack'] + data_csv['Defense'] + data_csv['Sp. Atk'] + data_csv['Sp. Def'] + data_csv['Speed']
    # This can also be done like this:
    data_csv['Total'] = data_csv.iloc[:, 4:10].sum(axis=1)

    # for index, row in data_csv.iterrows():
    #     print(index, row['Total'], row['Name'])

    # Saving the data using teh saving_data function I created:
    saving_data(data_csv, 'new_pokemon.csv')

    print(data_csv.to_string())

    # Removing a column:
    data_csv = data_csv.drop(columns=['Total'])
    print(data_csv.to_string())


def saving_data(data, name_of_file):
    # Saving as csv:
    data.to_csv(name_of_file, index=False, sep=',')  # Separation would be \t if saving as .txt
    print("Saved data as csv")

    # Saving as Excel:
    data.to_excel('new_pokemon.xlsx', index=False)
    print("Saved data as Excel")


def filtering_data():
    print("\n||-------------------------------------------FILTERING----------------------------------------------||\n")

    data_csv = get_csv_data('/Users/kamran/Projects/Machine_Learning_In_Python/Data/pokemon_data.csv')

    print(data_csv.loc[data_csv['Type 1'] == 'Fire'])  # This will filter all the data and display only fire type pokemons.

    print(data_csv.loc[(data_csv['Type 1'] == 'Water') & (data_csv['Type 2'] == 'Poison')])  # This will filter and display all pokemons that are water type and poison type.

    # Filtering through strings:
    print(data_csv.loc[data_csv['Name'].str.contains('Mega')])

    print(data_csv.loc[~data_csv['Name'].str.contains('Mega')])  # The ~ acts as a 'not'

    # You can utilise regular expressions (import re) to filter elements in your data.


def conditional_changes_in_data():
    print("\n||-------------------------------------CONDITIONAL-CHANGES--------------------------------------------||\n")

    # data_csv = get_csv_data('/Users/kamran/Projects/Machine_Learning_In_Python/Data/pokemon_data.csv')
    #
    # data_csv.loc[data_csv['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'  # This will change Fire to Flamer in Type 1 of the data.
    #
    # data_csv.loc[data_csv['Total'] > 500, 'Legendary'] = True  # Conditions like this can be done too.


def aggregate_statistics():
    return


if __name__ == "__main__":
    main()
