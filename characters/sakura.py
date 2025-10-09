from bot import Bot

class Sakura(Bot):
    def __init__(self, initial_direction, sprite_canvas, pos, is_bot=False, hide_status_bar = False):
        super(Sakura, self).__init__("sakura", initial_direction, sprite_canvas, pos, hide_status_bar)
        self.is_bot = is_bot

        self.set_animation_sprites("stance", list(range(0, 5)))
        self.set_animation_sprites("run", list(range(5, 11)))
        self.set_animation_sprites("damage", list(range(11, 13)))
        self.set_animation_sprites("fall", list(range(13, 17)))
        self.set_animation_sprites("attack", list(range(17, 30)))
        self.set_animation_sprites("jump", [30, 30, 31, 31, 32, 32, 33, 33, 34])

