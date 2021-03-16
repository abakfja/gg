import numpy as np

from .entity import Entity
from .scene import Scene


class Surface(Entity):
    """
    A surface is a concrete class
    A surface has a definitive bounding box and
    A surface has a representation of itself and
    and it also has a position in three dimensions
    """

    def __init__(self, shape: tuple, scene: Scene, alpha=False, **kwargs):
        super(Surface, self).__init__(scene, **kwargs)
        h, w = shape
        # You cannot edit the shape of the object because a lot of things depend on it
        self._shape = shape
        self._back = np.full((h, w, 3), np.array([0, 0, 0]), dtype='i2')
        self._char = np.full((h, w), ' ', dtype='<U1')
        self._front = np.full((h, w, 3), np.array([255, 255, 255]), dtype='i2')
        self.z = 0
        self.alpha = alpha

    def resize(self, shape):
        """
        Resize the current surface the arrays are all reset so you would have
        to blit on them again
        :param shape:
        :return:
        """
        h, w = shape
        self._shape = shape
        self._back = np.full((h, w, 3), np.array([0, 0, 0]), dtype='i2')
        self._char = np.full((h, w), ' ', dtype='<U1')
        self._front = np.full((h, w, 3), np.array([255, 255, 255]), dtype='i2')

    def _blit_char(self, chars, pos=np.zeros(2, dtype='i4')):
        h, w = chars.shape
        assert 0 <= pos[0] <= self.height and 0 <= pos[1] <= self.width, (
            'Cannot blit outside of screen'
        )
        self._char[
            pos[0]: min(pos[0] + h, self.height),
            pos[1]:min(pos[1] + w, self.width)
        ] = chars

    def _blit_bg(self, color, pos=np.zeros(2, dtype='i4')):
        h, w = color.shape[:2]
        assert 0 <= pos[0] <= self.height and 0 <= pos[1] <= self.width, (
            'Cannot blit outside of screen'
        )
        self._back[
            pos[0]: min(pos[0] + h, self.height),
            pos[1]:min(pos[1] + w, self.width)
        ] = color

    def _blit_fg(self, color, pos=np.zeros(2, dtype='i4')):
        h, w = color.shape[:2]
        assert 0 <= pos[0] <= self.height and 0 <= pos[1] <= self.width, (
            'Cannot blit outside of screen'
        )
        self._front[
            pos[0]: min(pos[0] + h, self.height),
            pos[1]:min(pos[1] + w, self.width)
        ] = color

    def blit(self, chars=None, fore=None, back=None, pos=np.zeros(2, dtype='i4')):
        """
        Change a sub array of each of the following but the size remains the same
        similar to pygame blit method
        :param chars:
        :param fore:
        :param back:
        :param pos:
        :return:
        """
        if chars is not None:
            self._blit_char(chars, pos)
        if fore is not None:
            self._blit_fg(fore, pos)
        if back is not None:
            self._blit_bg(back, pos)

    def fill(self, char: str):
        """
        Fill char with a single character
        :param char:
        :return:
        """
        self._char[:] = char

    def fill_background(self, color: tuple):
        """
        Fill background with a single color
        :param color:
        :return:
        """
        assert not self.alpha, (
            'Transparent surface cannot be filled'
        )
        self._back = np.tile(np.array(color), (
            self.height, self.width, 1))

    def fill_foreground(self, color: tuple):
        """
        Fill foreground with a single color
        :param color:
        :return:
        """
        self._front = np.tile(np.array(color), (
            self.height, self.width, 1))

    def clear(self):
        self._front.fill(0)
        self._back.fill(0)
        self._char.fill(' ')

    def get_bg(self):
        return self._back

    def get_fg(self):
        return self._front

    def get_char(self):
        return self._char

    def is_trans(self):
        return self.alpha

    @property
    def top(self):
        assert hasattr(self, 'pos'), (
            'The position of the object must be defined'
        )
        return self.y

    @property
    def bottom(self):
        assert hasattr(self, 'pos'), (
            'The position of the object must be defined'
        )
        assert hasattr(self, 'height'), (
            'A Renderable must have a width defined'
        )
        return self.y + self.height - 1

    @property
    def left(self):
        assert hasattr(self, 'pos'), (
            'The position of the object must be defined'
        )
        return self.x

    @property
    def right(self):
        assert hasattr(self, 'pos'), (
            'The position of the object must be defined'
        )
        assert hasattr(self, 'width'), (
            'A Renderable must have a width defined'
        )
        return self.x + self.width - 1

    """
    For interface Renderable
    """

    @property
    def width(self):
        return self._shape[1]

    @property
    def height(self):
        return self._shape[0]

    def render(self, screen):
        assert hasattr(self, 'pos'), (
            'Class generics must have a position defined'
        )
        screen.render(self.pos[0], self.pos[1], self)
