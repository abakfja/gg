import numpy as np
import math
from bbr import load_sprite
from gg import Sprite, MovingMixin
from .sprites import ball


class Ball(Sprite, MovingMixin):
    sprite = load_sprite(ball)

    def __init__(self, scene, vel, *args, **kwargs):
        super(Ball, self).__init__(self.sprite, scene, *args, **kwargs)
        self.alpha = True
        self.z = 1
        self.set_vel(vel)
        self.on_paddle = True
        self.powerup_timer = 0
        self.thru = False

    def set_angle(self, angle):
        vel = np.array([2 * math.cos(angle), math.sin(angle)])
        self.set_vel(vel)

    def switch_x(self):
        self.vel[1] *= -1

    def switch_y(self):
        self.vel[0] *= -1

    def update(self, timestamp):
        for target in self.scene.iter_bricks():
            if (self.y == target.bottom + 1 and self.vy < 0) \
                    or (self.y == target.top - 1 and self.vy > 0):
                if self.left > target.left - 2 and self.right < target.right + 2:
                    target.hit(self)
                    self.switch_y()
                elif self.left == target.left - 2 and self.vx > 0:
                    target.hit(self)
                    self.switch_x()
                    self.switch_y()
                elif self.left == target.right + 1 and self.vx < 0:
                    target.hit(self)
                    self.switch_x()
                    self.switch_y()

            elif (self.left == target.right + 1 and self.vx < 0) or \
                    (self.right == target.left - 1 and self.vx > 0):
                if target.top <= self.y <= target.bottom:
                    target.hit(self)
                    self.switch_x()

        if self.right >= self.scene.right and self.vx > 0:
            self.switch_x()
        elif self.left <= self.scene.left and self.vx < 0:
            self.switch_x()
        if self.top <= self.scene.top and self.vy < 0:
            self.switch_y()
        elif self.bottom >= self.scene.bottom and self.vy > 0:
            self.deactivate()
            self.scene.paddle.reset()
        if not self.on_paddle:
            self.move(self.vel)
        if timestamp - self.powerup_timer > 1000:
            self.reset()
