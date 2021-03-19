import math

import numpy as np

from gg import Sprite, MovingMixin
from gg.utils import load_sprite, collides
from .sprites import ball


class BoxedMovingMixin(MovingMixin):
    def __init__(self, *args, **kwargs):
        super(BoxedMovingMixin, self).__init__(*args, **kwargs)

    def switch_x(self):
        self.vel[1] *= -1

    def switch_y(self):
        self.vel[0] *= -1

    def right_hit(self):
        return self.right >= self.scene.right and self.vx > 0

    def left_hit(self):
        return self.left >= self.scene.left and self.vx > 0

    def top_hit(self):
        return self.top >= self.scene.top and self.vx > 0

    def bottom_hit(self):
        return self.bottom >= self.scene.bottom + 1 and self.vx > 0

    def box_contraints(self):
        if self.right >= self.scene.right and self.vx > 0:
            self.switch_x()
        elif self.left <= self.scene.left and self.vx < 0:
            self.switch_x()
        if self.top <= self.scene.top and self.vy < 0:
            self.switch_y()


class Ball(BoxedMovingMixin, Sprite):
    sprite = load_sprite(ball)

    def __init__(self, scene, vel, *args, **kwargs):
        super(Ball, self).__init__(self.sprite, scene, *args, **kwargs)
        self.alpha = True
        self.z = 1
        self.set_vel(vel)
        self.on_paddle = True
        self.powerup_timer = 0
        self.thru = False

    def set_launch_angle(self, angle):
        vel = np.array([-math.sin(math.radians(abs(angle))), 2 * math.cos(math.radians(angle))])
        if angle < 0:
            vel[1] *= -1
        self.set_vel(2 * vel)

    def update(self, timestamp):
        for target in self.scene.iter_bricks():
            if (self.top == target.bottom or collides(self, target) and self.vy < 0) \
                    or (self.bottom == target.top or collides(self, target) and self.vy > 0):
                if self.left > target.left - 1 and self.right < target.right + 2:
                    target.hit(self)
                    self.switch_y()
                elif self.left == target.left - 1 and self.vx > 0:
                    target.hit(self)
                    self.switch_x()
                    self.switch_y()
                elif self.left == target.right + 1 and self.vx < 0:
                    target.hit(self)
                    self.switch_x()
                    self.switch_y()

            elif (self.left == target.right or collides(self, target) and self.vx < 0) or \
                    (self.right == target.left or collides(self, target) and self.vx > 0):
                if target.top <= self.top <= target.bottom:
                    target.hit(self)
                    self.switch_x()
        self.box_contraints()
        if self.bottom_hit():
                self.deactivate()
                self.scene.paddle.reset()

        if not self.on_paddle:
            self.move(self.vel)
        if timestamp - self.powerup_timer > 1000:
            self.reset()
