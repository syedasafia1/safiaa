import mysql.connector
from mysql.connector import Error
# Establish a connection to the MySQL server
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='user'
)

mycursor = mydb.cursor()

class CulturalManager:
    def __init__(self, participants_name, location, duration):
        self.Participants_name = participants_name
        self.location = location
        self.duration = duration
        
        
    def __str__(self):
        return f'{self.participants_name}, {self.location},{self.duration}'

class Participants:
    @staticmethod
    def createDB():
        try:
            mycursor.execute("CREATE DATABASE Participants")
            print("Database 'Participants' created successfully.")
        except mysql.connector.Error as err:
            print(f'Error: {err}')  # Provide the error message

    @staticmethod
    def useDB():
        try:
            mycursor.execute("USE Participants")
            print("Using database 'Participants'.")
        except mysql.connector.Error as err:
            print(f'Error: {err}')  # Provide the error message

    @staticmethod
    def createParticipants():
        try:
            mycursor.execute("""
                CREATE TABLE Participants (
                    name VARCHAR(20),
                   
                )
            """)
            print('Table "PasspotPrinting" created successfully.')
        except mysql.connector.Error as err:
            print(f'Error: {err}')  # Provide the error message

# Create database, use it, and create the table
pq = PrintingQueue()
pq.createDB()
pq.useDB()
pq.createPassport()

# Close the cursor and connection
mycursor.close()
mydb.close()
