### read mode
# reading file
file = open('situation.txt', 'r')
text = file.read()
print("1a)", text)
file.close()

# more efficient way: no need to manually close files
with open('situation.txt', 'r') as file:
     print('1b)', file.read())

# reading line
file = open('situation.txt', 'r')
print('2)', file.readline())
file.close()

### append mode
with open('situation.txt', 'a') as file:
     file.write("Adding a writing with this.\n")

# note: however many times (n) I run the code with lines 17 and 18 there,
# in the printed run output, there would be (n -1) appended lines after n runs,
# but in the actual file, n no. of that line would be added

### writing mode [overwrites stuff]
#with open('situation.txt', 'w') as file:
     #file.write("It's way past 23:00 now.")
# note: make 23, 24 non-comments to overwrite the whole file after trying out the previous stuff

















