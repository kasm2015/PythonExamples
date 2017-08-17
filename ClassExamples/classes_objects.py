#CLASS EXAMPLES
class example:
    #DECLARE VARIABLES
    x=20
    y=10

    # CREATING CONSTRUCTOR
    def __init__(self):
        print("Constructor gets invoked")
        self.x=45
        self.y=60
    #DEFINE A FUNCTION
    def func(self):
        print("i am in class example")

#CREATING OBJECTS FOR THE ABOVE CLASS
obj1=example()
obj2=example()

'''
you can not directly display class variables like below ( uncomment the below line and run the program)
you will get error --> NameError: name 'x' is not defined '''
#print(x)

print("Display Object1 properties")
print(obj1.x)

print("Display object2 properties")
print(obj2.y)

#CALLING FUNCTION THROUGH OBJECT INSTANCE
print(obj1.func())