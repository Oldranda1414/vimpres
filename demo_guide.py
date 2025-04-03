# pylint: skip-file

# run this command: screenkey -s large --window

# Print the link of the slides

print("Hello world")

# make link a variable

message = "Hello world"

print(message)

# fix linting errors

"""this is a demo
"""

MESSAGE = "Hello world"

print(MESSAGE)

# add a loop

for i, c in enumerate(MESSAGE):
    print("character " + c + " is at index " + i + ".")

# add a function

def my_print(index, character):
    """this is a summary

    Args:
        index (int): some description
        character (char): some other description
    """
    print("character " + character + " is at index " + index + ".")

for i, c in enumerate(MESSAGE):
    my_print(i, c)
