from time import sleep
from PIL import Image, ImageTk, ImageOps
from screens.utils import create_fighter
from characters.character import CharacterNames

class TitleScreen():
    
    button_width = 180
    button_height = 50
    text_height = 30

    def __init__(self, canvas):
        self.canvas = canvas
        self.images = []
        self.WIDTH = canvas.winfo_reqwidth()
        self.HEIGHT = canvas.winfo_reqheight()
        self.active = True

        self.button_texts = ["story", "battle"]
        self.selected_item = 0
    
    def title_screen(self):
        self.set_background(filename="training")
        self.get_title_image()
        self.demo_character = create_fighter(self.canvas, False, CharacterNames.KAKASHI, (100, 400), character_select=True)
        self.demo_character.demo()
        for i in range(2):
            self.images.append(self.get_title_button(position=i))
            self.images.append(self.get_title_button(position=i, text=self.button_texts[i]))

        selekta_x, selekta_y = self.get_coords(0)
        self.selekta = Selekta(self.canvas, selekta_x, selekta_y)

        while self.active:
            self.canvas.update()
            self.demo_character.animate()
            self.selekta.animate()
            sleep(0.1)

        return self.selected_item

    def destroy(self):
        [self.canvas.delete(item) for item in self.images]
        self.demo_character.destroy()
        self.active = False

    def set_background(self, filename="rocks"):
        img = Image.open(rf'sprites\misc\{filename}.png')
        img = img.resize((self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(img)

        canvas_item = self.canvas.create_image(0, 0, image=bg_image, anchor="nw")
        self.images.append(bg_image)
        return canvas_item
    
    def get_title_image(self):
        width = 300
        img = Image.open(rf'sprites\misc\title.png')
        img = img.resize((width, 115), Image.Resampling.LANCZOS)
        select_image = ImageTk.PhotoImage(img)
        self.images.append(select_image)

        x, y = (self.WIDTH - width)/2, 30
        return self.canvas.create_image(x, y, image=select_image, anchor="nw")

    def get_title_button(self, position=0, text=None):
        img = Image.open(rf'sprites\misc\btn.png') if text is None else Image.open(rf'sprites\misc\{text}.png')
        ratio = img.width / img.height
        text_width = int(self.text_height * ratio)

        if text is None:
            img = img.resize((self.button_width, self.button_height), Image.Resampling.LANCZOS)
            img = ImageOps.mirror(img) if position % 2 == 0 else img
        else:
            img = img.resize((text_width, self.text_height), Image.Resampling.LANCZOS)

        select_image = ImageTk.PhotoImage(img)
        self.images.append(select_image)

        x, y = self.get_coords(position, text, text_width) 
        return self.canvas.create_image(x, y, image=select_image, anchor="nw")
    
    def get_coords(self, position, text=None, text_width=None):
        assert text_width is not None if text is not None else True
        x = self.WIDTH / 3 + 20 + ((self.button_width - text_width)/2 if text else 0)
        y = position * 65 + 165 + ((self.button_height - self.text_height)/2 if text else 0)
        return x, y

    def key_press(self, e):
        if e.char == "s":
            self.selected_item = (self.selected_item + 1) % len(self.button_texts)
        if e.char == "w":
            self.selected_item = (self.selected_item - 1) % len(self.button_texts)
        if e.char in ["s", "w"]:
            selekta_x, selekta_y = self.get_coords(self.selected_item)
            self.selekta.move(selekta_x, selekta_y)
        if e.char == " ":
            self.destroy()

    def key_release(self, e):
        pass

class Selekta():
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.img = None
        self.x_offset, self.y_offset = -10, 15
        self.item = self.create(x, y)

        self.speed = 1
        self.movement = 1


    def create(self, x, y):
        img = Image.open(rf'sprites\misc\selekta.png')
        img = img.resize((45, 15), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(img)
        return self.canvas.create_image(x + self.x_offset, y + self.y_offset, image=self.img, anchor="nw")
    
    def animate(self):
        self.canvas.move(self.item, self.speed, 0)
        self.movement += self.speed
        if abs(self.movement) > 5:
            self.speed = -self.speed

    def move(self, x, y):
        self.canvas.moveto(self.item, x + self.x_offset, y + self.y_offset)

