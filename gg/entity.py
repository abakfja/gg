from .interfaces import Renderable, Updatable


# Abstract class
class Entity(Renderable, Updatable):
    """
    An Entity has a position, and an association with a scene
    An entity has associated with it a definitive position
    and a scene to which it belongs and whether it is active
    you must implement *render* and *update* yourself

    An entity must have a bounding box
    """

    def __init__(self, scene, **kwargs):
        super(Entity, self).__init__(**kwargs)
        self.scene = scene
        self._active = True

    @property
    def x(self):
        assert hasattr(self, 'pos'), (
            'The position of the object must be defined'
        )
        return self.pos[1]

    @property
    def y(self):
        assert hasattr(self, 'pos'), (
            'The position of the object must be defined'
        )
        return self.pos[0]

    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

    def move(self, dpos):
        assert hasattr(self, 'pos'), (
            'The position of the object must be defined'
        )
        self.pos += dpos

    def is_active(self):
        return self._active
