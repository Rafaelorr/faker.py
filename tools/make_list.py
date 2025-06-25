# Define input and output file paths
input_file = input("Input filename: ")
output_file = input("Output filename: ")

# Read the lines from the input file
with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Process each line
modified_lines = []
for line in lines:
    # Remove trailing newline characters
    stripped_line = line.rstrip('\n')
    # Add quotes at start and end
    modified_line = f'"{stripped_line}"\n'
    modified_lines.append(modified_line)

# Write the modified lines to the output file
with open(output_file, 'w', encoding='utf-8') as file:
    file.writelines(modified_lines)

print(f"Processed {len(lines)} lines and saved to {output_file}")
