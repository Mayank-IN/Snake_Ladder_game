from board import Board


class ConfigGame:

    def __init__(self):
        self.board = Board()

    def config_game(self, board_size):

        while True:
            try:
                config = int(input("Enter 1 to add the snake\n"
                                   "Enter 2 to add a ladder\n"
                                   "Enter 3 to look at snake and ladder status\n"
                                   "Enter 0 to play\n"))
                if config not in (1, 2, 3, 0):
                    print("Enter Among the given Choices Correctly\n\n")
                    continue

                # Adding snake into the board
                if config == 1:
                    print("Enter Snake Position")
                    print("Note: Mouth of snake should be greater than tail")
                    while 1:
                        mouth = int(input("Enter Mouth of the snake: "))
                        tail = int(input("Enter Tail of the snake: "))

                        if mouth >= board_size or tail > board_size:
                            print("Mouth and Tail value should not exceed ", board_size-1)
                        elif mouth < tail:  # condition checking
                            print("Mouth of snake should be greater than tail, Please Enter Correctly\n\n")
                        else:
                            break
                    self.board.add_snake(mouth, tail)

                # Adding Ladder into the board
                elif config == 2:
                    print("Enter Ladder Position")
                    print("Note: Bottom of ladder should be lesser than Top")
                    while 1:
                        bottom = int(input("Enter Bottom of the Ladder: "))
                        top = int(input("Enter Top of the Ladder: "))
                        if top >= board_size or bottom >= board_size:
                            print("Bottom and top range should not exceed ", board_size-1)
                        elif top < bottom:
                            print("bottom of ladder should be lesser than top, Please Enter Correctly\n\n")

                        else:
                            break
                    self.board.add_ladder(bottom, top)

                # Status of snake and ladder position

                elif config == 3:
                    print("Snake Positions\n")
                    for snake_position in board.snake_list:
                        print(snake_position, "\t", board.snake_list.get(snake_position))

                    print("Ladder Positions\n")
                    for ladder_position in board.ladder_list:
                        print(ladder_position, "\t", board.ladder_list.get(ladder_position))

                # Play the Game
                elif config == 0:
                    return self.board
            except ValueError:
                print("Enter Numerical Value")
