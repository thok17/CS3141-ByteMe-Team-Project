import unittest
import random

class TestMethods(unittest.TestCase):

    def test_No_Players(self):
        TeamOne = []
        ChoicesOne = []
        TeamTwo = []
        ChoicesTwo = []
        Team_One_Index = 0
        Team_Two_Index = 0
        game_over = True

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
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 2 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 1:
            print('Congrats Team Two!')
        if Final_Team_One_Choice != 4 and Final_Team_Two_Choice == 4:
            print('Congrats Team Two! You shot Team One with a Gun. Gun always wins!')
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 1 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 2:
            print('Congrats Team One!')
        if Final_Team_One_Choice == 4 and Final_Team_Two_Choice != 4:
            print('Congrats Team One! You shot Team Two with a Gun. Gun always wins!')

        assert Final_Team_One_Choice == 4 and Final_Team_Two_Choice == 4

    def test_Ending_One(self):
        Final_Team_One_Choice = 1
        Final_Team_Two_Choice = 1

        if Final_Team_One_Choice == Final_Team_Two_Choice:
            print('Congrats. Both teams lose and win because it is a tie.')
            winner = 3
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 2 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 1:
            print('Congrats Team Two!')
            winner = 2
        if Final_Team_One_Choice != 4 and Final_Team_Two_Choice == 4:
            print('Congrats Team Two! You shot Team One with a Gun. Gun always wins!')
            winner = 2
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 1 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 2:
            print('Congrats Team One!')
            winner = 1
        if Final_Team_One_Choice == 4 and Final_Team_Two_Choice != 4:
            print('Congrats Team One! You shot Team Two with a Gun. Gun always wins!')
            winner = 1

        assert winner == 3

    def test_Ending_One_Part_Two(self):
        Final_Team_One_Choice = 2
        Final_Team_Two_Choice = 2

        if Final_Team_One_Choice == Final_Team_Two_Choice:
            print('Congrats. Both teams lose and win because it is a tie.')
            winner = 3
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 2 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 1:
            print('Congrats Team Two!')
            winner = 2
        if Final_Team_One_Choice != 4 and Final_Team_Two_Choice == 4:
            print('Congrats Team Two! You shot Team One with a Gun. Gun always wins!')
            winner = 2
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 1 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 2:
            print('Congrats Team One!')
            winner = 1
        if Final_Team_One_Choice == 4 and Final_Team_Two_Choice != 4:
            print('Congrats Team One! You shot Team Two with a Gun. Gun always wins!')
            winner = 1

        assert winner == 3

    def test_Ending_One_Part_Three(self):
        Final_Team_One_Choice = 3
        Final_Team_Two_Choice = 3

        if Final_Team_One_Choice == Final_Team_Two_Choice:
            print('Congrats. Both teams lose and win because it is a tie.')
            winner = 3
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 2 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 1:
            print('Congrats Team Two!')
            winner = 2
        if Final_Team_One_Choice != 4 and Final_Team_Two_Choice == 4:
            print('Congrats Team Two! You shot Team One with a Gun. Gun always wins!')
            winner = 2
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 1 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 2:
            print('Congrats Team One!')
            winner = 1
        if Final_Team_One_Choice == 4 and Final_Team_Two_Choice != 4:
            print('Congrats Team One! You shot Team Two with a Gun. Gun always wins!')
            winner = 1

        assert winner == 3

    def test_Ending_One_Part_Four(self):
        Final_Team_One_Choice = 4
        Final_Team_Two_Choice = 4

        if Final_Team_One_Choice == Final_Team_Two_Choice:
            print('Congrats. Both teams lose and win because it is a tie.')
            winner = 3
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 2 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 1:
            print('Congrats Team Two!')
            winner = 2
        if Final_Team_One_Choice != 4 and Final_Team_Two_Choice == 4:
            print('Congrats Team Two! You shot Team One with a Gun. Gun always wins!')
            winner = 2
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 1 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 2:
            print('Congrats Team One!')
            winner = 1
        if Final_Team_One_Choice == 4 and Final_Team_Two_Choice != 4:
            print('Congrats Team One! You shot Team Two with a Gun. Gun always wins!')
            winner = 1

        assert winner == 3

    def test_Ending_Two(self):
        Final_Team_One_Choice = 1
        Final_Team_Two_Choice = 2

        if Final_Team_One_Choice == Final_Team_Two_Choice:
            print('Congrats. Both teams lose and win because it is a tie.')
            winner = 3
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 2 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 1:
            print('Congrats Team Two!')
            winner = 2
        if Final_Team_One_Choice != 4 and Final_Team_Two_Choice == 4:
            print('Congrats Team Two! You shot Team One with a Gun. Gun always wins!')
            winner = 2
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 1 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 2:
            print('Congrats Team One!')
            winner = 1
        if Final_Team_One_Choice == 4 and Final_Team_Two_Choice != 4:
            print('Congrats Team One! You shot Team Two with a Gun. Gun always wins!')
            winner = 1

        assert winner == 2

    def test_Ending_Two_Part_Two(self):
        Final_Team_One_Choice = 2
        Final_Team_Two_Choice = 3

        if Final_Team_One_Choice == Final_Team_Two_Choice:
            print('Congrats. Both teams lose and win because it is a tie.')
            winner = 3
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 2 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 1:
            print('Congrats Team Two!')
            winner = 2
        if Final_Team_One_Choice != 4 and Final_Team_Two_Choice == 4:
            print('Congrats Team Two! You shot Team One with a Gun. Gun always wins!')
            winner = 2
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 1 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 2:
            print('Congrats Team One!')
            winner = 1
        if Final_Team_One_Choice == 4 and Final_Team_Two_Choice != 4:
            print('Congrats Team One! You shot Team Two with a Gun. Gun always wins!')
            winner = 1

        assert winner == 2

    def test_Ending_Two_Part_Three(self):
        Final_Team_One_Choice = 3
        Final_Team_Two_Choice = 1

        if Final_Team_One_Choice == Final_Team_Two_Choice:
            print('Congrats. Both teams lose and win because it is a tie.')
            winner = 3
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 2 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 1:
            print('Congrats Team Two!')
            winner = 2
        if Final_Team_One_Choice != 4 and Final_Team_Two_Choice == 4:
            print('Congrats Team Two! You shot Team One with a Gun. Gun always wins!')
            winner = 2
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 1 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 2:
            print('Congrats Team One!')
            winner = 1
        if Final_Team_One_Choice == 4 and Final_Team_Two_Choice != 4:
            print('Congrats Team One! You shot Team Two with a Gun. Gun always wins!')
            winner = 1

        assert winner == 2

    def test_Ending_Three(self):
        Final_Team_One_Choice = 1
        Final_Team_Two_Choice = 4

        if Final_Team_One_Choice == Final_Team_Two_Choice:
            print('Congrats. Both teams lose and win because it is a tie.')
            winner = 3
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 2 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 1:
            print('Congrats Team Two!')
            winner = 2
        if Final_Team_One_Choice != 4 and Final_Team_Two_Choice == 4:
            print('Congrats Team Two! You shot Team One with a Gun. Gun always wins!')
            winner = 2
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 1 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 2:
            print('Congrats Team One!')
            winner = 1
        if Final_Team_One_Choice == 4 and Final_Team_Two_Choice != 4:
            print('Congrats Team One! You shot Team Two with a Gun. Gun always wins!')
            winner = 1

        assert winner == 2

    def test_Ending_Three_Part_Two(self):
        Final_Team_One_Choice = 2
        Final_Team_Two_Choice = 4

        if Final_Team_One_Choice == Final_Team_Two_Choice:
            print('Congrats. Both teams lose and win because it is a tie.')
            winner = 3
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 2 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 1:
            print('Congrats Team Two!')
            winner = 2
        if Final_Team_One_Choice != 4 and Final_Team_Two_Choice == 4:
            print('Congrats Team Two! You shot Team One with a Gun. Gun always wins!')
            winner = 2
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 1 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 2:
            print('Congrats Team One!')
            winner = 1
        if Final_Team_One_Choice == 4 and Final_Team_Two_Choice != 4:
            print('Congrats Team One! You shot Team Two with a Gun. Gun always wins!')
            winner = 1

        assert winner == 2

    def test_Ending_Three_Part_Three(self):
        Final_Team_One_Choice = 3
        Final_Team_Two_Choice = 4

        if Final_Team_One_Choice == Final_Team_Two_Choice:
            print('Congrats. Both teams lose and win because it is a tie.')
            winner = 3
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 2 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 1:
            print('Congrats Team Two!')
            winner = 2
        if Final_Team_One_Choice != 4 and Final_Team_Two_Choice == 4:
            print('Congrats Team Two! You shot Team One with a Gun. Gun always wins!')
            winner = 2
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 1 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 2:
            print('Congrats Team One!')
            winner = 1
        if Final_Team_One_Choice == 4 and Final_Team_Two_Choice != 4:
            print('Congrats Team One! You shot Team Two with a Gun. Gun always wins!')
            winner = 1

        assert winner == 2

    def test_Ending_Four(self):
        Final_Team_One_Choice = 1
        Final_Team_Two_Choice = 3

        if Final_Team_One_Choice == Final_Team_Two_Choice:
            print('Congrats. Both teams lose and win because it is a tie.')
            winner = 3
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 2 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 1:
            print('Congrats Team Two!')
            winner = 2
        if Final_Team_One_Choice != 4 and Final_Team_Two_Choice == 4:
            print('Congrats Team Two! You shot Team One with a Gun. Gun always wins!')
            winner = 2
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 1 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 2:
            print('Congrats Team One!')
            winner = 1
        if Final_Team_One_Choice == 4 and Final_Team_Two_Choice != 4:
            print('Congrats Team One! You shot Team Two with a Gun. Gun always wins!')
            winner = 1

        assert winner == 1

    def test_Ending_Four_Part_Two(self):
        Final_Team_One_Choice = 2
        Final_Team_Two_Choice = 1

        if Final_Team_One_Choice == Final_Team_Two_Choice:
            print('Congrats. Both teams lose and win because it is a tie.')
            winner = 3
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 2 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 1:
            print('Congrats Team Two!')
            winner = 2
        if Final_Team_One_Choice != 4 and Final_Team_Two_Choice == 4:
            print('Congrats Team Two! You shot Team One with a Gun. Gun always wins!')
            winner = 2
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 1 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 2:
            print('Congrats Team One!')
            winner = 1
        if Final_Team_One_Choice == 4 and Final_Team_Two_Choice != 4:
            print('Congrats Team One! You shot Team Two with a Gun. Gun always wins!')
            winner = 1

        assert winner == 1

    def test_Ending_Four_Part_Three(self):
        Final_Team_One_Choice = 3
        Final_Team_Two_Choice = 2

        if Final_Team_One_Choice == Final_Team_Two_Choice:
            print('Congrats. Both teams lose and win because it is a tie.')
            winner = 3
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 2 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 1:
            print('Congrats Team Two!')
            winner = 2
        if Final_Team_One_Choice != 4 and Final_Team_Two_Choice == 4:
            print('Congrats Team Two! You shot Team One with a Gun. Gun always wins!')
            winner = 2
        if Final_Team_One_Choice == 1 and Final_Team_Two_Choice == 3 or Final_Team_One_Choice == 2 and \
                Final_Team_Two_Choice == 1 or Final_Team_One_Choice == 3 and Final_Team_Two_Choice == 2:
            print('Congrats Team One!')
            winner = 1
        if Final_Team_One_Choice == 4 and Final_Team_Two_Choice != 4:
            print('Congrats Team One! You shot Team Two with a Gun. Gun always wins!')
            winner = 1

        assert winner == 1
