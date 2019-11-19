n = int(input())

all = list()


f = list()
t = list()

c = 0
nc = 0
res = ""



for i in range(1, n):
    if all[i] % 2 == 0:
        f += all[i]
        c += 1
    else:
        t += all[i]
        nc += 1

if c >= nc:
    res = "YES"
else:
    res = "NO"

print(t)
print(f)
print(res)
