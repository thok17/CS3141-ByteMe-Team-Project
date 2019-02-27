from tkinter import*
root=Tk()
root.configure(background="green")
root.geometry("500x300")

aboveFrame = Frame(root,bg="green")
aboveFrame.pack(fill=X)
middleFrame=Frame(root,bg="black")
middleFrame.place(x=0,y=100)
label=Label(aboveFrame,text="Spotify_ sync",fg="black",bg="green")
label.grid(ipadx=2,ipady=2,sticky=N+W)

buttomFrame=Frame(root,bg="black")
buttomFrame.place(x=0,y=220)


button_1=Button(middleFrame,text="app_1",width=10, bg="white")
button_1.grid(row=0,padx=5,pady=5)
button_2=Button(middleFrame,text="app_2",width=10, bg="white")
button_2.grid(row=0,column=1,padx=5,pady=5)
button_3=Button(middleFrame,text="app_3",width=10, bg="white")
button_3.grid(row=1,padx=5,pady=5)
button_4=Button(middleFrame,text="app_4",width=10, bg="white")
button_4.grid(row=1,column=1,padx=5,pady=5)

label_1=Label(buttomFrame,text="Currently playing: ",bg="black",  fg="white", anchor=E, font=("Helvetica",13,"bold", "italic"))
label_2=Label(buttomFrame,text="Song: X, Artist: Y, Year: Y",bg="black",fg="white",width=25)
label_3=Label(buttomFrame,text="Duration: mm:ss",bg="black",fg="white",width=25)
label_1.pack()
label_2.pack()
label_3.pack()


root.mainloop()
