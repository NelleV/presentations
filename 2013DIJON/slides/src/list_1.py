l = [1, 5, 2, 7, 1]
l.append(9)
print l       # [1, 1, 5, 2, 7, 9]
l.sort()
print l       # [1, 1, 2, 5, 7, 9]
a = l.pop()
print a, l    # 9 [1, 1, 2, 5, 7]
l.append("string")
print "length:", len(l)  # length: 6
