# 4.10 Practice using slices
numeros =["uno","dos","tres","cuatro", "cinco","sies","siete","ocho","nueve","diez","once","doce"]
print(f"Here are the first 4 items of my list {numeros[0:4]}")
print(f'Here are the 4 items of my list found in the middle {numeros[4:8]}')
print(f"Here are the final four items found on my list {numeros[8:]}")

#4.11 Practice copying a list
print("\n")
my_sports= ["basketball","baseball","football","UFC"]
friends_sports= my_sports[:]
print(f"My favorite sports to watch are {my_sports}")
print(f"My friends favorite sports to watch are {friends_sports}")

my_sports.append("Boxing")
friends_sports.append("E-Sports")
print("\n")
print("The Following is an updated list of sport I like to watch...")
for x in my_sports:
    print(x)
print("\n")
print("the following is an updated list of the sports my friend watches...")
for x in friends_sports:
    print(x)

# 4.12 More Practice with For loops
print("\n")
pies = ["apple","cherry","pecan","blueberry"]

for x in pies:
    print(x.title())

for x in pies:
    print(x.upper())

print("\n")
shoebrands= ["nike","reebok","addidas","new balance", "puma"]

for x in shoebrands:
    print(x.title())
for x in shoebrands:
    print(x.upper())