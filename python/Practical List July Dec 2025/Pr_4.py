import random
letters=['a','b','c','d','e','f','g','h',
         'i','j','k','l','m','n','o','p',
         'q','r','s','t','u','v','w','x',
         'y','z','A','B','C','D','E','F',
         'G','H','I','J','K','L','M','N',
         'O','P','Q','R','S','T','U','V',
         'W','X','Y','Z']
number=[0,1,2,3,4,5,6,7,8,9]
symbols=['!','#','$','%','&','*','@']
print("Welcome to Password Generator")
n_letters=input("How many letters you want in Pasword-> ")
n_number=int(input("How many letters you want in Pasword-> "))
n_symbols=input("How many letters you want in Pasword-> ")
password=""
for i in range(1,int(n_letters)+1):
    char=random.choice(letters)
    password+=char
for i in range(1,n_number+1):
    char=str(random.choice(number))
    password+=char
for i in range(1,int(n_symbols)+1):
    char=random.choice(symbols)
    password+=char


print(password)
