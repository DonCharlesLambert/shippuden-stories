
from time import sleep

from const import PLAYER_ONE_POSITION, PLAYER_TWO_POSITION
from screens.utils import create_fighter

class FightScreen():
    def __init__(self, canvas):
        self.canvas = canvas
        self.images = []
        self.WIDTH = canvas.winfo_reqwidth()
        self.HEIGHT = canvas.winfo_reqheight()
        self.active = True

        self.selected_characters = [0, 1]
        self.fight_items = []

    
    def fight(self, character_one, character_two):
        self.player_one = create_fighter(self.canvas, False, character_one, PLAYER_ONE_POSITION)
        self.player_two = create_fighter(self.canvas, True, character_two, PLAYER_TWO_POSITION)
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
    
    def key_release(self, e):
        if not self.player_one.is_bot:
            if e.char in ['w', 'a', ' ', 'd']:
                self.player_one.stance()