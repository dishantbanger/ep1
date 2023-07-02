gym_equipments = ["dumbles","barbles","rop"]

for dumbles in gym_equipments:
    gym_equipments = input("type your choice")
    if gym_equipments == dumbles:
        print("it is the max weight u can lift")
    else:
        print("u can go with barbles")

    
for barbles in gym_equipments[1]:
    if barbles == 20:
        print("it is the max weight u can lift")
    else:
        print("u can go with rop")