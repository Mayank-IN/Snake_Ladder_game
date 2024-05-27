from default_game import DefaultGame
from config_game import ConfigGame
from player_position import PlayerPosition
from game_runner import GameRunner
import math


class Main:

    def __init__(self):
        self.players=[]
        self.default = DefaultGame()
        self.config = ConfigGame()

    '''
    This method load the player names to the PlayerPosition class with position attribute set at 0
    '''
    def load_player(self, player_name):

        player = PlayerPosition(player_name)
        self.players.append(player)

    '''
    This is the starting point in the project
    '''
    def snake_ladder_game(self):
        print("****************************<Welcome Snake & Ladder Game>********************************")
        '''
        While loop for continues interaction
        '''
        while True:

            try:
                # Choose Number of Player
                player_number = int(input("Enter Player Number"
                                          "(Minimum Number is 2): "))
                '''
                Condition to check Minimum Number of player(which is 2)
                '''
                if player_number < 2:
                    print("Player Number should be greater than 2")
                    continue

                # Adding Player Name

                for i in range(player_number):
                    self.load_player(input("Enter Player "+str(i+1)+" Name\n"))

                player_choice = int(input("Enter 0 for default Game\n"
                                          "Enter 1 to Configure the Game\n"))            # Choose of Game

                if player_choice == 0:
                    game = self.default.game_config()  # Calling DefaultGame Class
                    break

                # Configuration Choice
                elif player_choice == 1:
                    while 1:
                        board_size = int(input("Enter the size of board "
                                               "(should be a perfect square):\n"))  # Choosing board size
                        '''
                        Size of board should be perfect square (Condition checking)
                        '''
                        if board_size != int(math.sqrt(board_size)) ** 2:
                            print("Enter perfect square for a board size")
                        else:
                            break
                    game = self.config.config_game(board_size)  # Calling ConfigGame Class
                    break

                else:
                    print("Please Enter among given choices\n")   # print If User Input different choice
            except ValueError:
                print("Enter Among given Choices ")

        # Start Playing the Game
        play = GameRunner(game, self.players)
        play.start()
        self.restart()

    '''
    this is to re-start the game  
    '''
    @staticmethod
    def restart():

        choice = input("\nEnter 1 to ReStart the Game"
                           "\nEnter Any Number to Exit the Game\n")
        if choice == 1:
            Main()
        else:
            exit()


Main().snake_ladder_game()
