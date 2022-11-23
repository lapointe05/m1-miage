# Chaîne de caractères
t = "Bonjour! "
print(t)
print(isinstance(t,str))
# Nombre entier
n = 8
print(t,n)
print(isinstance(n,int))
# Nombre décimal
x = 20.5
print(t,x)
print(isinstance(x,float))
# Booléen
y = True
print(t,y)
print(isinstance(y,bool))

prenom = input("Votre prenom :")
age =""
while not(age.isdigit()) :
    age = input("Votre age:")
age = int(age)
print(prenom, isinstance(prenom, str))
print(age, isinstance(age, int))

x=""
y=""
while not(x.isdigit()) or not(y.isdigit()) :
    x = input("Saisissez un premier nombre entier : ")
    y = input("Saisissez un deuxième nombre entier : ")
print(f"{x} + {y} = ",int(x)+int(y))