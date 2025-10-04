from .deidara import Deidara
from .kakashi import Kakashi
from .sasori import Sasori
from .itachi import Itachi
from .kisame import Kisame
from .gaara import Gaara
from enum import Enum

class CharacterNames(Enum):
    DEIDARA = "deidara"
    KAKASHI = "kakashi"
    ITACHI = "itachi"
    KISAME = "kisame"
    SASORI = "sasori"
    GAARA = "gaara"

CHARACTERS = {
    CharacterNames.DEIDARA: Deidara,
    CharacterNames.KAKASHI: Kakashi,
    CharacterNames.ITACHI: Itachi,
    CharacterNames.KISAME: Kisame,
    CharacterNames.SASORI: Sasori,
    CharacterNames.GAARA: Gaara
}