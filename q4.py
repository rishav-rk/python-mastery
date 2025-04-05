num_of_nested_lists = int(input("Count of nested list : "))
master_list = []

#? Nested list user input
for _ in range(num_of_nested_lists):
    nested_list_vars = input("Enter comma-separated values : ")
    nested_list = [int(item) for item in nested_list_vars.split(",")]
    master_list.append(nested_list)

for nlist in master_list:
    print(nlist)
    print("Maximum in above list : ", max(nlist))
    print("Minimum in above list : ", min(nlist))
    for i in range(len(nlist)):
        if(nlist[i] % 2 == 0):
            nlist[i] = "Even"


print(master_list)