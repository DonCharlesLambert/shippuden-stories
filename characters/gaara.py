from bot import Bot

class Gaara(Bot):
    def __init__(self, initial_direction, sprite_canvas, pos, is_bot=False, hide_status_bar = False):
        super(Gaara, self).__init__("gaara", initial_direction, sprite_canvas, pos, hide_status_bar)
        self.is_bot = is_bot

        self.set_animation_sprites("stance", list(range(0, 6)))
        self.set_animation_sprites("run", list(range(6, 12)))
        self.set_animation_sprites("damage", list(range(12, 14)))
        self.set_animation_sprites("fall", list(range(14, 18)))
        self.set_animation_sprites("attack", list(range(18, 33)))
        self.set_animation_sprites("jump", [33, 33, 34, 34, 35, 35, 36, 36])

