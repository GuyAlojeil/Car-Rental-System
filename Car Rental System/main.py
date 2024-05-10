from carRental import Data , carRent
from time import sleep
import os

boss = {"Guy" : 2324 , "Ted" : 5056 , "Yara" : 6086 , "Charbel" : 9324}

def clear():
    os.system("cls")

def permission():
    clear()
    try:
        password = int(input("Enter the 4 digits passwrod : "))
        name = list(boss.values())
        sleep(1)
        if password in name:
            print("\nWelcome back " , list(boss.keys())[list(boss.values()).index(password)], " !")
            print(""" 
                    ==== Car Rental Shop ====
                1. open database
                2. number of cars
                """) 
            choice = int(input("Enter the number you want to explore : "))
            sleep(2)
            if choice == 1:
                print("\n\t\t\t==== Client Database ====\n")
                Data().showClient()
                input("press enter to return to the main page ")
                clear()
                main()
            elif choice == 2:
                print("The number of cars available is : ",Data().getCar())
                print(Data().showCar())
                input("press enter to return to the main page")
                clear()
                main()
            else: 
                print("! Please Enter a valid number !")
                sleep(4)
                permission()
        elif password == 0:
            sleep(1)
            main()
        else : 
            print("Wrong passwrod , please enter a valid one !")
            sleep(2)
            permission()
    except Exception as e: 
        print(e)
        sleep(4)
        clear()
        main()

def main():
    clear()
    print("""\t==== Car Rental System ====
          
          1. Rent a car for hours
          2. Rent a car for days
          3. Rent a car for weeks
          4. Return a car
          5. Administration
          6. exit
          """)
    try:
        choice = int(input("Enter the number you want to explore : "))
        if choice == 1:
            ID = Data().createID()
            print("The ID of the customer is ", ID)
            numberOfCars = int((input("Enter the number of car(s) : ")))
            hour = int(input("Enter the number of hours : "))
            for _ in range (0,numberOfCars):
                name = input("\nEnter the client name : ")
                phoneNumber = input("Enter the phone number of the client name : ")
                sellingDate = input("Enter the date of today [dd/mm/yy hour]: ")
                retruningDate = input("Enter the date for retuning the car [dd/mm/yy hour]: ")
                carNumber = int(input("Enter the car(s) number : "))
                if carNumber in Data().showCar():
                    Data(carNumber = carNumber).deleteCar()
                    Data(ID , name , phoneNumber , numberOfCars , sellingDate , retruningDate , carNumber).addClient()
                    carRent().requestHour(hour, carNumber)
                    sleep(4)
                    main()
                else:
                    print("This car is used")
                    sleep(4)
                    main()
        elif choice == 2:
            ID = Data().createID()
            print("The ID of the customer is ", ID)
            numberOfCars = int((input("Enter the number of car(s) : ")))
            hour = int(input("Enter the number of hours : "))
            for _ in range (0,numberOfCars):
                name = input("\nEnter the client name : ")
                phoneNumber = input("Enter the phone number of the client name : ")
                sellingDate = input("Enter the date of today [dd/mm/yy hour]: ")
                retruningDate = input("Enter the date for retuning the car [dd/mm/yy hour]: ")
                carNumber = int(input("Enter the car(s) number : "))
                if carNumber in Data().showCar():
                    Data(carNumber = carNumber).deleteCar()
                    Data(ID , name , phoneNumber , numberOfCars , sellingDate , retruningDate , carNumber).addClient()
                    carRent().requestDay(hour, carNumber)
                    sleep(4)
                    main()
                else:
                    print("This car is used")
                    sleep(4)
                    main()           
        elif choice == 3:
            ID = Data().createID()
            print("The ID of the customer is ", ID)
            numberOfCars = int((input("Enter the number of car(s) : ")))
            hour = int(input("Enter the number of hours : "))
            for _ in range (0,numberOfCars):
                name = input("\nEnter the client name : ")
                phoneNumber = input("Enter the phone number of the client name : ")
                sellingDate = input("Enter the date of today [dd/mm/yy hour]: ")
                retruningDate = input("Enter the date for retuning the car [dd/mm/yy hour]: ")
                carNumber = int(input("Enter the car(s) number : "))
                if carNumber in Data().showCar():
                    Data(carNumber = carNumber).deleteCar()
                    Data(ID , name , phoneNumber , numberOfCars , sellingDate , retruningDate , carNumber).addClient()
                    carRent().requestWeek(hour, carNumber)
                    sleep(4)
                    main()
                else:
                    print("This car is used")
                    sleep(4)
                    main()        
        elif choice == 4:
            print("Thank you for using our Service, hope you enjoyed driving our cars")
            ID = int(input("Please enter your ID : "))
            Data().getClient(ID)
            choice = int(input("How many car(s) you want to return : "))
            for _ in range(0,choice):
                carNumber = int(input("Enter the car number : "))
                Data().deleteClient(carNumber)
                Data().addCar(carNumber)
            print("Hope to see again !")
            sleep(5)
            main()               
        elif choice == 5: permission()
        elif choice == 6: exit()
        else:
            print("! Please enter a valid number !")
            sleep(4)
            main()
    except Exception as e: print(e)
main()