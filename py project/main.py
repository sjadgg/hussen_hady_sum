
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

#generat the key and the defult data
dd ={'scoree': 5 , 'increas':1} #defult data
key = (b'dVW30NYHSQdQBuCr6DQ2EOoyGusaf02Pc6irahQO-vc=') #that the kye
f = Fernet(key) #crypt and decrypt


# if data file dont existed or corrupted , generat a new file with defult data
if not os.path.exists('data') or os.path.getsize('data')==0:
    with open('data','wb')as d:
        hh= f.encrypt(json.dumps(dd).encode('utf-8')) #turn data var tipe from dictionary into json and encrypt yhis data by fernet
        d.write(hh) # write encrypt data into the file
else : #if data file already existid read the data
    with open('data','rb')as d:
        de=d.read()
        hh= f.decrypt(de) #decrypt the data
        
#load func , chek if data file existed then decyipt the data and set new data to old data 
def load():
    if os.path.exists('data') or os.path.getsize('data')!=0:
      with open('data','rb')as d:
        global dd
        de=d.read()
        hh= f.decrypt(de)
        dd=json.loads((hh.decode())) #read data and turn it into dictionary
        lable.config(text="score: "+str(dd['scoree'])) # show new data on label
         
# save data as json 
def sav():
    print("saved")
    global dd
    with open('data','wb')as d:
        hh= f.encrypt(json.dumps(dd).encode('utf-8'))
        d.write(hh)

#chek if score are greater than zero then sub 1 from it , and if score is lower than 0 show the lose message 
def damg():
    global dd
    if dd['scoree'] > 0:
        dd['scoree']-=1
        lable.config(text="score: "+str(dd['scoree']))
        root.after(1000, damg)
    else:
        messagebox.showinfo("YOU LOSER", "YOU LOSE IDEOT")
        root.destroy()

#what this func doing is increas scor when the tea pot is clecked
def score():
    dd['scoree']+= dd['increas']
    print(dd['scoree'])
    lable.config(text="score: "+str(dd['scoree']))
    #take window and button high,wide 
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    button_width = tea_pot.winfo_width()
    button_height = tea_pot.winfo_height()
    
# using secrets to genrat random number depent on wide,higt 
    x = secrets.randbelow(window_width - button_width)
    y = secrets.randbelow(window_height - button_height)
# set tea pot to the new position
    tea_pot.place(x=x, y=y)

#creat a label 
lable = tk.Label(root,text="score")
lable.pack(anchor="nw", padx=1, pady=1)
#creat an imgs
pot_photo = tk.PhotoImage(file="tea_pot.png").subsample(3, 3)
#creat buttons

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