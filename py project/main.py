
import base64
import secrets
import os
import json
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import tkinter as tk
from tkinter import messagebox
import time
import secrets

#buld up the wimdow
root = tk.Tk()
root.geometry("800x400")
root.title("hussen hady simulator")
dd ={'scoree': 5 , 'increas':1} #defult data
key = (b'dVW30NYHSQdQBuCr6DQ2EOoyGusaf02Pc6irahQO-vc=') #that the kye
f = Fernet(key)



if not os.path.exists('data') or os.path.getsize('data')==0:
    with open('data','wb')as d:
        hh= f.encrypt(json.dumps(dd).encode('utf-8'))
        d.write(hh) 
else :
    with open('data','rb')as d:
        de=d.read()
        hh= f.decrypt(de)
        

def load():
    if os.path.exists('data') or os.path.getsize('data')!=0:
      with open('data','rb')as d:
        global dd
        de=d.read()
        hh= f.decrypt(de)
        dd=json.loads((hh.decode()))
        lable.config(text="score: "+str(dd['scoree']))

            
    

def sav():
    print("saved")
    global dd
    with open('data','wb')as d:
        hh= f.encrypt(json.dumps(dd).encode('utf-8'))
        d.write(hh)

def damg():
    global dd
    if dd['scoree'] > 0:
        dd['scoree']-=1
        lable.config(text="score: "+str(dd['scoree']))
        root.after(1000, damg)
    else:
        messagebox.showinfo("YOU LOSER", "YOU LOSE IDEOT")
        root.destroy()
        

def on_button_click():
    new_windo=tk.Toplevel(root)
    new_windo.title('stor')
    flower = tk.Button(new_windo,command=buy_mint, borderwidth=0,text='flowe 4000$')
    flower.config(compound='top')
    flower.pack(side='right')

def score():
    dd['scoree']+= dd['increas']
    print(dd['scoree'])
    lable.config(text="score: "+str(dd['scoree']))
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    button_width = tea_pot.winfo_width()
    button_height = tea_pot.winfo_height()
    


    x = secrets.randbelow(window_width - button_width)
    y = secrets.randbelow(window_height - button_height)

    tea_pot.place(x=x, y=y)

def buy_mint():
    global incresed
    global scor
    if scor>3 :
        scor-=5
        lable.config(text="score: "+str(scor))
        print("true")
    else:
        print("false")

#score (text)

lable = tk.Label(root,text="score")
lable.pack(anchor="nw", padx=1, pady=1)
#imgs
pot_photo = tk.PhotoImage(file="tea_pot.png").subsample(3, 3)
#buttons

load_b = tk.Button(root, command=load,text='load')
load_b.config(compound='top')
load_b.pack(side='left')
save_b=tk.Button(root,command=sav,text='save')
save_b.config(compound='top')
save_b.pack(side='left')
tea_pot = tk.Button(root, image=pot_photo, command=score, borderwidth=0,text='traditional tea pot',font=("Arial", 10))
tea_pot.config(compound='top')
tea_pot.pack(side='left')
damg()
root.mainloop()

