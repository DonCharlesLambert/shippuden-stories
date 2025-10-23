from time import sleep
from PIL import Image, ImageTk

from const import PLAYER_ONE_POSITION, PLAYER_TWO_POSITION
from screens.utils import create_fighter
from screens.background import Backgrounds, FLOOR_HEIGHT


class FightScreen:
    def __init__(self, canvas):
        self.canvas = canvas
        self.images = []
        self.WIDTH = canvas.winfo_reqwidth()
        self.HEIGHT = canvas.winfo_reqheight()
        self.active = True

        self.selected_characters = [0, 1]
        self.fight_items = []
        self.floor_height = 0

    def fight(self, character_one, character_two, background=None):
        self.background = self.set_background(background)
        self.player_one = create_fighter(
            self.canvas, False, character_one, (100, self.floor_height)
        )
        self.player_two = create_fighter(
            self.canvas, True, character_two, (500, self.floor_height)
        )
        self.player_one.set_opponent(self.player_two)
        self.player_two.set_opponent(self.player_one)
        post_end_timer = 0
        while post_end_timer < 5:
            self.player_one.animate()
            self.player_two.animate()
            self.canvas.update()
            sleep(0.1)
            if self.player_one.dead or self.player_two.dead:
                post_end_timer += 0.1
        self.destroy()

    def set_background(self, background=None):
        background = Backgrounds.ROCKS if background is None else background
        img = Image.open(rf"sprites\misc\{background.value}.png")
        img = img.resize(
            (self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()),
            Image.Resampling.LANCZOS,
        )
        bg_image = ImageTk.PhotoImage(img)
        self.images.append(bg_image)
        self.floor_height = FLOOR_HEIGHT[background]
        canvas_item = self.canvas.create_image(0, 0, image=bg_image, anchor="nw")
        return canvas_item

    def destroy(self):
        self.canvas.delete(self.background)
        self.player_one.destroy()
        self.player_two.destroy()

    def key_press(self, e):
        if not self.player_one.is_bot:
            if e.char == "d":
                self.player_one.right()
            if e.char == "a":
                self.player_one.left()
            if e.char == " ":
                self.player_one.attack()
            if e.char == "w":
                self.player_one.jump()
            if e.char == "s":
                self.player_one.substitute()

    def key_release(self, e):
        if not self.player_one.is_bot:
            if e.char in ["w", "a", " ", "d"]:
                self.player_one.stance()
