import pygame
import button

pygame.init()#needed to initialize font

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

addition = False
subtraction = False
multiplication = False
division = False
second_num = 0

#pt 2 slides should be algorithm (continue button placement too)
#check if no operations are true:
# then allow input to first_num and set display num to first_num

#when operation is pressed:
#check if another operation is true then operation between first_num and secondnum will occur 
#(flags still active since no clear)
# -then clear previous flag and set new flag

# then
# -set first_num to display num
# -clear displaynum
# -have displaynum = secondnum
# -allow for input of second num 
# -operation later will be done on first_num and second_num

#when = button is pressed have operation done with first_num and displaynum (no flags cleared)
# -displaynum will be changed to first_num 
#c button will clear all flags as well as first_num, secondnum and displaynum
#have operations in seperate functions that are called when buttons are pressed
#clear and = are operations too but function differently from the others

#Handle divide by zero error?
#Limit number of numbers on the screen?

#decimals? use flag to set decimal mode
# convert first_num to float and add (input_num * (1/x)) tenth needs to change to hundredth/ thousandth?
# where x begins as 10 then is multiplied by ten as more parts of the decimal number are given

display_num = 0 #will not == first_num when addition/subtraction/etc(operation) is triggered
first_num = 0

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

#zero
calculator_button_0_img = pygame.image.load('calculator_assets/calculator_button_0.png').convert_alpha()
calculator_button_0 = button.Button(50,250,calculator_button_0_img,2)

#clear
calculator_button_16_img = pygame.image.load('calculator_assets/calculator_button_16.png').convert_alpha()
calculator_button_16 = button.Button(50,200,calculator_button_16_img,2)

#plus
calculator_button_10_img = pygame.image.load('calculator_assets/calculator_button_10.png').convert_alpha()
calculator_button_10 = button.Button(135,200,calculator_button_10_img,2)

#minus
calculator_button_11_img = pygame.image.load('calculator_assets/calculator_button_11.png').convert_alpha()
calculator_button_11 = button.Button(220,200,calculator_button_11_img,2)

#times
calculator_button_14_img = pygame.image.load('calculator_assets/calculator_button_14.png').convert_alpha()
calculator_button_14 = button.Button(135,250,calculator_button_14_img,2)

#division
calculator_button_13_img = pygame.image.load('calculator_assets/calculator_button_13.png').convert_alpha()
calculator_button_13 = button.Button(220,250,calculator_button_13_img,2)

#equals
calculator_button_12_img = pygame.image.load('calculator_assets/calculator_button_12.png').convert_alpha()
calculator_button_12 = button.Button(220,150,calculator_button_12_img,2)

text_font = pygame.font.SysFont(None, 70,bold = True, italic=True)
def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

def do_calculation(first_num, second_num,addition,subtraction,multiplication,division):
        answer = 0
        if addition:
           answer = first_num + second_num
        if subtraction:
            answer = first_num - second_num
        if multiplication:
            answer = first_num * second_num
        if division:
            answer = first_num / second_num
        return answer
        
while run:
    
    screen.fill((202, 228, 241))
    clock.tick(60)
    #do buttons as if statments then dictionary later
    calculator_frame.draw(screen)
    if calculator_button_1.draw(screen):
        print('1 pressed')
        if display_num == 0:
            display_num = 1
        else:
            display_num = display_num * 10 + 1
    if calculator_button_2.draw(screen):
        #can put these lines into its own function with number passed in
        print('2 pressed')
        if display_num == 0:
            display_num = 2
        else:
            display_num = display_num * 10 + 2
    if calculator_button_3.draw(screen):
        print('3 pressed')
        if display_num == 0:
            display_num = 3
        else:
            display_num = display_num * 10 + 3
    if calculator_button_4.draw(screen):
        print('4 pressed')
        if display_num == 0:
            display_num = 4
        else:
            display_num = display_num * 10 + 4
    if calculator_button_5.draw(screen):
        print('5 pressed')
        if display_num == 0:
            display_num = 5
        else:
            display_num = display_num * 10 + 5
    if calculator_button_6.draw(screen):
        print('6 pressed')
        if display_num == 0:
            display_num = 6
        else:
            display_num = display_num * 10 + 6
    if calculator_button_7.draw(screen):
        print('7 pressed')
        if display_num == 0:
            display_num = 7
        else:
            display_num = display_num * 10 + 7
    if calculator_button_8.draw(screen):
        print('8 pressed')
        if display_num == 0:
            display_num = 8
        else:
            display_num = display_num * 10 + 8

    if calculator_button_9.draw(screen):
        print('9 pressed')
        if display_num == 0:
            display_num = 9
        else:
            display_num = display_num * 10 + 9

    if calculator_button_0.draw(screen):
        print('0 pressed')
        if display_num == 0:
            display_num = 0
        else:
            display_num = display_num * 10 + 0

    if calculator_button_16.draw(screen):
        print('Clear pressed')
        display_num = 0
        addition = False
        subtraction = False
        multiplication = False
        division = False
        first_num = 0


    if calculator_button_10.draw(screen):
        print('Plus pressed')
        # if op_pressed:
        #  do_op
        addition = True
        subtraction = False
        multiplication = False
        division = False
        first_num = display_num
        second_num = 0
        display_num = 0

    calculator_button_11.draw(screen)
    calculator_button_14.draw(screen)
    calculator_button_13.draw(screen)
    if calculator_button_12.draw(screen):
        # if op_pressed:
        #  do_op # for each operation
        print('Equals pressed')

        if second_num == 0:
            second_num = display_num

        first_num = do_calculation(first_num, second_num, addition, subtraction, multiplication, division)
        display_num = first_num

    # calculator_button_16.draw(screen)
    # calculator_button_10.draw(screen)
    # calculator_button_11.draw(screen)
    # calculator_button_14.draw(screen)
    # calculator_button_13.draw(screen)
    # calculator_button_12.draw(screen)

    

    draw_text(str(display_num),text_font,(0,0,0),50,10)
    for event in pygame.event.get():

        
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()