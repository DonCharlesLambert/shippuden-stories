from bot import Bot

class Kisame(Bot):
    def __init__(self, initial_direction, sprite_canvas, pos, is_bot=False, hide_status_bar = False):
        super(Kisame, self).__init__("kisame", initial_direction, sprite_canvas, pos, hide_status_bar)
        self.is_bot = is_bot

        self.set_animation_sprites("stance", list(range(0, 4)))
        self.set_animation_sprites("run", list(range(4, 9)))
        self.set_animation_sprites("damage", list(range(9, 11)))
        self.set_animation_sprites("fall", list(range(9, 15)))
        self.set_animation_sprites("attack", list(range(15, 28)))
        self.set_animation_sprites("jump", [28, 28, 29, 29, 30, 30, 31, 31, 32, 32])

