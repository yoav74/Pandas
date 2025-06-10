# import tkinter
#
# import pandas as pd
# import matplotlib.pyplot as plt
# from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog
#
#
#
# def browse_file():
#     file_path = filedialog.askopenfilename(
#         title="Select a CSV file",
#         filetypes=[("CSV files", "*.csv")]
#     )
#     if file_path:
#         print(f"You selected: {file_path}")
#         Browse_Label.config(text=f"File Selected: {file_path}")
#         df = pd.read_csv(file_path)
#         current_df = df
#         text_zone.delete('1.0', tkinter.END)
#         text_zone.tag_configure('left', justify='left')
#         text_zone.insert('1.0', current_df.to_string(), 'left')
#         columnsCheckboxes.clear()
#         update_file(current_df)
#         chart_Btn = ttk.Button(frame,text = "Create Chart", command = lambda: create_chart(current_df))
#         chart_Btn.pack(side='top',padx = 5, pady=5)
#         change_col_btn = ttk.Button(frame, text="Update Selected Columns",
#                                     command=lambda: update_columns(current_df, sort_list, sort_btn))
#         change_col_btn.pack(side='top', padx=5, pady=5)
#         sort_list = ttk.Combobox(frame, values=list(current_df.columns))
#         sort_list.set("Sort By...")
#         sort_list.pack(side='top', padx=5, pady=5)
#         sort_btn = ttk.Button(frame, text="Sort", command=lambda: sort_df(current_df, sort_list.get()))
#         sort_btn.pack(side='top', padx=5, pady=5)
#
#
# def update_file(df):
#     for col in df.columns:
#         var = tkinter.IntVar(value=1)
#         checkbox = tkinter.Checkbutton(frame, text=col, variable=var)
#         checkbox.pack(side='top', anchor='w')
#         columnsCheckboxes.append(var)
#
#
# def update_columns(df, sort_list, sort_btn):
#     converted = [var.get() for var in columnsCheckboxes]
#     columns_to_keep = [col for col, keep in zip(df.columns, converted) if keep == 1]
#     new_df = pd.DataFrame(df[columns_to_keep])
#     current_df = new_df
#     if not new_df.empty:
#         empty_label.config(text='')
#         text_zone.delete('1.0', tkinter.END)
#         text_zone.tag_configure('left', justify='left')
#         text_zone.insert('1.0', new_df.to_string(), 'left')
#         sort_btn.config(command=lambda: sort_df(current_df, sort_list.get()))
#         sort_list.config(values=list(current_df.columns))
#     else:
#         empty_label.config(text="No Selected Columns")
#         empty_label.pack(side='top')
#         text_zone.delete('1.0', tkinter.END)
#         text_zone.tag_configure('left', justify='left')
#         text_zone.insert('1.0', df.to_string(), 'left')
#         for col in columnsCheckboxes:
#             col.set(1)
#         sort_btn.config(command=lambda: sort_df(df, sort_list.get()))
#         sort_list.config(values=list(df.columns))
#
#
# def sort_df(current_df, sort_by):
#     sorted_df = pd.DataFrame(current_df)
#     sorted_df.sort_values(by=[f'{sort_by}'], inplace=True, ascending=True)
#     text_zone.delete('1.0', tkinter.END)
#     text_zone.tag_configure('left', justify='left')
#     text_zone.insert('1.0', sorted_df.to_string(), 'left')
#
# def create_chart(df):
#     def plot():
#         x_col = x_combo.get()
#         y_col = y_combo.get()
#         if x_col and y_col:
#             plt.figure(figsize=(10, 6))
#             plt.plot(df[x_col], df[y_col], marker='o')
#             plt.xlabel(x_col)
#             plt.ylabel(y_col)
#             plt.title(f'{y_col} vs {x_col}')
#             plt.grid(True)
#             plt.tight_layout()
#             plt.show()
#
#     chart_window = Toplevel(root)
#     chart_window.title("Create Chart")
#     chart_window.geometry("300x150")
#
#     Label(chart_window, text="Select X-axis:").pack(pady=5)
#     x_combo = ttk.Combobox(chart_window, values=list(df.columns))
#     x_combo.pack(pady=5)
#
#     Label(chart_window, text="Select Y-axis:").pack(pady=5)
#     y_combo = ttk.Combobox(chart_window, values=list(df.columns))
#     y_combo.pack(pady=5)
#
#     Button(chart_window, text="Plot", command=plot).pack(pady=10)
#
#
# # Base
# root = Tk()
# root.title("Pandas")
# root.geometry("600x400")
# root.state('zoomed')
# frame = tkinter.Frame(root)
# frame.pack(expand=True, fill='both', padx=10, pady=10)
# # Labels and Buttons
# empty_label = ttk.Label(frame)
# Browse_Label = ttk.Label(text="File Selected:2 ")
# Browse_btn = ttk.Button(frame, text="Browse For files", command=browse_file)
# Quit_btn = ttk.Button(frame, text="Quit", command=root.quit)
# text_zone = tkinter.Text(frame, wrap='none')
# text_zone.pack(side="left", expand=True, fill='both')
# scroll_y = tkinter.Scrollbar(frame, orient='vertical', command=text_zone.yview)
# scroll_y.pack(side='right', fill='y')
# scroll_x = tkinter.Scrollbar(root, orient='horizontal', command=text_zone.xview)
# scroll_x.pack(side='bottom', fill='x')
# text_zone.config(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
# checkbox_frame = tkinter.Frame(root)
# checkbox_frame.pack(fill='x')
# sort_btn = ttk.Button
# columnsCheckboxes = []
# Browse_Label.pack()
# Browse_btn.pack(pady=5)
# Quit_btn.pack(pady=5)
#
# root.mainloop()


import tkinter
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
from mysql.connector import Error


class DatabaseManager:
    def __init__(self):
        self.connection = None
        self.is_connected = False

    def connect(self, host, database, username, password, port=3306):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                database=database,
                user=username,
                password=password,
                port=port
            )
            if self.connection.is_connected():
                self.is_connected = True
                return True, "Connected successfully!"
        except Error as e:
            self.is_connected = False
            return False, f"Error: {str(e)}"
        return False, "Connection failed"

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            self.is_connected = False

    def get_tables(self):
        if not self.is_connected:
            return []
        try:
            cursor = self.connection.cursor()
            cursor.execute("SHOW TABLES")
            tables = [table[0] for table in cursor.fetchall()]
            cursor.close()
            return tables
        except Error as e:
            messagebox.showerror("Database Error", f"Error fetching tables: {str(e)}")
            return []

    def get_table_data(self, table_name):
        if not self.is_connected:
            return None
        try:
            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql(query, self.connection)
            return df
        except Error as e:
            messagebox.showerror("Database Error", f"Error fetching data: {str(e)}")
            return None


# Global variables
db_manager = DatabaseManager()
current_df = None
columnsCheckboxes = []


def browse_file():
    global current_df
    file_path = filedialog.askopenfilename(
        title="Select a CSV file",
        filetypes=[("CSV files", "*.csv")]
    )
    if file_path:
        print(f"You selected: {file_path}")
        Browse_Label.config(text=f"File Selected: {file_path}")
        df = pd.read_csv(file_path)
        current_df = df
        display_data(current_df)
        setup_controls(current_df)


def display_data(df):
    text_zone.delete('1.0', tkinter.END)
    text_zone.tag_configure('left', justify='left')
    text_zone.insert('1.0', df.to_string(), 'left')


def setup_controls(df):
    global current_df
    current_df = df

    # Clear existing checkboxes
    for widget in checkbox_frame.winfo_children():
        widget.destroy()
    columnsCheckboxes.clear()

    # Clear existing control buttons
    for widget in controls_frame.winfo_children():
        widget.destroy()

    # Create column checkboxes
    update_file(df)

    # Create control buttons
    chart_Btn = ttk.Button(controls_frame, text="Create Chart", command=lambda: create_chart(current_df))
    chart_Btn.pack(side='top', padx=5, pady=5)

    change_col_btn = ttk.Button(controls_frame, text="Update Selected Columns",
                                command=lambda: update_columns(current_df))
    change_col_btn.pack(side='top', padx=5, pady=5)

    sort_list = ttk.Combobox(controls_frame, values=list(current_df.columns))
    sort_list.set("Sort By...")
    sort_list.pack(side='top', padx=5, pady=5)

    sort_btn = ttk.Button(controls_frame, text="Sort", command=lambda: sort_df(current_df, sort_list.get()))
    sort_btn.pack(side='top', padx=5, pady=5)


def update_file(df):
    for col in df.columns:
        var = tkinter.IntVar(value=1)
        checkbox = tkinter.Checkbutton(checkbox_frame, text=col, variable=var)
        checkbox.pack(side='top', anchor='w')
        columnsCheckboxes.append(var)


def update_columns(df):
    global current_df
    converted = [var.get() for var in columnsCheckboxes]
    columns_to_keep = [col for col, keep in zip(df.columns, converted) if keep == 1]

    if columns_to_keep:
        new_df = pd.DataFrame(df[columns_to_keep])
        current_df = new_df
        display_data(new_df)
        empty_label.config(text='')
    else:
        empty_label.config(text="No Selected Columns")
        display_data(df)
        for col in columnsCheckboxes:
            col.set(1)


def sort_df(df, sort_by):
    if sort_by and sort_by != "Sort By...":
        sorted_df = df.copy()
        sorted_df.sort_values(by=[sort_by], inplace=True, ascending=True)
        display_data(sorted_df)


def create_chart(df):
    def plot():
        x_col = x_combo.get()
        y_col = y_combo.get()
        if x_col and y_col:
            plt.figure(figsize=(10, 6))
            plt.plot(df[x_col], df[y_col], marker='o')
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.title(f'{y_col} vs {x_col}')
            plt.grid(True)
            plt.tight_layout()
            plt.show()

    chart_window = Toplevel(root)
    chart_window.title("Create Chart")
    chart_window.geometry("300x150")

    Label(chart_window, text="Select X-axis:").pack(pady=5)
    x_combo = ttk.Combobox(chart_window, values=list(df.columns))
    x_combo.pack(pady=5)

    Label(chart_window, text="Select Y-axis:").pack(pady=5)
    y_combo = ttk.Combobox(chart_window, values=list(df.columns))
    y_combo.pack(pady=5)

    Button(chart_window, text="Plot", command=plot).pack(pady=10)


def open_db_connection_dialog():
    def connect_to_db():
        host = host_entry.get() or "localhost"
        database = db_entry.get()
        username = user_entry.get()
        password = pass_entry.get()
        port = int(port_entry.get()) if port_entry.get() else 3306

        if not database or not username:
            messagebox.showerror("Error", "Database name and username are required!")
            return

        success, message = db_manager.connect(host, database, username, password, port)

        if success:
            messagebox.showinfo("Success", message)
            connection_status.config(text="Status: Connected", foreground="green")
            load_tables_btn.config(state="normal")
            disconnect_btn.config(state="normal")
            connect_btn.config(state="disabled")
            db_window.destroy()
        else:
            messagebox.showerror("Connection Error", message)

    db_window = Toplevel(root)
    db_window.title("Database Connection")
    db_window.geometry("350x300")
    db_window.grab_set()  # Make window modal

    # Connection form
    Label(db_window, text="MySQL Database Connection", font=("Arial", 12, "bold")).pack(pady=10)

    # Host
    Label(db_window, text="Host:").pack()
    host_entry = Entry(db_window, width=30)
    host_entry.insert(0, "localhost")
    host_entry.pack(pady=2)

    # Port
    Label(db_window, text="Port:").pack()
    port_entry = Entry(db_window, width=30)
    port_entry.insert(0, "3306")
    port_entry.pack(pady=2)

    # Database
    Label(db_window, text="Database Name:").pack()
    db_entry = Entry(db_window, width=30)
    db_entry.pack(pady=2)

    # Username
    Label(db_window, text="Username:").pack()
    user_entry = Entry(db_window, width=30)
    user_entry.pack(pady=2)

    # Password
    Label(db_window, text="Password:").pack()
    pass_entry = Entry(db_window, width=30, show="*")
    pass_entry.pack(pady=2)

    # Connect button
    connect_btn = Button(db_window, text="Connect", command=connect_to_db, bg="lightblue")
    connect_btn.pack(pady=10)


def disconnect_from_db():
    db_manager.disconnect()
    connection_status.config(text="Status: Disconnected", foreground="red")
    load_tables_btn.config(state="disabled")
    disconnect_btn.config(state="disabled")
    db_connect_btn.config(state="normal")
    table_combo.config(values=[])
    table_combo.set("")


def load_tables():
    tables = db_manager.get_tables()
    if tables:
        table_combo.config(values=tables)
        table_combo.set("Select a table...")
        load_table_btn.config(state="normal")
    else:
        messagebox.showinfo("Info", "No tables found in the database.")


def load_table_data():
    selected_table = table_combo.get()
    if selected_table and selected_table != "Select a table...":
        df = db_manager.get_table_data(selected_table)
        if df is not None:
            global current_df
            current_df = df
            display_data(df)
            setup_controls(df)
            Browse_Label.config(text=f"Table Loaded: {selected_table}")


# Base window
root = Tk()
root.title("CSV & MySQL Data Viewer")
root.geometry("800x600")
root.state('zoomed')

# Main container
main_container = tkinter.Frame(root)
main_container.pack(expand=True, fill='both', padx=10, pady=10)

# Left panel for controls
left_panel = tkinter.Frame(main_container, width=200)
left_panel.pack(side='left', fill='y', padx=(0, 10))
left_panel.pack_propagate(False)

# Right panel for data display
right_panel = tkinter.Frame(main_container)
right_panel.pack(side='right', expand=True, fill='both')

# File operations frame
file_frame = tkinter.LabelFrame(left_panel, text="File Operations", padx=5, pady=5)
file_frame.pack(fill='x', pady=(0, 10))

Browse_Label = ttk.Label(file_frame, text="No file selected")
Browse_Label.pack(pady=2)

Browse_btn = ttk.Button(file_frame, text="Browse CSV Files", command=browse_file)
Browse_btn.pack(pady=2)

# Database operations frame
db_frame = tkinter.LabelFrame(left_panel, text="Database Operations", padx=5, pady=5)
db_frame.pack(fill='x', pady=(0, 10))

connection_status = ttk.Label(db_frame, text="Status: Disconnected", foreground="red")
connection_status.pack(pady=2)

db_connect_btn = ttk.Button(db_frame, text="Connect to MySQL", command=open_db_connection_dialog)
db_connect_btn.pack(pady=2)

disconnect_btn = ttk.Button(db_frame, text="Disconnect", command=disconnect_from_db, state="disabled")
disconnect_btn.pack(pady=2)

load_tables_btn = ttk.Button(db_frame, text="Load Tables", command=load_tables, state="disabled")
load_tables_btn.pack(pady=2)

table_combo = ttk.Combobox(db_frame, state="readonly")
table_combo.pack(pady=2, fill='x')

load_table_btn = ttk.Button(db_frame, text="Load Table Data", command=load_table_data, state="disabled")
load_table_btn.pack(pady=2)

# Controls frame
controls_frame = tkinter.LabelFrame(left_panel, text="Data Controls", padx=5, pady=5)
controls_frame.pack(fill='x', pady=(0, 10))

# Column checkboxes frame
checkbox_frame = tkinter.LabelFrame(left_panel, text="Columns", padx=5, pady=5)
checkbox_frame.pack(fill='both', expand=True, pady=(0, 10))

# Error label
empty_label = ttk.Label(left_panel, foreground="red")
empty_label.pack()

# Quit button
Quit_btn = ttk.Button(left_panel, text="Quit", command=root.quit)
Quit_btn.pack(side='bottom', pady=5)

# Text display area with scrollbars
text_zone = tkinter.Text(right_panel, wrap='none')
text_zone.pack(side="left", expand=True, fill='both')

scroll_y = tkinter.Scrollbar(right_panel, orient='vertical', command=text_zone.yview)
scroll_y.pack(side='right', fill='y')

scroll_x = tkinter.Scrollbar(root, orient='horizontal', command=text_zone.xview)
scroll_x.pack(side='bottom', fill='x')

text_zone.config(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

root.mainloop()

# Clean up database connection on exit
if db_manager.is_connected:
    db_manager.disconnect()