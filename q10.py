# Given a Paragraph of text, write a function to return the most frequently occuring word ignoring case. If multiple words have the same frequency, return them as a list

paragraph = "The Python language is great. Python is easy to learn. Python is really good and fun to learn"
# paragraph = paragraph.replace(".",'')
# paragraph = paragraph.lower()
# words_list = paragraph.split()

# ? OR
words_list = paragraph.replace(".",'').lower().split()

duplicates_frequency = {item: words_list.count(item) for item in words_list if words_list.count(item) > 1}
max_value = max(duplicates_frequency.values())
most_frequently_occured_words = [key for key, value in duplicates_frequency.items() if value == max_value]

print(most_frequently_occured_words)