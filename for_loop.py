#normal forloop
print("normal example")
colours = ("red","green","blue")
for x in colours:
    print(x)

#loop through str
str = "helloworld"
for x in str:
    print(x)

#break 
print("break example")
colours = ("red","green","blue")
for x in colours:
    if(x == "green"):
         break
    print(x)

#continous
print("continous example")
colours = ("red","green","blue")
for x in colours:
    if(x == "green"):
         continue
    print(x)

#else
print("else example")
colours = ("red","green","blue")
for x in colours:
    print(x) 
else:
    print("all items proceed")

#range function
print("range function ex")
for x in range(10):
    print(x)

         
      
