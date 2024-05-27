
class PlayerPosition:

    def __init__(self, player, position=0):
        self.player_name = player
        self.position = position

    '''Upgrade the position to new Position'''
    def update_position(self, new_position):
        self.position = new_position