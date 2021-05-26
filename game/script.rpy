define e = Character("Eileen")
define m = Character("Me", color="#c8c8ff")
define n = Character("Nami", color="c8ffc8")

define pushleft = PushMove()
define pushright = PushMove()

default learned = False
default determined = False

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
    else:
        e "You have a lot to learn, lets get down to business!"

    hide nani happy and eileen happy

    hide bg one
    with dissolve

label act_two:
    scene bg two

    show eileen happy
    e "Over here, you got another realm like the previous one... "
    e "You can conquer as many realms as you're capable of."
    
    hide eileen happy
    show stick furious
    
    m "How are you able to even create somethin gout of nothing in the first place?"
    
    hide stick furious
    show nani happy
    
    n "Just simple think of a place in your head and pretend that you are there."
    
    show eileen happy at left

    e "You should try it out right!"
    e "Let's give you some space and see if you can pull it out."

menu:
    "(attempt to make a realm)":
        jump failed

    "(think off a place)":
        jump success

label failed:
    hide bg two
    with dissolve
    scene empty

    show eileen happy
    
    e "Great... Good to know that you are not determined."
    
    show nani happy at right
    n "Don't be like that!"
    n "He is just not confident with his new power."

    hide bg empty
    jump act_three

label success:
    hide bg two
    with dissolve
    scene bg three
    $ determined = True

    show eileen happy
    
    e "Holy moly! He actually pulled it off at the first shot!"
    
    show nani happy at right
    n "You should have faith in him from the start."
    n "With this power, you must be responsible for your creations and actions."
    
    hide bg three

    jump act_three

    
label act_three:
    scene bg two
    if learned and determined:
        n "You are worthy to do good things for the multivers."
        n "Don't let anything stop you from doing the right choices in life."
    
    elif learned and !determined:
        e "You have the brains but not the courage!"
        n "You should believe in yourself more."
        n "Good thing will happen if you set your mind on something."

    elif !learned and determined:
        e "You got guts, yet you don't use your brain to think."
        n "What she is trying to say is you must be careful on what you wish for."
        n "Bad things will happen if you're closed minded from the reality."
    
    else:
        e "Boy you must not like yourself."
        e "I'm starting to think that you are not worthy of this power."

    hide nani happy and eileen happy
    show stick furious

    m "Can we take a break for a moment?"

    hide stick furious
    show nani happy

    n "I guess we should..."

    hide nani happy

    ".:. The End"
return
