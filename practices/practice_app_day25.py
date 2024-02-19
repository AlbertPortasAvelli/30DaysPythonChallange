import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("File not found.")
        return None

def get_user_data():
    print("Enter data for DataFrame:")
    data = {}
    for column in ['id', 'title', 'url', 'num_points', 'num_comments', 'author', 'created_at']:
        data[column] = input(f"Enter {column}: ")
    df = pd.DataFrame(data)
    return df

def get_first_five_rows(df):
    return df.head()

def get_last_five_rows(df):
    return df.tail()

def get_title_column(df):
    return df['title']

def count_rows_columns(df):
    return df.shape

def filter_titles(df, keyword):
    return df[df['title'].str.contains(keyword, case=False)]

def explore_data(df):
    summary_statistics = df.describe()
    unique_authors = df['author'].unique()
    return summary_statistics, unique_authors

def main():
    while True:
        print("\nMenu:")
        print("1. Load data from CSV file")
        print("2. Input data manually")
        print("3. Get the first five rows")
        print("4. Get the last five rows")
        print("5. Get the title column")
        print("6. Count the number of rows and columns")
        print("7. Filter titles by keyword")
        print("8. Explore data")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            file_path = input("Enter the path to the CSV file: ")
            df = load_data(file_path)
        elif choice == '2':
            df = get_user_data()
        elif choice == '3':
            print(get_first_five_rows(df))
        elif choice == '4':
            print(get_last_five_rows(df))
        elif choice == '5':
            print(get_title_column(df))
        elif choice == '6':
            print("Number of rows and columns:", count_rows_columns(df))
        elif choice == '7':
            keyword = input("Enter keyword to filter titles: ")
            print(filter_titles(df, keyword))
        elif choice == '8':
            summary_statistics, unique_authors = explore_data(df)
            print("Summary Statistics:\n", summary_statistics)
            print("\nUnique Authors:\n", unique_authors)
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
