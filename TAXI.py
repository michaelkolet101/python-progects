import xlrd 
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
from tkinter import font as tkFont

def PICTHER(filename):

  img = Image.open(filename).resize((400,450), Image.ANTIALIAS)
  
  img = ImageTk.PhotoImage(img)
  panel = Label(root, image = img)
 
  panel.image = img
  panel.place(x = 0 ,y = 0)
  

def exel_to_dict():
	list_1 = []
	list_2 = []
	loc = ("workres.xlsx") 
	wb = xlrd.open_workbook(loc) 
	sheet = wb.sheet_by_index(0)
	for i in range(20):
		list_1.append(sheet.cell_value(i+1, 1))
		list_2.append(sheet.cell_value(i+1, 2)) 
	dictionary = dict(zip(list_1, list_2))
	return dictionary
	
def clikbtn1():
    
  dictionary = exel_to_dict()
  name_of_worker = E1.get()	
    
  if dictionary[name_of_worker] == "Working day":
    filename = "illegal.jpg" 
  else:
    filename = "approved.PNG" 
    
  PICTHER(filename)
    
    

root = Tk()
root.geometry("402x700")
root.resizable(width=True, height=True)
root.title("רפא - מערכת הזמנת מוניות")   

helv36 = tkFont.Font(family='Helvetica', size = 16)
helv37 = tkFont.Font(family='Helvetica', size = 16)

filename ="TAXI.jpg"
PICTHER(filename)

L2 = Label(root, text = "Enter full name",font = helv36)
L2.place(x = 130,y = 455,height = 50)

E1 = Entry(root)
E1.place(x = 130,y = 500,height = 30)

btn1 = Button(root, text='Confirm',height = "2", width = "10", bg = "yellow",font = helv37, command = clikbtn1)
btn1.place(x = 125,y = 540,height = 50)


L3 = Label(root, text = "Kol&Ing Technologies", bg = "black", width = "50",height = "2", fg = "white",bd = 4)
L3.place(x = 0,y = 660)

lv5 = Label(root, text = "Taxi booking", bg = "black",  fg = "white",bd = 4)
lv5.place(x= 15, y= 0)
lv5.config(font=("Courier", 44))
root.mainloop()

