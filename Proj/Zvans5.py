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

dienas_beigas = data.get("dienas_beigas", "")
stundu_intervāls = data.get("stundu_intervals", "")
dienas_tips = data.get("dienas_tips", "")
starbrīžu_garums = data.get("starbrīžu_garums", "")
laika_formāts = "%H:%M"  


def formula():
    start = datetime.strptime(laiks, laika_formāts)
    minūtes = int(stundu_intervāls.split()[0])  
    rēķins = start + timedelta(minutes=minūtes)
    with open('dienas_laiks.txt', 'w') as file:
        file.write(rēķins.strftime(laika_formāts))

formula()
with open('dienas_laiks.txt', 'r') as file:
    laiks = file.read()
Kvadrāts2_koordinātes = [(0, 0), (loga_platums * 0.2, 0), (loga_platums * 0.2, loga_augstums * 0.15), (0, loga_augstums * 0.15)]
Kvadrāts2 = canvas.create_polygon(Kvadrāts2_koordinātes, fill="#574873")
canvas.create_text(loga_platums * 0.1, loga_augstums * 0.075, text=laiks, font=(Mina, 50), fill="white")

def next(event):
    laiks_tagad = datetime.strptime(laiks, laika_formāts)
    dienas_beigas_laiks = datetime.strptime(dienas_beigas, laika_formāts)
    if laiks_tagad >= dienas_beigas_laiks:
        subprocess.Popen(['python', 'Skolas_Zvans.py'])
        logs.withdraw()
    else:
        subprocess.Popen(['python', 'Zvans5.py'])
        logs.withdraw()



Kvadrāts_koordinātes = [(0, loga_augstums*0.6), (loga_platums, loga_augstums*0.6), (loga_platums, loga_augstums), (0, loga_augstums)]
Kvadrāts = canvas.create_polygon(Kvadrāts_koordinātes, fill="#345f3b")

skola_att = lādē("skool.png")
skola_att = skola_att.resize((960, 520))
skola_att_tk = ImageTk.PhotoImage(skola_att)
canvas.create_image((loga_platums-960)//2, loga_augstums*0.63 -520, image=skola_att_tk, anchor=tk.NW)

Kvadrāts1_koordinātes = [(loga_platums*0.46, loga_augstums*0.63), (loga_platums*0.53, loga_augstums*0.63), (loga_platums*0.53, loga_augstums), (loga_platums*0.46, loga_augstums)]
Kvadrāts1 = canvas.create_polygon(Kvadrāts1_koordinātes, fill="#e1ddbf", width=2)

Turpināt_koordinātes = [(loga_platums * 0.75, loga_augstums*0.725), (loga_platums* 0.95, loga_augstums*0.725), (loga_platums*0.95,loga_augstums* 0.875), (loga_platums *0.75, loga_augstums* 0.875)]
Turpināt_poga = canvas.create_polygon(Turpināt_koordinātes, fill="#7A2222")
canvas.create_text(loga_platums * 0.85, loga_augstums * 0.8, text="Turpināt", font=(Mina, 50), fill="white")
canvas.tag_bind(Turpināt_poga, '<Button-1>', next)

logs.mainloop()