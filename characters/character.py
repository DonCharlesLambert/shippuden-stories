from .deidara import Deidara
from .kakashi import Kakashi
from .sasori import Sasori
from .itachi import Itachi
from .kisame import Kisame
from .gaara import Gaara
from .naruto import Naruto
from .sakura import Sakura
from enum import Enum

class CharacterNames(Enum):
    NARUTO = "naruto"
    SAKURA = "sakura"
    KAKASHI = "kakashi"
    GAARA = "gaara"
    ITACHI = "itachi"
    KISAME = "kisame"
    DEIDARA = "deidara"
    SASORI = "sasori"

CHARACTERS = {
    CharacterNames.NARUTO: Naruto,
    CharacterNames.SAKURA: Sakura,
    CharacterNames.KAKASHI: Kakashi,
    CharacterNames.GAARA: Gaara,
    CharacterNames.ITACHI: Itachi,
    CharacterNames.KISAME: Kisame,
    CharacterNames.DEIDARA: Deidara,
    CharacterNames.SASORI: Sasori,
}