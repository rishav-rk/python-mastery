# Write a Python program that:
# 1. Reads a large textfile(large_data.txt)
# 2. Allows the user to specify a starting and ending position to extract text.
# 3. Uses seek() and tell() to navigate and retrieve content between these positions.

def extract_text_between_positions(file_path, start_pos, end_pos):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file.seek(0, 2)  # Move to the end to get total size
            file_size = file.tell()
            
            if start_pos < 0 or end_pos > file_size or start_pos > end_pos:
                print("Invalid positions. Please enter values between 0 and", file_size)
                return
            
            file.seek(start_pos)  # Move to the start position
            data = file.read(end_pos - start_pos)
            print("\nExtracted Text:\n")
            print(data)

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print("An error occurred:", e)

# Main program
if __name__ == "__main__":
    file_path = 'large_data.txt'
    
    try:
        start = int(input("Enter the starting position: "))
        end = int(input("Enter the ending position: "))
        extract_text_between_positions(file_path, start, end)
    except ValueError:
        print("Please enter valid integer values for positions.")

