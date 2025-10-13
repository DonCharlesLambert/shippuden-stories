from storyline.common import Run, Speech, Fight, Background, Appear
from screens.background import Backgrounds
from characters.character import CharacterNames
from const import LEFT, RIGHT

STORY = [
    Background(Backgrounds.TRAINING),
    Appear(CharacterNames.KAKASHI, 500),
    Run(CharacterNames.NARUTO, 100),
    Speech(CharacterNames.NARUTO, "Train me please", side=LEFT),
    Speech(CharacterNames.KAKASHI, "nah lil bro", side=RIGHT),
    Fight(CharacterNames.NARUTO, CharacterNames.KAKASHI),
    Speech(CharacterNames.KAKASHI, "u got too strong", side=RIGHT),
]