from ..bot import Bot

class Itachi(Bot):
    def __init__(self, initial_direction, sprite_canvas, pos, is_bot=False):
        super(Itachi, self).__init__("itachi", initial_direction, sprite_canvas, pos)
        self.is_bot = is_bot

        self.set_animation_sprites("stance", list(range(0, 4)))
        self.set_animation_sprites("run", list(range(4, 10)))
        self.set_animation_sprites("damage", list(range(10, 12)))
        self.set_animation_sprites("fall", list(range(10, 16)))
        self.set_animation_sprites("attack", list(range(16, 29)))
        self.set_animation_sprites("jump", [29, 29, 30, 30, 31, 31, 32, 32, 33, 33])

