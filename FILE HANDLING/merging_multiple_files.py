# Write a program that:
# 1. Take multiple text files (file1.txt, file2.txt, file3.txt) as input.
# 2. Merges their content into a single output file (merged_output.txt)
# 3. Ensures that each file's content starts on a new line in the merged file.

# ! Following good practice using open() with with it ensures proper closing of file even if any error occurs
#  
def merge_files(file1, file2, file3):
    with open(file1, "r") as f1, open(file2, "r") as f2, open(file3, "r") as f3, open("merged_output.txt", "w") as output:
        content = f"{f1.read().strip()}\n{f2.read().strip()}\n{f3.read().strip()}"
        print(output.write(content), "characters are written to merged_output.txt file")
        


merge_files(input("file1 name: "), input("file2 name: "), input("file3 name: ") )