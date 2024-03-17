import pandas as pd


def input_from_console():
    """Function to input text from the console.

    Returns:
        str: The text inputted from the console.
    """
    return input("Enter text from console: ")


def input_from_file():
    """Function to read text from a file using Python's built-in capabilities.

    Returns:
        str: The text read from the file.
    """
    file_name = input("Enter the file name to read text from: ")
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found.")
        return None


def input_from_pandas(file_path):
    """Function to read text from a file using the pandas library.

    Args:
        file_path (str): The path to the input file.

    Returns:
        str: The text read from the file.
    """
    try:
        # Read the text file using pandas
        data_frame = pd.read_csv(file_path, sep="\n", header=None)
        # Convert DataFrame to string
        text = data_frame.to_string(header=False, index=False)
        return text
    except FileNotFoundError:
        print("File not found.")
        return None
