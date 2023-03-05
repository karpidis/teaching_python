# This program creates a list of different types and prints them
lista = [12, 15.0, "What did the Romans ever do for us", True,
         ["apple", "orange", "banana"], (1, 2, 3), {"name": "John", "age": 30}]

# iterate over the elements of the list and print each element and its data type
for x in lista:
    print(x)  # print the value of the element
    print(type(x))  # print the data type of the element
# Here we used a loop that we assign x with every item in the list and print them. We are not forced to use only one
# kind of variable type as it happens to other more strict programming languages as C, C++, Java etc
