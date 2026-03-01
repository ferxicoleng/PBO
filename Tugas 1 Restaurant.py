class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a restaurant that serves {self.cuisine_type} food")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now")
restauant = Restaurant('HaiDiLao','Chinese')

print(f"The restaurant name is {restauant.restaurant_name}.")
print(f"This restaurant provides {restauant.cuisine_type} food.")
restauant.describe_restaurant()
restauant.open_restaurant()
print( )

a_restauant = Restaurant('Gapyeong','Korean')

print(f"The restaurant name is {a_restauant.restaurant_name}.")
print(f"This restaurant provides {a_restauant.cuisine_type} food.")
a_restauant.describe_restaurant()
a_restauant.open_restaurant()
print( )

restauant = Restaurant('Sushi Mentai','Japanese')

print(f"The restaurant name is {restauant.restaurant_name}.")
print(f"This restaurant provides {restauant.cuisine_type} food.")
restauant.describe_restaurant()
restauant.open_restaurant()
print( )

restauant = Restaurant('Sederhana','Padang')

print(f"The restaurant name is {restauant.restaurant_name}.")
print(f"This restaurant provides {restauant.cuisine_type} food.")
restauant.describe_restaurant()
restauant.open_restaurant()
print( )
