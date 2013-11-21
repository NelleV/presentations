f = open("alice.txt", "r")
f.read() # reads all the file
l = f.readline() # Assigns to l the first line
l = f.readline() # Assings to l the second line

for l in f:
    print l

f.close()   # Always close the file after reading from it!
