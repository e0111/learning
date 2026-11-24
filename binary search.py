myArray = [1, 2, 7, 12, 14, 19, 24, 77]
numInput = int(input("Enter the number to be found: "))
LBound = 0
UBound = int(len(myArray) -1)
found = False

while found == False and LBound <= UBound:
    mid = (LBound + UBound)//2
    if numInput == myArray[mid]:
        print("The number to be found is in index", mid)
        found = True
    elif numInput > myArray[mid]:
        LBound = mid +1
    else:
        UBound = mid -1
if found == False:
    print("Number not found.")
   


      
