def uperlower(str):
    l1=[]
    l2=[]
    for i in range(len(str)):
        if str[i].isupper():
            l1.append(str[i])
        else:
            l2.append(str[i])
    return l1,l2
def sortedd(str):
    l1=[]
    for i in range(len(str)):
        l1.append(str[i])
    for i in range(len(l1)):
        min=i
        for j in range(i,len(l1)):
            if l1[min]>=l1[j]:
                min=j
        tem=l1[i]
        l1[i]=l1[min]
        l1[min]=tem
    return l1
def trigen(str):
    l1,l2=uperlower(str)
    l=sortedd(''.join(l1))+sortedd(''.join(l2))
    return "".join(l)
print(trigen('Oussama'))