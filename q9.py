# Write a function that takes two dictionary with integer values and merges them. If a key a exists in both, its value should be the sum of the values from both dictionaries

def merge_dictionaries(dict_1, dict_2):
    merged_dict = dict_1.copy()

    for key, value in dict_2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value

    return merged_dict

dictionary_one = {
    'a' : 10,
    'b' : 20, 
    'c' : 30,
}
dictionary_two = {
    'b' : 15, 
    'c' : 25,
    'd' : 40
}

print(merge_dictionaries(dictionary_one, dictionary_two))