
def contient_voy (mot) :
    l = len(mot)
    print (l)
    i = 0    
    while (i < l) :
        if (mot[i] == "a" or mot[i] == "A" or mot[i] == "e" or mot[i] == "E" or mot[i] == "u" or mot[i] == "U" or mot[i] == "o" or mot[i] == "O" or mot[i] == "y"or mot[i] == "Y") :       
            return  True
        i = i + 1
print(contient_voy("hssn"))
