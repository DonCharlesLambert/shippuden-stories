import random
from characters.player import Fighter


class Bot(Fighter):
    def __init__(self, name, initial_direction, sprite_canvas, pos, hide_status_bar = False):
        super(Bot, self).__init__(name, initial_direction, sprite_canvas, pos, hide_status_bar)
        self.is_bot = True

    def animate(self):
        super().animate()
        if self.is_bot:
            self.decide_movement()

    def decide_movement(self):
        if self.opponent and self.opponent.dead:
            self.stance()

        elif self.action_is(self.DAMAGE) or self.action_is(self.FALL):
            pass

        elif self.opponent and self.opponent.action_is(self.FALL) and not self.action_is(self.RUN):
            self.away()

        elif self.opponent and self.action_is(self.ATTACK) and not self.opponent.action_is(self.DAMAGE):
            self.stance()

        elif self.action_is(self.ATTACK):
            pass

        elif self.next_to_opponent():
            self.decide_to_attack()

        else:
            self.run_to_opponent()

    def decide_to_attack(self):
        if random.random() < 0.2:
            self.attack()
        else:
            self.stance()

    def run_to_opponent(self):
        if self.opponent.pos()[0] < self.pos()[0]:
            self.left()
        else:
            self.right()
