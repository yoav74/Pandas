import tkinter

import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def browse_file():
    file_path = filedialog.askopenfilename(
        title="Select a CSV file",
        filetypes=[("CSV files", "*.csv")]
    )
    if file_path:
        print(f"You selected: {file_path}")
        Browse_Label.config(text=f"File Selected: {file_path}")
        df = pd.read_csv(file_path)
        current_df = df
        text_zone.delete('1.0', tkinter.END)
        text_zone.tag_configure('left', justify='left')
        text_zone.insert('1.0', current_df.to_string(), 'left')
        columnsCheckboxes.clear()
        update_file(current_df)
        change_col_btn = ttk.Button(frame, text="Update Selected Columns",
                                    command=lambda: update_columns(current_df, sort_list, sort_btn))
        change_col_btn.pack(side='top', padx=5, pady=5)
        sort_list = ttk.Combobox(frame, values=list(current_df.columns))
        sort_list.set("Sort By...")
        sort_list.pack(side='top', padx=5, pady=5)
        sort_btn = ttk.Button(frame, text="Sort", command=lambda: sort_df(current_df, sort_list.get()))
        sort_btn.pack(side='top', padx=5, pady=5)


def update_file(df):
    for col in df.columns:
        var = tkinter.IntVar(value=1)
        checkbox = tkinter.Checkbutton(frame, text=col, variable=var)
        checkbox.pack(side='top', anchor='w')
        columnsCheckboxes.append(var)


def update_columns(df, sort_list, sort_btn):
    converted = [var.get() for var in columnsCheckboxes]
    columns_to_keep = [col for col, keep in zip(df.columns, converted) if keep == 1]
    new_df = pd.DataFrame(df[columns_to_keep])
    current_df = new_df
    if not new_df.empty:
        empty_label.config(text='')
        text_zone.delete('1.0', tkinter.END)
        text_zone.tag_configure('left', justify='left')
        text_zone.insert('1.0', new_df.to_string(), 'left')
        sort_btn.config(command=lambda: sort_df(current_df, sort_list.get()))
        sort_list.config(values=list(current_df.columns))
    else:
        empty_label.config(text="No Selected Columns")
        empty_label.pack(side='top')
        text_zone.delete('1.0', tkinter.END)
        text_zone.tag_configure('left', justify='left')
        text_zone.insert('1.0', df.to_string(), 'left')
        for col in columnsCheckboxes:
            col.set(1)
        sort_btn.config(command=lambda: sort_df(df, sort_list.get()))
        sort_list.config(values=list(df.columns))


def sort_df(current_df, sort_by):
    sorted_df = pd.DataFrame(current_df)
    sorted_df.sort_values(by=[f'{sort_by}'], inplace=True, ascending=True)
    text_zone.delete('1.0', tkinter.END)
    text_zone.tag_configure('left', justify='left')
    text_zone.insert('1.0', sorted_df.to_string(), 'left')


# Base
root = Tk()
root.title("Pandas")
root.geometry("600x400")
root.state('zoomed')
frame = tkinter.Frame(root)
frame.pack(expand=True, fill='both', padx=10, pady=10)
# Labels and Buttons
empty_label = ttk.Label(frame)
Browse_Label = ttk.Label(text="File Selected:2 ")
Browse_btn = ttk.Button(frame, text="Browse For files", command=browse_file)
Quit_btn = ttk.Button(frame, text="Quit", command=root.quit)
text_zone = tkinter.Text(frame, wrap='none')
text_zone.pack(side="left", expand=True, fill='both')
scroll_y = tkinter.Scrollbar(frame, orient='vertical', command=text_zone.yview)
scroll_y.pack(side='right', fill='y')
scroll_x = tkinter.Scrollbar(root, orient='horizontal', command=text_zone.xview)
scroll_x.pack(side='bottom', fill='x')
text_zone.config(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
checkbox_frame = tkinter.Frame(root)
checkbox_frame.pack(fill='x')
sort_btn = ttk.Button
columnsCheckboxes = []
Browse_Label.pack()
Browse_btn.pack(pady=5)
Quit_btn.pack(pady=5)

root.mainloop()
