#import libraries 
from cgitb import text
from faulthandler import disable
from socket import SocketIO
from sre_parse import SPECIAL_CHARS
import tkinter as tk 
from tkinter import END, Tk, ttk 
from tkinter import scrolledtext 
from string import ascii_uppercase as upper_letters, ascii_lowercase as lower_letters
import os 
import random 

os.system("cls")
def generate():
    password_length = length.get()
    password = ""
    for i in range(5):
        while len(password) != password_length:
            password += random.choice(upper_letters)
            if len(password) == password_length:
                break
            password += random.choice(lower_letters)
            if len(password) == password_length:
                break
            password += random.choice(SPECIAL_CHARS)

    # shuffle the password characters
    pass_list = list(password)
    random.shuffle(pass_list)
    passwd = ''.join(pass_list)

    text_area.insert(tk.INSERT,passwd+"\n",tk.END)
    text_area.update()
    
def clear():
    text_area.delete("1.0",END)   
    text_area.update()
    
    

# declare the window 
win = tk.Tk()
win.title("Password Generator")
win.geometry("450x320")
win.resizable(False,False)

try:
    # create a text area 
    label = tk.Label(text="Generated Passwords Below")
    label.grid(row=0,column=0,columnspan=3)
    text_area = scrolledtext.ScrolledText(win,wrap=tk.WORD,width=50,height=15)

    text_area.grid(row=1,column=0,columnspan=3)
    generate_pass_button = tk.Button(text="Generate",command=generate).grid(row=2,column=1)
    exit_button = tk.Button(text='Exit',command=exit).grid(row=2,column=2)
    length = tk.IntVar()
    pass_length = tk.Entry(textvariable=length).grid(column=0,row=2)
    clear_button = tk.Button(text="Clear",command=clear).grid(row=3,column=0)
    win.mainloop() 
except:
    pass

