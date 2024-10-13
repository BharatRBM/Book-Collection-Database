import mysql.connector


class ConnectDB:
    def __init__(self):
        self.db = None

    @staticmethod
    def read_config_file(file_path):
        config = {}
        with open(file_path, 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                config[key] = value
        return config

    def connect_to_file(self):
        config_file = self.read_config_file(
            file_path=r'C:\Users\murth\PycharmProjects\Book Collection '
                      r'Database\Connect_to_Database\password_database.txt')
        try:
            self.db = mysql.connector.connect(
                host=config_file['host'],
                user=config_file['user'],
                password=config_file['password'],
                database=config_file['database'])
            print("Connection successful!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.db = None

    def fetch_query_data(self, query):
        if self.db is None:
            print("No database connection. Use `connect_to_db()` to establish connection first.")
            return None

        cursor = self.db.cursor()
        cursor.execute(query)

        result = cursor.fetchall()
        return result

    def fetch_column_headers(self, query):
        cursor = self.db.cursor()
        cursor.execute(query)
        column_headers = [i[0] for i in cursor.description]
        return column_headers

    def close_connection(self):
        if self.db is not None:
            self.db.close()
            print("Connection closed.")
