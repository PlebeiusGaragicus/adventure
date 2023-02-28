import arcade


from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from src.input import SNESButton, MOVEMENT_SPEED, DEAD_ZONE


SPRITE_SCALING = 0.5


class Player(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale)

        joysticks = arcade.get_joysticks()
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
            self.joystick.push_handlers(self)
        else:
            print("There are no joysticks, plug in a joystick and run again.")
            self.joystick = None

            #arcade.close_window()


    def update(self):
        """ Move the player """

        if self.joystick:

            self.change_x = self.joystick.x * MOVEMENT_SPEED
            if abs(self.change_x) < DEAD_ZONE:
                self.change_x = 0

            self.change_y = -self.joystick.y * MOVEMENT_SPEED
            if abs(self.change_y) < DEAD_ZONE:
                self.change_y = 0

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1



    def on_joybutton_press(self, _joystick, button):
        """ Handle button-down event for the joystick """
        print("Button {} down".format(button))

        if button == SNESButton.A:
            print("A")
            arcade.set_background_color(arcade.color.AMAZON)
        if button == SNESButton.B:
            print("B")
            arcade.set_background_color(arcade.color.ANTIQUE_BRONZE)
        if button == SNESButton.X:
            print("X")
            arcade.set_background_color(arcade.color.ANTIQUE_FUCHSIA)
        if button == SNESButton.Y:
            arcade.set_background_color(arcade.color.ANTIQUE_RUBY)
        if button == SNESButton.L:
            arcade.set_background_color(arcade.color.ANTIQUE_WHITE)
        if button == SNESButton.R:
            arcade.set_background_color(arcade.color.AO)
        if button == SNESButton.START:
            arcade.set_background_color(arcade.color.APPLE_GREEN)
        if button == SNESButton.SELECT:
            arcade.set_background_color(arcade.color.AQUA)

    # def on_joybutton_release(self, _joystick, button):
    #     """ Handle button-up event for the joystick """
    #     pass

    # def on_joyhat_motion(self, _joystick, hat_x, hat_y):
    #     """ Handle hat events """
    #     print("Hat ({}, {})".format(hat_x, hat_y))