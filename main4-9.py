#Task 4...9
sizeList = 10
numbers = []
sumVal = sum_indEven = sumEven = sumMinMax = sumMinMaxInd = 0
maxVal = maxInd = minVal = minInd = 0

print("\nenter int value")
for i in range(sizeList):
    numbers.append(int(input("№{}:\t".format(i+1))))

print("\narray general:\t", numbers)

for i in range(sizeList):
    sumVal += numbers[i]

    if not i % 2:
        sum_indEven += i

    if not numbers[i] % 2:
        sumEven += numbers[i]

    if numbers[i] > numbers[maxInd]:
        maxVal = numbers[i]
        maxInd = i

    if numbers[i] < numbers[minInd]:
        minVal = numbers[i]
        minInd = i

if minInd > maxInd:
    temp = maxInd
    maxInd = minInd
    minInd = temp

for i in range(minInd+1, maxInd):
    sumMinMax += numbers[i]
    sumMinMaxInd += i

print("№4 sum of values Array = ", sumVal)
print("№5 sum of even Index = ", sum_indEven)
print("№6 sum of even Value = ", sumEven)
print("№7 min & max:\n\t\tmin = {},\tindexMin = {}\n\t\tmax = {},\tindexMax = {}".format(minVal, minInd, maxVal, maxInd))
print("№8 sum of min < Value < max = ", sumMinMax)
print("№9 sum of minInd < Value < maxInd = ", sumMinMaxInd)
