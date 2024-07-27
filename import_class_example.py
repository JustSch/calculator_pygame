from class_example import ClassExample #needs when name of class
                                       #doesn't match filename
                                       #or if multiple classes
                                       #in file
a = ClassExample(3) # creates an object we can get things from later

print(a.passed_in_variable)
print(a.not_passed_in_variable)

a.function_that_does_nothing()