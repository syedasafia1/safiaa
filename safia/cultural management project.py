import pymysql

mydb = pymysql.connect(
    host='localhost',          # Replace with your host
    user='root',      # Replace with your username
    password='user',  # Replace with your password
      # Replace with your database
)

mycursor = mydb.cursor()

class Participant:
    def _init_(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        
    def _str_(self):
        return f'{self.name}, {self.age}, {self.address}'

class Manager:
    @classmethod
    def createDB(cls):
        try:
            mycursor.execute("CREATE DATABASE MyDB")
            print('Database created successfully')
        except Exception as e:
            print('Issue while creating database:', e)

    @classmethod
    def useDB(cls):
        try:
            mycursor.execute("USE MyDB")
            print('Using MyDB')
        except Exception as e:
            print('Error using database:', e)

    @classmethod
    def createProgram(cls):
        try:
            mycursor.execute("CREATE TABLE Participant (name VARCHAR(30), age INT, address VARCHAR(30))")
            print('Table created successfully')
        except Exception as e:
            print('Issue while creating table:', e)
    @classmethod
    def insertProgram(cls):
        try:
            mycursor.execute("INSERT INTO Participant (name, age, address) VALUES ('safiya', 19, 'cowlbazar')")
            mydb.commit()
            print('Inserted successfully')
        except Exception as e:
            print('Issue while inserting data:', e)
    @classmethod
    def updateProgram(cls):
        try:
            mycursor.execute("UPDATE Participant SET age=34 WHERE name='misbah'")
            mydb.commit()
            print('Updated successfully')
        except Exception as e:
            print('Issue while updating:', e)
    @classmethod
    def deleteProgram(cls):
        try:
            mycursor.execute("DELETE FROM Participant WHERE name='misbha'")
            mydb.commit()
            print('Deleted successfully')
        except Exception as e:
            print('Issue while deleting:', e)
             
    
#Create an instance of Manager to use its methods
manager = Manager()
manager.createDB()
manager.useDB()
#manager.createProgram()

#manager.insertProgram()


#manager.updateProgram()
manager.deleteProgram()

# Close the database connection
mydb.close()