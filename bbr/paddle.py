from gg import Sprite
from gg import StatefulMixin
from gg.utils import load_sprites, collides
from .sprites import paddle


class Paddle(StatefulMixin, Sprite):
    sprites = load_sprites(paddle)
    SHAPE = sprites[0].shape
    COLORS = [
        (255, 0, 0),
        (0, 0, 255),
        (0, 255, 0)
    ]

    def __init__(self, scene, *args, **kwargs):
        state = {
            'length': 0,
            'grabbing': False,
            'last_powerup': None,
            'color': 0
        }
        kwargs['state'] = state
        super(Paddle, self).__init__(self.sprites[state['length']], scene, *args, **kwargs)
        self.fill_foreground((255, 0, 0))
        self._powerup_timer = 0

    def get_ball_angle(self, x):
        x = round(x)
        dx = ((((x - self.left) >> 1) << 1) - ((self.width >> 2) << 1)) >> 1
        if dx == 0:
            return 90
        elif dx == 1:
            return 60
        elif dx == -1:
            return -60
        elif dx == 2:
            return 45
        elif dx == -2:
            return -45
        elif dx == 3:
            return 30
        elif dx == -3:
            return -30
        else:
            print("fasd", x, dx)
            assert False

    def update_sprite(self):
        self.resize(self.sprites[self.state['length']].shape)
        self.fill_foreground(self.COLORS[self.state['color']])
        self.blit(self.sprites[self.state['length']])

    def update_color(self):
        self.fill_foreground(self.COLORS[self.state['color']])

    def elongate(self):
        self.update_state({'length': 1})
        self.update_sprite()

    def reset(self):
        self.update_state({'length': 0})
        self.update_sprite()

    def reduce(self):
        self.update_state({'length': 1})
        self.update_sprite()

    def grab(self):
        self.update_state({'grabbing': True})

    # def enable_powerup(self):

    def update(self, timestamp):
        for target in self.scene.iter_balls():
            if (
                    target.bottom >= self.top and
                    target.vy > 0 and
                    target.left >= self.left - 1 and
                    target.right <= self.right + 1
            ) or (collides(target, self)):
                if not self.state['grabbing']:
                    # print("collide")
                    target.set_launch_angle(self.get_ball_angle(target.left))
                else:
                    target.on_paddle = True
        #
        # for target in self.scene.iter_powerups():
        #     if target.top == self.top - 1 and target.vy > 0:
        #         if target.left >= self.left and target.right <= self.right:
        #             typ = target.type
        #             if typ == 0:
        #                 self._powerup_timer = timestamp
        #                 self.elongate()
        #             elif typ == 1:
        #                 self._powerup_timer = timestamp
        #                 self.reduce()
        #             elif typ == 2:
        #                 self._powerup_timer = timestamp
        #                 self.grab()
        #
        #             elif type == 3:
        #                 for ball in self.scene.iter_balls:
        #                     ball.random_velocity()
        #                     ball.thruball(timestamp)
        #             target.deactivate()
        if timestamp - self._powerup_timer > 1000:
            self.reset()
