print("Maximum de trois entiers")
nb1 = input("Enter the first number : ")
nb2 = input("Enter the second number : ")
nb3 = input("Enter the third number : ")
max = 0
if (nb1 > nb2):
    max = nb1
else:
    max = nb2
if (max > nb3):
    max = max
else: 
    max = nb3
print("Le maximum est : ",max)