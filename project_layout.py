from tkinter import*
root=Tk()
root.configure(background="green")
root.geometry("700x400")

aboveFrame = Frame(root,bg="green")
aboveFrame.pack(fill=X)
middleFrame=Frame(root,bg="black")
middleFrame.place(x=0,y=100)
label=Label(aboveFrame,text="Spotify_ sync",fg="black",bg="green")
label.grid(ipadx=2,ipady=2,sticky=N+W)

buttomFrame=Frame(root,bg="white")
buttomFrame.place(x=0,y=200)


button_1=Button(middleFrame,text="app_1",width=10, bg="white")
button_1.grid(row=0,padx=5,pady=5)
button_2=Button(middleFrame,text="app_2",width=10, bg="white")
button_2.grid(row=0,column=1,padx=5,pady=5)
button_3=Button(middleFrame,text="app_3",width=10, bg="white")
button_3.grid(row=1,padx=5,pady=5)
button_4=Button(middleFrame,text="app_4",width=10, bg="white")
button_4.grid(row=1,column=1,padx=5,pady=5)

label_1=Label(buttomFrame,text="Currently playing: ",bg="white")
label_2=Label(buttomFrame,text="Song: X, Artist: Y, Year: Y",bg="white")
label_3=Label(buttomFrame,text="Duration: mm:ss",bg="white")
label_1.grid(sticky=W)
label_2.grid(sticky=W)
label_3.grid(sticky=W)


root.mainloop()
