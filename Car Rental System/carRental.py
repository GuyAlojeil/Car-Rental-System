import sqlite3 as db
from prettytable import PrettyTable
import random

class Data:
    def __init__(self, ID = 0 , name = "" , phoneNumber = "" , numberOfCars = "" , sellingDate = "" , returningDate = "" , carNumber = 0):
        self.ID = ID
        self.name = name
        self.phoneNumber = phoneNumber
        self.numberOfCars = numberOfCars
        self.sellingDate = sellingDate
        self.returningDate = returningDate
        self.carNumber = carNumber
        
        self.connection = db.connect("rental.db")
        self.cursor = self.connection.cursor()
    
    def showClient(self):
        self.cursor.execute(''' SELECT * FROM client''')
        data = self.cursor.fetchall()
        table = PrettyTable()

        table.field_names = ["ID" , "Name" , "Phone Number" , "Number of cars" , "Selling Date" , "Returning Date" , "carNumber"]
        for i in data:
            table.add_row(i)
        print(table)
        
        self.connection.commit()
        self.connection.close() 
    def addClient(self):
        self.connection.execute('''INSERT INTO client 
                   (ID , Name , phoneNumber , numberOfCars , sellingDate , returningDate,carNumber) VALUES(?,?,?,?,?,?,?)''',
                   (self.ID , self.name , self.phoneNumber, self.numberOfCars , self.sellingDate , self.returningDate , self.carNumber))
        self.connection.commit()
        self.connection.close()   
    def deleteClient(self , carNumber):
        self.cursor.execute('''DELETE FROM client WHERE carNumber = ? ''' ,(carNumber,))

        self.connection.commit()
        self.connection.close()
    def getID(self):
        self.cursor.execute('''SELECT ID FROM client''')
        data = self.cursor.fetchall() 
        ids = []
        for i in data:
            i = str(i)
            i = i.replace("(" , "")
            i = i.replace(")" , "")
            i = i.replace("," , "")
            i = int(i)
            ids.append(i)
        self.connection.commit()
        self.connection.close()       
        return ids     
       
    def showCar(self):
        self.cursor.execute(''' SELECT * FROM car''')
        data = self.cursor.fetchall()
        carNumber = []
        for i in data:
            i = str(i)
            i = i.replace("(" , "")
            i = i.replace(")" , "")
            i = i.replace("," , "")
            i = int(i)
            carNumber.append(i)
        self.connection.commit()
        self.connection.close()
        return carNumber
            
    def addCar(self,carNumber):
        self.connection.execute('''INSERT INTO car (carNumber) VALUES(?)''',(carNumber,))
        self.connection.commit()
        self.connection.close()
    def deleteCar(self):
        self.connection.execute('''DELETE FROM car WHERE carNumber = ?''',(self.carNumber,))
        self.connection.commit()
        self.connection.close()
    def getCar(self):
        self.cursor.execute(''' SELECT * FROM car''')
        data = self.cursor.fetchall()
        self.connection.commit()
        self.connection.close()       
        return len(data)
    def createID(self):
        numbers = [0,1,2,3,4,5,6,7,8,9]
        newIDList = []
        for _ in range(0,6):
            newIDList.append(random.choice(numbers))
            
        newID = int(''.join(map(str,newIDList)))
        if newID in Data().getID():
            Data().createID()
        else:
            return newID

    def getClient(self , ID):
        self.cursor.execute('''SELECT * FROM client WHERE ID=?''',(ID,))
        data = self.cursor.fetchall()
        table = PrettyTable()

        table.field_names = ["ID" , "Name" , "Phone Number" , "Number of cars" , "Selling Date" , "Returning Date" , "carNumber"]
        for i in data:
            table.add_row(i)
        print(table)
        
        self.connection.commit()
        self.connection.close() 

class carRent:
    
    def __init__(self):
        pass

    def requestHour(self, hour , cars):       
        if cars > Data().getCar():
            print("Sorry! We have currently "+ Data().getCars() + " car available to rent.")
            return None      
        else:                    
            print("\nYou have rented ",cars,"car(s) for ",hour," hour(s).")
            print("You will be charged ",hour * 6,"$ per car and 10$ for every extra hour")
            print("We hope that you enjoy our service!")
     
    def requestDay(self, day , cars):
        if cars > Data().getCar():
            print("Sorry! We have currently "+ Data().getCars() + " car available to rent.")
            return None       
        else:                    
            print("\nYou have rented ",cars,"car(s) for ",day," day(s).")
            print("You will be charged ",day * 20,"$ per car and 15$ for every extra day")
            print("We hope that you enjoy our service!")
     
    def requestWeek(self, week , cars):
        if cars > Data().getCar():
            print("Sorry! We have currently "+ Data().getCars() + " car available to rent.")
            return None
        else:                    
            print("\nYou have rented ",cars,"car(s) for ",week," week(s).")
            print("You will be charged ",week * 50,"$ per car and 20$ for every extra day")
            print("We hope that you enjoy our service!")