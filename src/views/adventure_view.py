import arcade
from arcade.experimental.crt_filter import CRTFilter
from pyglet.math import Vec2

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

        width, height = self.window.get_size()
        # width, height = self.get_size()

        self.crt_filter = CRTFilter(width, height,
                            resolution_down_scale=0.5,
                            hard_scan=-4.0,
                            hard_pix=-1.5,
                            display_warp = Vec2(1.0 / 32.0, 1.0 / 24.0),
                            mask_dark=0.25,
                            mask_light=.75)


    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)


    def on_draw(self):
        # This command has to happen before we start drawing
        # self.clear()
        arcade.start_render()

        self.crt_filter.use()
        self.crt_filter.clear()

        self.all_sprites_list.draw()

        self.window.use()
        self.window.clear()
        self.crt_filter.draw()


    def on_update(self, delta_time):
        """ Movement and game logic """

        self.all_sprites_list.update()


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key in [arcade.key.Q, arcade.key.ESCAPE]:
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
