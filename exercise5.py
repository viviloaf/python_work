#more variables and printing

my_name = 'Vinh Nguyen'
my_age = 21
my_height = (5*12)+11.5 #inches
my_weight = 250 #lbs
my_eyes = 'Brown'
my_teeth = 'Mostly white'
my_hair = 'Black'

my_height_m = my_height*0.0254
my_weight_kg = my_weight*0.45359237

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"That's {my_height_m} in meters.")
print(f"He's {my_weight} pounds heavy.")
print(f"That's {my_weight_kg} in kilos")

print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair")
print(f"His teeth are usually {my_teeth} depending on the coffee")

#this is supposedly a tricky line but i am ballzy
total = my_age + my_height + my_weight
print(f"if I add {my_age}, {my_height}, and {my_weight} I get {total}.")
