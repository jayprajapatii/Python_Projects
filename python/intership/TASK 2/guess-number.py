import random
Cno = random.randrange(1,101)
userInput = int(input("Enter Your Number: ---> "))
if userInput > Cno:
    print("Computer Number ==>",Cno)
    print("Your guess number is too high")
elif Cno > userInput:
    print("Computer Number==>",Cno)
    print("Your guess number is too low")
else:
    print("Computer Number==>",Cno)
    print("Your guess number is equal")