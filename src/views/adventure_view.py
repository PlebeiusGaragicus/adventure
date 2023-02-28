import arcade
import os

from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from src.input import SNESButton, MOVEMENT_SPEED, DEAD_ZONE
from src.sprites.player import Player, SPRITE_SCALING


class AdventureView(arcade.View):
    def __init__(self):
        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        super().__init__()

        self.all_sprites_list = arcade.SpriteList()
        self.player_sprite = Player(":resources:images/animated_characters/female_person/"
                                    "femalePerson_idle.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.all_sprites_list.append(self.player_sprite)


    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)


    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        self.clear()
        self.all_sprites_list.draw()


    def on_update(self, delta_time):
        """ Movement and game logic """

        self.all_sprites_list.update()


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.ESCAPE:
            arcade.close_window()
        elif key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
