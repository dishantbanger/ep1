#variable
name = "dishant"
age = 25
print("my name is:",name)
print("my age is:",age)



x,y = "10","20"
print("x")
print(y)


#string
name = "Sandip Das"
print(type(name))
print(name)

#(tupple==cant change the value)
tuple = ("red","green","blue", 4, 5, 6,)
print(type(tuple))
print(tuple)
print(type(tuple[0]))
print("tuple[0] =", tuple[0])

#0 to 5 value togther
print(type(tuple[0:5]))
print("tuple[0;5] =",tuple[0:5])

#simplelist[3:]after3
print(tuple[3:])

 #list==can change the value
print("change value in list")
simpleList = ["red","green","blue", 4, 5, 6,]
simpleList[2]=3
print(simpleList)
print(type(simpleList))

#--get last value of item
print("get last value of item")
print(simpleList[-1])


#add new value tp list
#simpleList.insert("ram")
#print("new item added to list",simpleList)

simpleList2 = [1,2,2,3,3,3,4,4,4,4,5,5,5,5]
print(simpleList2)

#remove value.remove[5
simpleList.remove(5)
print("new item remove to list",simpleList)

#set
simpleset = {4,2,5,8,1}
print(type[simpleset])
print(simpleset)

for x in simpleset:
    print(x)



simpleset[0]=1
print(simpleset)

#adding and removing value

simpleset.add(10)
print(simpleset)
simpleset.remove(10)
print(simpleset)


#elimination duplicate

simpleset2 = {1,2,2,3,3,3,4,4,4,4,5,5,5,5}
print(simpleset2)

#set can use in mathematics operator
setA = {1,2,3,4,5}
setB = {6,7,8,9,0}
print(setA.union(setB))
print(setB.union(setA))

print(setA.intersection(setB))
print(setB.intersection(setA))

print(setA.difference(setB))
print(setB.difference(setA))

print(setA.symmetric_difference (setB))
print(setB.symmetric_difference(setA))
