dataArray = [9, 1, 3, 4, 8, 2, 10, 11, 67, 7]

count = 0
swap = True
while swap:
    swap = False
    for i in range(len(dataArray) -1 -count):
        if dataArray[i] > dataArray[i+1]:
             temp = dataArray[i]
             dataArray[i] = dataArray[i+1]
             dataArray[i+1] = temp
             swap = True
    count += 1

print(dataArray)
