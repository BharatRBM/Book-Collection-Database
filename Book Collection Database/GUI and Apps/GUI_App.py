from Connect_to_Database.Connect_DB import ConnectDB
import tkinter as tk

connect_to_database = ConnectDB()

connect_to_database.connect_to_file()


def execute_query():
    query = '''SELECT * FROM books.calendar
    WHERE YEAR = 2000'''
    sql_output = connect_to_database.fetch_query_data(query)
    for index, record in enumerate(sql_output):
        result_label = tk.Label(root, text=record)
        result_label.grid(row=index + 2, column=0, padx=10, pady=10)


root = tk.Tk()
root.title("Book Database GUI")

# Label for instructions
label = tk.Label(root, text="Click the button to query the database:")
label.grid(row=0, column=0, padx=10, pady=10)

# Button to trigger the query
query_button = tk.Button(root, text="Query Database", command=execute_query)
query_button.grid(row=1, column=0, padx=10, pady=10)

# Run the GUI
root.mainloop()

# Close the database connection
connect_to_database.close_connection()
