from dice import Dice
from time import sleep


class GameRunner:
    def __init__(self, game, players):
        self.game = game
        self.players = players
        self.dice = Dice()
        self.win_list = []

    '''
    Checking to snake position 
    '''
    def check_snake(self, current_position):
        for position in self.game.snake_list:
            if current_position == position:
                return self.game.snake_list.get(position)
        return 0

    '''
    Checking to Ladder position 
    '''
    def check_ladder(self, current_position):
        for position in self.game.ladder_list:
            if current_position == position:
                return self.game.ladder_list.get(position)
        return 0

    '''
    Checking to Win
    '''
    def check_for_win(self, current_position):
        if current_position == self.game.board_size:
            return True
        else:
            return False

    '''
    Game is played in this method
    '''
    def start(self):

        new_position = 0    # Reference local variable

        still_playing = len(self.players) - 1

        while still_playing:

            for player in self.players:

                initial_position = current_position = player.position
                print(player.player_name, "Chance:\nCurrent Position : ", initial_position)
                '''
                Turn variable is used for counting the occurrence of 6 on dice
                '''
                turn = 0
                while 1:
                    flag = 1
                    '''
                    Flag variable gives signal if new_position is greater than board size
                    '''
                    dice_value = self.dice.roll()                       # Dice Rolling
                    print("Dice Rolling...")
                    sleep(1)
                    print("You get: ", dice_value)

                    '''Condition to check the new_position is lesser than board size & used here for better experience'''
                    if dice_value + current_position <= self.game.board_size:
                        if dice_value == 6:
                            sleep(1)
                            print("\nYou get Another Chance:")
                            input("\nClick Enter for Another Chance")
                            turn += 1
                            continue
                        else:
                            '''
                            Occurrence of 6 is even than add it twice to the dice_value else once
                            '''
                            if turn % 2 == 0 and turn != 0:
                                dice_value += 6*2
                            elif turn != 0:
                                dice_value += 6

                        new_position = current_position + dice_value
                        '''Condition to check the new_position is lesser than board size'''
                        if new_position <= self.game.board_size:

                            if self.check_ladder(new_position) != 0:       # Ladder Checking
                                current_position = new_position = self.check_ladder(new_position)
                                turn = 0
                                print("WoW You climb the Ladder(^_^) to {position}"
                                      .format(position=new_position),
                                      "\nYou Get Another Chance:")
                                input("\nClick Enter for Another Chance\n")
                                continue       # '''If a ladder occur get another chance'''


                            elif self.check_snake(new_position) != 0:   # Snake Checking
                                new_position = self.check_snake(new_position)
                                print("Ooo You were slide down to the tail of Snake")
                                break
                            else:
                                break
                        else:
                            new_position = current_position
                            break
                    else:
                        flag = 0
                        print("You need {} to win".format(self.game.board_size-initial_position))
                        break
                '''Above flag signal is used here for avoiding wrong update'''
                if flag != 0:
                    player.update_position(new_position)   #''' Actual Position Update '''

                    print(player.player_name, " move from {initial_position} to {new_position}: "
                          .format(initial_position=initial_position, new_position=new_position))

                    if self.check_for_win(new_position):                    # Checking for Wining
                        print("{player} Win the Match".format(player=player.player_name))
                        self.players.remove(player)
                        self.win_list.append(player.player_name)
                        still_playing -= 1
                if still_playing!=0:
                    input("\nClick Enter for Another player Chance:\n")

        '''Creating Wining List'''
        print("---------Wining List---------")
        for index in range(len(self.win_list)):
            print(index+1, ": ", self.win_list[index])
        return
