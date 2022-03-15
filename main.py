from cars import Cars

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
  
  if _.seats == "": # <------ present exception
    _.seats = "null"
  print(_.color,_.seats) #<--- push command, w/ formatted exception
  if _.seats == "": # <--- separate if statement, which is considered AFTER previous command; not recursive
    print("NULL")

carlist = []
for _ in cars:
  carlist.append(_.model)

print(carlist) #<--- how to properly print list content with variables/objects; KIA is added because of line 47

colors = ["r","g","b","v"]
print(colors)