from numpy import ndarray

from .scene import Scene
from .surface import Surface


class Sprite(Surface):
    """
    A sprite is a surface with a definitive representation
    """

    def __init__(self, chars: ndarray, scene: Scene, pos, *args, **kwargs):
        shape = chars.shape
        super(Sprite, self).__init__(shape, scene, *args, **kwargs)
        self.blit(chars)
        self.pos = pos
