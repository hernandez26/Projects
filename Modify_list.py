#CHANGING LIST VALUES

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0]= 'Harley-Davidson'
print(motorcycles)

#ADDING ELEMENTS TO A LIST

#APPENDING
car_brands=['toyota', 'honda', 'ford', 'mercedes-benz']
print(car_brands)
car_brands.append('bmw')
print(car_brands)
car_brands.append('hyundai')
print(car_brands)

fill_this= []
fill_this.append('I')
fill_this.append('am')
fill_this.append('filling')
fill_this.append('this')
fill_this.append('list')

print(fill_this)


#INSERTING
airlines=['American','Virgin','United','Spirit']
print(airlines)
airlines.insert(0,'Frontier')
print(airlines)
airlines.insert(3,'AeroMexico')
print(airlines)
print("-----------------------------------------------------------------------")

#REMOVING with del statement
print(airlines)
del airlines[2]
print(airlines)

del airlines[4]
print(airlines)
print('----------------------------------------------------------------------')

#REMOVING with pop() Method

countries = [ 'USA', 'DR', 'Mexico', 'Canada']
print(countries)
print('-----------------------')
popped_countries = countries.pop()
print(countries)
print(popped_countries)
print('------------------------------------------------------')
#Practice with pop method

bikes= ['Huffy','RoadMaster','Nishiki']
NewestBike= bikes.pop()
Bikestatement = f"My newest bike is a {NewestBike.upper()}!"
print(Bikestatement)

OldestBike= bikes.pop(0)
OBS = f"My oldest bike is a {OldestBike.lower()}"
print(OBS)

bikes= ['Huffy','RoadMaster','Nishiki'] # I had to re-add the list here because the element positions were changed above.
WalmartBike = bikes.pop(1)
walBike = f"The bike I bought at Walmart is the {WalmartBike.title()}."
print(walBike)

# USING REMOVE() method
colleges =['College of DuPage', 'Concordia University','Lincoln College of Technology','Lewis University']
print(f"The list of colleges I attended is {colleges}")

colleges.remove('Concordia University')
print(colleges)
print('-----------------------------------------------------------------------')

colleges2 =['College of DuPage', 'Concordia University','Lincoln College of Technology','Lewis University']
print(colleges2)
lameschool= 'Lincoln College of Technology'
colleges2.remove(lameschool)
print(colleges2)
print(f"the following school was lame... {lameschool}")