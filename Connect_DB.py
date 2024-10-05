import mysql.connector


class ConnectDB:
    def __init__(self):
        self.db = None

    def read_config_file(self, file_path):
        config = {}
        with open(file_path, 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                config[key] = value
        return config

    def connect_to_file(self):
        config_file = self.read_config_file(
            file_path=r'password_database.txt')

        self.db = mysql.connector.connect(
            host=config_file['host'],
            user=config_file['user'],
            password=config_file['password'],
            database=config_file['database'])

        my_cursor = self.db.cursor()

        my_cursor.execute("SELECT * FROM book_details")

        my_result = my_cursor.fetchone()
        return my_result

    def close_connection(self):
        if self.db is not None:
            self.db.close()
            print("Connection closed.")

