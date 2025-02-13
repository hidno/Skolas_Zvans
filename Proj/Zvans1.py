import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont
import os, subprocess

logs = tk.Tk()
logs.title("Skolas Zvans")
logs.state('zoomed')  
loga_augstums = logs.winfo_screenheight()
loga_platums = logs.winfo_screenwidth()
logs.configure(bg="#87ceeb")

canvas = tk.Canvas(logs, bg="#87ceeb")
canvas.pack(fill=tk.BOTH, expand=True)
os.chdir(r"C:\Users\Hidno\Documents\Prog\Skolas_Zvans\Proj")

Mina = tkFont.Font(family="Mina", size=20)

def lādē(file):
    img = Image.open(file)
    img = img.convert('RGBA')  
    return img

def next(event):
    print("Turpināt")

Turpināt_koordinātes = [(loga_platums * 0.75, loga_augstums*0.725), (loga_platums* 0.95, loga_augstums*0.725), (loga_platums*0.95,loga_augstums* 0.875), (loga_platums *0.75, loga_augstums* 0.875)]
turpināt_poga = canvas.create_polygon(Turpināt_koordinātes, fill="#4A0A0A")
canvas.create_text(loga_platums * 0.85, loga_augstums * 0.8, text="Turpināt", font=(Mina, 50), fill="white")
canvas.tag_bind(turpināt_poga, '<Button-1>', next)

logs.mainloop()