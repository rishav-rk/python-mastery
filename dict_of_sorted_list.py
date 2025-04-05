# Given a dictionary where each key maps to a list of numbers, sort each list in descending order

data = {
    "A": [3, 1, 4, 1, 5],
    "B": [10, 2, 8, 6],
    "C": [7, 3, 1, 9]
}

for i in data.values():
    i.sort(reverse=True)

print(data)