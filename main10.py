#Task 10
size = 10
ind = 0
numbers = []
nums_sum = []
nums2 = []
nums3 = []

print("\nenter int value")
for i in range(size):
    numbers.append(int(input("№{}:\t".format(i+1))))

print("\narray general:\t", numbers)

for i in range(int(size/2)-1):
    nums2.append(numbers[i]-numbers[i+1])
    nums3.append(numbers[i + int(size/2)]-numbers[i + 1 + int(size/2)])
    nums_sum.append(nums2[i] + nums3[i])

print()
print("array 1 (i - (i+1))\n\t\tbefore middle:\t", nums2)
print("array 2 (i - (i+1))\n\t\tafter middle:\t", nums3)
print("\nsum = arra1 + arra2:\t", nums_sum)
