#normal import
#import moduling_file
#moduling_file.personex("dishant")


#using alias
import moduling_file as mf
a = mf.personex["age"]
print(a)

#use dir() to get all varaible
import moduling_file
x = dir(moduling_file)
print(x)

