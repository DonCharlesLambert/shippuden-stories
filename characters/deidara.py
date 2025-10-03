from ..bot import Bot

class Deidara(Bot):
    def __init__(self, initial_direction, sprite_canvas, pos, is_bot=False):
        super(Deidara, self).__init__("deidara", initial_direction, sprite_canvas, pos)
        self.is_bot = is_bot

