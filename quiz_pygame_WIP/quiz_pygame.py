# pygame example code
import pygame

pygame.init()
screen = pygame.display.set_mode((1366, 768))
clock = pygame.time.Clock()
running = True
dt = 0

# my code
game_display = pygame.display.set_mode((1366, 768))
Background = pygame.image.load("b17iuliana015.jpg")
# http://www.imageafter.com/image.php?image=b17iuliana015.jpg

# stack overflow code
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)

class InputBox:

        def __init__(self, x, y, w, h, text=''):
            self.rect = pygame.Rect(x, y, w, h)
            self.color = COLOR_INACTIVE
            self.text = text
            self.txt_surface = FONT.render(text, True, self.color)
            self.active = False

        def handle_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if self.rect.collidepoint(event.pos):
                    # Toggle the active variable.
                    self.active = not self.active
                else:
                    self.active = False
                # Change the current color of the input box.
                self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        print(self.text)
                        self.text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
                    # Re-render the text.
                    self.txt_surface = FONT.render(self.text, True, self.color)

        def update(self):
            # Resize the box if the text is too long.
            width = max(200, self.txt_surface.get_width()+10)
            self.rect.w = width

        def draw(self, screen):
            # Blit the text.
            screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
            # Blit the rect.
            pygame.draw.rect(screen, self.color, self.rect, 2)

# edited stack overflow code
input_box1 = InputBox(600, 500, 1000, 50)
input_boxes = [input_box1]

# pygame example code

while running:
    # stack overflow code
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # my code
        game_display.blit(Background, (0,0)) # draws the background image in the background before the other events happen, to ensure the background stays as the lowest element
        
        # stack overflow code
        for box in input_boxes:
            box.handle_event(event)

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)
                
    # pygame example code
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
