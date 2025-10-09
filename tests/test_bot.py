import unittest
from unittest.mock import MagicMock, patch
from tkinter import Canvas, Tk
from bot import Bot


class TestBot(unittest.TestCase):

    def setUp(self):
        
        self.mock_opponent = MagicMock()
        self.mock_opponent.pos.return_value = (100, 0)
        self.mock_opponent.action_is.return_value = False

        self.root = Tk()
        self.canvas = Canvas(self.root, width=1000, height=1000)
        
        self.bot = Bot(
            name="deidara",
            initial_direction="right",
            sprite_canvas=self.canvas,
            pos=(0, 0),
            hide_status_bar=True
        )
        self.bot.opponent = self.mock_opponent

        self.bot.action_is = MagicMock(return_value=False)
        self.bot.run_to_opponent = Bot.run_to_opponent.__get__(self.bot)

    def test_decide_movement_when_damaged_or_falling(self):
        self.bot.action_is = MagicMock(return_value=False)
        self.bot.action_is.side_effect = lambda action: action in [self.bot.DAMAGE, self.bot.FALL]
        with patch.object(self.bot, 'attack', wraps=self.bot.attack) as attack:
            with patch.object(self.bot, 'left', wraps=self.bot.left) as left:
                with patch.object(self.bot, 'right', wraps=self.bot.right) as right:
                    self.bot.decide_movement()
                    attack.assert_not_called()
                    left.assert_not_called()
                    right.assert_not_called()
                    
    
    def tearDown(self):
        try:
            self.canvas.destroy()
        except Exception:
            pass
        try:
            self.root.destroy()
        except Exception:
            pass

    def test_decide_movement_opponent_fallen(self):
        self.bot.action_is = MagicMock(return_value=False)
        self.bot.action_is.side_effect = lambda action: False
        self.mock_opponent.action_is.side_effect = lambda x: x == self.bot.FALL
        with patch.object(self.bot, 'away', wraps=self.bot.away) as away:
            self.bot.decide_movement()
            away.assert_called_once()
    
    def test_decide_movement_attack_but_opponent_not_damaged(self):
        self.bot.action_is = MagicMock(return_value=False)
        self.bot.action_is.side_effect = lambda action: action == self.bot.ATTACK
        self.mock_opponent.action_is.return_value = False
        with patch.object(self.bot, 'stance', wraps=self.bot.stance) as stance:
            self.bot.decide_movement()
            stance.assert_called_once()

    def test_decide_movement_next_to_opponent_triggers_attack_decision(self):
        self.bot.next_to_opponent = MagicMock(return_value=False)
        self.bot.next_to_opponent.return_value = True
        self.bot.decide_to_attack = MagicMock()
        with patch.object(self.bot, 'decide_to_attack', wraps=self.bot.decide_to_attack) as decide_to_attack:
            self.bot.decide_movement()
            decide_to_attack.assert_called_once()

    def test_decide_to_attack_triggers_attack_or_stance(self):
        with patch('random.random', return_value=0.1):
            with patch.object(self.bot, 'attack', wraps=self.bot.attack) as attack:
                self.bot.decide_to_attack()
                attack.assert_called_once()

        with patch('random.random', return_value=0.9):
            with patch.object(self.bot, 'stance', wraps=self.bot.stance) as stance:
                self.bot.decide_to_attack()
                stance.assert_called_once()

    def test_run_to_opponent_moves_correct_direction(self):
        self.bot.pos = MagicMock(return_value=(0, 0))
        self.mock_opponent.pos.return_value = (10, 0)
        with patch.object(self.bot, 'right', wraps=self.bot.right) as right:
            self.bot.run_to_opponent()
            right.assert_called_once()

        self.mock_opponent.pos.return_value = (-10, 0)
        with patch.object(self.bot, 'left', wraps=self.bot.left) as left:
            self.bot.run_to_opponent()
            left.assert_called_once()

if __name__ == "__main__":
    unittest.main()
