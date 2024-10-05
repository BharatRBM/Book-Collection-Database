from Connect_to_Database.Connect_DB import ConnectDB

connect_to_database = ConnectDB()
print(connect_to_database.connect_to_file())
connect_to_database.close_connection()
