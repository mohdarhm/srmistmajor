import pandas as pd

def display_unique_values(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Display unique values for each column
    for column in df.columns:
        unique_values = df[column].unique()
        print(f"Column: {column}")
        for value in unique_values:
            print(value)
        print("")

if __name__ == "__main__":
    # Path to the CSV file
    csv_file = "C:\\Users\\mohda\\Desktop\\major project\\model\\survey.csv"

    # Call the function to display unique values
    display_unique_values(csv_file)
