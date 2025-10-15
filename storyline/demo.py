from storyline.common import Run, Speech, Fight, Background, Appear, Teleport
from screens.background import Backgrounds
from characters.character import CharacterNames
from const import LEFT, RIGHT

# This story was written by an LLM... Can you write something better???

STORY = [
    # Scene 1 — Team 7 Reunion
    Background(Backgrounds.TRAINING),
    Appear(CharacterNames.NARUTO, 150),
    Appear(CharacterNames.SAKURA, 100),
    Appear(CharacterNames.KAKASHI, 500),
    Speech(CharacterNames.KAKASHI, "Alright, Team 7... time to see how much you've improved.", side=RIGHT),
    Speech(CharacterNames.NARUTO, "Heh, I’ve been training nonstop! I’ll show you how strong I’ve gotten!", side=LEFT),
    Speech(CharacterNames.SAKURA, "You’re not the only one who’s gotten stronger, Naruto!", side=LEFT),
    Fight(CharacterNames.NARUTO, CharacterNames.KAKASHI),
    Speech(CharacterNames.KAKASHI, "Impressive... You two really have grown.", side=RIGHT),

    # Scene 2 — Trouble in the Sand
    Background(Backgrounds.DESERT),
    Appear(CharacterNames.GAARA, 350),
    Speech(CharacterNames.GAARA, "These Akatsuki... they’re coming for me.", side=LEFT),
    Teleport(CharacterNames.DEIDARA, 300),
    Speech(CharacterNames.DEIDARA, "Heh, Kazekage, your art ends here... boom!", side=RIGHT),
    Fight(CharacterNames.GAARA, CharacterNames.DEIDARA),
    Speech(CharacterNames.DEIDARA, "You were strong... but my art is an explosion!", side=RIGHT),

    # Scene 3 — Team 7 on the Move
    Background(Backgrounds.ROCKS),
    Appear(CharacterNames.NARUTO, 100),
    Appear(CharacterNames.SAKURA, 350),
    Appear(CharacterNames.KAKASHI, 550),
    Speech(CharacterNames.NARUTO, "We have to save Gaara! I won’t let them take him!", side=LEFT),
    Speech(CharacterNames.KAKASHI, "Stay sharp. The Akatsuki are dangerous.", side=RIGHT),
    Run(CharacterNames.NARUTO, 150),

    # Scene 4 — Akatsuki Hideout
    Background(Backgrounds.UCHICHA),
    Appear(CharacterNames.SASORI, 100),
    Appear(CharacterNames.DEIDARA, 200),
    Run(CharacterNames.NARUTO, 400),
    Run(CharacterNames.SAKURA, 450),
    Speech(CharacterNames.DEIDARA, "Ah the nine tails jinchuriki...", side=RIGHT),
    Speech(CharacterNames.DEIDARA, "Your friend Gaara was so easy to kill", side=RIGHT),
    Run(CharacterNames.DEIDARA, -25),
    Speech(CharacterNames.NARUTO, "I’ll never forgive you!", side=LEFT),
    Run(CharacterNames.NARUTO, -25),
    Speech(CharacterNames.SASORI, "...", side=RIGHT),
    Fight(CharacterNames.SAKURA, CharacterNames.SASORI),

    # Scene 5 — Rescue and Resolve
    Background(Backgrounds.DESERT),
    Appear(CharacterNames.NARUTO, 150),
    Appear(CharacterNames.GAARA, 400),
    Speech(CharacterNames.NARUTO, "We did it, Gaara... you’re safe now.", side=LEFT),
    Speech(CharacterNames.GAARA, "Thank you, Naruto... You’ve changed, too.", side=RIGHT),
    Speech(CharacterNames.NARUTO, "Heh... guess we both have.", side=LEFT),
]
