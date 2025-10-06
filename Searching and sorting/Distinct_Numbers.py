n = int(input())
my_list = input().split() # Split the input string into a list of strings
unique_numbers = {}
for elem in my_list:
    if elem!=' ':
        int(elem)
        unique_numbers[elem]=1

print(len(unique_numbers))
