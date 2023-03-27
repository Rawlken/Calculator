print('''----------------------------------------------------------------------------------
This Project Made By Halil Buğra Bayraktar.
Welcome To The Calculator!
----------------------------------------------------------------------------------''')
while True:
    number1 = float(input("Enter A Number: "))
    number2 = float(input("Enter A Number: "))
    transaction = input("For Addition (+) For Extraction (-) For Multiplication (*) For Partition (/) Enter: ")
    if (transaction == "+" ):
        total = number1 + number2
        print('Sum Of Two Numbers: ',total)
    elif (transaction == "-"):
        extraction = number1 - number2
        print("Difference Of Two Numbers: ",extraction)
    elif (transaction == "*"):
        multiplication = number1 * number2
        print("Multiplication Of Two Numbers: ",multiplication)
    elif (transaction == "/"):
        result = number1 / number2 
        print("Division Of Two Numbers: ",result)
    else:
        print("You Enter An Invalid Result")
        exit()
    print('''----------------------------------------------------------------------------------''')
