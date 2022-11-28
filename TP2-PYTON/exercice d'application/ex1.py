string = input("entrer un string : ")
s = [0,1,2,3,]
l = len(string)
i = 0
count = 0
while (i < l) :
    if (string[i] >= '0' and string[i] <= '9') :
        count = count + 1
    i = i + 1
print(count)
    