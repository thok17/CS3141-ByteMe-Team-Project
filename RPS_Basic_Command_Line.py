
import random

TeamOne = []
ChoicesOne = []
TeamTwo = []
ChoicesTwo = []
Team_One_Index = 0
Team_Two_Index = 0
game_over = False


def do_stuff():
    print(
        'Welcome to Rock, Paper, Scissors! The game of all kids to decide on something. '
        '\n(Psst if it\'s a draw the start the program again! ;D)'
        '\nSo how to play. Well, it\'s simple. Pick 1 for Rock, 2 for Paper and 3 for Scissors. '
        '\nSo Rock beats Scissors. Scissors cuts Paper and Paper covers Rock. Got it Lets play')
    number_of_players = int(input('Please input the number of players: '))
    if number_of_players <= 0:
        game_over = True
    else:
        for x in range(number_of_players):
            name_of_player = str(input('Please enter your name: '))
            team_player_wants = int(input(
                'What team would you like to join? \n1 or 2? \n Hint: If you do not put either 1 or 2, something bad happens. '))
            if team_player_wants == 1:
                TeamOne.append(name_of_player)
                global Team_One_Index
                Team_One_Index += 1
            if team_player_wants == 2:
                TeamTwo.append(name_of_player)
                global Team_Two_Index
                Team_Two_Index += 1
                pass
            if team_player_wants != 1 and team_player_wants != 2:
                game_over = True
                pass


def play_game():
    if game_over == True:
        computer_One_choice = 4
        computer_Two_choice = 4
    else:
        computer_One_choice = random.randint(1, 3)
        computer_Two_choice = random.randint(1, 3)
    if Team_One_Index != 0:
        for y in range(len(TeamOne)):
            TeamOne.reverse()
            name_of_player = TeamOne.pop()
            print(name_of_player + '. What do you want to play?')
            the_Choice = int(input('Reminder: 1 = Rock, 2 = Paper, 3 = Scissors \nYour choice: '))
            if the_Choice != 1 or the_Choice != 2 or the_Choice != 3:
                ChoicesOne.append(random.randint(1, 3))
            else:
                ChoicesOne.append(the_Choice)
        Final_Team_One_Choice = ChoicesOne[random.randint(0, (Team_One_Index - 1))]
    else:
        Final_Team_One_Choice = computer_One_choice
    if Team_Two_Index != 0:
        for w in range(len(TeamTwo)):
            TeamTwo.reverse()
            name_of_player = TeamTwo.pop()
            print(name_of_player + '. What do you want to play?')
            the_Choice = int(input('Reminder: 1 = Rock, 2 = Paper, 3 = Scissors \nYour choice: '))
            if the_Choice != 1 or the_Choice != 2 or the_Choice != 3:
                ChoicesTwo.append(random.randint(1, 3))
            else:
                ChoicesTwo.append(the_Choice)
        Final_Team_Two_Choice = ChoicesTwo[random.randint(0, (Team_Two_Index - 1))]
    else:
        Final_Team_Two_Choice = computer_Two_choice
    if Final_Team_One_Choice == Final_Team_Two_Choice:
        print('Congrats. Both teams lose and win because it is a tie.')
    if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 2 or Final_Team_One_Choice == 2 and Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 1:
        print('Congrats Team Two!')
    if Final_Team_One_Choice != 4 and Final_Team_Two_Choice == 4:
        print('Congrats Team Two! You shot Team One with a Gun. Gun always wins!')
    if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 2 and Final_Team_Two_Choice == 1 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 2:
        print('Congrats Team One!')
    if Final_Team_One_Choice == 4 and Final_Team_Two_Choice != 4:
        print('Congrats Team One! You shot Team Two with a Gun. Gun always wins!')


do_stuff()
play_game()
