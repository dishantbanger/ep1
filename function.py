#define function 
def my_first_function():
    print("hello function")

#calling
my_first_function() 

#define funcion with single parameter
def function(name):
    print("hi " + name)
function("dishant")

def fullname(first_name, last_name):
    print("hi "+ first_name + last_name)
fullname("dishant ","banger")

#arbitary argumenet
def colours(*colours):
    print("the  second colour is "+ colours[2])

colours("red ","green ","yellow ","blue ")   

#arbitary argumenet are not sure how much **
def name_colours(**colours):
    print("the  second name colour is "+ colours["green"])
name_colours(red = "red colour ",green = "green clour ",yellow = "yellow color ") 

#return statement
def sum(a,b):
    return a+b
sumvalue = sum(5,5)
print("the sum is ",sumvalue)
print("the sum is ",type(sumvalue))
