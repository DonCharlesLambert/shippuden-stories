
from enum import Enum

class Backgrounds(Enum):
    ROCKS = "rocks"
    TRAINING = "training"

FLOOR_HEIGHT = {
    Backgrounds.TRAINING: 400,
    Backgrounds.ROCKS: 370,
}