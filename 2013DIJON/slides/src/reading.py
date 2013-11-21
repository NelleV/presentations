my_file = open("alice.txt")
for i, line in enumerate(my_file):
    if i > 10:
        break
    print i, line
