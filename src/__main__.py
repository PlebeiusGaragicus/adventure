import logging
import arcade

from .constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from .views.splash_screen import SplashScreen

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[logging.StreamHandler()],
         format="%(name)s [%(levelname)s] (%(filename)s @ %(lineno)d) %(message)s")

    logging.getLogger("arcade.application").setLevel(logging.INFO)


    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    view = SplashScreen()
    window.show_view(view)
    # arcade.Window.set_mouse_visible(False)
    arcade.run()
