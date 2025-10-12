
class Run:
    def __init__(self, character, x):
        self.character = character
        self.x = x

class Speech:
    def __init__(self, speaker, text, side):
        self.speaker = speaker
        self.text = text
        self.side = side
    
class Fight:
    def __init__(self, player_one, ai):
        self.player_one = player_one
        self.ai = ai