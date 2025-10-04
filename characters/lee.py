from ..bot import Bot

class Lee(Bot):
    def __init__(self, initial_direction, sprite_canvas, pos, is_bot=False, hide_status_bar = False):
        super(Lee, self).__init__("lee", initial_direction, sprite_canvas, pos, hide_status_bar)
        self.is_bot = is_bot

        self.set_animation_sprites("stance", list(range(0, 4)))
        self.set_animation_sprites("run", list(range(4, 10)))
        self.set_animation_sprites("damage", list(range(10, 12)))
        self.set_animation_sprites("fall", list(range(12, 15)))
        self.set_animation_sprites("attack", list(range(15, 30)))
        self.set_animation_sprites("jump", [30, 30, 31, 31, 32, 32, 33, 33])

