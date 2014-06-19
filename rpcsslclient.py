import xmlrpc.client
from tkinter import *

master = Tk()

s = xmlrpc.client.ServerProxy('https://localhost:8000')

def openlink():
  s.browse("http://news.google.com")

b = Button(master, text="OK", command=openlink)
b.pack()

mainloop();