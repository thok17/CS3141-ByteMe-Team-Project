from tkinter import*
import os
import sys
import subprocess

voteCount=0
groupCount=0
profileCount=0


def apps():
    mainFrameVote.place_forget()
    mainFrameGroup.place_forget()
    mainFrameProfile.place_forget()
    mainFrameApp.place(x=0,y=25,relheight="1",relwidth="0.884")
    middleFrame.pack()
    rps=PhotoImage(file="rps.png")
    botton_1=Button(middleFrame,image=rps,compound=TOP, command=rps1)
    botton_1.image=rps
    botton_1.grid(row=0,padx=10,pady=10)
    botton_2=Button(middleFrame,text="app_2",width=10, bg="white")
    botton_2.grid(row=0,column=1,padx=10,pady=10)
    botton_3=Button(middleFrame,text="app_3",width=10, bg="white")
    botton_3.grid(row=1,padx=10,pady=10)
    botton_4=Button(middleFrame,text="app_4",width=10, bg="white")
    botton_4.grid(row=1,column=1,padx=10,pady=10)
def rps1():
    subprocess.Popen('python RPS_GUI.py')
    

def votes():
    global voteCount
    mainFrameGroup.place_forget()
    mainFrameApp.place_forget()
    mainFrameProfile.place_forget()
    mainFrameVote.place(x=0,y=25,relheight="1",relwidth="0.884")
    if (voteCount==0):
        lblVote=Label(mainFrameVote,text="This is the vote room",font=("Helvetica",12,"bold", "italic"))
        lblVote.pack()
    voteCount+=1


def profiles():
    global profileCount
    mainFrameGroup.place_forget()
    mainFrameApp.place_forget()
    mainFrameVote.place_forget()
    mainFrameProfile.place(x=0,y=25,relheight="1",relwidth="0.884")
    if (profileCount==0):
        lblProfile=Label(mainFrameProfile,text="This room will show some user \n information from Spotify profile",font=("Helvetica",12,"bold", "italic"))
        lblProfile.pack()
    profileCount+=1
def groups():
    global groupCount
    mainFrameVote.place_forget()
    mainFrameApp.place_forget()
    mainFrameProfile.place_forget()
    mainFrameGroup.place(x=0,y=25,relheight="1",relwidth="0.884")
    if (groupCount==0):
        lblGroups=Label(mainFrameGroup,text="This room will show who's in the group, \n and give options for leaving the group \n or add new members to the group",font=("Helvetica",12,"bold", "italic"))
        lblGroups.pack()
    groupCount+=1

def backToMusic():
    mainFrameApp.place_forget()
    mainFrameVote.place_forget()
    mainFrameProfile.place_forget()
    mainFrameGroup.place_forget()
    
    
root=Tk()
root.configure(background="green")
root.geometry("350x260")
root.maxsize(350,260)
root.title('Spotify sync')




aboveFrame = Frame(root,bg="green")
aboveFrame.pack(side=TOP,fill=X)
profile=PhotoImage(file="profileIcon.png")
btnProfile=Button(aboveFrame,image=profile,fg="black", bg="green",command=profiles)
lblProfile=Label(aboveFrame,text="Spotify_ sync_logo",fg="black",bg="green")
btnProfile.pack(side=RIGHT,ipadx=5)
lblProfile.pack()

menubar = Menu(btnProfile)
setting = Menu(menubar, tearoff=0)
setting.add_command(label="something")
setting.add_command(label="something")
setting.add_separator()
setting.add_command(label="Log out", command=root.quit)
menubar.add_cascade(label="Settings", menu=setting)







# display the menu
root.config(menu=menubar)

#label.grid(ipadx=105,ipady=2,sticky=N+W)
#btnSettings.grid(row=0,column=2,sticky=E)

bottomLeftFrame=Frame(root,bg="white")
menyFrame=Frame(root,bg="green")
menyFrame.pack(side=RIGHT,fill=Y)
bottomLeftFrame.pack(fill=X)
bottomRightFrame=Frame(root,bg="black")
bottomRightFrame.pack(fill=X)

#Frames for our app-layout
mainFrameApp=Frame(root,bg="green")
middleFrame=Frame(mainFrameApp,bg="black")

#Frame for our vote-layout
mainFrameVote=Frame(root,bg="green")

#Frame for our group-layout
mainFrameGroup=Frame(root,bg="green")
#Frame for our profile-layout
mainFrameProfile=Frame(root,bg="green")




    



music=PhotoImage(file="musicIcon.png")
musicSmall=PhotoImage(file="musicSmallIcon.png")
mute=PhotoImage(file="unmute.png")
vote=PhotoImage(file="voteIcon.png")
app=PhotoImage(file="appIcon.png")
group=PhotoImage(file="groupIcon.png")
btnMusic=Button(menyFrame,text="music",image=musicSmall,compound=TOP,borderwidth=2,relief="groove",fg="black", bg="green", command=backToMusic)
btnMusic.grid()
btnApp=Button(menyFrame,text="app", image=app,compound=TOP,borderwidth=2,relief="groove",fg="black", bg="green",command=apps)
btnApp.grid()
btnVote=Button(menyFrame,text="vote", image=vote,compound=TOP,borderwidth=2,relief="groove",fg="black", bg="green",command=votes)
btnVote.grid()
btnGroup=Button(menyFrame,text="group", image=group,compound=TOP,borderwidth=2,relief="groove",fg="black", bg="green",command=groups)
btnGroup.grid()


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
