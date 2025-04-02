# run this command: screenkey -s large --window

# Print the link of the slides

print("Hello world")

# make link a variable

message = "Hello world"

print(message)

# fix linting errors

"""this is a demo
"""

LINK = "Hello world"

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
