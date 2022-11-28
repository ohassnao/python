def der_conn (mot) :
    l = len(mot)
    print (l)
    i = -1    
    while (i >= -l ) :
        if (mot[i] != "a" and mot[i] != "i" and mot[i] != "I" and  mot[i] != "A" and mot[i] != "e" and mot[i] != "E" and mot[i] != "u" and mot[i] != "U" and mot[i] != "o" and mot[i] != "O" and mot[i] != "y" and mot[i] != "Y") :       
            return (mot[i],i + l)
        i = i - 1
print(der_conn("hassnaoui"))