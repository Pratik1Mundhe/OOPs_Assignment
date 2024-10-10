class  Bike:
    def  __init__(self, model_name, acceleration):
        self.model_name = model_name
        self.acceleration = acceleration
        self.current_speed =  0
        self.color =  "black"

    def accelerate(self):
        self.current_speed += self.acceleration


def create_bike_object(model_name=None, acceleration=0):
	# Fill code here
	return Bike(model_name, acceleration)
	
def get_bike_object_color(bike_object):

# Fill code here
    return bike_object.color
	# return  "To fill get_bike_object_color code" # Change this

def get_bike_object_current_speed(bike_object):
	# Fill code here
    return bike_object.current_speed
	# return  "To fill get_bike_object_current_speed code" # Change this

def change_bike_color(bike_object, new_color):
	# Fill code here
    bike_object.color = new_color
    return bike_object.color
	# return  "To fill change_bike_color code" # Change this

def increase_bike_speed(bike_object):
	# Fill code here
    bike_object.accelerate()
    return bike_object.current_speed
	# return  "To fill increase_bike_speed code" # Change this


if  __name__  ==  '__main__':
    bike_object =  create_bike_object()
    print(bike_object)
    print(get_bike_object_color(bike_object))
    print(get_bike_object_current_speed(bike_object))
    print(change_bike_color(bike_object, "red"))
    print(increase_bike_speed(bike_object))
    print(get_bike_object_current_speed(bike_object))
