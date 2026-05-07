no = int(input("enter the number :=>"))
a, b = 0, 1

for i in range(no):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
