import numpy as np

from bbr.background import Bg
from bbr.ball import Ball
from bbr.bricks import GlassBrick, RainbowBrick
from bbr.paddle import Paddle
from bbr.powerup import PowerUp
from gg import Scene
from gg.utils import Pos, Vel


class Level(Scene):
    def __init__(self, game, *args, **kwargs):
        self.game = game
        super(Level, self).__init__(self.game.shape, *args, **kwargs)
        self.paddle = Paddle(self, pos=Pos([self.bottom, self.left + (self.width // 4) * 2]))
        self.background = Bg(self, self.game.shape, pos=Pos([0, 0]))
        self.bricks = []
        self.balls = []
        self.powerups = []
        self.gen()

    def gen(self):
        # pass
        self.generate_bricks()
        ball_pos = self.paddle.pos + Pos([-1, np.random.randint(0, self.paddle.width // 2) * 2])
        self.balls.append(Ball(self, pos=ball_pos, vel=Vel([0, 0])))
        self.add(*self.bricks, self.background, self.paddle, *self.balls)

    def iter_balls(self):
        for it in self.balls:
            if it.is_active():
                yield it

    def iter_bricks(self):
        for it in self.bricks:
            if it.is_active():
                yield it

    def iter_powerups(self):
        for it in self.powerups:
            if it.is_active():
                yield it

    def add_powerup(self, pos, vel):
        # print(vel)
        power = PowerUp(self, np.random.randint(0, 4), pos=pos, vel=vel)
        self.powerups.append(power)
        self.add(power)

    def update(self, timestamp):
        super(Level, self).update(timestamp)
        self.balls = [x for x in self.iter_balls()]
        self.bricks = [x for x in self.iter_bricks()]
        self.powerups = [x for x in self.iter_powerups()]
        if len(self.balls) == 0:
            self.game.lives -= 1
            ball_pos = self.paddle.pos + [-1, np.random.randint(0, self.paddle.width // 2) * 2]
            self.balls.append(
                Ball(self, pos=ball_pos, vel=Vel([0, 0]))
            )
            self.add(*self.balls)

    def generate_bricks(self):
        for it in range(7):
            self.bricks.append(
                RainbowBrick(self, pos=Pos([2, 4 + it * RainbowBrick.SHAPE[1]]))
            )
        for it in range(7):
            self.bricks.append(
                GlassBrick(self, pos=Pos(
                    [2 + 1 * GlassBrick.SHAPE[0], 4 + it * GlassBrick.SHAPE[1]]
                ))
            )

    def receive_input(self, char):
        if char in ['j', 'l']:
            direction = -3 if char == 'j' else 3
            # print(direction)
            direction = min(self.right - self.paddle.right, direction)
            # print(direction)
            direction = max(self.left - self.paddle.left, direction)
            # print(direction)
            self.paddle.move(Pos([0, direction]))
            for it in self.iter_balls():
                if it.on_paddle:
                    it.move(Pos([0, direction]))
        elif char == 'k':
            for it in self.iter_balls():
                it.on_paddle = False
                it.set_launch_angle(self.paddle.get_ball_angle(it.x))
