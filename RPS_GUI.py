from tkinter import *
import os
import sys

import random

TeamOne = []
ChoicesOne = []
TeamTwo = []
ChoicesTwo = []
Team_One_Index = 0
Team_Two_Index = 0
game_over = False
counter_One = 1;
Final_Team_One_Choice=1;
Final_Team_Two_Choice=1;
gameWindow=1;
winnerWindow=1;

def restart():
        global winnerWindow
        winnerWindow.destroy()
        winnerWindow.quit()
        startWindow = Tk()
        startWindow.title('Group Rock Paper Scissors')
        startWindow.maxsize(300, 250)
        startWindow.minsize(300, 250)
        startWindow.config(background='Black')
        v=StringVar()
        lblEntry = Label(text="Please input the number of players: ",bg="black", fg="white")
        e = Entry(startWindow,textvariable=v)
        lblEntry.pack()
        e.pack()
        clickToPlay = Button(startWindow, text='Play!', width=8, font='Bizon 20 bold', bg='Black', fg='Yellow', relief=RIDGE, bd=0, command=lambda:doStuff(startWindow))
        clickToPlay.place(x=75, y=125)
        startWindow.mainloop()


def theyAreWantRock():
        the_Choice = 1
        global Team_One_Index
        global Team_Two_Index
        if Team_One_Index > 0:
                ChoicesOne.append(the_Choice)
                Team_One_Index -= 1
                loopForTeamOne()
        else:
                ChoicesTwo.append(the_Choice)
                Team_Two_Index -= 1
                loopForTeamTwo()
        
                
def theyAreWantPaper():
        the_Choice = 2
        global Team_One_Index
        global Team_Two_Index
        if Team_One_Index > 0:
                ChoicesOne.append(the_Choice)
                Team_One_Index -= 1
                loopForTeamOne()
        elif Team_Two_Index>0:
                ChoicesTwo.append(the_Choice)
                Team_Two_Index -= 1
                loopForTeamTwo()

def theyAreWantScissor():
        the_Choice = 3
        global Team_One_Index
        global Team_Two_Index
        if Team_One_Index > 0:
                ChoicesOne.append(the_Choice)
                Team_One_Index -= 1
                loopForTeamOne()
        else:
                ChoicesTwo.append(the_Choice)
                Team_Two_Index -= 1
                loopForTeamTwo()
                
def loopForTeamOne():
        global Team_One_Index
        global Team_Two_Index
        if (Team_One_Index!=0):
                name_of_player = TeamOne.pop()
                label_name['text'] = "Please do your move\n{}:".format(name_of_player)
        else:
                global Final_Team_One_Choice
                Final_Team_One_Choice = ChoicesOne[random.randint(0,len(ChoicesOne)-1)]
                if (Team_Two_Index!=0):
                        loopForTeamTwo()
                else:
                        winner()
                #Team_One_Index-=1           
                #loopForTeamOne(gameWindow)
        
                
def loopForTeamTwo():
        global Team_Two_Index
        if (Team_Two_Index !=0):
                name_of_player = TeamTwo.pop()
                label_name['text'] = "Please do your move\n{}:".format(name_of_player)
        else:
                global Final_Team_Two_Choice
                Final_Team_Two_Choice = ChoicesTwo[random.randint(0,len(ChoicesTwo)-1)]
                winner()
                #Team_Two_Index-=1
                #loopForTeamTwo(gameWindow)

def settingUpTheGame(set_up_window):
        set_up_window.destroy()
        set_up_window.quit()
        global gameWindow
        gameWindow = Tk()
        gameWindow.title("Let's play!")
        gameWindow.maxsize(300, 250)
        gameWindow.minsize(300, 250)
        global label_name
        label_name = Label(gameWindow, text='Welcome to the game!', font='Bizon 20 bold', bg='PeachPuff2')
        label_name.pack(side=TOP)
        #gameWindow.maxsize(300, 250)
        gameWindow.minsize(300, 250)
        gameWindow.config(background='White')
        rock = Button(gameWindow, text='Rock', width=8, font='Bizon 12 bold', bg='Black', fg='Yellow', relief=RIDGE, bd=0, command=theyAreWantRock)
        rock.place(x=0, y=125)
        paper = Button(gameWindow, text='Paper', width=8, font='Bizon 12 bold', bg='Black', fg='Yellow', relief=RIDGE, bd=0, command=theyAreWantPaper)
        paper.place(x=100, y=125)
        scissor = Button(gameWindow, text='Scissors', width=8, font='Bizon 12 bold', bg='Black', fg='Yellow', relief=RIDGE, bd=0, command=theyAreWantScissor)
        scissor.place(x=200, y=125)
        TeamOne.reverse()
        TeamTwo.reverse()
        computer_One_choice = random.randint(1,3)
        computer_Two_choice = random.randint(1,3)
        if Team_One_Index==0:
                global Final_Team_One_Choice
                Final_Team_One_Choice = computer_One_choice
        if Team_Two_Index==0:
                global Final_Team_Two_Choice
                Final_Team_Two_Choice = computer_One_choice
        
        if Team_One_Index != 0:
                loopForTeamOne()
       #else:Final_Team_One_Choice = computer_One_choice"""
        elif (Team_Two_Index != 0):
                loopForTeamTwo()
        #else:Final_Team_Two_Choice = computer_Two_choice"""
        else:
                winner()

def winner():
        global gameWindow
        gameWindow.destroy()
        gameWindow.quit()
        global winnerWindow
        winnerWindow = Tk()
        winnerWindow.title("The game has ended")
        winnerWindow.maxsize(300, 250)
        winnerWindow.minsize(300, 250)
        winner=PhotoImage(file="winnerIcon.png")
        winnerlbl=Label(winnerWindow,image=winner,compound=TOP)
        winnerlbl.image=winner
        label_name = Label(winnerWindow, text='', font='Bizon 15 bold', bg='PeachPuff2')
        winnerlbl.pack()
        label_name.pack(side=TOP)
        global Final_Team_One_Choice
        global Final_Team_Two_Choice
        print(Final_Team_One_Choice)
        print(Final_Team_Two_Choice)
        if Final_Team_One_Choice == Final_Team_Two_Choice:
                label_name['text']='Congrats! \n Both teams lose and win \nbecause it is a tie.'
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 2 or Final_Team_One_Choice == 2 and Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 1:
                label_name['text']='Congrats Team Two!'
        if Final_Team_One_Choice != 4 and Final_Team_Two_Choice == 4:
                label_name['text']='Congrats Team Two! \n You shot Team One with a Gun.\nGun always wins!'
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 2 and Final_Team_Two_Choice == 1 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 2:
                label_name['text']='Congrats Team One!'
        if Final_Team_One_Choice == 4 and Final_Team_Two_Choice != 4:
               label_name['text']=='Congrats Team One! \n You shot Team Two with a Gun. \n Gun always wins!'
        replay = Button(winnerWindow, text='Play again', width=8, font='Bizon 10 bold', bg='Black', fg='Yellow', relief=RIDGE, bd=0, command=restart)
        replay.pack(side=TOP,pady=10)
        mainloop()
        

def theyWantTeamOne(set_up_window,number_of_players):
        team_player_wants = 1
        global counter_One
        counter_One += 1
        nameTeamGetProcess(set_up_window,number_of_players,counter_One, startWindow,team_player_wants)
        
def theyWantTeamTwo(set_up_window,number_of_players):
        team_player_wants = 2
        global counter_One
        counter_One += 1
        nameTeamGetProcess(set_up_window,number_of_players,counter_One, startWindow,team_player_wants)


#I needed to let number_of_players to be a parameter here as well. 
def nameTeamGetProcess(set_up_window,number_of_players,counter_One, startWindow,team_player_wants):
        if counter_One > 1:
                name_of_player = v.get()
                v.set('')
                print(name_of_player)
                if team_player_wants == 1:
                        TeamOne.append(name_of_player)
                        global Team_One_Index
                        Team_One_Index += 1
                if team_player_wants == 2:
                        TeamTwo.append(name_of_player)
                        global Team_Two_Index
                        Team_Two_Index += 1
        if counter_One <= number_of_players:
                #.set("Please enter your name Player {}:".format(counter_One))
                #need to define raw_input
                #name_of_player = raw_input('Please enter your name: ')
                label_1['text'] = "Please enter your name Player {}\nthen click the team you want to join: ".format(counter_One)
        if counter_One > number_of_players:     
                settingUpTheGame(set_up_window) 

#This problem got fixed by letting v be a parameter in the function as well. 
def doStuff(startWindow):
        #Close [startWindow] before advancing:
        global v
        s = v.get()
        number_of_players = int(s)
        
        startWindow.destroy()
        startWindow.quit()
        if number_of_players==0:
                global Final_Team_One_Choice
                global Final_Team_Two_Choice
                Final_Team_One_Choice=random.randint(1,3)
                Final_Team_Two_Choice=random.randint(1,3)
                global gameWindow
                gameWindow=Tk()
                winner()
                mainloop()
                

        set_up_window = Tk()
        set_up_window.title('Lets Play!')
        #master.maxsize(300, 250)
        set_up_window.minsize(300, 250)
        set_up_window.config(background='Yellow')
        
        
        label_set_Up=Label(set_up_window, text='Welcome to the set up!', font='Bizon 20 bold', bg='PeachPuff2')
        label_set_Up.pack(side=TOP,fill=X)
        global label_1
        label_1=Label(set_up_window,text='Please enter your name player 1,\nthen click the team you want to join: ', font='Bizon 15 bold', bg='PeachPuff2')
        label_1.pack()
        v = StringVar()
        e = Entry(set_up_window, textvariable=v)
        e.pack()
        clickForTeamOne = Button(set_up_window, text='Team 1', width=8, font='Bizon 20 bold', bg='Black', fg='Yellow', relief=RIDGE, bd=0, command=lambda:theyWantTeamOne(set_up_window,number_of_players))
        clickForTeamOne.place(x=5, y=125)
        clickForTeamTwo = Button(set_up_window, text='Team 2', width=8, font='Bizon 20 bold', bg='Black', fg='Yellow', relief=RIDGE, bd=0, command=lambda:theyWantTeamTwo(set_up_window,number_of_players))
        clickForTeamTwo.place(x=150, y=125)
                #nameTeamGetProcess(number_of_players,counter_One,set_up_window,0)
        mainloop()
        


startWindow = Tk()
startWindow.title('Group Rock Paper Scissors')
startWindow.maxsize(300, 250)
startWindow.minsize(300, 250)
startWindow.config(background='Black')
v=StringVar()
lblEntry = Label(text="Please input the number of players: ",bg="black", fg="white")
e = Entry(startWindow,textvariable=v)
lblEntry.pack()
e.pack()
clickToPlay = Button(startWindow, text='Play!', width=8, font='Bizon 20 bold', bg='Black', fg='Yellow', relief=RIDGE, bd=0, command=lambda:doStuff(startWindow))
clickToPlay.place(x=75, y=125)



startWindow.mainloop()
