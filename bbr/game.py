from time import perf_counter

import numpy as np

from gg import ForegroundColor, BackgroundColor
from gg import Game
from .level import Level


class BrickBreaker(Game):
    def __init__(self, *args, **kwargs):
        super(BrickBreaker, self).__init__(*args, **kwargs)
        self.level = Level(self)

    def lives_repr(self):
        return ''.join([u'🤎 ' for i in range(self.lives)] + [u'🤍 ' for i in range(10 - self.lives)])

    def exec_(self):
        frame = 0
        times = np.zeros(100)
        render = np.zeros((100, 4))
        while True:
            st = perf_counter()
            print(str(BackgroundColor(0, 0, 0)) + str(ForegroundColor(255, 255, 255)))
            print('Score:', self.score)
            print('Time: {:.1f}s'.format(frame / 3))
            print('Lives:', self.lives_repr())
            if self.inp.is_available():
                c = self.inp.getch()
                self.level.receive_input(c)
                self.inp.clear()
            self.level.update(frame)
            self.level.render(self.screen)
            nd = perf_counter()
            res = self.screen.display()
            if self.lives == 0:
                break
            times[frame % 100] = nd - st
            render[frame % 100] = res
            frame += 1
        print(np.mean(times))
        print(np.mean(render[:, 0]))
        print(np.mean(render[:, 1]))
        print(np.mean(render[:, 2]))
        print(np.mean(render[:, 3]))

        self.end()
