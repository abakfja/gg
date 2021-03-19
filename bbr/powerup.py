from bbr.ball import BoxedMovingMixin
from gg import Sprite
from gg.utils import load_sprites, Vel
from .sprites import powerup


class PowerUp(BoxedMovingMixin, Sprite):
    sprites = load_sprites(powerup)
    SHAPE = sprites[0].shape

    def __init__(self, scene, typ, *args, **kwargs):
        super(PowerUp, self).__init__(self.sprites[typ], scene, *args, **kwargs)
        self.vel = kwargs.get('vel')
        self.fill_foreground((255, 255, 255))
        self.alpha = True
        self.type = typ
        self.acc = 0.02

    def update(self, timestamp):
        self.vel += Vel([self.acc, 0])
        self.box_contraints()
        self.move(self.vel)

# class LevelModifier(PowerUp):
#     class Types:
#         MULTI_BALL
#
#
#
# class BallModifier(PowerUp):
#     class Types:
#         THRU_BALL
#         FAST_BALL
#
#
# class PaddleModifier(PowerUp):
#     class Types:
#         PADDLE_LONG
#         PADDLE_SHORT
#         PADDLE_GRAB
#         PADDLE_SHOOT
