# Write a lambda function to filter out words from a given list that start with vowels.

list_of_words = ['Aron', 'Jessica', 'Oswald', 'Richie', 'Issac', 'Emily', 'Usman']

words_with_vowels = list(filter(lambda st: st[0].lower() in ('a', 'e', 'i', 'o', 'u'), list_of_words))

print(words_with_vowels)