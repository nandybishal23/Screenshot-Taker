import PIL.ImageGrab
import datetime
from tkinter import *
import time

root = Tk()

root.title("Screen_Shot")

def take_ss():
    root.withdraw()
    time.sleep(1)
    img=PIL.ImageGrab.grab()
    img.save("Output.png")
    root.withdraw()

    root.update()
    root.deiconify()    

l1=Label(root,text='ScreenShot Taker',width=30,bg='coral',fg='white',font="time 20")
l1.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
btn1=Button(root, text='Take Shot',font="time 20",width=15,bg='black',fg='gold',command=take_ss,activebackground="gold",activeforeground="black")
btn1.grid(row=2,column=0,columnspan=2,padx=10,pady=10)
root.mainloop()
