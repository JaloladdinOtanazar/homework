import itertools

txt = "LMaasleitbtui"
car_brands = ["Mazda", "Tesla", "BMW", "Audi", "Toyota", "Ford", "Honda", "Nissan", "Chevy", "Jeep"]
possible_cars = [car for car in car_brands if car.lower() in txt.lower()]
if possible_cars:
    print("possible cars are ", possible_cars)
else:
    print("Nothing found")