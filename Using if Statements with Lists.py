#Checkiing for Special items.

requested_toppings= ['cheese', 'pineapple', 'sausage', 'pepperoni', 'green pepper']

for x in requested_toppings:
    print(f"Adding {x}")

print("\nFinished making this Pizza!")


#Adding if statement to FOR LOOP for special situations
print("-------------------------------------------------------")

requested_toppings= ['mushroom','spinach','canadian bacon', 'extra cheese', 'bbq sauce']

for x in requested_toppings:
    if x is 'spinach':
        print('Sorry we are all out of Spinach right now.')
    else:
        print(f"Adding {x}")

print("\nFinished making this Pizza!")

#CHECKING THAT A LIST IS NOT EMPTY!
print("------------------------------------------------------------")
requested_toppings = []

if requested_toppings:
    for x in requested_toppings:
        print(f"Adding {x}.")
    print("\nFinished making your Pizza!")
else:
    print("Are you sure you want a plain pizza?")


# USING MULTIPLE LIST
print("----------------------------------------------------------")

available_toppings= ['cheese', 'pineapple','extra_cheese','pepperoni', 'sausage']
requested_toppings=['bbq sauce','canadian bacon','sausage']

for x in requested_toppings:
    if x in available_toppings:
        print(f"Adding {x}")
    else:
        print(f"Sorry we don't have {x}.")
print("\nFinished making your Pizza!")
