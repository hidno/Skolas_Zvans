import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont
import os, subprocess

logs = tk.Tk()
logs.title("Skolas Zvans")
logs.state('zoomed')  
loga_augstums = logs.winfo_screenheight()
loga_platums = logs.winfo_screenwidth()
logs.configure(bg="#E7E2E2")

canvas = tk.Canvas(logs, bg="#E7E2E2")
canvas.pack(fill=tk.BOTH, expand=True)
os.chdir(r"C:\Users\Hidno\Documents\Prog\Skolas_Zvans\Proj")

def lādē(file):
    img = Image.open(file)
    img = img.convert('RGBA')  
    return img

pulksteņa_att = lādē("clock_p.png")
pulksteņa_att = pulksteņa_att.resize((400, 400))

pulksteņa_att_tk = ImageTk.PhotoImage(pulksteņa_att)

foto1_lokācija = tk.Label(logs, image=pulksteņa_att_tk, bg="#E7E2E2")
foto1_lokācija.image = pulksteņa_att_tk 
foto1_lokācija.place(x=((loga_platums-400)//2), y=0)

Mina = tkFont.Font(family="Mina", size=20)

def start_game(event):
    subprocess.Popen(['python', 'Zvans1.py'])
    logs.withdraw()

sākt_koordinātes = [(0, loga_augstums * 0.5),(loga_platums * 0.45, loga_augstums * 0.5),(loga_platums * 0.49, loga_augstums * 0.6),(loga_platums * 0.45, loga_augstums * 0.7),(0, loga_augstums * 0.7)]
sākt_poga = canvas.create_polygon(sākt_koordinātes, fill="#7A2222")
canvas.create_text(loga_platums * 0.225, loga_augstums * 0.6, text="Sākt Spēli", font=(Mina, 90), fill="white")
canvas.tag_bind(sākt_poga, '<Button-1>', start_game)

def settings(event):
    subprocess.Popen(['python', 'Iestatījumi.py'])
    logs.withdraw()

iestatīt_koordinātes = [(0, loga_augstums * 0.725),(loga_platums * 0.35, loga_augstums * 0.725),(loga_platums * 0.39, loga_augstums * 0.8),(loga_platums * 0.35, loga_augstums * 0.875),(0, loga_augstums * 0.875)]
iestatījumu_poga = canvas.create_polygon(iestatīt_koordinātes, fill="#4A0A0A")
canvas.create_text(loga_platums * 0.175, loga_augstums * 0.8, text="Iestatījumi", font=(Mina, 50), fill="white")
canvas.tag_bind(iestatījumu_poga, '<Button-1>', settings)

logs.mainloop()