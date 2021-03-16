from numpy import ndarray

from .scene import Scene
from .surface import Surface


class Sprite(Surface):
    """
    A sprite is a surface with a definitive representation
    """

    def __init__(self, chars: ndarray, scene: Scene, pos, **kwargs):
        shape = chars.shape
        super(Sprite, self).__init__(shape, scene, **kwargs)
        self.blit(chars)
        self.pos = pos
