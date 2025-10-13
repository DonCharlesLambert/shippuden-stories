
from enum import Enum

class Backgrounds(Enum):
    ROCKS = "rocks"
    TRAINING = "training"
    DESERT = "desert"
    UCHICHA = "uchiha"

FLOOR_HEIGHT = {
    Backgrounds.TRAINING: 400,
    Backgrounds.ROCKS: 370,
    Backgrounds.DESERT: 370,
    Backgrounds.UCHICHA: 400,
}