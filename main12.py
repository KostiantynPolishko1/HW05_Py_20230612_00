#Task 12
size = 10
ind = 0
numbers = []
nums_pair = []
count = 0

print("\nenter int value")
for i in range(size):
    numbers.append(int(input("№{}:\t".format(i+1))))

print("\narray general:\t", numbers)

for i in range(size-1):
    if abs(numbers[i]-numbers[i+1]) == 1:
        count += 1
        nums_pair.append(str(numbers[i]) + " and " + str(numbers[i+1]))

print("qty of pairs in step = 1: ", count)
for i in range(count):
    print("pair №{}: ".format(i+1), end='')
    print(nums_pair[i])
