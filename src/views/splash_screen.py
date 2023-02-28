import arcade
import time

from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class SplashScreen(arcade.View):
    def __init__(self):
        super().__init__()
        self.alpha = 0  # initialize alpha to 0 (fully transparent)

    
    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.start_time = time.time()
        print(f"load_time: {self.start_time}")


    def on_update(self, delta_time):
        if time.time() > self.start_time + 3:
            self.show_next_view()


    def on_draw(self):
        self.clear()
        color_with_alpha = arcade.color.WHITE + (self.alpha,)  # create a color object with the desired alpha value
        arcade.draw_text("Loading screen...", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         color_with_alpha,
                         font_size=30, anchor_x="center")
        self.alpha = min(self.alpha + 5, 255)  # increase alpha up to 255


    def show_next_view(self):
        from src.views.adventure_view import AdventureView
        next_view = AdventureView()
        self.window.show_view(next_view)
