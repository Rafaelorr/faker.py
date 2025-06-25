# Define the input and output file paths
input_file_path = input("Input filename: ")
output_file_path = input("Output filename: ")

# Open the input file for reading
with open(input_file_path, 'r', encoding='utf-8') as infile:
    # Open the output file for writing
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        # Process each line in the input file
        for line in infile:
            # Strip leading/trailing whitespace
            line = line.strip()
            # Skip empty lines
            if not line:
                continue
            # Split the line at tab character
            parts = line.split('\t')
            if parts:
                street_name = parts[0]
                # Write the street name to the output file
                outfile.write(street_name + '\n')

print("File filter succesfully.")
