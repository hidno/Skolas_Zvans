import os, subprocess, json
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

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
    logs.withdraw()

def datu_glabā():
     with open('Dati.json', 'r') as file:
        data = json.load(file)
        ievade1.set(data.get('dienas_sakums', ''))
        ievade2.set(data.get('dienas_beigas', ''))
        ievade3.set(data.get('stundu_intervals', ''))
        ievade4.set(data.get('dienas_tips', ''))
        ievade5.set(data.get('pusdienlaiks', ''))

def saglabā(event=None):
    data = {
        'dienas_sakums': ievade1.get(),
        'dienas_beigas': ievade2.get(),
        'stundu_intervals': ievade3.get(),
        'dienas_tips': ievade4.get(),
        'pusdienlaiks': ievade5.get()
    }
    with open('Dati.json', 'w') as file:
        json.dump(data, file)

atpakaļ_koordinātes = [(0, loga_augstums* 0.725),(loga_platums * 0.35, loga_augstums*0.725),(loga_platums*0.39, loga_augstums*0.8),(loga_platums * 0.35, loga_augstums*0.875),(0,loga_augstums*0.875)]
atpakaļ_poga = canvas.create_polygon(atpakaļ_koordinātes, fill="#4A0A0A")
canvas.create_text(loga_platums * 0.175, loga_augstums * 0.8, text="Atpakaļ", font=(Mina, 50), fill="white")
canvas.tag_bind(atpakaļ_poga, '<Button-1>', back)

kvadrāts_koordinātes = [(0, 0),(loga_platums, 0),(loga_platums, loga_augstums*0.25),(0,loga_augstums*0.25)]
kvadrāts = canvas.create_polygon(kvadrāts_koordinātes, fill="#4A0A0A")
canvas.create_text(loga_platums / 2, loga_augstums*0.125, text="Iestatījumi", font=(Mina,70), fill="white")



Dienu_Sākumi = ["7:00", "7:30", "8:00", "8:30", "9:00", "9:30", "10:00", "10:30", "11:00", "11:30", "12:00"]
kvadrāts1_koordinātes = [(loga_platums * 0.25, loga_augstums * 0.305), (loga_platums * 0.45, loga_augstums * 0.305), (loga_platums * 0.45, loga_augstums * 0.345), (loga_platums * 0.25, loga_augstums * 0.345)]
kvadrāts1 = canvas.create_polygon(kvadrāts1_koordinātes, fill="#4A0A0A")
canvas.create_text(loga_platums*0.35, loga_augstums*0.325, text="Dienas Sākums", font=(Mina, 25), fill="white")
ievade1 = ttk.Combobox(logs, values=Dienu_Sākumi, background="#d0c8c8",font=(Mina, 25), width=30)
ievade1_window = canvas.create_window(loga_platums*0.45, loga_augstums*0.325,anchor="w", window=ievade1)



Dienu_Beigas = ["15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00"]
kvadrāts2_koordinātes = [(loga_platums * 0.25, loga_augstums * 0.355), (loga_platums * 0.45, loga_augstums * 0.355), (loga_platums * 0.45, loga_augstums * 0.395), (loga_platums * 0.25, loga_augstums * 0.395)]
kvadrāts2 = canvas.create_polygon(kvadrāts2_koordinātes, fill="#4A0A0A")
canvas.create_text(loga_platums*0.35, loga_augstums*0.375, text="Dienas Beigas", font=(Mina, 25), fill="white")
ievade2 = ttk.Combobox(logs, values=Dienu_Beigas, background="#d0c8c8",font=(Mina, 25), width=30)
ievade2_window = canvas.create_window(loga_platums*0.45, loga_augstums*0.375,anchor="w", window=ievade2)



Stundu_Intervāli = ["30 min", "45 min", "60 min", "75 min", "90 min", "105 min", "120 min"]
kvadrāts3_koordinātes = [(loga_platums * 0.25, loga_augstums * 0.405), (loga_platums * 0.45, loga_augstums * 0.405), (loga_platums * 0.45, loga_augstums * 0.445), (loga_platums * 0.25, loga_augstums * 0.445)]
kvadrāts3 = canvas.create_polygon(kvadrāts3_koordinātes, fill="#4A0A0A")
canvas.create_text(loga_platums*0.35, loga_augstums*0.425, text="Stundu Intervāls", font=(Mina, 25), fill="white")
ievade3 = ttk.Combobox(logs, values=Stundu_Intervāli, background="#d0c8c8",font=(Mina, 25), width=30)
ievade3_window = canvas.create_window(loga_platums*0.45, loga_augstums*0.425,anchor="w", window=ievade3)



Dienu_tipi = ["Parasta Diena", "Svētku Diena", "Brīvdiena", "Pirmssvētku Diena"]
kvadrāts4_koordinātes = [(loga_platums * 0.25, loga_augstums * 0.455), (loga_platums * 0.45, loga_augstums * 0.455), (loga_platums * 0.45, loga_augstums * 0.495), (loga_platums * 0.25, loga_augstums * 0.495)]
kvadrāts4 = canvas.create_polygon(kvadrāts4_koordinātes, fill="#4A0A0A")
canvas.create_text(loga_platums*0.35, loga_augstums*0.475, text="Dienas Tips", font=(Mina, 25), fill="white")
ievade4 = ttk.Combobox(logs, values=Dienu_tipi, background="#d0c8c8",font=(Mina, 25), width=30)
ievade4_window = canvas.create_window(loga_platums*0.45, loga_augstums*0.475,anchor="w", window=ievade4)


Pusdienlaiki = ["12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00"]
kvadrāts5_koordinātes = [(loga_platums * 0.25, loga_augstums * 0.505), (loga_platums * 0.45, loga_augstums * 0.505), (loga_platums * 0.45, loga_augstums * 0.545), (loga_platums * 0.25, loga_augstums * 0.545)]
kvadrāts5 = canvas.create_polygon(kvadrāts5_koordinātes, fill="#4A0A0A")
canvas.create_text(loga_platums*0.35, loga_augstums*0.525, text="Pusdienlaiks", font=(Mina, 25), fill="white")
ievade5 = ttk.Combobox(logs, values=Pusdienlaiki, background="#d0c8c8", font=(Mina, 25), width=30)
ievade5_window = canvas.create_window(loga_platums*0.45, loga_augstums*0.525,anchor="w",window=ievade5)



saglabā_koordinātes = [(loga_platums * 0.75, loga_augstums*0.725), (loga_platums* 0.95, loga_augstums*0.725), (loga_platums*0.95,loga_augstums* 0.875), (loga_platums *0.75, loga_augstums* 0.875)]
saglabā_poga = canvas.create_polygon(saglabā_koordinātes, fill="#7A2222")
canvas.create_text(loga_platums * 0.85, loga_augstums * 0.8, text="Saglabāt", font=(Mina, 50), fill="white")
canvas.tag_bind(saglabā_poga, '<Button-1>', saglabā)

datu_glabā()
logs.mainloop()