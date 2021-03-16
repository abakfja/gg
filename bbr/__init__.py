import numpy as np


def load_sprite(rep):
    arr = rep.split("\n")[1:-1]
    n = len(max(arr, key=len))
    return np.array([list(x + (' ' * (n - len(x)))) for x in arr])


def load_sprites(rep):
    return list(map(load_sprite, rep))
