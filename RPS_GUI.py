from tkinter import *
import sys
import os

import random

TeamOne = []
ChoicesOne = []
TeamTwo = []
ChoicesTwo = []
Team_One_Index = 0
Team_Two_Index = 0
game_over = False
counter_One = 1;

def theyAreWantRock():
	the_Choice = 1
	if Team_One_Index > 0:
		ChoicesOnes.append(the_Choice)
		Team_One_Index += -1
	else:
		ChoicesTwo.append(the_Choice)
		Team_Two_Index += -1
	
		
def theyAreWantPaper():
	the_Choice = 2
	if Team_One_Index > 0:
		ChoicesOnes.append(the_Choice)
		Team_One_Index += -1
	else:
		ChoicesTwo.append(the_Choice)
		Team_Two_Index += -1

def theyAreWantScissor():
	the_Choice = 3
	if Team_One_Index > 0:
		ChoicesOnes.append(the_Choice)
		Team_One_Index += -1
	else:
		ChoicesTwo.append(the_Choice)
		Team_Two_Index += -1		
		
def loopForTeamOne(gameWindow):
	if Team_One_Index != 0:
		name_of_player = TeamOne.pop()
		gameWindow.label_name['text'] = "Please choose Rock, Paper or Scissors {}:".format(name_of_player)
		loopForTeamOne(gameWindow)
		
def loopForTeamTwo(gameWindow):
	if Team_Two_Index != 0:
		name_of_player = TeamTwo.pop()
		gameWindow.label_name['text'] = "Please choose Rock, Paper or Scissors {}:".format(name_of_player)
		loopForTeamTwo(gameWindow)		

def settingUpTheGame(gameWindow):
        gameWindow = Tk()
        gameWindow.title("Let's play!")
        label_name = Label(gameWindow, text='Welcome to the game!', font='Bizon 20 bold', bg='PeachPuff2')
        gameWindow.maxsize(300, 250)
        gameWindow.minsize(300, 250)
        gameWindow.config(background='White')
        rock = Button(gameWindow, text='Rock', width=8, font='Bizon 20 bold', bg='Black', fg='Yellow', relief=RIDGE, bd=0, command=lambda:theyAreWantRock)
        rock.place(x=75, y=225)
        paper = Button(gameWindow, text='Paper', width=8, font='Bizon 20 bold', bg='Black', fg='Yellow', relief=RIDGE, bd=0, command=lambda:theyAreWantPaper)
        paper.place(x=100, y=225)
        scissor = Button(gameWindow, text='Scissors', width=8, font='Bizon 20 bold', bg='Black', fg='Yellow', relief=RIDGE, bd=0, command=lambda:theyAreWantScissor)
        scissor.place(x=125, y=225)
        TeamOne.reverse()
        TeamTwo.reverse()
        computer_One_choice = random.randint(1,3)
        computer_Two_choice = random.randint(1,3)
        if Team_One_Index != 0:
                loopForTeamOne(gameWindow)
        else:
                Final_Team_One_Choice = computer_One_choice
        if Team_Two_Index != 0:
                loopForTeamTwo(gameWindow)
        else:
                Final_Team_Two_Choice = computer_Two_choice		

def theyWantTeamOne():
	team_player_wants = 1
	counter_One += 1
	nameTeamGetProcess(counter_One, startWindow)
	
def theyWantTeamTwo():
	team_player_wants = 2
	counter_One += 1
	nameTeamGetProcess(counter_One, startWindow)


def nameTeamGetProcess(counter_One, startWindow):
        if counter_One > 1:
                name_of_player = v.get()
                if team_player_wants == 1:
                        TeamOne.append(name_of_player)
                        global Team_One_Index
                        Team_One_Index += 1
                if team_player_wants == 2:
                        TeamTwo.append(name_of_player)
                        global Team_Two_Index
                        Team_Two_Index += 1
        if counter_One <= number_of_players:
                v.set("Please enter your name Player {}:".format(counter_One))
                name_of_player = raw_input('Please enter your name: ')
                startWindow.label_1['text'] = "Please enter your name Player {}:".format(counter_One)
        if counter_One > number_of_players:	
                settingUpTheGame()	

def doStuff(startWindow):
	#Close [startWindow] before advancing:
	s = v.get()
	number_of_players = int(s)
	
	startWindow.destroy()
	startWindow.quit()

	master = Tk()
	master.title('Lets Play!')
	master.maxsize(300, 250)
	master.minsize(300, 250)
	master.config(background='Yellow')
	
	label_1 = Label(master, text='Welcome to the set up!', font='Bizon 20 bold', bg='PeachPuff2')
	label_1.pack(side=TOP)
	v = StringVar()
	e = Entry(master, textvariable=v)
	e.pack()
	v.place(x=75, y=100)
	if number_of_players <= 0:
		game_over = True
	else:
		counter_One = 1;
		clickForTeamOne = Button(startWindow, text='Team 1', width=8, font='Bizon 20 bold', bg='Black', fg='Yellow', relief=RIDGE, bd=0, command=lambda:theyWantTeamOne(counter_One))
		clickForTeamOne.place(x=75, y=225)
		clickForTeamTwo = Button(startWindow, text='Team 2', width=8, font='Bizon 20 bold', bg='Black', fg='Yellow', relief=RIDGE, bd=0, command=lambda:theyWantTeamTwo(counter_One))
		clickForTeamOne.place(x=100, y=225)
		nameTeamGetProcess(startWindow)
	


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
