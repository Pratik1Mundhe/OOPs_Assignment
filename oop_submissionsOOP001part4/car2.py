import math
class Car:
    is_engine_started = False
    current_speed = 0
    
    def __init__(self, max_speed,acceleration, tyre_friction,color="Red"):
        self.color = color
        if max_speed<0:
            raise ValueError("Invalid value for max_speed")
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction

    def start_engine(self):
        self.is_engine_started = True

    def accelerate(self):
        if self.current_speed+ self.acceleration <= self.max_speed:
            self.current_speed += self.acceleration
        else:
            self.current_speed = self.max_speed


    def apply_brakes(self):
        if self.current_speed - self.tyre_friction >= 0:
            self.current_speed -= self.tyre_friction
        else:
            self.current_speed = 0
    
    def sound_horn(self):
        if self.is_engine_started:
            print("Beep Beep")
        else:
            print("Start the engine to sound_horn")

    def stop_engine(self):
        self.is_engine_started = False



class Truck(Car):
    weight =0
    def __init__(self, max_speed,acceleration, tyre_friction,max_cargo_weight,color="Red"):
        self.max_cargo_weight = max_cargo_weight
        super().__init__(max_speed, acceleration, tyre_friction,color)

    def load(self,weight):
        if self.current_speed:
            print("Cannot load cargo during motion")
        elif weight<0:
            raise ValueError("Invalid value for weight")
        elif self.weight+ weight <= self.max_cargo_weight:
                self.weight += weight
        else:
            print("Cannot load cargo more than max limit: {}".format(self.max_cargo_weight))


    def unload(self,weight):
        if self.current_speed:
            print("Cannot load cargo during motion")
        elif weight<0:
            raise ValueError("Invalid value for weight")
        elif self.weight- weight >=0:
                self.weight -= weight
        else:
            self.weight = 0

    def sound_horn(self):
        print("Honk Honk")




class RaceCar(Car):
    nitro_points =0
    def __init__(self, max_speed, acceleration, tyre_friction, color="Red"):
        super().__init__(max_speed, acceleration, tyre_friction, color)

    def sound_horn(self):
        print("Peep Peep\nBeep Beep")

    def apply_brakes(self):
        
        if self.current_speed > self.max_speed/2:
            self.nitro_points += 10
        super().apply_brakes()
    
    def accelerate(self):
        super().accelerate()
        if self.nitro_points>0:
            self.nitro_points = max(0,self.nitro_points-10)
            if self.current_speed + math.ceil(0.3*self.acceleration) <= self.max_speed:
                self.current_speed += math.ceil(0.3*self.acceleration)

    