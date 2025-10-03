from tkinter import *
from .characters.character import CHARACTERS
import winsound
from time import sleep
from PIL import Image
from PIL import ImageTk

WIDTH = 600
HEIGHT = 400
#bruh

class Battle:
    images = []
    PLAYER_ONE_POSITION = (100, 370)
    PLAYER_TWO_POSITION = (400, 370)
    LEFT  = "left"
    RIGHT = "right"

    def __init__(self, game_window):
        self.game_window = game_window
        self.canvas = Canvas(game_window, width=WIDTH, height=HEIGHT)
        self.canvas.bind("<KeyPress>", self.key_press)
        self.canvas.bind("<KeyRelease>", self.key_release)
        self.canvas.pack()
        self.canvas.focus_set()

        winsound.PlaySound(r'life-is-good\music\LifeIsGood.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
        self.game_window.after(0, self.game)

    def game(self):
        self.set_background()
        self.character_select()
        self.fight()

    def character_select(self):
        # add character select
        time = 0
        while time < 1:
            self.canvas.update()
            sleep(0.1)
            time += 0.1

    def fight(self):
        self.player_one = self.create_fighter(False, "deidara", self.PLAYER_ONE_POSITION)
        self.player_two = self.create_fighter(True, "kakashi", self.PLAYER_TWO_POSITION)
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

    def set_background(self):
        img = Image.open(r'life-is-good\sprites\misc\rocks.png')
        img = img.resize((self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(img)

        self.canvas.create_image(0, 0, image=bg_image, anchor="nw")
        self.images.append(bg_image)

    def key_press(self, e):
        self.player_one_controller_press(e)
        self.player_two_controller_press(e)

    def key_release(self, e):
        self.player_one_controller_release(e)
        self.player_two_controller_release(e)

    def player_one_controller_press(self, e):
        if not self.player_one.is_bot:
            if e.char == "d":
                self.player_one.right()
            if e.char == "a":
                self.player_one.left()
            if e.char == " ":
                self.player_one.attack()
            if e.char == "w":
                self.player_one.jump()

    def player_two_controller_press(self, e):
        if not self.player_two.is_bot:
            if e.char == "l":
                self.player_two.right()
            if e.char == "j":
                self.player_two.left()
            if e.char == "k":
                self.player_two.attack()
            if e.char == "i":
                self.player_two.jump()

    def player_one_controller_release(self, e):
        if not self.player_one.is_bot:
            if e.char in ['w', 'a', ' ', 'd']:
                self.player_one.stance()

    def player_two_controller_release(self, e):
        if not self.player_two.is_bot:
            if e.char in ['i', 'j', 'k', 'l']:
                self.player_two.stance()

    def create_fighter(self, ai, name, position):
        direction = self.RIGHT
        if position == self.PLAYER_TWO_POSITION:
            direction = "left"
        Character = CHARACTERS[name]
        fighter = Character(direction, self.canvas, position, is_bot=ai)
        return fighter


root = Tk()
root.title("Naruto: Shippuden Stories")
img = PhotoImage(file=r"life-is-good\sprites\Future\smile.png")
root.iconphoto(False, img)
Battle(root)
root.mainloop()
input()

