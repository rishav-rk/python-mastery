user_input = input("Enter comman-separated string : ")
print("\nEntered string : ", user_input)
words_list = [word.lower() for word in user_input.split(",") if len(word) >= 4]

updated_list = ','.join(words_list)

print(updated_list)