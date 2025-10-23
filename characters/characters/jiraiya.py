from characters.bot import Bot


class Jiraiya(Bot):
    def __init__(
        self, initial_direction, sprite_canvas, pos, is_bot=False, hide_status_bar=False
    ):
        super(Jiraiya, self).__init__(
            "jiraiya", initial_direction, sprite_canvas, pos, hide_status_bar
        )
        self.is_bot = is_bot

        self.set_animation_sprites("stance", list(range(0, 6)))
        self.set_animation_sprites("run", list(range(6, 12)))
        self.set_animation_sprites("damage", list(range(12, 14)))
        self.set_animation_sprites("fall", list(range(14, 19)))
        self.set_animation_sprites("attack", list(range(19, 37)))
        self.set_animation_sprites("jump", [37, 37, 38, 38, 39, 39, 40, 40])
        self.resize_ratio = 0.9
