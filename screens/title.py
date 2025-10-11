from time import sleep
from PIL import Image, ImageTk, ImageOps
from screens.utils import create_fighter
from characters.character import CharacterNames

class TitleScreen():
    def __init__(self, canvas):
        self.canvas = canvas
        self.images = []
        self.WIDTH = canvas.winfo_reqwidth()
        self.HEIGHT = canvas.winfo_reqheight()
        self.active = True

        self.selected_item = 0
    
    def title_screen(self):
        button_texts = ["story", "battle"]
        self.set_background(filename="training")
        self.get_title_image()
        self.demo_character = create_fighter(self.canvas, False, CharacterNames.KAKASHI, (100, 400), character_select=True)
        self.demo_character.demo()
        for i in range(2):
            self.images.append(self.get_title_button(position=i))
            self.images.append(self.get_title_button(position=i, text=button_texts[i]))

        while self.active:
            self.canvas.update()
            self.demo_character.animate()
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
        button_width = 180
        button_height = 50
        ratio = img.width / img.height
        text_height = 30
        text_width = int(text_height * ratio)

        if text is None:
            img = img.resize((button_width, button_height), Image.Resampling.LANCZOS)
            img = ImageOps.mirror(img) if position % 2 == 0 else img
        else:
            img = img.resize((text_width, text_height), Image.Resampling.LANCZOS)

        select_image = ImageTk.PhotoImage(img)
        self.images.append(select_image)

        x = self.WIDTH / 3 + 20 + ((button_width - text_width)/2 if text else 0)
        y = position * 65 + 165 + ((button_height - text_height)/2 if text else 0)
        return self.canvas.create_image(x, y, image=select_image, anchor="nw")
    

    def key_press(self, e):
        if e.char == "s":
            self.destroy()
        if e.char == "w":
            self.destroy()

    def key_release(self, e):
        pass