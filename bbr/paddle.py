import numpy as np

from gg import Sprite
from . import load_sprites
from .sprites import paddle


class Paddle(Sprite):
    sprites = load_sprites(paddle)
    SHAPE = sprites[0].shape

    def __init__(self, scene, *args, **kwargs):
        self.state = 1
        super(Paddle, self).__init__(self.sprites[self.state], scene, *args, **kwargs)
        self.fill_foreground((255, 0, 0))
        self._powerup_timer = 0
        self._grabbing = False

    def get_ball_angle(self, x):
        center = self.left + self.width // 2 - 1
        dx = (x - center) // 2
        if dx == 0:
            return np.array([-1, 0])
        elif dx == 1:
            return np.array([-2, 1])
        elif dx == -1:
            return np.array([-2, -1])
        elif dx == 2:
            return np.array([-1, 2])
        elif dx == -2:
            return np.array([-1, -2])
        elif dx == 3:
            return np.array([-1, 4])
        elif dx == -3:
            return np.array([-1, -4])
        else:
            print(x, center, dx)
            assert False

    def elongate(self):
        self.state = 2
        self.resize(self.sprites[self.state].shape)
        self.fill_foreground((255, 0, 0))
        self.blit(self.sprites[self.state])

    def reset(self):
        self.state = 1
        self.resize(self.sprites[self.state].shape)
        self.fill_foreground((255, 0, 0))
        self.blit(self.sprites[self.state])

    def reduce(self):
        self.state = 0
        self.resize(self.sprites[self.state].shape)
        self.fill_foreground((255, 0, 0))
        self.blit(self.sprites[self.state])

    def grab(self):
        self._grabbing = True

    def update(self, timestamp):
        for target in self.scene.iter_balls():
            if target.y == self.y - 1 and target.vy > 0:
                if target.left >= self.left - 1 and target.right <= self.right - 1:
                    if not self._grabbing:
                        target.set_vel(self.get_ball_vel(target.x))
                    else:
                        target.on_paddle = True

        for target in self.scene.iter_powerups():
            if target.y == self.y - 1 and target.vy > 0:
                if target.left >= self.left and target.right <= self.right:
                    typ = target.type
                    if typ == 0:
                        self._powerup_timer = timestamp
                        self.elongate()
                    elif typ == 1:
                        self._powerup_timer = timestamp
                        self.reduce()
                    elif typ == 2:
                        self._powerup_timer = timestamp
                        self.grab()
                    elif type == 3:
                        for ball in self.scene.iter_balls:
                            ball.random_velocity()
                            ball.thruball(timestamp)
                    target.deactivate()
        if timestamp - self._powerup_timer > 1000:
            self.reset()
