a = input().split()
a[0] = int(a[0])
a[1] = int(a[1])
a[2] = int(a[2])
res = 0
if a[1] >= a[0] and a[1] >= a[2]:
    res = a[1]


elif a[2] >= a[0] and a[2] >= a[1]:
    res = a[2]


else:
    res = a[0]

print(res)