class Rectangle:
    
   def __init__(self, length, breadth): 
       self.length = length
       self.breadth = breadth  
       # write your code here
        
   
   def calculate_area(self):
       # write your code here  
       return self.length * self.breadth
       
   def calculate_perimeter(self):
       # write your code here 
       return (self.length+ self.breadth)*2
      
if __name__ == "__main__":  
   rectangle_one = Rectangle(5, 5) 
   print("area of rectangle is ", rectangle_one.calculate_area()) 
   print("perimeter of rectangle is ",  rectangle_one.calculate_perimeter())  

