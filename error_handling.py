print("error handlig")
try:
    print(x)
except:

    print("x is not define")

#multipe error handling
print("multipe error handlig")
try:
    print("hi"+ 3)
except NameError:
    print("x is not define")
except:
    print("error")

# else error handling
print("multipe error handlig")
try:
    print(x)
except NameError:
    print("x is not define")
else:
    print("no error")

#finally error handling
print("multipe error handlig")
try:
    print(x)
except NameError:
    print("x is not define")
finally:
    print("no error")

#get type error
print("get error")
import sys
try:
    print(x)
except:
    print("error hai bhai")



