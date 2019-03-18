from tkinter import*

root=Tk()
root.configure(background="green")
root.geometry("350x260")

aboveFrame = Frame(root,bg="green")
aboveFrame.pack(fill=X)
settings=PhotoImage(file="settingsIcon.png")
btnSettings=Button(aboveFrame,image=settings,fg="black", bg="green")
label=Label(aboveFrame,text="Spotify_ sync_logo",fg="black",bg="green")
label.grid(ipadx=105,ipady=2,sticky=N+W)
btnSettings.grid(row=0,column=2,sticky=E)

bottomLeftFrame=Frame(root,bg="white")
menyFrame=Frame(root,bg="green")
menyFrame.pack(side=RIGHT)
bottomLeftFrame.pack(fill=X)
bottomRightFrame=Frame(root,bg="black")
bottomRightFrame.pack(fill=X)


mainFrame=Frame(root,bg="green")
middleFrame=Frame(mainFrame,bg="black")
def self():
    mainFrame.place(x=0,y=25,relheight="1",relwidth="0.884")
    middleFrame.grid()
    rps=PhotoImage(file="rps.png")
    botton_1=Button(middleFrame,image=rps,compound=TOP)
    botton_1.image=rps
    botton_1.grid(row=0,padx=5,pady=5)
    botton_2=Button(middleFrame,text="app_2",width=10, bg="white")
    botton_2.grid(row=0,column=1,padx=5,pady=5)
    botton_3=Button(middleFrame,text="app_3",width=10, bg="white")
    botton_3.grid(row=1,padx=5,pady=5)
    botton_4=Button(middleFrame,text="app_4",width=10, bg="white")
    botton_4.grid(row=1,column=1,padx=5,pady=5)
    

def backToMusic():
    mainFrame.place_forget()
    middleFrame.grid_forget()
    



music=PhotoImage(file="musicIcon.png")
musicSmall=PhotoImage(file="musicSmallIcon.png")
mute=PhotoImage(file="unmute.png")
vote=PhotoImage(file="voteIcon.png")
app=PhotoImage(file="appIcon.png")
group=PhotoImage(file="groupIcon.png")
btnMusic=Button(menyFrame,text="music",image=musicSmall,compound=TOP,borderwidth=2,relief="groove",fg="black", bg="green", command=backToMusic)
btnMusic.grid()
btnApp=Button(menyFrame,text="app", image=app,compound=TOP,borderwidth=2,relief="groove",fg="black", bg="green",command=self)
btnApp.grid()
btnVote=Button(menyFrame,text="vote", image=vote,compound=TOP,borderwidth=2,relief="groove",fg="black", bg="green")
btnVote.grid()
btnVote=Button(menyFrame,text="group", image=group,compound=TOP,borderwidth=2,relief="groove",fg="black", bg="green")
btnVote.grid()


label_1=Label(bottomLeftFrame,image=music,text="Currently playing",bg="white",  fg="white", anchor=E, font=("Helvetica",12,"bold", "italic"))
label_1_song=Label(bottomLeftFrame,text="Song: X",bg="white",fg="black",width=35)
label_1_artist=Label(bottomLeftFrame,text="artist: X",bg="white",fg="black",width=35)
label_1_duration=Label(bottomLeftFrame,text="Duration: mm:ss",bg="white",fg="black",width=35)
label_mute=Label(bottomLeftFrame,image=mute,bg="white")
label_2=Label(bottomRightFrame,text="Do you want to change song to ",bg="black",  fg="white", anchor=E,font=("Helvetica",12,"bold", "italic"))
label_2_song=Label(bottomRightFrame,text="Song: X",bg="black",fg="white",width=35)
label_2_artist=Label(bottomRightFrame,text="Artist: X",bg="black",fg="white",width=35)
label_2_change=Label(bottomRightFrame,text="Yes, I want to change to this song song",bg="black",fg="white",width=35)
cYes=Checkbutton(bottomRightFrame)
cNo=Checkbutton(bottomRightFrame)


label_1_song.grid(row=2,ipadx=5,ipady=2)
label_1_artist.grid(row=3,ipadx=5,ipady=2)
label_1_duration.grid(row=1,ipadx=5)
label_mute.grid(row=1,column=2,sticky="w")
label_1.grid(row=0,ipadx=5)
label_2.grid(columnspan=2)
label_2_song.grid()
label_2_artist.grid()
label_2_change.grid()
cYes.grid(row=3,column=1,columnspan=1)





root.mainloop()
