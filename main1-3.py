#Task 1
numbers = [1, 2, 3, 4, 5]

print("\tList: ", end='')
for i in numbers:
    print(i, " ", end='')

#Task 2
numbers2 = []

print("\n\nenter number of list")
for i in range(0, 5):
    numbers2.append(int(input("\t№{}: ".format(i+1))))
print("List 2: ", numbers2)

#Task 3
numbers3 = []
sizeList = abs(int(input("\nenter size of list: ")))

print("enter number of list")
for i in range(sizeList):
    numbers3.append(int(input("\t№{}: ".format(i+1))))
print("List 3: ", numbers3)

