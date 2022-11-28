string = input("entrer une phrase : ")
l = len(string)
i = 0
while (i < l) :
    if ((string[i] >= 'a' and string[i] <= 'z') or (string[i] >= 'A' and string[i] <= 'Z' or string[i] == " " )) :
        print(string[i], end="")
    i  = i + 1