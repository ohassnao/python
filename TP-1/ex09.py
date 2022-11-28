nb = int(input("n = "))
i = 1
fct = 1
if (nb < 0) :
    print("La factorielle n'est pas définie pour les nombres négatifs.")
elif (nb == 0) :
    print("La factorielle de 0 vaut 1 .")
else :
    while (i <= nb) :
        fct *= i
        i+=1
    print("La factorielle de" , nb, "vaut",fct ,".")