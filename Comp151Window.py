import arcade

class Comp151Window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Demo Window")
        self.player =None
        self.targets = []
        self.score = 0

    def setup(self):
        pass

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        arcade.start_render()
        #do drawing here
        arcade.finish_render()
