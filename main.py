import requests
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("300x300")
root.config(bg="Black")



def get_chuck_jokes():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    data = response.json()
    return data["value"]


msg_joke = Message(root, text=get_chuck_jokes(),bg="black", fg="white", font="Arial 20")
msg_joke.pack()


def next():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    data = response.json()
    joke = data["value"]
    msg_joke.config(text=get_chuck_jokes())

btn_next = Button(root, text="NEXT JOKE", fg="pink", command=next)
btn_next.pack()



root.mainloop()




