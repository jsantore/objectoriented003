import random

import arcade

class ShipGoldWindow(arcade.Window):
    def __init__(self):
        super().__init__(1200, 1000, "Collect the Gold")
        self.ship = None
        self.goals = arcade.SpriteList()
        self.score =0
        self.sound = None
        self.throw_sound = None

    def setup(self):
        self.ship = arcade.Sprite("pirate-galleon.png")
        self.sound = arcade.load_sound(":resources:sounds/coin2.wav")
        self.throw_sound = arcade.load_sound(":resources:sounds/lose2.wav")
        for number in range(7):
            gold = arcade.Sprite("gold-coins-large.png")
            gold.center_x = random.randint(30, 1170)
            gold.center_y = random.randint(30, 970)
            self.goals.append(gold)

    def on_update(self, delta_time):
        gold_piles_collected =  arcade.check_for_collision_with_list(self.ship,self.goals)
        if gold_piles_collected:
            arcade.play_sound(self.sound)
            self.score += len(gold_piles_collected)
            for gold in gold_piles_collected:
                self.goals.remove(gold)
                self.score+=1

    def on_draw(self):
        arcade.start_render()
        self.ship.draw()
        self.goals.draw()
        score_text = arcade.Text(f"Score {self.score}", 20, 900, arcade.color.RUBY_RED, font_size=18)
        score_text.draw()
        arcade.finish_render()

    def on_mouse_motion(self, x, y, dx, dy):
        self.ship.center_x = x
        self.ship.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        pile = arcade.Sprite("gold-coins-large.png")
        pile.center_x = self.ship.center_x
        pile.center_y = self.ship.center_y - 74
        self.goals.append(pile)
        arcade.play_sound(self.throw_sound)
        self.score -= 1