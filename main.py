from tkinter import Canvas, Tk, PhotoImage
import winsound
from time import sleep
from PIL import Image, ImageTk

from const import States, WIDTH, HEIGHT
from screens.title import TitleScreen
from screens.select import SelectScreen
from screens.fight import FightScreen


class Battle:
    images = []

    def __init__(self, game_window):
        self.game_window = game_window
        self.canvas = Canvas(game_window, width=WIDTH, height=HEIGHT)
        self.canvas.bind("<KeyPress>", self.key_press)
        self.canvas.bind("<KeyRelease>", self.key_release)
        self.canvas.pack()
        self.canvas.focus_set()

        self.title_select = 0

        # winsound.PlaySound(rf'music\LifeIsGood.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
        self.game_window.after(0, self.game)

    def game(self):
        self.state = States.TITLE # should change to a dynamic getter
        self.screen = TitleScreen(self.canvas)
        choice = self.screen.title_screen()

        self.set_background()
        while True:
            self.state = States.SELECT
            self.screen = SelectScreen(self.canvas)
            character_one, character_two = self.screen.select_screen()
            
            self.state = States.FIGHT
            self.screen = FightScreen(self.canvas)
            self.screen.fight(character_one, character_two)

    def set_background(self, filename="rocks"):
        img = Image.open(rf'sprites\misc\{filename}.png')
        img = img.resize((self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(img)

        canvas_item = self.canvas.create_image(0, 0, image=bg_image, anchor="nw")
        self.images.append(bg_image)
        return canvas_item


    def key_press(self, e):
        self.screen.key_press(e)

    def key_release(self, e):
        if self.state in [States.FIGHT]:
            self.screen.key_release(e)



root = Tk()
root.title("Naruto: Shippuden Stories")
img = PhotoImage(file=rf"sprites\Future\smile.png")
root.iconphoto(False, img)
Battle(root)
root.mainloop()
