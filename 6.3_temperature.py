def convert_cel_to_far(cel_degrees):
    """return conversion of degrees Celsius to degrees Fahrenheit by multiplying given degrees Celsius as a parameter (float number)"""
    cel_degrees = float(input(f"Please give current temperature in degrees Celsius: "))
    fahrenheit_degrees = (cel_degrees * 9/5 + 32)
    return f"{cel_degrees:.2f} degress C = {fahrenheit_degrees:.2f} degrees F"

print(convert_cel_to_far(float)) # mogę tu wpisać dowolną liczbę, a nawet int lub float, ale i tak bierze to co z inputu w ciele funkcji
##print(help(convert_cel_to_far))
##print(convert_cel_to_far(27))



def convert_far_to_cel(far_degrees):
    """return conversion of degrees Fahrenheit to degrees Celsius by using an expresion with given degrees Fahrenheit as parameter (float number)"""
    far_degrees = float(input(f"Please give current temperaure in degrees Fahrenheit: "))
    cel_degrees = (far_degrees - 32) * 5/9
    return f"{far_degrees:.2f} degrees F = {cel_degrees:.2f} degrees C"

##print(help(convert_far_to_cel))
print(convert_far_to_cel(float)) # mogę tu wpisać dowolną liczbę, a nawet int lub float, ale i tak bierze to co z inputu w ciele funkcji

print(help(convert_cel_to_far))
print(help(convert_far_to_cel))
