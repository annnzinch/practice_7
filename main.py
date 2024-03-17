import app.io.input as io_input
import app.io.output as io_output


def main():
    # Input text from the console
    input_text = io_input.input_from_console()

    # Output text to the console
    io_output.output_to_console(input_text)

    # Input text from a file
    input_text_file = io_input.input_from_file()

    # Output text to a file using the pandas library
    io_output.output_to_file(input_text_file, "output_pandas.txt")

    file_path = r"C:\Users\zinch\PycharmProjects\python_practice_7\pandas_input_file.txt"
    # Input text from a file
    input_text_pandas = io_input.input_from_pandas(file_path)

    # Output text to the console
    io_output.output_to_console(input_text_pandas)


if __name__ == "__main__":
    main()
