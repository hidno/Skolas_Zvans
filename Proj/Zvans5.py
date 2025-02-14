from datetime import datetime, timedelta
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.font as tkFont
import os, json, subprocess, pygame





logs = tk.Tk()
logs.title("Skolas Zvans")
logs.state('zoomed')  
logs.configure(bg="#1e90ff")
loga_augstums = logs.winfo_screenheight()
loga_platums = logs.winfo_screenwidth()

canvas = tk.Canvas(logs, bg="#1e90ff")
canvas.pack(fill=tk.BOTH, expand=True)

os.chdir(r"C:\Users\Hidno\Documents\Prog\Skolas_Zvans\Proj")
Mina = tkFont.Font(family="Mina", size=20)
pygame.mixer.init()





with open('dati.json', 'r') as file:
    data = json.load(file)

with open('dienas_laiks.txt', 'r') as file:
    laiks = file.read()

with open('dienas_beigas.txt', 'r') as file:
    dienas_beigas = file.read()

stundu_intervāls = data.get("stundu_intervals", "")
dienas_tips = data.get("dienas_tips", "")
starbrīžu_garums = data.get("starbrīžu_garums", "")
pusdienlaiks = data.get("pusdienlaiks", "")
pusdienas_garums = data.get("pusdienas_garums", "")

laika_formāts = "%H:%M"

starbrīžu_garums = int(data.get('starbrīžu_garums', "0").split()[0])
pusdienas_garums = int(data.get('pusdienas_garums', "0").split()[0])
stundu_intervāls = int(data.get('stundu_intervals', "0").split()[0])

dienas_beigas = datetime.strptime(dienas_beigas, laika_formāts)
starbrīžu_garums = datetime.strptime('starbrīžu_garums', laika_formāts)
pusdienlaiks = datetime.strptime(pusdienlaiks, laika_formāts)
 




if dienas_tips == "Piektdiena":
    starbrīžu_garums = starbrīžu_garums // 2  
    dienas_beigas = dienas_beigas - timedelta(minutes=starbrīžu_garums)  
    dienas_beigas = dienas_beigas.strftime(laika_formāts)

    with open('dienas_beigas.txt', "w") as file:
        file.write(dienas_beigas)





def formula():
    laiks = datetime.strptime(laiks, laika_formāts)
    stundu_intervāls = int(stundu_intervāls.split()[0])  
    if laiks >= pusdienlaiks:
        laiks = laiks + timedelta(stundu_intervals=stundu_intervāls + pusdienas_garums + starbrīžu_garums)
    else:
        laiks = laiks + timedelta(stundu_intervals=stundu_intervāls + starbrīžu_garums)

    with open('dienas_laiks.txt', 'w') as file:
        file.write(laiks.strftime(laika_formāts))





def lādē(file):
    img = Image.open(file)
    img = img.convert('RGBA')  
    return img

with open('dienas_beigas.txt', 'r') as file:
    dienas_beigas = file.read()

with open('dienas_laiks.txt', 'r') as file:
    laiks = file.read()

def next(event):
    laiks = datetime.strptime(laiks, laika_formāts)
    dienas_beigas = datetime.strptime(dienas_beigas, laika_formāts)
    if laiks >= dienas_beigas:
        zvans_att = lādē("Zvans.png")
        zvans_att = zvans_att.resize((800, 800))  
        zvans_tk = ImageTk.PhotoImage(zvans_att)
        canvas.create_image(loga_platums// 2, loga_augstums// 2, image=zvans_tk)
        logs.update()
        pygame.mixer.music.load("Zvana_Audio.mp3")
        pygame.mixer.music.play()
        
        subprocess.Popen(['python', 'Skolas_Zvans.py'])
        logs.withdraw()
    else:
        zvans_att = lādē("Zvans.png")
        zvans_att = zvans_att.resize((800, 800))  
        zvans_tk = ImageTk.PhotoImage(zvans_att)
        canvas.create_image(loga_platums// 2, loga_augstums// 2, image=zvans_tk)
        logs.update()
        pygame.mixer.music.load("Zvana_Audio.mp3")
        pygame.mixer.music.play()
        
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

Kvadrāts2_koordinātes = [(0, 0), (loga_platums * 0.2, 0), (loga_platums * 0.2, loga_augstums * 0.15), (0, loga_augstums * 0.15)]
Kvadrāts2 = canvas.create_polygon(Kvadrāts2_koordinātes, fill="#574873")
canvas.create_text(loga_platums * 0.1, loga_augstums * 0.075, text=laiks, font=(Mina, 50), fill="white")

Turpināt_koordinātes = [(loga_platums * 0.75, loga_augstums*0.725), (loga_platums* 0.95, loga_augstums*0.725), (loga_platums*0.95,loga_augstums* 0.875), (loga_platums *0.75, loga_augstums* 0.875)]
Turpināt_poga = canvas.create_polygon(Turpināt_koordinātes, fill="#7A2222")
canvas.create_text(loga_platums * 0.85, loga_augstums * 0.8, text="Turpināt", font=(Mina, 50), fill="white")
canvas.tag_bind(Turpināt_poga, '<Button-1>', next)

logs.mainloop()