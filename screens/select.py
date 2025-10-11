
from PIL import Image, ImageTk
from time import sleep

from const import PLAYER_ONE_POSITION, PLAYER_TWO_POSITION
from screens.utils import create_fighter
from characters.character import CharacterNames

class SelectScreen():
    def __init__(self, canvas):
        self.canvas = canvas
        self.images = []
        self.WIDTH = canvas.winfo_reqwidth()
        self.HEIGHT = canvas.winfo_reqheight()
        self.active = True

        self.selected_characters = [0, 1]
        self.select_items = []

    
    def select_screen(self):
        self.set_background()
        names = list(CharacterNames)
        for i, character in enumerate(names):
            self.select_items.append(self.get_character_select(character.value, i))
        
        self.player_one_icon = self.get_character_select("1p", self.selected_characters[0])
        self.player_two_icon = self.get_character_select("2p", self.selected_characters[1], offset=True)
        self.mock_player_one = create_fighter(self.canvas, False, names[self.selected_characters[0]], PLAYER_ONE_POSITION, character_select=True)
        self.mock_player_two = create_fighter(self.canvas, False, names[self.selected_characters[1]], PLAYER_TWO_POSITION, character_select=True)
        

        time = 0
        while self.active:
            self.canvas.update()
            self.mock_player_one.animate()
            self.mock_player_two.animate()
            if self.mock_player_one.name != names[self.selected_characters[0]].value:
                self.mock_player_one.destroy()
                self.mock_player_one = create_fighter(self.canvas, False, names[self.selected_characters[0]], PLAYER_ONE_POSITION, character_select=True)
                self.canvas.delete(self.player_one_icon)
                self.player_one_icon = self.get_character_select("1p", self.selected_characters[0])

            if self.mock_player_two.name != names[self.selected_characters[1]].value:
                self.mock_player_two.destroy()
                self.mock_player_two = create_fighter(self.canvas, False, names[self.selected_characters[1]], PLAYER_TWO_POSITION, character_select=True)
                self.canvas.delete(self.player_two_icon)
                self.player_two_icon = self.get_character_select("2p", self.selected_characters[1], offset=True)
            sleep(0.1)
            time += 0.1

        return names[self.selected_characters[0]], names[self.selected_characters[1]]
    
    def destroy(self):
        [self.canvas.delete(item) for item in self.select_items]
        self.canvas.delete(self.player_one_icon)
        self.canvas.delete(self.player_two_icon)
        self.mock_player_one.destroy()
        self.mock_player_two.destroy()
        self.active = False

    
    def get_character_select(self, character_name, position=0, offset=False):
        img = Image.open(rf'sprites\select\{character_name}.png')
        select_image = ImageTk.PhotoImage(img)
        self.images.append(select_image)

        x = 90 + (150 * (position // 3)) + (0 if not offset else 100 )
        y = (position % 3) * 50 + 20
        return self.canvas.create_image(x, y, image=select_image, anchor="nw")
    
    
    def set_background(self, filename="rocks"):
        img = Image.open(rf'sprites\misc\{filename}.png')
        img = img.resize((self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(img)
        self.images.append(bg_image)

        canvas_item = self.canvas.create_image(0, 0, image=bg_image, anchor="nw")
        return canvas_item

    def key_press(self, e):
        if e.char == "s":
            self.selected_characters[0] = (self.selected_characters[0] + 1) % len(CharacterNames)
        if e.char == "w":
            self.selected_characters[0] = (self.selected_characters[0] - 1) % len(CharacterNames)
        if e.char == "d":
            self.selected_characters[1] = (self.selected_characters[1] + 1) % len(CharacterNames)
        if e.char == "a":
            self.selected_characters[1] = (self.selected_characters[1] - 1) % len(CharacterNames)
        if e.char == " ":
            self.destroy()

    def key_release(self, e):
        pass