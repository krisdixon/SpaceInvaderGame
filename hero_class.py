
class Hero(Game_Object):
    def__init__(self, image, x_coordinate, y_coordinate):
        self_is_alive = True
        self.img = image
        self.xcor = x_coordinate
        self.ycor = y_coordinate
    def show(self, game_display): 
        game_display.blit(self.img, (self.xcor, self.ycor))
        

