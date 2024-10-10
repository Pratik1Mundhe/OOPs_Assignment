class Animal:
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        self.age_in_months = age_in_months
        self.breed = breed
        self.required_food_in_kgs = required_food_in_kgs
        

    def animal_make_sound(self, sound):
        print(sound)
    
    def animal_breath(self, place):
        print(f'Breath in {place}')

    def animal_grow(self, age_inc, food_inc):
        self.age_in_months += age_inc
        self.required_food_in_kgs += food_inc


class Deer(Animal):
    numDeer =0

    def __init__(self, age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months,breed, required_food_in_kgs)
        type(self).numDeer+=1
    def make_sound(self):
        self.animal_make_sound("Buck Buck")

    def grow(self):
        self.animal_grow(1,2)

    def breathe(self):
        self.animal_breath("air")


class Lion(Animal):
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months,breed, required_food_in_kgs)

    def make_sound(self):
        self.animal_make_sound("Roar")

    def grow(self):
        self.animal_grow(1,4)

    def breathe(self):
        self.animal_breath("air")

    def hunt(self):
        if Deer.numDeer >0:
            Deer.numDeer-=1
        else:
            print("No deer to hunt")

class Shark(Animal):
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months,breed, required_food_in_kgs)

    def make_sound(self):
        self.animal_make_sound("Roar")

    def grow(self):
        self.animal_grow(1,8)

    def breathe(self):
        self.animal_breath("air")






