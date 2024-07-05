import pygame
import button

pygame.init()#needed to initialize font

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Pygame Calculator')

clock = pygame.time.Clock()
run = True

calculator_frame_img =  pygame.image.load('calculator_assets/calculator_frame.png').convert_alpha()
calculator_frame = button.Button(0,2,calculator_frame_img,7)


#might not use if text cant be placed on top
#try to draw text after it 
#display itself will need to be drawn after the calculator_frame
calculator_display = pygame.image.load('calculator_assets/calculator_display.png').convert_alpha()


calculator_button_1_img = pygame.image.load('calculator_assets/calculator_button_1.png').convert_alpha()
calculator_button_1 = button.Button(50,400,calculator_button_1_img,2)



while run:
    
    screen.fill((202, 228, 241))
    clock.tick(60)

    calculator_frame.draw(screen)
    calculator_button_1.draw(screen)
    for event in pygame.event.get():

        
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()