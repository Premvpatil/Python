# Python program that demonstrate file handling and string manipulation .this program read a text file, process the 
# content by performing string manipulation eg : converting text to uppercase, reverse the word and write modify
# content to new fie

# Function to read from the input file, process the content, and write to a new file
def process_file(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as input_file:
            lines = input_file.readlines()

        # Process each line
        modified_lines = []
        for line in lines:
            # Convert to uppercase and reverse each word
            processed_line = ' '.join(word[::-1].upper() for word in line.strip().split())
            modified_lines.append(processed_line)

        # Write modified content to the new file
        with open(output_file_path, 'w') as output_file:
            for modified_line in modified_lines:
                output_file.write(modified_line + '\n')

        print(f"Processed content written to {output_file_path}")

    except FileNotFoundError:
        print(f"The file {input_file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# File paths
input_file_path = 'input.txt'    # Change this to your input file path
output_file_path = 'output.txt'   # The output file where modified content will be saved

# Process the file
process_file(input_file_path, output_file_path)
