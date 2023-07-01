def function_name(name):
    print("hi "+name)

function_name("dishant")

def names(*names):
    print(names)
names("dishant ,"+"disha ,"+"papa ,"+"maa")

def sum(a,b):
    return a+b
sumvalue=sum(10,20)
print(sumvalue)

print("for loop")

things= ("car","bike","ven","cycle")
for x in things:
    if (x == "bike"):
        break
    
    print(x)

#if_else

#a = input("write first value")
#1
# b = input("write second value")

#if a>b:
#    print("a is big")
#elif a == b:
 #   print("barabar")
#else:
 #10
 #    print("b is big")

#import if_else
#if_else



numberInt = 25
numberFloat = 2.5

numNew = numberInt + numberFloat
print(numNew)
print("datatype of float",type(numNew))
#print(type(numberInt))



#practice for error handling
print("hello")
try:
    print(x)
except:
    print("error")