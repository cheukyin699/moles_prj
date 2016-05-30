import player
import mole

class State:
    '''
    Base class for all states
    '''
    def __init__(self, surface):
        self.surface = surface

    def handle(self, evt):
        pass

    def update(self, d):
        pass

    def draw(self):
        pass

class GameState(State):
    '''
    Class for handling the game and stuff
    Derives the State class
    '''
    def __init__(self, surface):
        State.__init__(self, surface)

    def handle(self, evt):
        pass

    def update(self, d):
        pass

    def draw(self):
        pass
