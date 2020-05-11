bicycles= ['Nishiki','Schwinn','trek','cannondale','redline','specialized']
print(bicycles)

#ACCESSING ELEMENTS IN A LIST
Cool_bikes =['Nishiki','Trek','Specialized','Cannondale']
print(Cool_bikes[0])

# FORMATTING ELEMENTS IN A LIST
format_these = ['Harley Davidson', 'honda', 'YAMAHA']
print(format_these[0].lower())
print(format_these[1].upper())
print(format_these[2].title())

# INDEX POSITIONS START AT 0 NOT 1

position_test = ['I am zero', 'I am one', 'I am two', 'I am three']
print(position_test[1])
print(position_test[3])
#Last position starts with -1
print(position_test[-1])
print(position_test[-3])

# YOU CAN USE F STRINGS WITH LISTS TOO
my_bikes = ['Nishiki','Huffy','RoadMaster']
Bike_story= f"The first bike I bought myself was a {my_bikes[1]}. But I ended up giving that {my_bikes[1]} to a homeless man. \nI then bought a {my_bikes[2]} from walmart but it was kind of crappy and i didnt use it. \nMy wife bought me new bike last year as a graduation present. It was a {my_bikes[0]}. This is the best bike I have ever had. I love riding my {my_bikes[0]}!"
print(Bike_story)