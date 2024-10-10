from car2 import RaceCar


racecar = RaceCar(color="Red", max_speed=250, acceleration=50, tyre_friction=30)  
racecar.start_engine()  
racecar.accelerate()  
racecar.accelerate()  
racecar.accelerate()  
print(racecar.current_speed  )
# 150  
racecar.apply_brakes()  
print(racecar.current_speed  )
# 120  
print(racecar.nitro_points)  
# 10  
racecar.accelerate()  
print(racecar.current_speed  )
# 185 # 120 + 50 + (50 * 30 / 100)  
print(racecar.nitro_points  )
# 0  
# car.sound_horn() 