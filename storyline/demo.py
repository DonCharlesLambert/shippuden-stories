from storyline.common import Run, Speech, Fight
from characters.character import CharacterNames
from const import LEFT, RIGHT

STORY = [
    Run(CharacterNames.NARUTO, 100),
    Run(CharacterNames.KAKASHI, 500),
    Speech(CharacterNames.NARUTO, "Train me please", side=LEFT),
    Speech(CharacterNames.KAKASHI, "nah lil bro", side=RIGHT),
    Fight(CharacterNames.NARUTO, CharacterNames.KAKASHI),
    Speech(CharacterNames.KAKASHI, "u got too strong", side=RIGHT),
]