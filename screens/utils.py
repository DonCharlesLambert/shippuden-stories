from characters.character import CHARACTERS
from const import WIDTH, LEFT, RIGHT
from PIL import Image, ImageTk


def create_fighter(canvas, ai, name, position, character_select=False):
    direction = RIGHT if position[0] < WIDTH / 2 else LEFT
    Character = CHARACTERS[name]
    fighter = Character(
        direction, canvas, position, is_bot=ai, hide_status_bar=character_select
    )
    return fighter
