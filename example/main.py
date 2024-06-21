
from setup import *

class Game():
    def __init__(self, setup:dict):
        self.setup = setup
        self.game = True
    
    def mainloop(self, *args, **kwargs):
        '''Your looping function'''
        while self.game:
            self.main()
    
    def main(self):
        '''Your main looped function'''
        pass


if __name__=="__main__":
    game = Game(setup)
    game.mainloop()
