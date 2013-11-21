
# Let's find the 100th Fibonacci number
i = 0
j = 1
n = 0
while n < 100:
    n += 1
    temp = j
    j = i + j
    i = temp

print i
