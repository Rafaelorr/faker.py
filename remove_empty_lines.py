# Specify the filename
filename = 'faker/lijsten/achternamen.py'

# Read the file and filter out empty lines
with open(filename, 'r') as file:
    lines = file.readlines()

# Remove empty lines (lines that are just whitespace)
non_empty_lines = [line for line in lines if line.strip() != '']

# Write the non-empty lines back to the file
with open(filename, 'w') as file:
    file.writelines(non_empty_lines)

print(f"Empty lines removed from {filename}.")
