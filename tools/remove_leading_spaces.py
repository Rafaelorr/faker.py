"""This script removes the spaces in the begining of lines in the selected text file."""
def remove_leading_spaces(input_file, output_file):
    """This function removes the spaces in the begining of lines in a text file."""
    with open(input_file, 'r', encoding="utf-8") as input_file:
        lines = input_file.readlines()

    # Remove leading spaces from each line
    cleaned_lines = [line.lstrip() for line in lines]

    with open(output_file, 'w', encoding="utf-8") as outfile:
        outfile.writelines(cleaned_lines)

    print(f"Leading spaces removed and saved to '{output_file}'.")


# Example usage
if __name__ == "__main__":
    input_path = input("Input filename: ")
    output_path = input("Output filename: ")
    remove_leading_spaces(input_path, output_path)
