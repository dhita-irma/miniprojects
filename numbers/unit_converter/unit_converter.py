# Unit Converter (temp, currency, volume, mass and more) - Converts various units between one another.
# The user enters the type of unit being entered, the type of unit they want to convert to and then the value.
# The program will then make the conversion.


weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ").upper()


def weight_converter():
    if unit == 'K':
        result = weight * 2.2
        print(f"{str(weight)} kg equals to {result} lbs. ")
    else:
        result = weight * 0.45
        print(f"{str(weight)} lbs equals to {result} kg. ")


weight_converter()