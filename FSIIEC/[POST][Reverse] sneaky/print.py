# Function to read a file and print its contents, replacing literal '\n' with new lines
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            # Replace literal \n strings with actual new lines
            content = content.replace('\\n', '\n')
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'sneaky.txt'  # Replace with your file path
read_file(file_path)
