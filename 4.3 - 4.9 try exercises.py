#4.3 counting to twenty
twentynums= [x for x in range(1,21)]
print(twentynums)

viente = []
for x in range(1,21):
    viente.append(x)
print(viente)

# 4.4 one million
milli= [x for x in range(1,1000001)]
#print(milli)

#4.5 print min max and sum of million
print(min(milli))
print(max(milli))
print(sum(milli))

#4.6 odd numbers
odd = [x for x in range(1,10,2)]
print(odd)

oddlist = list(range(1,10,2))
print(oddlist)
#4.7 Threes
m3 =[x*3 for x in range(1,11)]
print(m3)

#4.8 cubes
cubed=[]
for x in range(1,11):
    cubed.append(x**3)
print(cubed)

#4.9 cubes LIST COMPREHENSION
cubes=[x**3 for x in range(1,11)]
print(cubes)



