# Samuel Clackler
# Lab Section 11
# Submission Date: 11/12/24
# Sources:

import openpyxl

wb = openpyxl.load_workbook('prompt.txt')

print(type(wb))

for sheet in wb.prompt.txt:
    print(sheet,type(sheet), type(wb[sheet]))

print(wb.active)

# Open the input and output files
with open("prompt.txt", "r") as infile, open("out.txt", "w") as outfile:
    # Read each line in prompt.txt
    for line in infile:
        # Strip the line to remove any trailing newline characters
        line = line.strip()
        # Split the line by tabs to get each key-value pair
        pairs = line.split("\t")
        
        # Initialize an empty string to build the line
        output_line = ""
        
        # Process each key-value pair
        for pair in pairs:
            # Split each pair by the ':' to separate the key and value
            key, value = pair.split(":")
            # Convert the value to an integer
            count = int(value)
            
            # Add the appropriate character to the output_line based on the key
            if key == "w":
                output_line += " " * count  # Add 'count' number of spaces
            elif key == "*":
                output_line += "*" * count  # Add 'count' number of asterisks
        
        # Write the constructed line to out.txt, followed by a newline
        outfile.write(output_line + "\n")