no=int(input("enter the nu ber:=>"))
or_no=no

rev=0
while no>0:
    rem=no%10
    rev=(rev*10)+rem
    no=no//10
    
if or_no==rev:
    print(or_no,"is palidrom number")
else:
    print(or_no,"is not a palidrom")