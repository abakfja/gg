from bbr.sprites import bullet
from gg import MovingMixin, Sprite
from gg.utils import load_sprite, Vel


class Bullet(MovingMixin, Sprite):
    def __init__(self, scene, *args, **kwargs):
        super(Bullet, self).__init__(self.sprite, scene, *args, **kwargs)
        self.vel = Vel([1, 0])
        self.fill_foreground((255, 255, 255))
        self.alpha = True

    def update(self, timestamp):
        self.move(self.vel)


class AlienBullet(Bullet):
    sprite = load_sprite(bullet[0])
    SHAPE = sprite.shape

    def __init__(self, scene, *args, **kwargs):
        super(AlienBullet, self).__init__(self.sprite, scene, *args, **kwargs)
        self.vel = Vel([1, 0])

    def update(self, timestamp):
        self.move(self.vel)


class PaddleBullet(Bullet):
    sprite = load_sprite(bullet[1])
    SHAPE = sprite.shape

    def __init__(self, scene, *args, **kwargs):
        super(PaddleBullet, self).__init__(self.sprite, scene, *args, **kwargs)
        self.vel = Vel([-1, 0])

    def update(self, timestamp):
        self.move(self.vel)
