from characters.characters.deidara import Deidara
from characters.characters.kakashi import Kakashi
from characters.characters.sasori import Sasori
from characters.characters.itachi import Itachi
from characters.characters.kisame import Kisame
from characters.characters.gaara import Gaara
from characters.characters.naruto import Naruto
from characters.characters.sakura import Sakura
from characters.characters.lee import Lee
from enum import Enum

class CharacterNames(Enum):
    NARUTO = "naruto"
    SAKURA = "sakura"
    KAKASHI = "kakashi"
    LEE = "lee"
    GAARA = "gaara"
    ITACHI = "itachi"
    KISAME = "kisame"
    DEIDARA = "deidara"
    SASORI = "sasori"

CHARACTERS = {
    CharacterNames.NARUTO: Naruto,
    CharacterNames.SAKURA: Sakura,
    CharacterNames.KAKASHI: Kakashi,
    CharacterNames.LEE: Lee,
    CharacterNames.GAARA: Gaara,
    CharacterNames.ITACHI: Itachi,
    CharacterNames.KISAME: Kisame,
    CharacterNames.DEIDARA: Deidara,
    CharacterNames.SASORI: Sasori,
}