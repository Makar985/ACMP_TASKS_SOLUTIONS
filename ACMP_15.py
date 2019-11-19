n = int(input())
s = 0
a = [[] for i in range(n)]
for i in range(n):
    t = input().split()
    a[i].extend(t)
    s += t.count("1")
    
print(s // 2)