import arcade


class MaFenetre(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Mon premier programme")
        self.background_color = arcade.color.SKY_BLUE

    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(300, 200, 50, arcade.color.YELLOW)


MaFenetre()
arcade.run()