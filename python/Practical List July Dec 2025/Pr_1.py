Internal_Python = int(input("Enter Python Internal Marks ->"))
Internal_PHP = int(input("Enter PHP Internal Marks ->"))
Internal_Mern = int(input("Enter Mern Internal Marks ->"))
Internal_DMM = int(input("Enter DMM Internal Marks ->"))
Internal_CDP1 = int(input("Enter CDP1 Internal Marks ->"))

External_Python = int(input("Enter Python External Marks ->"))
External_PHP = int(input("Enter PHP External Marks ->"))
External_Mern = int(input("Enter Mern External Marks ->"))
External_DMM = int(input("Enter DMM External Marks ->"))
External_CDP1 = int(input("Enter CDP1 External Marks ->"))
Result = True

if Internal_DMM < 16 or Internal_PHP < 16 or Internal_Mern < 16 or Internal_Python < 16 or Internal_CDP1 < 16:
    Result = False
    print("Student is fail in Internal Subject")
    exit()
if External_DMM < 24 or External_PHP < 24 or External_Python < 24 or External_Mern < 24 or External_CDP1 < 24:
    Result = False
    print("Student is fail in External Subject")
    exit()
Total_Internal_Marks = Internal_Mern + Internal_Python + Internal_PHP + Internal_DMM + Internal_CDP1
Total_External_Marks = External_Python + External_DMM + External_PHP + External_Mern + External_CDP1
Total_Marks = Total_External_Marks + Total_Internal_Marks
Percentage = round(Total_Marks / 5, 2)
if Percentage >= 70.0:
    Grade = "Distinction"
elif 70.0 >= Percentage >= 60.0:
    Grade = "First"
elif 60.0 >= Percentage >= 50.0:
    Grade = "Second"
else:
    Grade = "Pass"

print(f"The Result is {Grade} Grade with {Percentage} %, obtained total marks {Total_Marks} out of 500")
