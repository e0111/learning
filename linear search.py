## ok let's first brainstorm with things I already know 
numbers = [1, 21, 67, 3, 77]
numinput = int(input("Enter the number to be searched for:"))
i = 0
while i < len(numbers):
    if numinput == numbers[i]:
       print("The number you were searching for is in index", i)
       break
    else:
        i = i + 1
else:
    print("Number not found in the list.")


