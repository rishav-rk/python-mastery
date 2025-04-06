# Write a Python program that:
# 1. Reads a large text file (data.txt) line by line using readline() to optimize memory usage.
# 2. Replaces all occurrences of a specific word with another word.
# 3. Writes the modified content to a new file (modified_data.txt)

with open("data.txt", "r") as readfile, open("modified_data.txt", "w") as writefile:
    file_size = readfile.seek(0,2)
    readfile.seek(0,0)

    to_replace = input("Enter the word to replace : ")
    to_replace_with = input("Enter the word to replace with : ")

    while readfile.tell() != file_size:
        line = readfile.readline()
        line = line.replace(to_replace, to_replace_with)
        writefile.write(line)

