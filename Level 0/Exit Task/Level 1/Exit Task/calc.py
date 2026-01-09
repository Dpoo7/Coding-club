while True:
    print("\n==========Simple Calculator==========")
    print("1.ADDITION(+)")
    print("2.SUBSTRACTION(-)")
    print("3.MULTIPLICATION(*)")
    print("4.DIVISION(\)")
    print("5.EXIT")

    ch=input("\nEnter Choice between (1-4):")

    if ch in["1","2","3","4"]:
        n1=float(input("\nEnter Number 1:"))
        n2=float(input("Enter Number 2:"))

        if ch == "1":
            print("ANSWER:",n1+n2)

        elif ch == "2":
            print("ANSWER:",n1-n2)

        elif ch == "3":
            print("ANSWER:",n1*n2)

        elif ch == "4":
            if n2 != 0:
                print("ANSWER:",n1/n2)
            else:
                print("ERROR:")

        elif ch == "5":
            print("EXIT CALCULATOR")
            break

    else:
        print("ENTER NUMBER BETWEEN 1 TO 5")
