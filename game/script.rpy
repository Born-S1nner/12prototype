# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define m = Character("Me", color="#c8c8ff")


# The game starts here.

label start:

    scene bg room

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    hide eileen happy

    show stick furious
    
    m "Thanks for the heads up!"

    m "What do I do next?"

    hide stick furious

    show eileen happy

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
