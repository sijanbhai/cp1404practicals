"""
Allows the user to look up hexadecimal color codes for common color names.
"""

COLOR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "BlueViolet": "#8a2be2"
}

color_name = input("Enter color name: ").strip().capitalize()  # Make input case-insensitive
while color_name != "":
    try:
        print(f"{color_name} is {COLOR_TO_HEX[color_name]}")
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter color name: ").strip().capitalize()  # Prompt for next color name
