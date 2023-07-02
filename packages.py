import os
import shutil
#f.string= formating string
print(os.getcwd)
space = (shutil.disk_usage("/"))
print(space)
total , used, free =  (shutil.disk_usage("/"))

print ("total space is :" , total // (2**30))
print("used space is :", used // (2**30))
print("free space is :",free // (2**30))

#f.string= formating string
print (f"total space is : {total // (2**30)} gb")

