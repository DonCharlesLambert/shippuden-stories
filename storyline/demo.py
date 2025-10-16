from storyline.common import Run, Speech, Fight, Background, Appear, Teleport
from screens.background import Backgrounds
from characters.character import CharacterNames
from const import LEFT, RIGHT

STORY = [
    # Scene 1 — Team 7 Reunion
    Background(Backgrounds.DESERT),
    Appear(CharacterNames.NARUTO, 150),
    Appear(CharacterNames.ITACHI, 500),
    Speech(CharacterNames.NARUTO, "This is just a demo story, try and run an actual story!", side=LEFT),
    Speech(CharacterNames.ITACHI, "Yeah run the program using python -m main --story [storyname]", side=RIGHT),
    Speech(CharacterNames.NARUTO, "Let's fight", side=LEFT),
    Fight(CharacterNames.NARUTO, CharacterNames.ITACHI),
    Speech(CharacterNames.NARUTO, "Decent battle, now where is Sasuke!", side=LEFT),
]