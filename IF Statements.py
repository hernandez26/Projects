# Simple Example
cars= ['audi','bmw','subaru','toyota']

for x in cars:
    if x in cars == 'bmw':
        print(x.upper())
    else:
        print(x.title())


# Difference of equal signs
cool = "Jonathan"
if cool == "Jonathan":
    print(True)
else:
    print(False)

# Dealing with CASE
nickname = "Jman"

if nickname.lower()== "jman":
    print("True")
else:
    print("False")
print(nickname)

print("---------------------------------------------")
requested_toppings= "mushrooms"
if requested_toppings != "anchovies":
    print("Hold the anchovies!")
print("------------------------------------------------")
print("Checking for age")
age = 18
if age == 18:
    print(True)
else:
    print(False)

print("-----------------------------------------------")
answer = 17
if answer!= 42:
    print("That is not the correct answer. Please try again!")

print("----------------------------------------------------")
print("Using AND in IF Statement")
age1 = 25
age3 = 12

if age1 >= 21 and age3 >= 21:
    print(True)
else:
    print(False)

age2 = 24
age4= 22
if age2 >= 21 and age4 >= 21:
    print(True)
else:
    print(False)



print("----------------------------------")
print("Using OR in IF Statement")
orage0= 9
orage1 =5
if (orage0 >=7) or (orage1 >=7):
    print(True)
else:
    print(False)

if ( orage0 <= 4) or (orage1 <= 4):
    print(True)
else:
    print(False)

print("----------------------------------")
print("Using 'in' in IF Statement")

tops= ["pepperoni", "sausage", "cheese", "Sauce"]
if "cheese" in tops:
    print(True)
else:
    print(False)

if "pineapple" in tops:
    print(True)
else:
    print(False)

print("-------------------------------------------")
print("Using NOT in IF Statement")

banned = ["andrew", 'kiki', "davey", "benny"]
User= "Max"
User2 = "kiki"
if User not in banned:
    print(f"{User.upper()}, you are allowed to post!")
else:
    print(f"{User.lower()}, you are banned buddy!")

if User2 not in banned:
    print(f"{User2.upper()}, you are allowed to post!")
else:
    print(f"{User2.lower()}, you are banned buddy!")

print("------------------------------------")
print("Working with Boolean Expressions")
game_active = True
can_edit = False

print("\n\n")
print("---------------------------------------")
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

print("---------------------------------------------------------")
print("TOO YOUNG SCENERIO")
age = 17
if age >= 18:
    print("you are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("You are too young to vote!")
    print("Please register to vote as soon as you turn 18!")

print("---------------------------------------------------------")
print("Amusement park scenerio, IF-ELIF_ELSE practice")

age = 18
if age < 4:
    print("The price for you is $0")
elif 4 <= age < 18:
    print("the price for you is $25")
else:
    print("You are older than 17 so your price is $40")
print("-----------More Practice-----------------")
age = 12

if age < 4:
    price = 0
elif 4 <= age < 18:
    price = 25
else:
    price =40
print(f"Your admission price based on your age is ${price}.")

print("----------------------------------------------------------")
print("Multiple Elif scenerio practice")

age = 1

if age < 4:
    price = 0
elif 4 <= age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Based on your age, your admission price is ${price}.")

print("---------------------------------------------------------")
print("PRACTICE OMITTING THE ELSE AND USING ELIF INSTEAD")

age = 61
if age < 4:
    price = 0
elif 4 <= age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"The price is ${price} for you!")

print("----------------------------------------------------------")
print("PRACTICE USING MULTIPLE IF STATEMENTS")

customer_toppings = ['pepperoni','mushroom','sausage']
print("Requested Toppings...")
if 'cheese' in customer_toppings:
    print("-CHEESE")
if 'sausage' in customer_toppings:
    print("-SAUSAGE")
if 'mushroom' in customer_toppings:
    print("-MUSHROOM")
if 'pineapple' in customer_toppings:
    print("-PINEAPPLE")
if 'pepperoni' in customer_toppings:
    print('-PEPPERONI')

print("The Pizza is now complete!")

