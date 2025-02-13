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

skola_att = lādē("skool.png")
skola_att = skola_att.resize((640, 360))
skola_att_tk = ImageTk.PhotoImage(skola_att)
skola_lokācija = tk.Label(canvas, image=skola_att_tk, bg="#87ceeb")
skola_lokācija.image = skola_att_tk 
skola_lokācija.place(x=((loga_platums-640)//2), y=loga_augstums*0.6 -360)

kvadrāts_koordinātes = [(0, loga_augstums*0.6), (loga_platums, loga_augstums*0.6), (loga_platums, loga_augstums), (0, loga_augstums)]
kvadrāts = canvas.create_polygon(kvadrāts_koordinātes, fill="#345f3b")

Turpināt_koordinātes = [(loga_platums * 0.75, loga_augstums*0.725), (loga_platums* 0.95, loga_augstums*0.725), (loga_platums*0.95,loga_augstums* 0.875), (loga_platums *0.75, loga_augstums* 0.875)]
turpināt_poga = canvas.create_polygon(Turpināt_koordinātes, fill="#7A2222")
canvas.create_text(loga_platums * 0.85, loga_augstums * 0.8, text="Turpināt", font=(Mina, 50), fill="white")
canvas.tag_bind(turpināt_poga, '<Button-1>', next)

logs.mainloop()