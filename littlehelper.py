import re


def replace_timestamps_in_file(input_file, output_file):
    # Regular expression to match timestamps
    timestamp_pattern = r'\b\d{2}:\d{2}:\d{2}\.\d{3}\b'

    # Read the input file with UTF-8 encoding
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Replace timestamps with blanks
    cleaned_text = re.sub(timestamp_pattern, '', text)

    # Write the cleaned text to the output file with UTF-8 encoding
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)


# Example usage
input_file = 'input.txt'
output_file = 'output.txt'
replace_timestamps_in_file(input_file, output_file)

print(f"Timestamps have been removed and the cleaned text has been saved to {output_file}.")
