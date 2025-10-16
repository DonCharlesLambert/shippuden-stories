
from PIL import Image, ImageTk
from time import sleep
from const import LEFT, PLAYER_ONE_POSITION
from screens.fight import FightScreen
from screens.utils import create_fighter
from characters.character import CharacterNames
from storyline.stories import STORIES
from storyline.common import Background, Speech, Run, Fight, Appear, Teleport
from screens.background import FLOOR_HEIGHT
import os

class StoryScreen():
    def __init__(self, canvas, story):
        self.canvas = canvas
        self.images = []
        self.WIDTH = canvas.winfo_reqwidth()
        self.HEIGHT = canvas.winfo_reqheight()
        self.active = True
        self.story = story

        self.await_press = False
        self.fight = None
        self.present_characters = {}
        self.floor_height = 0
        self.background = None
        self.skip_text = False

    def story_screen(self):
        for part in STORIES.get(self.story, "demo"):
            if type(part) == Background:
                self.clear()
                self.set_background(part.background)
                self.background = part.background
            if type(part) == Speech:
                self.speak(part.speaker, part.text, part.side)
            if type(part) == Teleport:
                self.teleport(part.character, part.x)
            if type(part) == Appear:
                self.appear(part.character, part.x)
            if type(part) == Run:
                self.run(part.character, part.x)
            if type(part) == Fight:
                self.fight = FightScreen(self.canvas)
                self.fight.fight(part.player_one, part.ai, self.background)
                self.fight = None
        while self.await_press:
            self.animate()
    
    def speak(self, speaker, text, side=LEFT):
        mug = self.get_mug(speaker, side)
        dialogue = self.set_dialogue(side)
        text_x = 10 if side == LEFT else self.WIDTH - 290
        text_obj = self.canvas.create_text(text_x, 90, text="")
        self.skip_text = False
        for i in range(0, len(text)):
            if self.skip_text: i = len(text) - 1
            self.canvas.delete(text_obj)
            text_obj = self.canvas.create_text(text_x, 90, text=text[0:i+1], anchor="nw", fill="white", font=("MS Gothic", 12), width=250)
            self.animate()
            if self.skip_text and i == len(text) - 1: break 
        self.await_press = True
        while self.await_press:
            self.animate()
        self.canvas.delete(text_obj)
        self.canvas.delete(mug)
        self.canvas.delete(dialogue)

    def appear(self, name, x):
        fighter = self.present_characters.get(name, None)
        if fighter is None:
            initial_positon = x, self.floor_height
            self.present_characters[name] = create_fighter(self.canvas, False, name, initial_positon, True)


    def run(self, name, x):
        initial_x = 1 if x < self.WIDTH / 2 else self.WIDTH - 1
        self.appear(name, initial_x)
        fighter = self.present_characters[name]
        while abs(fighter.pos()[0] - x) > 10:
            if fighter.pos()[0] > x:
                fighter.left()
            else:
                fighter.right()
            self.animate()
        fighter.stance()
            
    def teleport(self, name, x):
        fighter = self.present_characters.get(name, None)
        if fighter is not None:
            self.destroy_character(name)
            # XXX - deal with this later

        img = Image.open(rf'sprites\common\teleport\0.png')
        teleport_image = ImageTk.PhotoImage(img)
        teleport_item = self.canvas.create_image(x, self.floor_height, image=teleport_image, anchor="s")
        for i in range(1, 6):
            teleport_image = ImageTk.PhotoImage(Image.open(rf'sprites\common\teleport\{i}.png'))
            self.canvas.itemconfig(teleport_item, image=teleport_image)
            if i == 1:
                self.appear(name, x)
                self.canvas.tag_raise(teleport_item)
            self.animate()





    def animate(self):
        [fighter.animate() for fighter in self.present_characters.values()]
        self.canvas.update()
        sleep(0.1)

    def clear(self):
        [fighter.destroy() for fighter in self.present_characters.values()]
        self.present_characters = {}

    def destroy_character(self, name):
        self.present_characters[name].destroy()
        self.present_characters.pop(name)        
    
    def set_background(self, background):
        img = Image.open(rf'sprites\misc\{background.value}.png')
        img = img.resize((self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight()), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(img)
        self.images.append(bg_image)
        self.floor_height = FLOOR_HEIGHT[background]
        canvas_item = self.canvas.create_image(0, 0, image=bg_image, anchor="nw")
        return canvas_item
    
    def get_mug(self, name=CharacterNames.NARUTO, side=LEFT):
        img = Image.open(os.path.join('sprites', name.value, "mug.png"))
        width = int(100 * (img.width/img.height))
        img = img.resize((width, 100), Image.Resampling.LANCZOS)
        mug_image = ImageTk.PhotoImage(img)
        self.images.append(mug_image)
        canvas_item = self.canvas.create_image(0 if side == LEFT else self.WIDTH - img.width, 0, image=mug_image, anchor="nw")
        return canvas_item


    def set_dialogue(self, side=LEFT):
        img = Image.open(rf'sprites\misc\dialogue.png')
        width = 300
        height = int((img.height/img.width) * width)
        img = img.resize((width, height), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(img)
        self.images.append(bg_image)

        canvas_item = self.canvas.create_image(0 if side == LEFT else self.WIDTH-width, 80, image=bg_image, anchor="nw")
        return canvas_item
    
    
    def key_press(self, e):
        if self.fight is not None:
            self.fight.key_press(e)
        self.skip_text = True
        self.await_press = False

    def key_release(self, e):
        if self.fight is not None:
            self.fight.key_release(e)