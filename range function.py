for value in range(1, 5):
    print(value)
print("\n")
for x in range(1,6):
    print(x)

#Using range to make a list of Numbers
numbers = list(range(1,6))
print(numbers)

even_numbers =list(range(2,11,2))
print(even_numbers)
odd_numbers = list(range(1,10,2))
print(odd_numbers)

squares =[]
for x in range(1, 11):
    square = x ** 2
    squares.append(square)
print(squares)


# More Efficient way
squared =[]
for x in range(1,11):
    squared.append(x**2)
print(squared)

#min,max, sum

digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehensions

sq2 = [x**2 for x in range(11)]
print(sq2)

cubed= [x**3 for x in range(1,11)]
print(cubed)

times2 = [x*2 for x in range(11)]
print(times2)




