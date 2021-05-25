define e = Character("Eileen")
define m = Character("Me", color="#c8c8ff")
define n = Character("Nami", color="c8ffc8")

label start:

    scene bg room
    with fade

    show eileen happy

    e "You've created a new Ren'Py game."

    hide eileen happy

    show stick furious
    
    m "Thanks for the heads up!"

    m "What do I do next?"

    hide stick furious

    show eileen happy

    e "Once you add a story, pictures, and music, you can release it to the world!"

    show nani happy at right
    with fade

    n "How can we do that?"

    hide nani happy

    e "Just simply follow our documentation on our official website."

    hide bg room
    with dissolve

    return
