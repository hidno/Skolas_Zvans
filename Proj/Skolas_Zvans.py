import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont
import os, subprocess, json





logs = tk.Tk()
logs.title("Skolas Zvans")
logs.state('zoomed')  
logs.configure(bg="#E7E2E2")
loga_augstums = logs.winfo_screenheight()
loga_platums = logs.winfo_screenwidth()

canvas = tk.Canvas(logs, bg="#E7E2E2")
canvas.pack(fill=tk.BOTH, expand=True)

os.chdir(r"C:\Users\Hidno\Documents\Prog\Skolas_Zvans\Proj")
Mina = tkFont.Font(family="Mina", size=20)





with open('dati.json', 'r') as file:
    data = json.load(file)

dienas_sākums = data.get("dienas_sakums", "")





def start_game(event=None):
    if dienas_sākums in ["7:00", "7:30", "8:00", "8:30", "9:00", "9:30"]:
        subprocess.Popen(['python', 'Zvans1.py'])
        logs.withdraw()
    elif dienas_sākums in ["10:00", "10:30", "11:00", "11:30"]:
        subprocess.Popen(['python', 'Zvans2.py'])
        logs.withdraw()
    else:
        subprocess.Popen(['python', 'Zvans3.py'])
        logs.withdraw()


def settings(event):
    subprocess.Popen(['python', 'Iestatījumi.py'])
    logs.withdraw()


def lādē(file):
    img = Image.open(file)
    img = img.convert('RGBA')  
    return img


pulksteņa_att = lādē("clock_p.png")
pulksteņa_att = pulksteņa_att.resize((400, 400))
pulksteņa_att_tk = ImageTk.PhotoImage(pulksteņa_att)
pulksteņa_lokācija = tk.Label(logs, image=pulksteņa_att_tk, bg="#E7E2E2")
pulksteņa_lokācija.image = pulksteņa_att_tk 
pulksteņa_lokācija.place(x=((loga_platums-400)//2), y=0)

sākt_koordinātes = [(0, loga_augstums * 0.5),(loga_platums * 0.45, loga_augstums * 0.5),(loga_platums * 0.49, loga_augstums * 0.6),(loga_platums * 0.45, loga_augstums * 0.7),(0, loga_augstums * 0.7)]
sākt_poga = canvas.create_polygon(sākt_koordinātes, fill="#7A2222")
canvas.create_text(loga_platums * 0.225, loga_augstums * 0.6, text="Sākt Spēli", font=(Mina, 90), fill="white")
canvas.tag_bind(sākt_poga, '<Button-1>', start_game)

iestatīt_koordinātes = [(0, loga_augstums * 0.725),(loga_platums * 0.35, loga_augstums * 0.725),(loga_platums * 0.39, loga_augstums * 0.8),(loga_platums * 0.35, loga_augstums * 0.875),(0, loga_augstums * 0.875)]
iestatījumu_poga = canvas.create_polygon(iestatīt_koordinātes, fill="#4A0A0A")
canvas.create_text(loga_platums * 0.175, loga_augstums * 0.8, text="Iestatījumi", font=(Mina, 50), fill="white")
canvas.tag_bind(iestatījumu_poga, '<Button-1>', settings)

logs.mainloop()