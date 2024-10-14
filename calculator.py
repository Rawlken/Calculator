print('''----------------------------------------------------------------------------------
Welcome To The Calculator!
----------------------------------------------------------------------------------''')

while True:
    try:
        number1 = float(input("Enter A Number: "))
    except ValueError:
        print("You Enter An Invalid Result")
        print('''----------------------------------------------------------------------------------''')
        continue
    try:
        number2 = float(input("Enter A Number: "))
    except ValueError:
        print("You Enter An Invalid Result")
        print('''----------------------------------------------------------------------------------''')
        continue
    transaction = input("For Addition (+) For Extraction (-) For Multiplication (*) For Partition (/) Enter: ")

    if (transaction != "+" and transaction != "-" and transaction != "*" and transaction != "/"):
        print("You Enter An Invalid Result")
        
    else:
        if (transaction == "+" ):
            total = number1 + number2
            print('Sum Of Two Numbers: ', total)
        elif (transaction == "-"):
            extraction = number1 - number2
            print("Difference Of Two Numbers: ", extraction)
        elif (transaction == "*"):
            multiplication = number1 * number2
            print("Multiplication Of Two Numbers: ", multiplication)
        elif (transaction == "/"):
            if (number2 == 0):
                print("You Can't Divide By Zero")
                print('''----------------------------------------------------------------------------------''')
                continue
            result = number1 / number2 
            print("Division Of Two Numbers: ", result)
        else:
            print("You Enter An Invalid Result")
            exit()
    

    print('''----------------------------------------------------------------------------------''')
