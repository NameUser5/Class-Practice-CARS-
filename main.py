from cars import Cars
from pricing import Prices

car1 = Cars("Toyota","Celica",2000,"Cherry Luxe","cloth")
car2 = Cars("Ford","Model T",1930,"British Racing Green","leather")
car3 = Cars("Rolls Royce","Wraith",2014,"Pearl","nubuck")
car4 = Cars("Kia","Stinger",2022,"Gray","")

cars = [car1,car2,car3]
colors = []

for _ in cars:
  print(_.color)

for _ in cars:
  colors.append(_.color)
  print(colors)

print(colors,car4.color)

car1.car_sounds()
car2.car_sounds()
car3.car_sounds()

full_list = []

# for _ in Cars():
#   full_list.append(_.make)
#   print(full_list)

car1.alt_year()
car2.alt_year()


alt3 = car3.alt_year()
print(alt3) ####

print(car1.axles)
print(car4.axles)
print(car2.axles,car4.color)
print(car4.seats,car1.color)
print([car4.seats,car1.color])

car4.color = "Blue"

print(car4.color,car4.axles)

cars.append(car4)

print(cars) # <---- prints location, NOT list; list has objects; it's an onion; a trunk containing buckets

for _ in cars:
  print(_.make,_.model)
  
  if _.seats == "": # <------ METHOD 1: present exception
    _.seats = "null"
  print(_.color,_.seats) #<--- push command, w/ formatted exception
  # if _.seats == "": # <--- METHOD 2: separate if statement, which is considered AFTER previous command; not recursive, overrides ALL printing in line 53
  #   print("NULL")

carlist = []
for _ in cars:
  carlist.append(_.model)

print(carlist) #<--- how to properly print list content with variables/objects; KIA is added because of line 47

colors = ["r","g","b","v"]
print(colors)

#base_price, mid_price = 0, deluxe_price = 0)

price1 = Prices(25000,32000,46000)
price2 = Prices(18000,35000,64000)
price3 = Prices(86000,96000,106000)
price4 = Prices(36000,45000,52000)

car1.base = price1.base_price
car1.mid = price1.mid_price
car1.deluxe = price1.deluxe_price

car2.base = price2.base_price
car2.mid = price2.mid_price
car2.deluxe = price2.deluxe_price

car3.base = price3.base_price
car3.mid = price3.mid_price
car3.deluxe = price3.deluxe_price

car4.base = price4.base_price
car4.mid = price4.mid_price
car4.deluxe = price4.deluxe_price

print(car1.base)
print(car4.deluxe)

import random



'''INDIE PROJECT: Mystery box -- random car, random build; ask user if they want one, for free

Tier 2: make the user "pay" for one. The more they pay, the higher the chances of getting a lux model -- raffle-type gambling :)

Tier 3: the more paid, the higher changes of getting lux make AND lux model, in color of choice

Tier 4: set probablity percentage for each make, model, color,and year; aggregate probability (like Terraria and other games)

Tier 5: complex probability--eg: some attributes are crap and will hurt your chances of getting a top tier car aka lower the more desirable probabilities. Like a slot machine, but worse.'''