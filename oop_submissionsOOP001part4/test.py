from zoo6 import Deer
deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
print(deer.age_in_months)
# 1
print(deer.breed)
# "ELK"
print(deer.required_food_in_kgs)
# 10
deer.grow()
print(deer.required_food_in_kgs)
# 12
print(deer.age_in_months)
# 2
deer.make_sound() # Prints
# "Buck Buck"
deer.breathe() # Prints
# "Breathe in air"
deer = Deer(age_in_months=10, breed="ELK", required_food_in_kgs=10)
# ValueError: Invalid value for field age_in_months: 10