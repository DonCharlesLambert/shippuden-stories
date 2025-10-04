from tkinter import *
from .characters.character import CharacterNames, CHARACTERS
from .const import PROJECT_NAME
import winsound
from time import sleep
from enum import Enum
from PIL import Image
from PIL import ImageTk

WIDTH = 600
HEIGHT = 400
#bruh

class States(Enum):
    TITLE = "title"
    SELECT = "select"
    FIGHT = "fight"

class Battle:
    images = []
    PLAYER_ONE_POSITION = (100, 370)
    PLAYER_TWO_POSITION = (400, 370)
    LEFT  = "left"
    RIGHT = "right"
    state = States.TITLE

    def __init__(self, game_window):
        self.game_window = game_window
        self.canvas = Canvas(game_window, width=WIDTH, height=HEIGHT)
        self.canvas.bind("<KeyPress>", self.key_press)
        self.canvas.bind("<KeyRelease>", self.key_release)
        self.canvas.pack()
        self.canvas.focus_set()

        self.selected_characters = [0, 1]

        # winsound.PlaySound(rf'{PROJECT_NAME}\music\LifeIsGood.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
        self.game_window.after(0, self.game)

    def game(self):
        self.set_background()
        while True:
            character_one, character_two = self.character_select()
            self.fight(character_one, character_two)

    def character_select(self):
        self.state = States.SELECT
        names = list(CharacterNames)
        select_items = []
        for i, character in enumerate(names):
            select_items.append(self.get_character_select(character.value, i))
        mock_player_one = self.create_fighter(False, names[self.selected_characters[0]], self.PLAYER_ONE_POSITION, character_select=True)
        mock_player_two = self.create_fighter(False, names[self.selected_characters[1]], self.PLAYER_TWO_POSITION, character_select=True)
        
        mock_player_one.set_opponent(mock_player_two)
        mock_player_two.set_opponent(mock_player_one)

        time = 0
        while self.state == States.SELECT:
            self.canvas.update()
            mock_player_one.animate()
            mock_player_two.animate()
            if mock_player_one.name != names[self.selected_characters[0]].value:
                mock_player_one.destroy()
                mock_player_one = self.create_fighter(False, names[self.selected_characters[0]], self.PLAYER_ONE_POSITION, character_select=True)
                mock_player_one.set_opponent(mock_player_two)
                mock_player_two.set_opponent(mock_player_one)
            if mock_player_two.name != names[self.selected_characters[1]].value:
                mock_player_two.destroy()
                mock_player_two = self.create_fighter(False, names[self.selected_characters[1]], self.PLAYER_TWO_POSITION, character_select=True)
                mock_player_two.set_opponent(mock_player_one)
                mock_player_one.set_opponent(mock_player_two)
            sleep(0.1)
            time += 0.1

        [self.canvas.delete(item) for item in select_items]
        mock_player_one.destroy()
        mock_player_two.destroy()
        return names[self.selected_characters[0]], names[self.selected_characters[1]]

    def fight(self, character_one, character_two):
        self.state = States.FIGHT
        self.player_one = self.create_fighter(False, character_one, self.PLAYER_ONE_POSITION)
        self.player_two = self.create_fighter(True, character_two, self.PLAYER_TWO_POSITION)
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

    def set_background(self):
        img = Image.open(rf'{PROJECT_NAME}\sprites\misc\rocks.png')
        img = img.resize((self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(img)

        self.canvas.create_image(0, 0, image=bg_image, anchor="nw")
        self.images.append(bg_image)

    
    def get_character_select(self, character_name, position=0):
        img = Image.open(rf'{PROJECT_NAME}\sprites\select\{character_name}.png')
        select_image = ImageTk.PhotoImage(img)
        self.images.append(select_image)

        x = 50 + (150 * (position // 3))
        y = (position % 3) * 50 + 20
        return self.canvas.create_image(x, y, image=select_image, anchor="nw")


    def key_press(self, e):
            self.player_one_controller_press(e)
            self.player_two_controller_press(e)

    def key_release(self, e):
        if self.state == States.FIGHT:
            self.player_one_controller_release(e)
            self.player_two_controller_release(e)

    def player_one_controller_press(self, e):
        if self.state == States.FIGHT:
            if not self.player_one.is_bot:
                if e.char == "d":
                    self.player_one.right()
                if e.char == "a":
                    self.player_one.left()
                if e.char == " ":
                    self.player_one.attack()
                if e.char == "w":
                    self.player_one.jump()
        if self.state == States.SELECT:
            if e.char == "s":
                self.selected_characters[0] = (self.selected_characters[0] + 1) % len(CharacterNames)
            if e.char == "w":
                self.selected_characters[0] = (self.selected_characters[0] - 1) % len(CharacterNames)
            if e.char == " ":
                self.state = "help me up"

    def player_two_controller_press(self, e):
        if self.state == States.FIGHT:
            if not self.player_two.is_bot:
                if e.char == "l":
                    self.player_two.right()
                if e.char == "j":
                    self.player_two.left()
                if e.char == "k":
                    self.player_two.attack()
                if e.char == "i":
                    self.player_two.jump()
        if self.state == States.SELECT:
            if e.char == "k":
                self.selected_characters[1] = (self.selected_characters[1] + 1) % len(CharacterNames)
            if e.char == "i":
                self.selected_characters[1] = (self.selected_characters[1] - 1) % len(CharacterNames)

    def player_one_controller_release(self, e):
        if not self.player_one.is_bot:
            if e.char in ['w', 'a', ' ', 'd']:
                self.player_one.stance()

    def player_two_controller_release(self, e):
        if not self.player_two.is_bot:
            if e.char in ['i', 'j', 'k', 'l']:
                self.player_two.stance()

    def create_fighter(self, ai, name, position, character_select=False):
        direction = self.RIGHT
        if position == self.PLAYER_TWO_POSITION:
            direction = "left"
        Character = CHARACTERS[name]
        fighter = Character(direction, self.canvas, position, is_bot=ai, hide_status_bar=character_select)
        return fighter


root = Tk()
root.title("Naruto: Shippuden Stories")
img = PhotoImage(file=rf"{PROJECT_NAME}\sprites\Future\smile.png")
root.iconphoto(False, img)
Battle(root)
root.mainloop()
