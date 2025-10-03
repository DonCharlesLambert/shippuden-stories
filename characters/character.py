from .deidara import Deidara
from .kakashi import Kakashi
from enum import Enum

class CharacterNames(Enum):
    DEIDARA = "deidara"
    KAKASHI = "kakashi"

CHARACTERS = {
    CharacterNames.DEIDARA: Deidara,
    CharacterNames.KAKASHI: Kakashi
}