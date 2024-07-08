import pygame
import button

pygame.init()#needed to initialize font

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

addition = 0
subtraction = 0
multiplication = 0
division = 0
display_num = 0

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

calculator_button_2_img = pygame.image.load('calculator_assets/calculator_button_2.png').convert_alpha()
calculator_button_2 = button.Button(135,400,calculator_button_2_img,2)

calculator_button_3_img = pygame.image.load('calculator_assets/calculator_button_3.png').convert_alpha()
calculator_button_3 = button.Button(220,400,calculator_button_3_img,2)

calculator_button_4_img = pygame.image.load('calculator_assets/calculator_button_4.png').convert_alpha()
calculator_button_4 = button.Button(50,350,calculator_button_4_img,2)

calculator_button_5_img = pygame.image.load('calculator_assets/calculator_button_5.png').convert_alpha()
calculator_button_5 = button.Button(135,350,calculator_button_5_img,2)

calculator_button_6_img = pygame.image.load('calculator_assets/calculator_button_6.png').convert_alpha()
calculator_button_6 = button.Button(220,350,calculator_button_6_img,2)

calculator_button_7_img = pygame.image.load('calculator_assets/calculator_button_7.png').convert_alpha()
calculator_button_7 = button.Button(50,300,calculator_button_7_img,2)

calculator_button_8_img = pygame.image.load('calculator_assets/calculator_button_8.png').convert_alpha()
calculator_button_8 = button.Button(135,300,calculator_button_8_img,2)

calculator_button_9_img = pygame.image.load('calculator_assets/calculator_button_9.png').convert_alpha()
calculator_button_9 = button.Button(220,300,calculator_button_9_img,2)

calculator_button_0_img = pygame.image.load('calculator_assets/calculator_button_0.png').convert_alpha()
calculator_button_0 = button.Button(70,400,calculator_button_0_img,2)

while run:
    
    screen.fill((202, 228, 241))
    clock.tick(60)

    calculator_frame.draw(screen)
    calculator_button_1.draw(screen)
    calculator_button_2.draw(screen)
    calculator_button_3.draw(screen)
    calculator_button_4.draw(screen)
    calculator_button_5.draw(screen)
    calculator_button_6.draw(screen)
    calculator_button_7.draw(screen)
    calculator_button_8.draw(screen)
    calculator_button_9.draw(screen)
    for event in pygame.event.get():

        
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()