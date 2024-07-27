
import button
class LoadButtons():
    def __init__(self,pygame):
        calculator_frame_img =  pygame.image.load('calculator_assets/calculator_frame.png').convert_alpha()
        self.calculator_frame = button.Button(0,2,calculator_frame_img,7)


        #might not use if text cant be placed on top
        #try to draw text after it 
        #display itself will need to be drawn after the calculator_frame
        self.calculator_display = pygame.image.load('calculator_assets/calculator_display.png').convert_alpha()


        calculator_button_1_img = pygame.image.load('calculator_assets/calculator_button_1.png').convert_alpha()
        self.calculator_button_1 = button.Button(50,400,calculator_button_1_img,2)

        calculator_button_2_img = pygame.image.load('calculator_assets/calculator_button_2.png').convert_alpha()
        self.calculator_button_2 = button.Button(135,400,calculator_button_2_img,2)

        calculator_button_3_img = pygame.image.load('calculator_assets/calculator_button_3.png').convert_alpha()
        self.calculator_button_3 = button.Button(220,400,calculator_button_3_img,2)

        calculator_button_4_img = pygame.image.load('calculator_assets/calculator_button_4.png').convert_alpha()
        self.calculator_button_4 = button.Button(50,350,calculator_button_4_img,2)

        calculator_button_5_img = pygame.image.load('calculator_assets/calculator_button_5.png').convert_alpha()
        self.calculator_button_5 = button.Button(135,350,calculator_button_5_img,2)

        calculator_button_6_img = pygame.image.load('calculator_assets/calculator_button_6.png').convert_alpha()
        self.calculator_button_6 = button.Button(220,350,calculator_button_6_img,2)

        calculator_button_7_img = pygame.image.load('calculator_assets/calculator_button_7.png').convert_alpha()
        self.calculator_button_7 = button.Button(50,300,calculator_button_7_img,2)

        calculator_button_8_img = pygame.image.load('calculator_assets/calculator_button_8.png').convert_alpha()
        self.calculator_button_8 = button.Button(135,300,calculator_button_8_img,2)

        calculator_button_9_img = pygame.image.load('calculator_assets/calculator_button_9.png').convert_alpha()
        self.calculator_button_9 = button.Button(220,300,calculator_button_9_img,2)

        #zero
        calculator_button_0_img = pygame.image.load('calculator_assets/calculator_button_0.png').convert_alpha()
        self.calculator_button_0 = button.Button(50,250,calculator_button_0_img,2)

        #clear
        calculator_button_16_img = pygame.image.load('calculator_assets/calculator_button_16.png').convert_alpha()
        self.calculator_button_16 = button.Button(50,200,calculator_button_16_img,2)

        #plus
        calculator_button_10_img = pygame.image.load('calculator_assets/calculator_button_10.png').convert_alpha()
        self.calculator_button_10 = button.Button(135,200,calculator_button_10_img,2)

        #minus
        calculator_button_11_img = pygame.image.load('calculator_assets/calculator_button_11.png').convert_alpha()
        self.calculator_button_11 = button.Button(220,200,calculator_button_11_img,2)

        #times
        calculator_button_14_img = pygame.image.load('calculator_assets/calculator_button_14.png').convert_alpha()
        self.calculator_button_14 = button.Button(135,250,calculator_button_14_img,2)

        #division
        calculator_button_13_img = pygame.image.load('calculator_assets/calculator_button_13.png').convert_alpha()
        self.calculator_button_13 = button.Button(220,250,calculator_button_13_img,2)

        #equals
        calculator_button_12_img = pygame.image.load('calculator_assets/calculator_button_12.png').convert_alpha()
        self.calculator_button_12 = button.Button(220,150,calculator_button_12_img,2)