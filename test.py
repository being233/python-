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

photo_1=NONE
photo_2=NONE
#变量声明

class PictureProcess():
    
    def selectPicture(self):
        pic_name = filedialog.askopenfilename(title='选择图片', filetypes=[('jpg','png'), ('All Files', '*')])
        return pic_name
        
    def add_together(self,r_a,r_b):
        image_add=cv.add(r_a,r_b)
        cv.imwrite('add.png',image_add)
        return image_add
        
#图片处理过程使用面向对象编程

Pic1=PictureProcess()

def pic_select_a(): 
    global photo_1
    l1=Pic1.selectPicture()      
    r_a=cv.imread(l1)
    image_a=Image.open(l1)
    
    photo_1 = ImageTk.PhotoImage(image_a)
    l_1=tk.Label(win, image=photo_1)
    l_1.pack()
botton1=tk.Button(win,text='选择图片a',width=10,height=2,command=pic_select_a)
botton1.pack()
#建立选择图片a按钮及其功能

win.mainloop()
