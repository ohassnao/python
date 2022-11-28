l = [1,2,3,4,5,6,7,8,9]
N = len(l) - 1
i = N
while i >= 0 :
    if l[i] % 2 == 0 :
        l.remove(l[i])
    i = i - 1
print(l)