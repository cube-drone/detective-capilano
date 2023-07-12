# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define ha = Character("Chief Dasse")
define ws = Character("Assistant Wayland Smunders")
define sc = Character("Capilano")
define j = Character("John")

# The game starts here.

label start:
    $ quick_menu = False

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show delmond basic at center
    "POLICE PRECINCT. We spend a second dwelling on a large, cement, brutalist building on a gray day."

    "A serious looking police chief is sitting at her desk. The desk itself is clean, organized, and utterly 
        devoid of modern technology. Instead, there sits a large bakelite touch-tone phone. Behind her are 
        framed awards and medals."
    
    "The woman sitting at the desk is wearing a crisp, pressed uniform with a lot of very official looking bits
        and bangles on it. Her hair is arranged in a severe bun, chestnut brown but with a significant decampment
        of encroaching grey hairs."
    
    "A thin, hawkish man in a blue shirt walks in, a worried look on his face."

    ws "Chief Dasse - Chief Dasse!"
    
    ha "What is it?"

    ws "We have a, uh, routine traffic fatality, but the officer on the scene has requested that we send a detective."

    ha "Something suspicious about the circumstances, hm?"

    ws "Yes - but it's a highway accident, so the city will be breathing down our neck if we can't clear the scene quickly."

    ha "So we need a detective right {i}now{/i}, then?"

    ha "How about..."

    jump how_about

define goode_and_dunn = True
define briggs_and_stratton = True
define smith_and_wesson = True
define abbott_and_costello = True
define hall_and_oates = True
define astaire_and_rogers = True
define bert_and_ernie = True
define dorian_and_turk = True
define ferrell_and_oteri = True
define hamm_and_deggs = True

label how_about:

    menu: 
        "Goode and Dunn?" if goode_and_dunn:
            ws "They're on vacation leave right now."
            $ goode_and_dunn = False
            jump how_about
        
        "Briggs and Stratton?" if briggs_and_stratton:
            ws "I already checked with them, they've got engine trouble."
            $ briggs_and_stratton = False
            jump how_about
        
        "Smith and Wesson?" if smith_and_wesson:
            ws "I can't get a hold of them, they've been at the shooting range all day."
            $ smith_and_wesson = False
            jump how_about
        
        "Abbott and Costello?" if abbott_and_costello:
            ws "On administrative leave after they got in that big scrap at the baseball field."
            ha "Big scrap at the {i}baseball field?{/i}"
            ws "One of them got Lieutenant Hu's name wrong, again."
            ha "Hu?"
            ws "Exactly, sir."
            $ abbott_and_costello = False
            jump how_about
        
        "Hall and Oates?" if hall_and_oates:
            ws "They left the force, sir, to become private eyes."
            ha "That's unfortunate. Watch out, boys - that life'll chew you up."
            $ hall_and_oates = False
            jump how_about
        
        "Astaire and Rogers?" if astaire_and_rogers:
            ws "They're tapped out, sir."
            ha "Damn."
            $ astaire_and_rogers = False
            jump how_about
        
        "Bert and Ernie?" if bert_and_ernie:
            ws "They're getting married this week, sir."
            ha "Oh. Wonderful. Have you remembered to send them flowers and a card, from the precinct?"
            ws "Of course, sir."
            $ bert_and_ernie = False
            jump how_about

        "Dorian and Turk?" if dorian_and_turk:
            ws "You don't want to put those scrubs on a real case."
            $ dorian_and_turk = False
            jump how_about

        "Ferrell and O'Teri?" if ferrell_and_oteri:
            ws "No."
            ha "... Wise."
            $ ferrell_and_oteri = False
            jump how_about
        
        "Hamm and Deggs?" if hamm_and_deggs:
            ws "They're a good pair - I'm sure they'd be able to turn this over, easy."
            ha "Yeah. Why are you waffling, then? Let's use them!"
            ws "But they're busy with a case right now, for that baseball team - the Holland A's."
            ws "We've also got them on the Ashley Brown murder."
            ha "Okay, gotcha, Hamm and Deggs are too busy with Holland A's and Ash Brown."
            ws "Exactly, sir."
            $ hamm_and_deggs = False
            jump how_about
        
        "Capilano?":
            ws "Capilano? Really? Is she... the {i}best{/i} choice for this?"
            ha "It sounds like she's our {b}only{/b} choice for this."
            ws "Well, I suppose that's true. I'll get her on the phone."
            ha "On the phone? Is she not in today?"
            ws "She should be, but she's late. {i}Again{/i}."
            ha "How often would you say that she's late to work, Smunders?"
            ws "I wouldn't say that I can recall her being on time for work, ever, sir."
            ha "Hm. Noted."
            jump start_home
            

label start_home:
    scene bg room

    "We cut to the interior of an extremely messy apartment. The television, again, helps to establish
        the time frame by being a behemoth of wood and chrome with a tiny screen."
    
    "A woman is sleeping,
        face-down, fully clothed, on the ugliest chesterfield you have ever seen. In front of her is a
        coffee table with an overstuffed ashtray."

    "The phone is ringing."

    sc "Guh."

    "You should pick up the phone, it's ringing."

    sc "Nghuh."

    "Look, if you don't pick up the phone, we can't get this story started. Up! UP!"

    sc "Okay, okay, jesus. Fuck."

    "The woman uncomfortably peels herself off of the couch. She has short hair, a slim build, and a leather
        jacket that probably smells like a grown-ass adult just slept in it."

    sc "Where are the - uh - you know, the images? I can't see shit."

    "I'm not going to get any art ready until the whole script is done. Art is a lot more expensive to make than
        text, you know. Don't worry, there will be art before too long."

    sc "Okay, well, how am I supposed to answer the phone if I can't see it?"

    "I can help."

    sc "How's that?"

    "She picks up the phone."

    sc "Hello?"

    ws "You're late for work, Ms. Capilano."

    sc "{i}groggily{/i} who is this? Smunders?"

    ws "Yes, it's me."