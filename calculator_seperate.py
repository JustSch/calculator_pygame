import pygame
import button
from load_buttons import LoadButtons

pygame.init()#needed to initialize font

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

addition = False
subtraction = False
multiplication = False
division = False
equals =  False #keep track of if calculation was performed yet or not
                #needed incase equal sign is pressed before next calculation

first_num = 0
second_num = 0

display_num = 0

#pt 2 slides should be algorithm (continue button placement too)

#check if no operations are true (firstnum will be empty):
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

#when = button is pressed have operation done with first_num and secondnum (no flags cleared)
# -displaynum will be changed to first_num 
#c button will clear all flags as well as first_num, secondnum and displaynum
#have operations in seperate functions that are called when buttons are pressed
#clear and = are operations too but function differently from the others

#Handle divide by zero error?
#Limit number of numbers on the screen?

#decimals? use flag to set decimal mode
# convert first_num to float and add (input_num * (1/x)) tenth needs to change to hundredth/ thousandth?
# where x begins as 10 then is multiplied by ten as more parts of the decimal number are given


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Pygame Calculator')

clock = pygame.time.Clock()
run = True

calculator_buttons = LoadButtons(pygame)

text_font = pygame.font.SysFont(None, 70,bold = True, italic=True)
def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

def do_calculation(first_num, second_num,addition,subtraction,multiplication,division):       
        if addition:
           first_num = first_num + second_num
        if subtraction:
            first_num = first_num - second_num
        if multiplication:
            first_num = first_num * second_num
        if division:
            #handle division by zero error here
            first_num = first_num / second_num
        print('result is ' + str(first_num))
        return first_num
        
while run:
    
    screen.fill((202, 228, 241))
    clock.tick(60)
    #do buttons as if statments then dictionary later
    calculator_buttons.calculator_frame.draw(screen)
    if calculator_buttons.calculator_button_1.draw(screen):
        print('1 pressed')
        display_num = display_num * 10 + 1
    if calculator_buttons.calculator_button_2.draw(screen):
        #can put these lines into its own function with number passed in
        print('2 pressed')
        display_num = display_num * 10 + 2
    if calculator_buttons.calculator_button_3.draw(screen):
        print('3 pressed')
        display_num = display_num * 10 + 3
    if calculator_buttons.calculator_button_4.draw(screen):
        print('4 pressed')
        display_num = display_num * 10 + 4
    if calculator_buttons.calculator_button_5.draw(screen):
        print('5 pressed')
        display_num = display_num * 10 + 5
    if calculator_buttons.calculator_button_6.draw(screen):
        print('6 pressed')
        display_num = display_num * 10 + 6
    if calculator_buttons.calculator_button_7.draw(screen):
        print('7 pressed')
        display_num = display_num * 10 + 7
    if calculator_buttons.calculator_button_8.draw(screen):
        print('8 pressed')
        display_num = display_num * 10 + 8
    if calculator_buttons.calculator_button_9.draw(screen):
        print('9 pressed')
        display_num = display_num * 10 + 9


    if calculator_buttons.calculator_button_0.draw(screen):
        print('0 pressed')
        display_num = display_num * 10 + 0

    if calculator_buttons.calculator_button_16.draw(screen):
        print('Clear pressed')
        display_num = 0
        addition = False
        subtraction = False
        multiplication = False
        division = False
        equals = False
        first_num = 0
        second_num = 0


    if calculator_buttons.calculator_button_10.draw(screen):
        print('Plus pressed')
        if not equals:
            if first_num == 0:
                first_num = display_num
            elif second_num == 0:
                second_num = display_num
                display_num = do_calculation(first_num, second_num, addition, subtraction, multiplication, division)
        else:
            equals = False
        addition = True
        subtraction = False
        multiplication = False
        division = False
        first_num = display_num
        second_num = 0
        display_num = 0

    if calculator_buttons.calculator_button_11.draw(screen):
        print('Minus pressed')
        if not equals:
            if first_num == 0:
                first_num = display_num
            elif second_num == 0:
                second_num = display_num
                display_num = do_calculation(first_num, second_num, addition, subtraction, multiplication, division)
        else:
            equals = False
        addition = False
        subtraction = True
        multiplication = False
        division = False
        first_num = display_num
        second_num = 0
        display_num = 0
    if calculator_buttons.calculator_button_14.draw(screen):
        print('Times pressed')
        if not equals:
            if first_num == 0:
                first_num = display_num
            elif second_num == 0:
                second_num = display_num
                display_num = do_calculation(first_num, second_num, addition, subtraction, multiplication, division)
        else:
            equals = False
        addition = False
        subtraction = False
        multiplication = True
        division = False
        first_num = display_num
        second_num = 0
        display_num = 0

    if calculator_buttons.calculator_button_13.draw(screen):
        print('Divide pressed')
        if not equals:
            if first_num == 0:
                first_num = display_num
            elif second_num == 0:
                second_num = display_num
                display_num = do_calculation(first_num, second_num, addition, subtraction, multiplication, division)
        else:
            equals = False
        addition = False
        subtraction = False
        multiplication = False
        division = True
        first_num = display_num
        second_num = 0
        display_num = 0
    if calculator_buttons.calculator_button_12.draw(screen):     
        print('Equals pressed')
        if second_num == 0:
            second_num = display_num

        first_num = do_calculation(first_num, second_num, addition, subtraction, multiplication, division)
        display_num = first_num
        equals = True

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