import os, subprocess
import tkinter as tk
import tkinter.font as tkFont

logs = tk.Tk()
logs.title("Iestatījumi")
logs.state('zoomed')  
loga_augstums = logs.winfo_screenheight()
loga_platums = logs.winfo_screenwidth()
logs.configure(bg="#E7E2E2")

Mina = tkFont.Font(family="Mina", size=20)

canvas = tk.Canvas(logs, bg="#E7E2E2")
canvas.pack(fill=tk.BOTH, expand=True)

os.chdir(r"C:\Users\Hidno\Documents\Prog\Skolas_Zvans\Proj")

def back(event):
    subprocess.Popen(['python', 'Skolas_Zvans.py'])
    logs.destroy()
 
atpakaļ_koordinātes = [(0, loga_augstums * 0.725),(loga_platums * 0.35, loga_augstums * 0.725),(loga_platums * 0.39, loga_augstums * 0.8),(loga_platums * 0.35, loga_augstums * 0.875),(0, loga_augstums * 0.875)]
atpakaļ = canvas.create_polygon(0, 575, 450, 575, 500, 640, 450, 700, 0, 700, fill="#7A2222")
canvas.create_text(loga_platums * 0.175, loga_augstums * 0.8, text="Atpakaļ", font=(Mina, 50), fill="white")
canvas.tag_bind(atpakaļ, '<Button-1>', back)

logs.mainloop()
