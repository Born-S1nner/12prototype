define e = Character("Eileen")
define m = Character("Me", color="#c8c8ff")
define n = Character("Nami", color="c8ffc8")

label start:

    scene bg room
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

    n "Ren'Py allows you to create your own space dimension and mold it to your will."

    jump act_one
    
label act_one:

    e "Right! Let's get started on your tutorial"

    hide nani happy
    hide eileen happy

    ".:. The End"
    return
