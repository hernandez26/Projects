dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# lets try to change one of the dimensions
# dimensions[0]= 250
#it is not possible because a tuple cannot be changed

newT = (300, 400, 200,500, 100)
for x in newT:
    print(f"This number is {x}")

print('--------------------------------------------------------------')

practice = ( 300, 500)
print("These are the Original 2 numbers in the Tuple: ")
for x in practice:
    print(x)

practice =( 1, 2)
print("\nthis is the new tuple with the same name:")
for x in practice:
    print(x)

# 4-13 TUPLE PRACTICE
Buffet = ("Lasagna","Mashed Potatoes","Corn","Chicken","Carrot Cake")
for x in Buffet:
    print(f"When I go to the buffet I eat {x}")

# Buffet[0]= "Pizza" Does not work
print("Last step_____________________________________________________________________________--")
print(f"This is the original menu: ")
for x in Buffet:
    print(x)


Buffet =("Tacos","Empanadas","Flautas","Burritos","Enchiladas")
print(f"This is the new buffet menu:")
for x in Buffet:
    print(x)


