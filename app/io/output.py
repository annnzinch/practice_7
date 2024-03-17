import os


def output_to_console(text):
    """Function to output text to the console.

    Args:
        text (str): The text to be outputted to the console.

    Returns:
        None
    """
    print("Output to console:")
    print(text)


def output_to_file(text, file_name):
    """Function to output text to a file using Python's built-in capabilities.

    Args:
        text (str): The text to be written to the file.
        file_name (str): The name of the file to write the text to.

    Returns:
        None
    """

    file_path = os.path.join("data", file_name)
    with open(file_path, 'w') as file:
        file.write(text)
    print(f"Text written to file '{file_name}' successfully.")
