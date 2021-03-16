import numpy as np

from gg import Surface


class Bg(Surface):
    def __init__(self, shape, scene, pos, *args, **kwargs):
        super(Bg, self).__init__(shape, scene, *args, **kwargs)
        self.pos = pos
        self.z = -1

    def update(self, timestamp):
        timestamp *= 2
        ii = (50 - 1 - timestamp % 50) if timestamp // 50 & 1 else timestamp % 50
        self.blit(back=np.array([
            [(ii + col, 0, ii + row) for col in range(self.width)] for row in range(self.height)
        ]))
