import tkinter as tk
from datetime import datetime

#frame
root = tk.Tk()
root.geometry("1000x400")

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

#widgets
time = tk.Label(root, text=dt_string)
time.pack(side=tk.LEFT)

ans = tk.Label(root, text="")
ans.pack(side=tk.RIGHT)

#conversion
b = tk.Button(root, text="Convert")
b.pack(side=tk.CENTER)

#tkinter GUI
root.mainloop()
