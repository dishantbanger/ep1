persion =  {
"name": "dishant",
"age": 25,
"location": "ajmer"
}
#check the key is present or not
print('name' in persion) 
print(type(persion['name']))
print(type(persion['age']))
print(type(persion['location']))
print(persion["name"])
print(persion.get("location"))
#changed value
persion.update({"age":24})
print(persion["age"])

#adding value
persion["eye_colour"] = "blue"
print(persion)

#delete value
persion.pop("eye_colour")
print(persion)

#delete the last item
persion.popitem()
print(persion)

#delete particular key
del persion["age"]
print(persion)

#empty dic
persion.clear()
print(persion)

#practice exp.
persion = {
"job_role" : "devops",
"skills" : "linux ,python ,aws ,ansible ,docker ,jenkins ,kubernates",
"english" : "yes/no"
}

print("job_role,skills,english" in persion)
print("interview" in persion)
print(type[persion])
print(input("english"))
