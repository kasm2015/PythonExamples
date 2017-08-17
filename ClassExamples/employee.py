#CLASS EXAMPLES
class employee(object):
    #DEFINE FUNCTION
    def __init__(self,name,salary,age):
        self.name = name
        self.salary = salary
        self.age = age

x = employee('Syed','10000','18')
print(x.name)
print(x.salary)
print(x.age)