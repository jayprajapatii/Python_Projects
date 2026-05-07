no=int(input("enter the number:=>"))
for i in range(2,no):
    if no % i == 0:
        print(no,"is not a prime number")
        break
else:
    print(no,"is a prime number")
        
    