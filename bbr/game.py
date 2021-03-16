from gg import ForegroundColor, BackgroundColor
from gg import Game
from .level import Level


class BrickBreaker(Game):
    def __init__(self, *args, **kwargs):
        super(BrickBreaker, self).__init__(*args, **kwargs)
        self.level = Level(self)

    def lives_repr(self):
        return ''.join([u'❤ ' for i in range(self.lives)])

    def exec_(self):
        frame = 0

        while 1:
            print(str(BackgroundColor(0, 0, 0)) + str(ForegroundColor(255, 255, 255)))
            print('Score:', self.score)
            print('Time: {:.1f}s'.format(frame * 0.03))
            print('Lives:', self.lives_repr())
            if self.inp.is_available():
                c = self.inp.getch()
                self.level.receive_input(c)
                self.inp.clear()
            self.level.update(frame)
            self.level.render(self.screen)
            self.screen.display()
            if self.lives == 0:
                break
            frame += 1
        self.end()
