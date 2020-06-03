print("Choose your calculation operator")
print("1: ADDITION")
print("2: SUBTRACTION")
print("3: MULTIPLICATION")
print("4: DIVISION")

calculation = input()

if calculation == "1":
    value1=input("Enter first value: ")
    value2 = input("Enter second value: ")
    print("The sum is " + str(int(value1) + int(value2)))
elif calculation == "2":
    value1=input("Enter first value: ")
    value2 = input("Enter second value: ")
    print("The difference is " + str(int(value1) - int(value2)))
elif calculation == "3":
    value1 = input("Enter first value: ")
    value2 = input("Enter second value: ")
    print("The product is " + str(int(value1) * int(value2)))
elif calculation == "4":
    value1 = input("Enter first value: ")
    value2 = input("Enter second value: ")
    print("The results is " + str(int(value1) / int(value2)))
else:
    print ("Error Invalid inputs")