class Participant:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def __str__(self):
        return f'{self.name},{self.age},{self.address}'
    
class CulturalManager:
    def createDB():
        try:
            mycursor.execute("CREATE DATABASE Cultural Manager")
            print("DataBase created successfully")
        except Exception:
            print("Issue while creating DB")
    def useDB():
        try:
            mycursor.execute("USE Todolist")
            print("Using DB")
        except Exception:
            print("Issue while creating DB")
    def CreateTask():
        try:
            mycursor.execute("Create Table taskmgr(task varchar(20),status varchar(20))")
            print("Created Table successfully")
        except Exception:
            print("Already created Table")
    def InsertTask():
        try:
            mycursor.execute("insert into taskmgr(name,status)values('gvm','pending)")
            print("insert successfully")
        except Exception:
            print("Issue while inserting")
    
    def  updateTask():
        try:
            mycursor.execute("update taskmgr set )")
            print("Created Table successfully")
        except Exception:
            print("Already created Table")
        

            
            
        