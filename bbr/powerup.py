from gg import Sprite, MovingMixin
from . import load_sprites
from .sprites import powerup


class PowerUp(Sprite, MovingMixin):
    sprites = load_sprites(powerup)
    SHAPE = sprites[0].shape

    def __init__(self, scene, typ, *args, **kwargs):
        super(PowerUp, self).__init__(self.sprites[typ], scene, *args, **kwargs)
        self.fill_foreground((255, 255, 255))
        self.alpha = True
        self.type = typ

    def update(self, timestamp):
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
