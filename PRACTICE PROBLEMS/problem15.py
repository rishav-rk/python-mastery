# Write a Python script to read content from a file called "data.txt", count the number of words and lines, and write this count in to a new file "summary.txt"

try:
    with open("data.txt", "r") as file, open("summary.txt", "w") as file_write:
        content = file.readlines()
        newlines = len(content)
        words = 0
        for line in content:
            word = len(line.split())
            words += word
        
        # writing data to file
        file_write.write(f"New Lines: {newlines}\nTotal Words: {words}")
        print("Check summary.txt file to see results")


except FileNotFoundError:
    print("File Not Found")