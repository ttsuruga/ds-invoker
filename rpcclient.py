import xmlrpc.client
from tkinter import *

master = Tk()

s = xmlrpc.client.ServerProxy('http://localhost:8000')

def openlink():
  #s.browse("http://news.google.com")
  s.browse("file:///C:/Users/take2/Desktop/pytest-2014-06-11/pytest/canvas.html")

b = Button(master, text="OK", command=openlink)
b.pack()

mainloop();

