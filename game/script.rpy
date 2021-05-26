define e = Character("Eileen")
define m = Character("Me", color="#c8c8ff")
define n = Character("Nami", color="c8ffc8")

define pushleft = PushMove()
define pushright = PushMove()

label start:

    scene bg one
    with fade

    m "Where am I..."
    m "Who am I..."
    m "Why am I here?"

    show stick furious
    with fade

    m "Anyone there?"
    e "Hello stranger!"
    m "WAAAHH!!!!"

    show eileen happy at left
    e "Welcome to Ren'Py server!"

label choices:
    default learned = False
    e "Is there anything you want to know?"

menu:
    "Who are you?":
        jump who

    "What is Ren'Py?":
        jump what

label who:
    hide stick furious
    show nani happy at right

    n "It doesn't matter, we are not part of your reality to begin with."

    jump act_one

label what:
    hide stick furious
    show nani happy at right
    $ learned = True

    n "Ren'Py allows you to create your own space dimension and mold it to your will."

    jump act_one
    
label act_one:
    if learned:
        e "Right! Let's get started on your tutorial"

        hide nani happy
        hide eileen happy

        ".:. Cool End"
    else:
        e "You have a lot to learn, lets get down to business!"

        hide nani happy
        hide eileen happy

        ".:. Weeb End"
    return
