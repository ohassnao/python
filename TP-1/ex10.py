nb = int(input("Nombre max de lettres ? "))
i = 1
char = ""
string = ""
while(i <= nb and char != "stop") :
    char = input("Lettre : ")
    string = string + (char if char != "stop" else "")
    i += 1
print(string)