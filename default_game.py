from board import Board


class DefaultGame:

    def __init__(self):
        self.board = Board()

    def game_config(self):
        '''
        # Adding snakes to the board
        self.board.add_snake(99, 80)
        self.board.add_snake(94, 75)
        self.board.add_snake(62, 19)
        self.board.add_snake(50, 11)
        self.board.add_snake(16, 6)
        self.board.add_snake(74, 53)
        self.board.add_snake(89, 68)

        # Adding ladder to the board
        self.board.add_ladder(28, 84)
        self.board.add_ladder(78, 98)
        self.board.add_ladder(8, 31)
        self.board.add_ladder(21, 42)
        self.board.add_ladder(71, 91)
        self.board.add_ladder(2, 38)
        self.board.add_ladder(51, 68)
        '''
        # Adding snakes to the board
        self.board.add_snake(24, 4)
        self.board.add_snake(14, 5)
        self.board.add_snake(20, 13)

        # Adding ladder to the board
        self.board.add_ladder(3, 23)
        self.board.add_ladder(11, 18)
        self.board.add_ladder(5, 16)

        return self.board
