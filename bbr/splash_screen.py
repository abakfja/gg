from gg import Scene

class Level(Scene):
    def __init__(self, game, *args, **kwargs):
        self.game = game
        super(Level, self).__init__(self.game.shape, *args, **kwargs)