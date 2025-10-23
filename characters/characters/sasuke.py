from characters.bot import Bot


class Sasuke(Bot):
    def __init__(
        self, initial_direction, sprite_canvas, pos, is_bot=False, hide_status_bar=False
    ):
        super(Sasuke, self).__init__(
            "sasuke", initial_direction, sprite_canvas, pos, hide_status_bar
        )
        self.is_bot = is_bot

        self.set_animation_sprites("stance", list(range(0, 4)))
        self.set_animation_sprites("run", list(range(4, 7)))
        self.set_animation_sprites("damage", list(range(7, 9)))
        self.set_animation_sprites("fall", list(range(9, 12)))
        self.set_animation_sprites("attack", list(range(12, 21)))
        self.set_animation_sprites("jump", [21, 21, 21, 21, 22, 22, 22, 22, 23])

        self.resize_ratio = 0.87
