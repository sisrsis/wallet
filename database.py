import mysql.connector

class Mysql():
    def __init__(self,host:str,user:str,password:str,database:str):
        self.mydb = mysql.connector.connect(host=host,user=user,password=password,database=database,auth_plugin='mysql_native_password')
        
        
    def insert(self,table:str,field_value:dict):
        data_for_query = "INSERT INTO " + table + " ("
        for key in field_value.keys():
            data_for_query = data_for_query + str(key) + ","
        data_for_query = data_for_query[:len(data_for_query) - 1]
        data_for_query = data_for_query + ")  VALUES  ("
        for value in field_value.values():
            data_for_query = data_for_query + str(value) + ","
        data_for_query = data_for_query[:len(data_for_query) - 1]
        data_for_query = data_for_query + ")"
        print(data_for_query)
        mycursor = self.mydb.cursor()
        mycursor.execute(data_for_query)
        self.mydb.commit()