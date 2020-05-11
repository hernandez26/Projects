#5.8 Hello Admin
print("\n 5.8 Hello Admin example-----------------------")
user_names= ['user', 'admin', 'boss','manager','employee','owner']


for x in user_names:
    if x is 'admin':
        print(f"Hello {x}, would you like to see a status report?")
    else:
        print(f"Hello {x}, Thank you for logging in again.")


#5.9 No Users
print("\n 5-9 No Users example--------------------------------------")
user_names= []

if user_names:
    for x in user_names:
        if x is 'Admin':
            print(f"Hello {x}, Welcome!")
        else:
            print(f"{x} Why are you logging in?")
else:
    print("This list is empty!")

#5.10 Checking Usernames
print("\n5-10 Checking Usernames example----------------------------------")
current_users = ['JMAN','jonny','Joshtraww','pitabear', 'moneymanAJ']
new_users = ['rudydj','takui','jman','rodose','joshtraww']
cu=[]
for x in current_users:
    cu.append(x.lower())
    cu.append(x.upper())
    cu.append(x.title())
#print(cu)

for x in new_users:
    if x in cu:
        print(f"The Username {x} is unavailable")
    else:
        print(f"Congrats! {x} is an available username!")


# 5.11 Ordinal Numbers
print("\nOrdinal Numbers Example----------------------------")
numbers = [1,2,3,4,5,6,7,8,9]

for x in numbers:
    if x is 1:
        print(f"\n{x}st")
    elif x is 2:
        print(f"\n{x}nd")
    elif x is 3:
        print(f"\n{x}rd")
    else:
        print(f"\n{x}th")

