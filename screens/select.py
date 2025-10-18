
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

        self.current_choosing = 0
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
        
        self.selekta = Selekta(self.canvas, PLAYER_ONE_POSITION[0], PLAYER_ONE_POSITION[1])

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
            self.selekta.animate()
            sleep(0.1)
            time += 0.1

        return names[self.selected_characters[0]], names[self.selected_characters[1]]
    
    def destroy(self):
        [self.canvas.delete(item) for item in self.select_items]
        self.canvas.delete(self.player_one_icon)
        self.canvas.delete(self.player_two_icon)
        self.mock_player_one.destroy()
        self.mock_player_two.destroy()
        self.selekta.destroy()
        self.active = False

    
    def get_character_select(self, character_name, position=0, offset=False):
        img = Image.open(rf'sprites\select\{character_name}.png')
        select_image = ImageTk.PhotoImage(img)
        self.images.append(select_image)
        CHARACTERS_PER_COL = 4

        x = 90 + (150 * (position // CHARACTERS_PER_COL)) + (0 if not offset else 100 )
        y = (position % CHARACTERS_PER_COL) * 50 + 20
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
            self.selected_characters[self.current_choosing] = (self.selected_characters[self.current_choosing] + 1) % len(CharacterNames)
        if e.char == "w":
            self.selected_characters[self.current_choosing] = (self.selected_characters[self.current_choosing] - 1) % len(CharacterNames)
        if e.char == "d":
            self.current_choosing = (self.current_choosing + 1) % 2
        if e.char == "a":
            self.current_choosing = (self.current_choosing - 1) % 2
        if e.char in ["a", "d"]:
            selekta_x, selekta_y = PLAYER_ONE_POSITION if self.current_choosing == 0 else PLAYER_TWO_POSITION
            self.selekta.move(selekta_x, selekta_y)
        if e.char == " ":
            self.destroy()

    def key_release(self, e):
        pass


class Selekta():
    # similar to title selekta may need to change
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.img = None
        self.x_offset, self.y_offset = 0, -100
        self.item = self.create(x, y)

        self.speed = 1
        self.movement = 1


    def create(self, x, y):
        img = Image.open(rf'sprites\misc\sidelekta.png')
        img = img.resize((10, 30), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(img)
        return self.canvas.create_image(x + self.x_offset, y + self.y_offset, image=self.img, anchor="n")
    
    def animate(self):
        self.canvas.move(self.item, 0, self.speed)
        self.movement += self.speed
        if abs(self.movement) > 5:
            self.speed = -self.speed

    def move(self, x, y):
        self.canvas.moveto(self.item, x + self.x_offset, y + self.y_offset)

    def destroy(self):
        self.canvas.delete(self.item)