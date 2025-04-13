f = input("Enter the file name you wish to open: ")

try:
    with open(f, 'r') as input_file:
        content = input_file.read()

        if not content.strip():
            print("Error: The input file is empty.")
        else:
            modified_content = content.upper()

            with open('output.txt', 'w') as output_file:
                output_file.write(modified_content)

            print(f"File processed successfully! {len(content)} characters were modified.")
except FileNotFoundError:
    print(f"Error: The file '{f}' was not found.")
except IOError as e:
    print(f"Error: An I/O error occurred while processing the file. Details: {e}")
