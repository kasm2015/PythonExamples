'''ThIS IS FUNCTION TO ADD TWO NUMBERS'''
def add(num1,num2):
    #below is the line for doc string for the function
    """ this is a function to add two numbers """
    num3 =num1+num2
    return num3

result = add(10,30)
print("Addition of two numbers --> ",result)
#retrieve the doc string for the function
print(add.__doc__)

#THIS IS FUNCTION TO SUBSTRACT TWO NUMBERS
def sub(n1,n2):
    """ this is a function to substract two numbers """
    n3 = n1 - n2
    return n3

result  = sub(10,30)
print("Substraction of two numbers --> ",result)
print(sub.__doc__)