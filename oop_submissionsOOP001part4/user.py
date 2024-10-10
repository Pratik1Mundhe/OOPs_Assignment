class User:
    counter = 0
    def __init__(self, name):
        self.name = name
        type(self).counter += 1

    @classmethod
    def get_counter(cls):
        return cls.counter
    

user_object = User("New User")
print(user_object.get_counter())