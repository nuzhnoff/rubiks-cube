class Cube:
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.front = [1]*9
        self.up    = [2]*9
        self.down  = [3]*9
        self.top   = [4]*9
        self.left  = [5]*9
        self.right = [6]*9