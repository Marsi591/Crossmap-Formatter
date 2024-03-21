def format_text(text):
    parts = text.split(", ")
    formatted_parts = ", ".join(parts)
    return "{" + formatted_parts + "}"

def format_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        with open(output_file_path, 'w') as output_file:
            for line in input_file:
                user_input = line.strip()
                formatted_text = format_text(user_input)
                formatted_text = formatted_text[:-2] + formatted_text[-1]  # Removing the comma before the closing brace
                formatted_text_with_comma = formatted_text + ","
                output_file.write(formatted_text_with_comma + '\n')

# Change to Your Own Input and Output
input_file_path = "input.txt"
output_file_path = "output.txt"
format_file(input_file_path, output_file_path)
print("Formatted text has been written to", output_file_path)
