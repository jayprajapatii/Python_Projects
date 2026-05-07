import random

text=input("Enter name of friends separated by comma(,) ->")
friend_list=text.split(',')
random_choice=random.randrange(0,len(friend_list))
print(f"{friend_list[random_choice]} will deliver the sessio")