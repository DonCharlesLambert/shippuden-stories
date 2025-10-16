from tkinter import Canvas, Tk, PhotoImage
import winsound
import argparse

from const import WIDTH, HEIGHT
from screens.title import TitleScreen
from screens.select import SelectScreen
from screens.fight import FightScreen
from screens.story import StoryScreen


class Game:
    images = []

    def __init__(self, game_window, story_name="demo"):
        self.game_window = game_window
        self.canvas = Canvas(game_window, width=WIDTH, height=HEIGHT)
        self.canvas.bind("<KeyPress>", self.key_press)
        self.canvas.bind("<KeyRelease>", self.key_release)
        self.canvas.pack()
        self.canvas.focus_set()

        self.title_select = 0
        self.story_name = story_name

        # winsound.PlaySound(rf'music\LifeIsGood.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
        self.game_window.after(0, self.game)

    def game(self):
        while True:
            self.screen = TitleScreen(self.canvas)
            choice = self.screen.title_screen()

            if choice == 1:
                self.free_battle()
            else:
                self.story()

    def story(self):
            self.screen = StoryScreen(self.canvas, story = self.story_name)
            self.screen.story_screen()

    def free_battle(self):
        while True:
            self.screen = SelectScreen(self.canvas)
            character_one, character_two = self.screen.select_screen()
            
            self.screen = FightScreen(self.canvas)
            self.screen.fight(character_one, character_two)

    def key_press(self, e):
        self.screen.key_press(e)

    def key_release(self, e):
        self.screen.key_release(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Shippuden Stories')
    parser.add_argument('-s', '--story', default="demo")
    args = parser.parse_args()

    root = Tk()
    root.title("Naruto: Shippuden Stories")
    img = PhotoImage(file=rf"sprites\Future\smile.png")
    root.iconphoto(False, img)
    Game(root, story_name=args.story)
    root.mainloop()
