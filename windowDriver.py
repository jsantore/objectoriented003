import arcade
from Comp151Window import Comp151Window

def main():
    our_window = Comp151Window(1200, 1000)
    our_window.setup()
    arcade.run()

main()