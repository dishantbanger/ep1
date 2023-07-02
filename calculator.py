num_1 = float(input("enter the num1 :"))
num_2 = float(input("enter the num2 :"))
choice = input("enter the operator +,-,*,/")
if choice == "+":
    sum = num_1 + num_2
    print ("sum of two number is :",sum)

if choice == "-":
    sum = num_1 - num_2
    print("sub of two number is :",sum)

if choice == "*":
    sum = num_1 * num_2
    print("mul of two number is :",sum)

if choice == "/":
    sum = num_1 / num_2
    print("div of two number is :",sum)

else:
    print("invalid choice")

