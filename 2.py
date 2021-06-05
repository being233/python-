import tkinter as tk
from tkinter import filedialog
from tkinter.constants import NONE
from PIL import Image,ImageTk
import cv2 as cv
#调用库函数

win=tk.Tk()
win.title('实验二')
win.geometry('1024x1024')
#建立窗口

#photo_a=NONE
#photo_b=NONE
#photo_add=NONE
#r_a=NONE
#r_b=NONE
#变量声明

class PictureProcess():
    
    def selectPicture(self):
        pic_name = filedialog.askopenfilename(title='选择图片', filetypes=[('jpg','png'), ('All Files', '*')])
        return pic_name
    def add_together(self,r_a,r_b):
        print(type(r_a))
        print('type(r_a)')
        image_add=cv.add(r_a,r_b)
        print(type(image_add))
        print('type(image_add)')        
        cv.imwrite('add.png',image_add)
        path_add='add.png'
        #image_add=Image.fromarray(array_add)
        return path_add
        
#图片处理过程使用面向对象编程

Pic=PictureProcess()
Pic1=PictureProcess()
Pic2=PictureProcess()
#建立两个对象分别对应进行处理的两张图片

def pic_select_a(): 
    global photo_a,path_a    #若需在方法中调用图片，则需提前声明全局变量
    path_a=Pic1.selectPicture()
    image_a=Image.open(path_a)
    #r_a=cv.imread(path_a)
    print(path_a+'3')     
    photo_a = ImageTk.PhotoImage(image_a)
    l_1=tk.Label(win, image=photo_a)
    l_1.pack()
botton1=tk.Button(win,text='选择图片a',width=10,height=2,command=pic_select_a)
botton1.pack()
#建立选择图片a按钮及其功能

def pic_select_b(): 
    global photo_b,path_b
    path_b=Pic2.selectPicture()    
    image_b=Image.open(path_b)
    r_b=cv.imread(path_b)
    photo_b = ImageTk.PhotoImage(image_b)
    l_2=tk.Label(win, image=photo_b)
    l_2.pack()
botton2=tk.Button(win,text='选择图片b',width=10,height=2,command=pic_select_b)
botton2.pack()
#建立选择图片b按钮及其功能

def pic_add():
    global photo_add
    print(path_a+'2')
    r_a=cv.imread(path_a)
    r_b=cv.imread(path_b)
    print(type(r_a))
    print('type(r_a)')
    #image_add_r=Pic.add_together(r_a,r_b)
    print(Pic.add_together(r_a,r_b))
    image_add_re=Image.open(Pic.add_together(r_a,r_b))
    print(type(image_add_re))
    photo_add=ImageTk.PhotoImage(image_add_re)
    l_add=tk.Label(win,image=photo_add)
    l_add.pack()
botton3=tk.Button(win,text='图片相加',width=10,height=2,command=pic_add)
botton3.pack()
#建立图片相加按钮及其功能
win.mainloop()
