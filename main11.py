#Task 11
size = 10
ind = 0
numbers = []
nums_bool = []
count = 0

print("\nenter int value")
for i in range(size):
    numbers.append(int(input("№{}:\t".format(i+1))))
    nums_bool.append(numbers[i] % 2)
    if not nums_bool[i]:
        count += 1

print("\narray general:\t", numbers)
print("condition array \"BOOL\" based on array Up:\n\tTrue - even number\n\tFalse - odd number")
print("\narray \"BOOL\":\t", nums_bool)
print("qty of \"True\" = ", count)
