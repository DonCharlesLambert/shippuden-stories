from characters.bot import Bot


class Sasori(Bot):
    def __init__(
        self, initial_direction, sprite_canvas, pos, is_bot=False, hide_status_bar=False
    ):
        super(Sasori, self).__init__(
            "sasori", initial_direction, sprite_canvas, pos, hide_status_bar
        )
        self.is_bot = is_bot

        self.set_animation_sprites("stance", list(range(0, 6)))
        self.set_animation_sprites("run", list(range(6, 12)))
        self.set_animation_sprites("damage", list(range(12, 14)))
        self.set_animation_sprites("fall", list(range(12, 18)))
        self.set_animation_sprites("attack", list(range(18, 40)))
        self.set_animation_sprites("jump", [40, 40, 41, 41, 42, 42, 43, 43, 44])
