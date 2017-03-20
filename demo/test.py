

result = []
result.append(1)
flag2=1
flag3=1
flag5=1
count = 1
next2 = 2
next3 = 3
next5 = 5
i2 = i3 = i5 = 0

while count < 1500:
    current = min(next2, next3, next5)
    result.append(current)
    if current == next2:
        i2 += 1
        next2 = result[i2] * 2
    if current == next3:
        i3 += 1
        next3 = result[i3] * 3
    if current == next5:
        i5 += 1
        next5 = result[i5] * 5


    count += 1
print result.__len__()

print result[1499]


