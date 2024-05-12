import sqlite3 as db
from prettytable import PrettyTable
from carRental import Data

data  = Data().getID()
ids = []
for i in data:
    i = str(i)
    i = i.replace("(" , "")
    i = i.replace(")" , "")
    i = i.replace("," , "")
    i = int(i)
    ids.append(i)
    

# table = PrettyTable()

# connection = db.connect("rental.db")
# cursor = connection.cursor()

# Id = int(input())
# name = input()
# phonenumber = input()
# numberofcars = input()
# sellingdate = input()
# returningdate = input()
#carNumber = input()
# for i in range(1,101):
    # cursor.execute('''INSERT INTO car (carNumber) VALUES(?)''',(i,))

# connection.execute('''INSERT INTO car 
#                    (ID , Name , phoneNumber , numberOfCars , sellingDate , returningDate,carNumber) VALUES(?,?,?,?,?,?,?)''',
#                    (Id , name , phonenumber,numberofcars , sellingdate , returningdate,carNumber))

# cursor.execute(''' SELECT * FROM car''')
# data = cursor.fetchall()

# table.field_names = ["ID" , "Name" , "Phone Number" , "Number of cars" , "Selling Date" , "Returning Date" , "carNumber"]
# for i in data:
#     table.add_row(i)

# print(table)

# cursor.execute('''DELETE FROM car WHERE ID = ? ''' ,(Id,))

# connection.commit()
# connection.close()
