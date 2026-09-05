alphabets = ["a", "b", "c", "d", "e"]

# printing the list
print("1)", alphabets)

# element at specific list
print("2)", alphabets[0])

# range of index
print("3)", alphabets[0:2])

# stepping through index
print("4)", alphabets[1::2])

# printing from backwards
print("5)", alphabets[::-1])

#using loop to print elements
for alphabet in alphabets:
    print("6)",alphabet)

# length of list
print("7)", len(alphabets))

# checking if list is in order
print("8)", "c" in alphabets)

# replacing element
alphabets[0] = "n"
print("9)",alphabets)

# appending to list
alphabets.append("t")
print("10)", alphabets)

# removing from list (from the end)
alphabets.remove("t")
print("11)", alphabets)

# inserting element at a specific index (does not replace the pre-existing element)
alphabets.insert(1, "s")
print("12)", alphabets)

# sorting the list in alphabetical order
alphabets.sort()
print("13)", alphabets)

# reversing the elements
alphabets.reverse()
print("14)", alphabets)

# index of a specific index
print("15)", alphabets.index("e"))

# count of a specific element
print("16)", alphabets.count("e"))

# clear list
alphabets.clear()
print("17)", alphabets)




