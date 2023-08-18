from tkinter import *
from tkinter import ttk
y=0
a= ttk.Notebook()
frame1 = ttk.Frame(a)
frame2 = ttk.Frame(a)
frame3 = ttk.Frame(a)
frame4 = ttk.Frame(a)
frame5 = ttk.Frame(a)

root = ttk.Frame(a)

def quiz(y):
    a.add(frame1, text="Q1")
    a.add(frame2, text="Q2")
    a.add(frame3, text="Q3")
    a.add(frame4, text="Q4")
    a.add(frame5, text="Q5")

    Label(frame1, text="Total keywords in python?",font=("Arial",50,"bold")).grid(row=2,column=2)
    Button(frame1, text="33",font=("Arial",30,"bold"),bg="light blue",command=a1_right).grid(row=3,column=1)
    Button(frame1, text="31",font=("Arial",30,"bold"),bg="light green",command=a1_wrong).grid(row=3,column=2)
    Button(frame1, text="30",font=("Arial",30,"bold"),bg="light pink",command=a1_wrong).grid(row=3,column=3)
    
    Label(frame2, text="Output of 2**3 ?",font=("Arial",50,"bold")).grid(row=2,column=2)
    Button(frame2, text="6",font=("Arial",30,"bold"),bg="light blue",command=a2_right).grid(row=3,column=1)
    Button(frame2, text="8",font=("Arial",30,"bold"),bg="light green",command=a2_wrong).grid(row=3,column=2)
    Button(frame2, text="9",font=("Arial",30,"bold"),bg="light pink",command=a2_wrong).grid(row=3,column=3)

    Label(frame3, text="world most handsome man 2023 ?",font=("Arial",50,"bold")).grid(row=2,column=2)
    Button(frame3, text="kim taehyung",font=("Arial",30,"bold"),bg="light blue",command=a3_right).grid(row=3,column=1)
    Button(frame3, text="kim namjoon",font=("Arial",30,"bold"),bg="light green",command=a3_wrong).grid(row=3,column=2)
    Button(frame3, text="kim seokjin",font=("Arial",30,"bold"),bg="light pink",command=a3_wrong).grid(row=3,column=3)

    Label(frame4, text="what is the capital of south korea?",font=("Arial",50,"bold")).grid(row=2,column=2)
    Button(frame4, text="delhi",font=("Arial",30,"bold"),bg="light blue",command=a4_wrong).grid(row=3,column=1)
    Button(frame4, text="seoul",font=("Arial",30,"bold"),bg="light green",command=a4_right).grid(row=3,column=2)
    Button(frame4, text="beijing",font=("Arial",30,"bold"),bg="light pink",command=a4_wrong).grid(row=3,column=3)

    Label(frame5, text="which country is the land of rising sun",font=("Arial",50,"bold")).grid(row=2,column=2)
    Button(frame5, text="india",font=("Arial",30,"bold"),bg="light blue",command=a5_wrong).grid(row=3,column=1)
    Button(frame5, text="japan",font=("Arial",30,"bold"),bg="light green",command=a5_right).grid(row=3,column=2)
    Button(frame5, text="china",font=("Arial",30,"bold"),bg="light pink",command=a5_wrong).grid(row=3,column=3)


def a1_right():
    Label(frame1,text="correct",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame1,text="marks obtained : 1",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)

def a1_wrong():
    Label(frame1,text="incorrect",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame1,text="marks obtained : 0",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)
    
def a2_right():
    Label(frame2,text="correct",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame2,text="marks obtained : 1",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)

def a2_wrong():
    Label(frame2,text="incorrect",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame2,text="marks obtained : 0",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)

def a3_right():
    Label(frame3,text="correct",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame3,text="marks obtained : 1",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)

def a3_wrong():
    Label(frame3,text="incorrect",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame3,text="marks obtained : 0",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)

def a4_right():
    Label(frame4,text="correct",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame4,text="marks obtained : 1",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)

def a4_wrong():
    Label(frame4,text="incorrect",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame4,text="marks obtained : 0",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)

def a5_right():
    Label(frame5,text="correct",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame5,text="marks obtained : 1",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)

def a5_wrong():
    Label(frame5,text="incorrect",font=("Arial",40,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame5,text="marks obtained : 0",font=("Arial",40,"bold"),background="black",fg="white").grid(row=1,column=3)


quiz(y)
a.pack()  
root.mainloop()
