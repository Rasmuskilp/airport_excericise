import pyodbc

class MSDBConnection():
    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'homework_db'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.docker_Northwind = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID='
            + self.username + ';PWD=' + self.password)
        self.cursor = self.docker_Northwind.cursor()
    def __sql_query(self,sql_query): # Makes it private
        return self.cursor.execute(sql_query)
    # cursor.execute("SELECT * FROM Passengers WHERE name LIKE 'Jessica'")
    def insert_to(self):
        query = "INSERT INTO Passengers (name , passport) VALUES ('Tom', 'A152521')"
        query2 = 'SELECT * FROM Passengers'
        item = self.__sql_query(query)
        item2 = self.__sql_query(query2)
        # record = item.fetchall()
        print(item2.fetchall())
    def select_from(self):
        query = 'SELECT * FROM Flight_trip'
        item = self.__sql_query(query)
        print( item.fetchall())
    def add_to(self):
        query = "INSERT INTO Flight_trip (passenger) VALUES ('Jess')"
        item = self.__sql_query(query)
        query2 = "SELECT * FROM Flight_trip"
        item2 = self.__sql_query(query2)
        print(item2.fetchall())
airport = MSDBConnection()
print(airport.insert_to())
print(airport.select_from())
print(airport.add_to())
