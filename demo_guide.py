# run this command: screenkey -s large --window

# Print the link of the slides

print("https://oldranda1414.github.io/vimpres/")

# make link a variable

link = "https://oldranda1414.github.io/vimpres/"

print(link)

# fix linting errors

"""this is a demo
"""

LINK = "https://oldranda1414.github.io/vimpres/"

print(LINK)

# add a loop

for i, c in enumerate(LINK):
    print("character " + c + " is at index " + i + ".")

# add a function

def my_print(index, character):
    """this is a summary

    Args:
        index (int): some description
        character (char): some other description
    """
    print("character " + character + " is at index " + index + ".")

for i, c in enumerate(LINK):
    my_print(i, c)
