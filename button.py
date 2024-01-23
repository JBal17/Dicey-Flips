import pygame
import time

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check if mouse is over button and clicked
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True and self.clicked == False:
                self.clicked = True
                time.sleep(0.2)
                print('Clicked')
                action = True
            if pygame.mouse.get_pressed()[0] == False:
                self.clicked = False

        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
    
    def hide(self, surface, bg_colour):
        pygame.draw.rect(surface, bg_colour, self.rect) # covers button rectangle 
    
def main():
    pass
    
if __name__ == "__main__":
    main()