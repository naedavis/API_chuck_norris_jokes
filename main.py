from tkinter import messagebox

import requests
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("300x300")
root.config(bg="Black")


def get_chuck_jokes():
    try:
        response = requests.get("https://api.chucknorris.io/jokes/random")
        data = response.json()
        return data["value"]
    except requests.exceptions.ConnectionError as x:
        messagebox.showinfo("error", "Connection Error")



msg_joke = Message(root, text=get_chuck_jokes(),bg="black", fg="white", font="Arial 20")
msg_joke.pack()


def next_joke():
    try:
        response = requests.get("https://api.chucknorris.io/jokes/random")
        data = response.json()
        joke = data["value"]
        msg_joke.config(text=get_chuck_jokes())
    except requests.exceptions.ConnectionError as x:
        messagebox.showinfo("error", "Connection Error")


btn_next = Button(root, text="NEXT JOKE", fg="pink", command=next_joke)
btn_next.pack()


root.mainloop()




