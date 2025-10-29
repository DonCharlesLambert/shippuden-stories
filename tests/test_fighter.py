import unittest
from unittest.mock import MagicMock, patch
from tkinter import Canvas, Tk
from characters.player import Fighter


class TestFighter(unittest.TestCase):
    def setUp(self):
        self.mock_opponent = MagicMock()
        self.mock_opponent.pos.return_value = (100, 0)
        self.mock_opponent.action_is.return_value = False

        self.root = Tk()
        self.canvas = Canvas(self.root, width=1000, height=1000)

        self.fighter = Fighter(
            name="deidara",
            initial_direction="right",
            sprite_canvas=self.canvas,
            pos=(0, 0),
        )
        self.fighter.opponent = self.mock_opponent

    def tearDown(self):
        try:
            self.canvas.destroy()
        except Exception:
            pass
        try:
            self.root.destroy()
        except Exception:
            pass

    def test_substitute(self):
        initial_substitutions = self.fighter.substitutions
        initial_animatable_children = len(self.fighter.animatable_children)
        self.fighter.substitute()
        self.assertEqual(self.fighter.substitutions, initial_substitutions - 1)
        self.assertEqual(
            len(self.fighter.animatable_children), initial_animatable_children + 1
        )

        for i in range(15):
            self.fighter.animate()

    def test_take_damage(self):
        self.fighter.health = 40
        with patch.object(
            self.fighter.status_bar,
            "update_chakra",
            wraps=self.fighter.status_bar.update_chakra,
        ) as chakra:
            self.fighter.take_damage()
            self.assertGreater(40, self.fighter.health)
            chakra.assert_called_once()

        self.fighter.health = 1
        with patch.object(self.fighter, "die", wraps=self.fighter.die) as die:
            self.fighter.take_damage()
            self.assertGreater(1, self.fighter.health)
            die.assert_called_once()


if __name__ == "__main__":
    unittest.main()
