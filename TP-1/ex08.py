nb1 = int(input("Numero de debut : "))
nb2 = int(input("Numero de fin : "))
nb3 = int(input("Numero de z : "))
i = nb1
while (i < nb2) :
    print("z"*(nb3 + 1) + "igzag " , i)
    print(i + 1, "z"*(nb3 + 1) + "igzag")
    i += 2

