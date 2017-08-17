from abc import ABC,abstractmethod

class Employee(ABC):
    @abstractmethod

    def calculate_salary(self,sal):

        pass

class Developer(Employee):

    def calculate_salary(self,sal):

        finalsalary = sal * 1.10
        return  finalsalary

    def position_1(self,position):
        self.position = position
        return  position
employee1 = Developer()
print(employee1.calculate_salary(10000 ))

print(employee1.position_1('Web Developer'))