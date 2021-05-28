define e = Character("Eileen", image="eileen")
define m = Character("Me", color="#c8c8ff")
define n = Character("Nami", color="c8ffc8", image="nani")
define h = Character("Hatsune", color="00cc99")

image define eileen happy = "eileen happy.png"
image define nani happy = "nani happy.png"

image define side eileen hap = "side eileen hap.png"
image define nani eileen hap = "side nani hap.png"

default learned = False
default determined = False
default respect = 0

label start:

    m "Where am I..."
    m "Who am I..."
    m "Why am I here?"


    scene bg one
    with dissolve
    show stick furious
    with dissolve

    m "Anyone there?"

    show eileen happy at left
    with moveinleft
    e "Hello stranger!"
    m "WAAAHH!!!!" with hpunch

    e "Welcome to Ren'Py server!"
    e "Is there anything you want to know?"

menu:
    "Who are you?":
        jump who

    "What is Ren'Py?":
        jump what

label who:
    hide stick furious
    show nani happy at right
    with moveinright

    n "It doesn't matter, we are not part of your reality to begin with."

    jump act_one

label what:
    hide stick furious
    show nani happy at right
    with moveinright
    $ learned = True
    $ respect += 1

    n "Ren'Py allows you to create your own space dimension and mold it to your will."

    jump act_one
    
label act_one:
    if learned:
        e "Right! Let's get started on your tutorial"
    else:
        e "You have a lot to learn, lets get down to business!"

    n "Let's head to another realm."

    hide nani happy
    hide eileen happy
    with dissolve

label act_two:
    scene bg two
    with dissolve
    
    show eileen happy
    with moveinleft
    
    e "Over here, you got another realm like the previous one... "
    e "You can conquer as many realms as you're capable of."
    
    hide eileen happy
    show stick furious
    
    m "How are you able to even create something out of nothing in the first place?"
    
    hide stick furious
    show nani happy
    
    n "Just simple think of a place in your head and pretend that you are there."
    
    show eileen happy at left

    e "You should try it out right!"
    e "Let's give you some space and see if you can pull it out."

    hide eileen happy
    with moveoutleft

    n "You got this."

    hide nani happy
    with moveoutright

menu:
    "(attempt to make a realm)":
        jump failed

    "(think off a place)":
        jump success

label failed:
    scene empty
    with fade

    show eileen happy
    
    e "Great... Good to know that you are not determined."
    
    show nani happy at right
    n "Don't be like that!"
    n "He is just not confident with his new power."

    jump act_three

label success:
    scene bg three
    with fade
    $ respect += 1
    $ determined = True

    show eileen happy
    with moveinleft

    e "Holy moly! He actually pulled it off at the first shot!"
    
    show nani happy at right
    with moveinright
    n "You should have faith in him from the start."
    n "With this power, you must be responsible for your creations and actions."
    
    jump act_three
 
label act_three:
    scene bg two
    with pixellate
    
    show eileen happy at left
    show nani happy at right
    
    if learned and determined:
        n "You are worthy to do good things for the multivers."
        n "Don't let anything stop you from doing the right choices in life."
    
    elif learned and not determined:
        e "You have the brains but not the courage!"
        n "You should believe in yourself more."
        n "Good thing will happen if you set your mind on something."

    elif not learned and determined:
        e "You got guts, yet you don't use your brain to think."
        n "What she is trying to say is you must be careful on what you wish for."
        n "Bad things will happen if you're closed minded from the reality."
    
    else:
        e "Boy you must not like yourself."
        e "I'm starting to think that you are not worthy of this power."

    hide nani happy
    hide eileen happy
    show stick furious

    m "Can we take a break for a moment?"

    hide stick furious
    show nani happy

    n "I guess we should..."

    hide nani happy

label act_four:
    scene bg four
    with dissolve

    e hap "Over here is the Realm Station."
    e "You can travel at larger distance by using the train."
    n hap "In case you want some reference from the previous creators, you can use this station to explore them."    
    n "All you have to do is ask Hatsune the direction and she will guide you."
    n "Isn't that right, Hatsune?"
    h "It's true, but don't disturb me during my break hours."

menu:
    "Who exactly is she?":
        jump rude
    "What does she do in here?":
        jump curious

label rude:
    h "Rude! I am the Hatsune of Pathfinder!" with hpunch
    h "You better respect me or else I will send you to the abyss!"
    jump act_five

label curious:
    h "Well you simpleton, I am in charge of ensuring the pathway from life and death." with hpunch
    if learned:
        h "I expected much from you, smart boy."
        h "I guess I shouldn't have mush expectation from you"
    else:
        h "Of course, You wouldn't understand about my job for you, small brain."
    jump act_five

label act_five:
    n hap "Now now, it's rude to treat the newcomer like that."
    e hap "Then again, she is always a wild card."
    n "let's just move on to the next point."
    e "Bye Hatsune!"
    h "..."

menu:
    "Apologize to Hatsune":
        jump apology
    "Leave the room":
        jump act_six

label apology:
    respect += 1
    m "Sorry about the respond."
    h "Don't be!"with hpunch
    h "..."
    h "Just get out of here."
    h "..."

label act_six:

return
