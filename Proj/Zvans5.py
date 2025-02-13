import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont
import os, json, subprocess
from datetime import datetime, timedelta

logs = tk.Tk()
logs.title("Skolas Zvans")
logs.state('zoomed')  
loga_augstums = logs.winfo_screenheight()
loga_platums = logs.winfo_screenwidth()
logs.configure(bg="#191970")

canvas = tk.Canvas(logs, bg="#191970")
canvas.pack(fill=tk.BOTH, expand=True)
os.chdir(r"C:\Users\Hidno\Documents\Prog\Skolas_Zvans\Proj")

Mina = tkFont.Font(family="Mina", size=20)

def lādē(file):
    img = Image.open(file)
    img = img.convert('RGBA')  
    return img

with open('dati.json', 'r') as file:
    data = json.load(file)

with open('dienas_laiks.txt', 'r') as file:
    laiks = file.read()

stundu_intervāls = data.get("stundu_intervals", "")
laika_formāts = "%H:%M"  

def next(event):
    subprocess.Popen(['python', 'Skolas_Zvans.py'])
    logs.withdraw()

kvadrāts_koordinātes = [(0, loga_augstums*0.6), (loga_platums, loga_augstums*0.6), (loga_platums, loga_augstums), (0, loga_augstums)]
kvadrāts = canvas.create_polygon(kvadrāts_koordinātes, fill="#345f3b")

def formula():
    start = datetime.strptime(laiks, laika_formāts)
    minūtes = int(stundu_intervāls.split()[0])  
    rēķins = start + timedelta(minutes=minūtes)
    with open('dienas_laiks.txt', 'w') as file:
        file.write(rēķins.strftime(laika_formāts))

skola_att = lādē("skool.png")
skola_att = skola_att.resize((960, 520))
skola_att_tk = ImageTk.PhotoImage(skola_att)
canvas.create_image((loga_platums-960)//2, loga_augstums*0.63 -520, image=skola_att_tk, anchor=tk.NW)

kvadrāts1_koordinātes = [(loga_platums*0.46, loga_augstums*0.63), (loga_platums*0.53, loga_augstums*0.63), (loga_platums*0.53, loga_augstums), (loga_platums*0.46, loga_augstums)]
kvadrāts1 = canvas.create_polygon(kvadrāts1_koordinātes, fill="#e1ddbf", width=2)

formula()
with open('dienas_laiks.txt', 'r') as file:
    laiks = file.read()
kvadrāts2_koordinātes = [(0, 0), (loga_platums * 0.2, 0), (loga_platums * 0.2, loga_augstums * 0.15), (0, loga_augstums * 0.15)]
kvadrāts2 = canvas.create_polygon(kvadrāts2_koordinātes, fill="#574873")
canvas.create_text(loga_platums * 0.1, loga_augstums * 0.075, text=laiks, font=(Mina, 50), fill="white")

Turpināt_koordinātes = [(loga_platums * 0.75, loga_augstums*0.725), (loga_platums* 0.95, loga_augstums*0.725), (loga_platums*0.95,loga_augstums* 0.875), (loga_platums *0.75, loga_augstums* 0.875)]
turpināt_poga = canvas.create_polygon(Turpināt_koordinātes, fill="#7A2222")
canvas.create_text(loga_platums * 0.85, loga_augstums * 0.8, text="Turpināt", font=(Mina, 50), fill="white")
canvas.tag_bind(turpināt_poga, '<Button-1>', next)

logs.mainloop()