#Calculator

if input() == str("new"):
    print("Options: \n  1. Addition \n  2. Subtraction \n  3. Multiplication \n  4. Division")
    option = int(input("Enter an Option: "))
    if option > 4:
        print("Error! Enter Valid Option")
        option = int(input("Option: "))
        print("Selected Option: ", option)
    if option == 1:
            number1 = float(input("Enter A Number: "))
            number2 = float(input("Enter Another Number: "))
            ans= float(number1 + number2)
            print("Ans: ", ans)
    if input() == str("save"):
        x = float(ans)
        number3 = float(input("Enter A Number: "))
        ans = float(x + number3)
        print(ans)
    if option == 2:
        number1 = float(input("Enter A Number: "))
        number2 = float(input("Enter Another Number: "))
        ans= float(number1 - number2)
        print("Ans: ", ans)
    if input() == str("save"):
        x = float(ans)
        number3 = float(input("Enter A Number: "))
        ans = float(x - number3)
        print(ans)
    if option == 3:
        number1 = float(input("Enter A Number: "))
        number2 = float(input("Enter Another Number: "))
        ans= float(number1 * number2)
        print("Ans: ", ans)
    if input() == str("save"):
        x = float(ans)
        number3 = float(input("Enter A Number: "))
        ans = float(x * number3)
        print(ans)
    if option == 4:
        number1 = float(input("Enter A Number: "))
        number2 = float(input("Enter Another Number: "))
        ans= float(number1 / number2)
        print("Ans: ", ans)
    if input() == str("save"):
        x = float(ans)
        number3 = float(input("Enter A Number: "))
        ans = float(x / number3)
        print(ans)



