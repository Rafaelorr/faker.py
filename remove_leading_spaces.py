def remove_leading_spaces(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Remove leading spaces from each line
    cleaned_lines = [line.lstrip() for line in lines]

    with open(output_file, 'w') as outfile:
        outfile.writelines(cleaned_lines)

    print(f"Leading spaces removed and saved to '{output_file}'.")


# Example usage
if __name__ == "__main__":
    input_path = input("Input filename: ")
    output_path = input("Output filename: ")
    remove_leading_spaces(input_path, output_path)
