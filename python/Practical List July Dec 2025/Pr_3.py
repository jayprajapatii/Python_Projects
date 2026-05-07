heights=input("Enter all heights seperated by a space==>")
heights_list=heights.split()
count=0
for heights in heights_list:
    count+=1
for i in range (count):
    heights_list[i]=int(heights_list[i])
total=0
for person in heights_list:
    total+=person
avg=total/count
print(round(avg,2))
