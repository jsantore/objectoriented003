import arcade

class Comp151Window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Demo Window")
        self.player =None
        self.targets = arcade.SpriteList()
        self.score = 0

    def setup(self):
        self.player = arcade.Sprite("f1-ship1-6.png")
        rock = arcade.Sprite(":resources:images/space_shooter/meteorGrey_med1.png")
        self.targets.append(rock)
        rock.center_y = 500
        rock.center_x = 700
        self.player.center_x = 200
        self.player.center_y = 500

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.targets.draw()
        arcade.finish_render()
