import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import tkinter.font as tkFont

logs = tk.Tk()
logs.title("Skolas Zvans")
logs.state('zoomed')  
loga_augstums = logs.winfo_screenheight()
loga_platums = logs.winfo_screenwidth()
logs.configure(bg="#E7E2E2")

canvas = tk.Canvas(logs, bg="#E7E2E2")
canvas.pack(fill=tk.BOTH, expand=True)

def lādē(file):
    img = Image.open(file)
    img = img.convert('RGBA')  
    return img

pulksteņa_att = lādē(r"C:\Users\Hidno\Documents\Prog\Skolas_Zvans\Proj\clock_p.png")
pulksteņa_att = pulksteņa_att.resize((400, 400))

pulksteņa_att_tk = ImageTk.PhotoImage(pulksteņa_att)


foto1_lokācija = tk.Label(logs, image=pulksteņa_att_tk, bg="#E7E2E2")
foto1_lokācija.image = pulksteņa_att_tk 
foto1_lokācija.place(x=((loga_platums-400)//2), y=0)

Mina = tkFont.Font(family="Mina", size=20)

def start_game():
    print("Sākt Spēli")
     
sākt = canvas.create_polygon(0, 400, 550, 400, 600, 475, 550, 550, 0, 550, fill="#7A2222")
canvas.create_text(270, 475, text="Sākt Spēli", font=(Mina,50), fill="white", )
canvas.tag_bind(sākt, '<Button-2>', start_game)

def settings():
    logs.destroy()
    subprocess.run(["python", "Iestatījumi.py"])

iestatīt = canvas.create_polygon(0, 575, 450, 575, 500, 640, 450, 700, 0, 700, fill="#4A0A0A")
canvas.create_text(225, 637, text="Iestatījumi", font=(Mina,40), fill="white")
canvas.tag_bind(iestatīt, '<Button-1>', settings)

logs.mainloop()