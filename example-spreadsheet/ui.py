import tkinter as tk
from tkinter import filedialog
import pandas as pd

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=300, bg='lightsteelblue')
canvas.pack()


def getExcel():
    import_file_path = filedialog.askopenfilename()
    df = pd.read_excel(import_file_path)
    print(df)


browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel,
                               bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas.create_window(150, 150, window=browseButton_Excel)

root.mainloop()
