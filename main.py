from bbr.game import BrickBreaker
from gg import Screen

W = 110
H = 50
SZ = (H, W)

if __name__ == '__main__':
    game = BrickBreaker(Screen(SZ))
    game.exec_()
