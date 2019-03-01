from tkinter import*

root=Tk()
root.configure(background="green")
root.geometry("600x300")

aboveFrame = Frame(root,bg="green")
aboveFrame.pack(fill=X)
middleFrame=Frame(root,bg="black")
middleFrame.place(x=0,y=100)
label=Label(aboveFrame,text="Spotify_ sync",fg="black",bg="green")
label.grid(ipadx=2,ipady=2,sticky=N+W)

bottomLeftFrame=Frame(root,bg="black")
bottomLeftFrame.place(x=0,y=220)
bottomRightFrame=Frame(root,bg="black")
bottomRightFrame.place(x=300,y=220)



botton_1=Button(middleFrame,text="app_1",width=10, bg="white")
botton_1.grid(row=0,padx=5,pady=5)
botton_2=Button(middleFrame,text="app_2",width=10, bg="white")
botton_2.grid(row=0,column=1,padx=5,pady=5)
botton_3=Button(middleFrame,text="app_3",width=10, bg="white")
botton_3.grid(row=1,padx=5,pady=5)
botton_4=Button(middleFrame,text="app_4",width=10, bg="white")
botton_4.grid(row=1,column=1,padx=5,pady=5)

label_1=Label(bottomLeftFrame,text="Currently playing",bg="black",  fg="white", anchor=E, font=("Helvetica",12,"bold", "italic"))
label_2=Label(bottomLeftFrame,text="Song: X, Artist: Y, Year: Y",bg="black",fg="white",width=35)
label_3=Label(bottomLeftFrame,text="Duration: mm:ss",bg="black",fg="white",width=35)
label_4=Label(bottomRightFrame,text="Do you want to change song to ",bg="black",  fg="white", anchor=E,font=("Helvetica",12,"bold", "italic"))
label_5=Label(bottomRightFrame,text="Song: X, Artist: Y, Year: Y",bg="black",fg="white",width=35)
label_6=Label(bottomRightFrame,text="Yes, I want to change to this song song",bg="black",fg="white",width=35)
cYes=Checkbutton(bottomRightFrame)
cNo=Checkbutton(bottomRightFrame)


label_2.grid(row=2,ipadx=5,ipady=2)
label_3.grid(row=1,ipadx=5)
label_1.grid(row=0,ipadx=5)
label_4.grid(columnspan=2)
label_5.grid()
label_6.grid()
cYes.grid(row=2,column=1,columnspan=1)


root.mainloop()
