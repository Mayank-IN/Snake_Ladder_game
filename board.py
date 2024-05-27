
class Board:

    def __init__(self, board_size=25):
        self.board_size = board_size  # Initialising board size and dictionary for snake and ladder
        self.snake_list = {}
        self.ladder_list = {}

    '''Function to add a snake'''
    def add_snake(self, mouth, tail):
        self.snake_list[mouth] = tail

    ''' Function to add a Ladder'''
    def add_ladder(self, bottom, top):
        self.ladder_list[bottom] = top
