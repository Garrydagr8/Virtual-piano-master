import pygame
import sys
from tkinter import *

pygame.init()

def value_Cs(event):
    num1.set("C#1")
    sound = pygame.mixer.Sound("C:\\Users\\GARRYDAGR8\\Downloads\\Compressed\\wav-piano-sound-master\\wav-piano-sound-master\\wav\\c1s.wav")
    sound.play()
    return
def value_Ds(event):
    num1.set("D#1")
    sound = pygame.mixer.Sound("C:\\Users\\GARRYDAGR8\\Downloads\\Compressed\\wav-piano-sound-master\\wav-piano-sound-master\\wav\\d1s.wav")
    sound.play()
    return
def value_Fs(event):
    num1.set("F#1")
    sound = pygame.mixer.Sound("C:\\Users\\GARRYDAGR8\\Downloads\\Compressed\\wav-piano-sound-master\\wav-piano-sound-master\\wav\\f1s.wav")
    sound.play()
    return
def value_Gs(event):
    num1.set("G#1")
    sound = pygame.mixer.Sound("C:\\Users\\GARRYDAGR8\\Downloads\\Compressed\\wav-piano-sound-master\\wav-piano-sound-master\\wav\\g1s.wav")
    sound.play()
    return
def value_As(event):
    num1.set("A#1")
    sound = pygame.mixer.Sound("C:\\Users\\GARRYDAGR8\\Downloads\\Compressed\\wav-piano-sound-master\\wav-piano-sound-master\\wav\\a1s.wav")
    sound.play()
    return
def value_C(event):
    num1.set("C1")
    sound = pygame.mixer.Sound("C:\\Users\\GARRYDAGR8\\Downloads\\Compressed\\wav-piano-sound-master\\wav-piano-sound-master\\wav\\c1.wav")
    sound.play()
    return
def value_D(event):
    num1.set("D1")
    sound = pygame.mixer.Sound("C:\\Users\\GARRYDAGR8\\Downloads\\Compressed\\wav-piano-sound-master\\wav-piano-sound-master\\wav\\d1.wav")
    sound.play()
    return
def value_E(event):
    num1.set("E1")
    sound = pygame.mixer.Sound("C:\\Users\\GARRYDAGR8\\Downloads\\Compressed\\wav-piano-sound-master\\wav-piano-sound-master\\wav\\e1.wav")
    sound.play()
    return
def value_F(event):
    num1.set("F1")
    sound = pygame.mixer.Sound("C:\\Users\\GARRYDAGR8\\Downloads\\Compressed\\wav-piano-sound-master\\wav-piano-sound-master\wav\\f1.wav")
    sound.play()
    return
def value_G(event):
    num1.set("G1")
    sound = pygame.mixer.Sound("C:\\Users\\GARRYDAGR8\\Downloads\\Compressed\\wav-piano-sound-master\\wav-piano-sound-master\\wav\\g1.wav")
    sound.play()
    return
def value_A(event):
    num1.set("A1")
    sound = pygame.mixer.Sound("C:\\Users\\GARRYDAGR8\\Downloads\\Compressed\\wav-piano-sound-master\\wav-piano-sound-master\\wav\\a1.wav")
    sound.play()
    return
def value_B(event):
    num1.set("B1")
    sound = pygame.mixer.Sound("C:\\Users\\GARRYDAGR8\\Downloads\\Compressed\\wav-piano-sound-master\\wav-piano-sound-master\\wav\\b1.wav")
    sound.play()
    return
def value_C2(event):
    num1.set("C2")
    sound = pygame.mixer.Sound("C:\\Users\\GARRYDAGR8\\Downloads\\Compressed\\wav-piano-sound-master\\wav-piano-sound-master\\wav\\c2.wav")
    sound.play()
    return

root = Tk()
frame = Frame(root)
frame.pack()

root.title('PIANO')
num1 = StringVar()

topframe = Frame(root)
topframe.pack(side = TOP)
txtDisplay = Entry(frame,textvariable = num1,bd = 20,insertwidth = 20,font = 10,justify = 'left',width = 4,)
txtDisplay.pack(side = TOP)

button1 = Button(topframe,padx=8,height=6,pady=8,bd=8,text="C# ",bg = "black",fg = "white",command=value_Cs)
button1.pack(side=LEFT)

button22 = Button(topframe ,state=DISABLED,height=7,width=1,padx=0,pady=0,relief=RIDGE)
button22.pack(side=LEFT)
button2 = Button(topframe,padx=8,height=6,pady=8,bd=8,text="D# ",bg = "black",fg = "white",command=value_Ds)
button2.pack(side=LEFT)
button22 = Button(topframe ,state=DISABLED,height=7,width=1,padx=0,pady=0,relief=RIDGE)
button22.pack(side=LEFT)
button3 = Button(topframe,padx=8,height=6,pady=8,bd=8,text="F# ",bg = "black",fg = "white",command=value_Fs)
button3.pack(side=LEFT)
button22 = Button(topframe ,state=DISABLED,height=7,width=1,padx=0,pady=0,relief=RIDGE)
button22.pack(side=LEFT)
button4 = Button(topframe,padx=8,height=6,pady=8,bd=8,text="G# ",bg = "black",fg = "white",command=value_Gs)
button4.pack(side=LEFT)
button22 = Button(topframe ,state=DISABLED,height=7,width=1,padx=0,pady=0,relief=RIDGE)
button22.pack(side=LEFT)
button2 = Button(topframe,padx=8,height=6,pady=8,bd=8,text="A# ",bg = "black",fg = "white",command=value_As)
button2.pack(side=LEFT)
button22 = Button(topframe ,state=DISABLED,height=7,width=1,padx=0,pady=0,relief=RIDGE)
button22.pack(side=LEFT)

button1.bind_all("s",value_Cs)
button2.bind_all("d",value_Ds)
button3.bind_all("g",value_Fs)
button4.bind_all("h",value_Gs)
button2.bind_all("j",value_As)

frame1 = Frame(root)
frame1.pack(side=TOP)

button1 = Button(frame1,padx=16,height=8,pady=16,bd=8,text="C ",fg = "black",command=value_C)
button1.pack(side=LEFT)

button2 = Button(frame1,padx=16,height=8,pady=16,bd=8,text="D ",fg = "black",command=value_D)
button2.pack(side=LEFT)

button3 = Button(frame1,padx=16,height=8,pady=16,bd=8,text="E ",fg = "black",command=value_E)
button3.pack(side=LEFT)

button4 = Button(frame1,padx=16,height=8,pady=16,bd=8,text="F ",fg = "black",command=value_F)
button4.pack(side=LEFT)
button5 = Button(frame1,padx=16,height=8,pady=16,bd=8,text="G ",fg = "black",command=value_G)
button5.pack(side=LEFT)
button6 = Button(frame1,padx=16,height=8,pady=16,bd=8,text="A ",fg = "black",command=value_A)
button6.pack(side=LEFT)
button7 = Button(frame1,padx=16,height=8,pady=16,bd=8,text="B ",fg = "black",command=value_B)
button7.pack(side=LEFT)
button8 = Button(frame1,padx=16,height=8,pady=16,bd=8,text="C ",fg = "black",command=value_C2)
button8.pack(side=LEFT)

button1.bind_all("z",value_C)
button2.bind_all("x",value_D)
button3.bind_all("c",value_E)
button4.bind_all("v",value_F)
button5.bind_all("b",value_G)
button6.bind_all("n",value_A)
button7.bind_all("m",value_B)
button8.bind_all(",",value_C2)

root.mainloop()
