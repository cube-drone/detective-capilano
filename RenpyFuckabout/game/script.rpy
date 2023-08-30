# TODO: Detective Capilano is red green colorblind
# TODO: crimefighting bazooka
# TODO: more jokes in the becky phase, it drags a bit

# TODO: set up a brick joke in the apartment at the beginning, pay it off at the end

init python: 
    import random

    renpy.music.register_channel(name="ambient", mixer="music", loop=True)
    renpy.music.register_channel(name="ambient_2", mixer="music", loop=False)

    renpy.music.register_channel(name="hero_vox", mixer="voice")
    renpy.music.register_channel(name="narr_vox", mixer="voice")
    renpy.music.register_channel(name="other_vox", mixer="voice")
    renpy.music.set_pan(pan=-1, channel="hero_vox", delay=0)
    renpy.music.set_pan(pan=1, channel="other_vox", delay=0)

    voice_base_volume = 0.6

    def capilano_voice(event, interact=True, **kwargs):
        if not interact:
            return
        
        if event == "show_done":
            a = str(random.randint(0,15)).zfill(2)
            vol = voice_base_volume + (random.random()*0.1)
            renpy.sound.play(f'sounds/saxjingles/jingles_SAX{a}.ogg', relative_volume=vol, channel="hero_vox")
        elif event == "slow_done":
            renpy.sound.stop(fadeout=0.1, channel="hero_vox")

    def hit_voice(event, interact=True, **kwargs):
        if not interact:
            return
        
        if event == "show_done":
            a = str(random.randint(0,14)).zfill(2)
            vol = voice_base_volume
            renpy.sound.play(f'sounds/hitjingles/jingles_HIT{a}.ogg', channel="other_vox", relative_volume=vol)
        elif event == "slow_done":
            renpy.sound.stop(fadeout=0.1, channel="other_vox")

    def pizz_voice(event, interact=True, **kwargs):
        if not interact:
            return
        
        if event == "show_done":
            a = str(random.randint(0,15)).zfill(2)
            vol = voice_base_volume + (random.random()*0.1)
            renpy.sound.play(f'sounds/pizzjingles/jingles_PIZZI{a}.ogg', channel="other_vox", relative_volume=vol)
        elif event == "slow_done":
            renpy.sound.stop(fadeout=0.1, channel="other_vox")
    
    def steel_voice(event, interact=True, **kwargs):
        if not interact:
            return
        
        if event == "show_done":
            a = str(random.randint(0,15)).zfill(2)
            vol = voice_base_volume + (random.random()*0.1)
            renpy.sound.play(f'sounds/steeljingles/jingles_STEEL{a}.ogg', channel="other_vox", relative_volume=vol)
        elif event == "slow_done":
            renpy.sound.stop(fadeout=0.1, channel="other_vox")
    
    def bit_voice(event, interact=True, **kwargs):
        if not interact:
            return
        
        if event == "show_done":
            a = str(random.randint(0,15)).zfill(2)
            vol = voice_base_volume - 0.1
            renpy.sound.play(f'sounds/bitjingles/jingles_NES{a}.ogg', channel="narr_vox", relative_volume=vol)
        elif event == "slow_done":
            renpy.sound.stop(fadeout=0.1, channel="narr_vox")
    
    def phone_voice(event, interact=True, **kwargs):
        if not interact:
            return
        
        if event == "show_done":
            vol = voice_base_volume
            renpy.sound.play(f'sounds/phone.ogg', channel="other_vox", relative_volume=vol)
        elif event == "slow_done":
            renpy.sound.stop(fadeout=0.1, channel="other_vox")

    def bike_voice(event, interact=True, **kwargs):
        if not interact:
            return
        
        if event == "show_done":
            vol = voice_base_volume
            renpy.sound.play(f'sounds/bike.ogg', channel="other_vox", relative_volume=vol)
        elif event == "slow_done":
            renpy.sound.stop(fadeout=0.1, channel="other_vox")
    
    def badge_voice(event, interact=True, **kwargs):
        if not interact:
            return
        
        if event == "show_done":
            vol = voice_base_volume
            renpy.sound.play(f'sounds/ding.ogg', channel="other_vox", relative_volume=vol)
        elif event == "slow_done":
            renpy.sound.stop(fadeout=0.1, channel="other_vox")
    
    def condoms_voice(event, interact=True, **kwargs):
        if not interact:
            return
        
        if event == "show_done":
            vol = voice_base_volume
            renpy.sound.play(f'sounds/yeah.ogg', channel="other_vox", relative_volume=vol)
        elif event == "slow_done":
            renpy.sound.stop(fadeout=0.1, channel="other_vox")
    
    def gum_voice(event, interact=True, **kwargs):
        if not interact:
            return
        
        if event == "show_done":
            vol = voice_base_volume
            renpy.sound.play(f'sounds/pop.ogg', channel="other_vox", relative_volume=vol)
        elif event == "slow_done":
            renpy.sound.stop(fadeout=0.1, channel="other_vox")
    
    def belt_voice(event, interact=True, **kwargs):
        if not interact:
            return
        
        if event == "show_done":
            vol = voice_base_volume
            renpy.sound.play(f'sounds/belt.ogg', channel="other_vox", relative_volume=vol)
        elif event == "slow_done":
            renpy.sound.stop(fadeout=0.1, channel="other_vox")
    
    def keys_voice(event, interact=True, **kwargs):
        if not interact:
            return
        
        if event == "show_done":
            vol = voice_base_volume
            renpy.sound.play(f'sounds/keys.ogg', channel="other_vox", relative_volume=vol)
        elif event == "slow_done":
            renpy.sound.stop(fadeout=0.1, channel="other_vox")
    
    def notepad_voice(event, interact=True, **kwargs):
        if not interact:
            return
        
        if event == "show_done":
            vol = voice_base_volume
            renpy.sound.play(f'sounds/writing.ogg', channel="other_vox", relative_volume=vol)
        elif event == "slow_done":
            renpy.sound.stop(fadeout=0.1, channel="other_vox")
    
    def clock_voice(event, interact=True, **kwargs):
        if not interact:
            return
        
        if event == "show_done":
            vol = voice_base_volume
            renpy.sound.play(f'sounds/clock.ogg', channel="other_vox", relative_volume=vol)
        elif event == "slow_done":
            renpy.sound.stop(fadeout=0.1, channel="other_vox")
    
    def snake_voice(event, interact=True, **kwargs):
        if not interact:
            return
        
        if event == "show_done":
            vol = voice_base_volume
            renpy.sound.play(f'sounds/hiss.ogg', channel="other_vox", relative_volume=vol)
        elif event == "slow_done":
            renpy.sound.stop(fadeout=0.1, channel="other_vox")

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character(None, 
    what_font="fonts/LibreBaskerville-Regular.ttf",
    who_font="fonts/LibreBaskerville-Bold.ttf",
    what_color=color("#ffdcdd"),
    who_color=color("#ffdcdd"),
    callback=bit_voice,
)

define sc = Character("Detective Capilano",
    what_color=color("#f3ff00"), #audient, the observant
    who_color=color("#f3ff00"),    
    what_font="fonts/RobotoSlab-Medium.ttf",
    who_font="fonts/RobotoSlab-Bold.ttf",
    callback=capilano_voice
)
define sc_fast = Character("Detective Capilano",
    what_color=color("#f3ff00"), #audient, the observant
    who_color=color("#f3ff00"),    
    what_font="fonts/RobotoSlab-Medium.ttf",
    who_font="fonts/RobotoSlab-Bold.ttf",
    callback=capilano_voice,
    what_slow_cps=90
)
define hm = Character("Hank Maxhank",
    what_font="fonts/LibreBaskerville-Regular.ttf",
    who_font="fonts/LibreBaskerville-Bold.ttf",
    what_color=color("#ff0209"), # world, the opposition
    who_color=color("#ff0209"),    
    image="hank",
    callback=hit_voice
)
define annp = Character("Ann Portent",
    what_font="fonts/Marcellus-Regular.ttf", 
    who_font="fonts/Marcellus-Regular.ttf",
    what_color=color("#72a9ff"), # misk
    who_color=color("#72a9ff"),
    callback=hit_voice,
    what_slow_cps=40
)
define pat = Character("Pat \"Red\" Haring", 
    what_font="fonts/Anton-Regular.ttf", 
    who_font="fonts/Anton-Regular.ttf",
    what_color=color("#82ff00"), # kiro, himbo energy
    who_color=color("#82ff00"),
    callback=steel_voice
)
define ha = Character("The Chief",
    what_font="fonts/Literata-Regular.ttf",
    who_font="fonts/Literata-Bold.ttf",
    what_color=color("#01fe0b"), # cystam, The Man
    who_color=color("#01fe0b"),
    callback=hit_voice,
    what_size=45,
    who_size=55,
)
define becky = Character("Becky Segsihan",
    what_font="fonts/Delius-Regular.ttf",
    who_font="fonts/Delius-Regular.ttf",
    what_color=color("#ff007e"), # path, freedom and han solo
    who_color=color("#ff007e"),
    callback=steel_voice
)
define ws = Character("Assistant Wayland Smunders",
    what_font="fonts/Rajdhani-Regular.ttf",
    who_font="fonts/Rajdhani-Bold.ttf",
    what_color=color("#786dff"), # stacks, the know-it-all
    who_color=color("#786dff"),
    callback=pizz_voice,
    what_slow_cps=40,
    what_size=45,
    who_size=55,
)
define parm = Character("Paramedic",
    what_font="fonts/Jost-Regular.ttf",
    who_font="fonts/Jost-Bold.ttf",
    what_color=color("#b769ff"), # blit, The Downer
    who_color=color("#b769ff"),
    callback=pizz_voice
)
define trfc = Character("Jr. Officer Jemby Nichols",
    what_font="fonts/VarelaRound-Regular.ttf",
    who_font="fonts/VarelaRound-Regular.ttf",
    what_color=color("#04f17a"), # oth, the secure
    who_color=color("#04f17a"),
    callback=steel_voice
)
define z = Character("Zip", 
    what_font="fonts/IndieFlower-Regular.ttf",
    who_font="fonts/IndieFlower-Regular.ttf",
    what_color=color("#ff9b00"), # mersenne, the wildcard
    who_color=color("#ff9b00"),
    what_size=50,
    who_size=75,
    callback=pizz_voice
)
define tim = Character("Timothy Victrola",
    what_font="fonts/Oxygen-Regular.ttf",
    who_font="fonts/Oxygen-Bold.ttf",
    what_color=color("#01fff8"), # zariel, the absent
    who_color=color("#01fff8"),
    callback=pizz_voice
)

define yougot = Character("You Got:",
    what_slow_cps=5
) 
# props to your mother
define notepad = Character("Notepad",
    what_color=color("#fdffd9"),
    who_color=color("#fdffd9"),    
    what_font="fonts/RobotoSlab-Medium.ttf",
    who_font="fonts/RobotoSlab-Bold.ttf",
    callback=notepad_voice,
)
define cb = Character("Magic Cue Ball",
    what_color=color("#ffffff"),
    who_color=color("#ffffff"),    
    who_font="fonts/RobotoSlab-Bold.ttf",
    what_font="fonts/RobotoSlab-Medium.ttf",
)
define phone = Character("Phone",
    what_color=color("#fdffd9"),
    who_color=color("#fdffd9"),    
    what_font="fonts/RobotoSlab-Medium.ttf",
    who_font="fonts/RobotoSlab-Bold.ttf",
    callback=phone_voice,
)
define clock = Character("Clock",
    what_color=color("#fdffd9"),
    who_color=color("#fdffd9"),    
    what_font="fonts/RobotoSlab-Medium.ttf",
    who_font="fonts/RobotoSlab-Bold.ttf",
    callback=clock_voice,
)
define crimeputer = Character("Crimeputer",
    what_color=color("#fdffd9"),
    who_color=color("#fdffd9"),    
    what_font="fonts/RobotoSlab-Medium.ttf",
    who_font="fonts/RobotoSlab-Bold.ttf",
    callback=bit_voice,
)
define badge = Character("Badge",
    what_color=color("#fdffd9"),
    who_color=color("#fdffd9"),    
    what_font="fonts/RobotoSlab-Medium.ttf",
    who_font="fonts/RobotoSlab-Bold.ttf",
    callback=badge_voice,
)
define belt = Character("Belt",
    what_color=color("#fdffd9"),
    who_color=color("#fdffd9"),    
    what_font="fonts/RobotoSlab-Medium.ttf",
    who_font="fonts/RobotoSlab-Bold.ttf",
    callback=belt_voice,
)
define cigarettes = Character("Cigarettes",
    what_color=color("#fdffd9"),
    who_color=color("#fdffd9"),    
    what_font="fonts/RobotoSlab-Medium.ttf",
    who_font="fonts/RobotoSlab-Bold.ttf",
    callback=snake_voice,
)
define gun = Character("Gun",
    what_color=color("#fdffd9"),
    who_color=color("#fdffd9"),    
    what_font="fonts/RobotoSlab-Medium.ttf",
    who_font="fonts/RobotoSlab-Bold.ttf",
    callback=snake_voice,
)
define tie = Character("Tie",
    what_color=color("#fdffd9"),
    who_color=color("#fdffd9"),    
    what_font="fonts/RobotoSlab-Medium.ttf",
    who_font="fonts/RobotoSlab-Bold.ttf",
    callback=snake_voice,
)
define carkeys = Character("Car Keys",
    what_color=color("#fdffd9"),
    who_color=color("#fdffd9"),    
    what_font="fonts/RobotoSlab-Medium.ttf",
    who_font="fonts/RobotoSlab-Bold.ttf",
    callback=keys_voice,
)
define bike = Character("Bike",
    what_color=color("#fdffd9"),
    who_color=color("#fdffd9"),    
    what_font="fonts/RobotoSlab-Medium.ttf",
    who_font="fonts/RobotoSlab-Bold.ttf",
    callback=bike_voice,
)
define gum = Character("Gum",
    what_color=color("#fdffd9"),
    who_color=color("#fdffd9"),    
    what_font="fonts/RobotoSlab-Medium.ttf",
    who_font="fonts/RobotoSlab-Bold.ttf",
    callback=gum_voice,
)
define yuyuyuzu = Character("Yuyuyuzu Hoodie",
    what_color=color("#fdffd9"),
    who_color=color("#fdffd9"),    
    what_font="fonts/RobotoSlab-Medium.ttf",
    who_font="fonts/RobotoSlab-Bold.ttf",
)
define plant = Character("Obvious Plant",
    what_color=color("#fdffd9"),
    who_color=color("#fdffd9"),    
    what_font="fonts/RobotoSlab-Medium.ttf",
    who_font="fonts/RobotoSlab-Bold.ttf",
)
define condoms = Character("Condoms",
    callback=condoms_voice,
    what_color=color("#fdffd9"),
    who_color=color("#fdffd9"),    
    what_font="fonts/RobotoSlab-Medium.ttf",
    who_font="fonts/RobotoSlab-Bold.ttf",
)
define dressshirt = Character("Kerosene-Soaked Dress Shirt",
    callback=bit_voice,
    what_color=color("#fdffd9"),
    who_color=color("#fdffd9"),    
    what_font="fonts/RobotoSlab-Medium.ttf",
    who_font="fonts/RobotoSlab-Bold.ttf",
)

define car = Character("Toyomi Paradise",
    what_color=color("#fdffd9"),
    who_color=color("#fdffd9"),    
    what_font="fonts/RobotoSlab-Medium.ttf",
    who_font="fonts/RobotoSlab-Bold.ttf",
)
# one-off joke characters
# WEALTHY DOWAGER
define wd = Character("",
    what_font="fonts/GreatVibes-Regular.ttf",
    who_font="fonts/GreatVibes-Regular.ttf",
    what_color=color("#ff00e6"),
    who_color=color("#ff00e6"),
    what_size=75,
    who_size=75,
)
define bch = Character("Big Chili Henk",
    what_font="fonts/Itim-Regular.ttf",
    who_font="fonts/Itim-Regular.ttf",
    what_color=color("#488efb"), # misk
    who_color=color("#488efb"),
    what_size=45,
    who_size=55,
)
define client = Character("Soft Serve Steve",
    what_font="fonts/Itim-Regular.ttf",
    who_font="fonts/Itim-Regular.ttf",
    what_color=color("#488efb"), # misk
    who_color=color("#488efb"),
    what_size=45,
    who_size=55,
)

image yougot:
    "yougot 1.png"
    pause 0.248
    "yougot 2.png"
    pause 0.248
    "yougot 3.png"
    pause 0.248
    "yougot 4.png"
    pause 0.248
    "yougot 5.png"
    pause 0.248
    "yougot 6.png"
    pause 0.248
    "yougot 3.png"
    pause 0.248
    "yougot 1.png"
    pause 0.248
    "yougot 2.png"
    pause 0.248
    "yougot 1.png"
    pause 0.248
    "yougot 2.png"
    pause 0.248
    "yougot 3.png"
    pause 0.248
    "yougot 3.png"
    pause 0.248
    "yougot 3.png"
    pause 0.248
    repeat

image detective_looking:
    "detective small lookleft.png"
    pause 0.5
    "detective small lookright.png"
    pause 0.5
    "detective small lookleft question.png"
    pause 0.5
    "detective small lookright question.png"
    pause 0.5
    repeat

image detective_akira:
    "detective akira 1.png"
    pause 1
    "detective akira 2.png"
    pause 1
    "detective akira 3.png"
    pause 1

image detective_victory:
    "detective umbrella.png"
    pause 0.4
    "detective umbrella 2.png"
    pause 0.4
    "detective umbrella flip.png"
    pause 0.4
    "detective umbrella flip 2.png"
    pause 0.4
    repeat

image detective_jerk:
    "detective pensive over jerk.png"
    pause 0.3
    "detective pensive over jerk 2.png"
    pause 0.3
    repeat

define hasTie = False
define hasBadge = False
define isHydrated = False
define hasEggRoll = False
define hasCatLuck = False
define hasBelt = False
define hasCigarettes = False
define hasGun = False
define hasCarKeys = False
define hasCueBall = False
define hasBike = False
define hasGum = False
define hasWatchTan = True
define hasSportsClothing = False
define hasHair = False
define hasChili = False
define hasCondoms = False
define hasGymMembership = False
# turn in your badge and gum
define carExploded = False
define hasStrangulation = False
define hasDressShirt = False
# it would be really, really hard to have both hasStrangulation=False and hasDressShirt=False

# The game starts here.

label start:
    $ quick_menu = False

    scene bg traffic jam

    "Scene of the crash:"
    
    play ambient_2 "ambient/honk.ogg" volume 0.4    

    play music "music/Verano Sensual.mp3"

    "Traffic, lots of it. There's been a car crash."

    "Some traffic obstructions are up: one lane of traffic has opened to allow cars to flow through slowly,
        although sharing one lane in both directions is not nearly enough to clear the traffic."

    "This is a major throughfare and a huge snarl."

    "Furious honking. Road rage brewing."
    
    scene bg car crash

    "A junior police officer and a paramedic are gathered around a car that has very badly crashed."

    show paramedic
    parm "Call it - he's dead."
    hide paramedic

    show jemby serious
    trfc "Oh, no. You - barely even got in there, are you sure?"
    hide jemby

    show paramedic eyebrow
    parm "Are you new here, kid? The steering wheel's gone clean through his chest. He's not gonna walk that off."

    parm "It's going to take an act of god and a spatula to get this guy out of here."
    hide paramedic

    # trfc finds something suspicious
    show jemby serious
    trfc "This is... very strange, for a traffic accident."
    hide jemby

    show paramedic eyebrow
    parm "What do you mean?"
    hide paramedic

    show jemby lean
    "The junior police officer reaches down."
    hide jemby

    show jemby cinder
    trfc "Well, for one, most people in traffic accidents aren't driving with a pet cinder block 
        next to their gas pedal."
    trfc "I think it might have been... {i}murder most foul{/i}." 
    hide jemby

    show paramedic
    parm "Oh, for the love of shit. You think this was a {b}homicide{/b}? Because you found a {b}rock{/b}?"
    hide paramedic

    show jemby
    trfc "It could be. I'm gonna call it in."
    hide jemby

    show paramedic
    parm "Can I start bagging this guy up?"
    hide paramedic

    show jemby
    trfc "No, we can't touch anything. It's all {i}evidence{/i} now."
    hide jemby

    show paramedic nonplussed
    parm "This is {i}unbelievably inconvenient{/i}."
    hide paramedic
    
    scene bg car crash squad
    "The junior police officer heads to the squad car."
    
    #angry
    show paramedic
    with hpunch
    parm "- I'M SURE THE HONKING WILL CLEAN UP THE CRASH FASTER -"
    hide paramedic
    stop ambient_2

    "The junior police officer returns."

    show paramedic
    parm "How long does this usually take? I've got to bag up the body, and the traffic department's already
        giving us dirty looks about clearing this road."
    hide paramedic
    
    show jemby
    trfc "I don't know, this is the first time I've requested a detective. Dispatch says that they should have
        someone out in five minutes or so."
    hide jemby

    show paramedic
    parm "I hope they're here {i}soon{/i}."
    hide paramedic
    
    show jemby
    trfc "..."
    hide jemby

    show paramedic
    parm "..."

    parm "So... we just wait?"
    hide paramedic

    show jemby serious
    trfc "Yeah."
    hide jemby

    show paramedic
    parm "It's really wet out today."
    hide paramedic
    
    show jemby serious
    trfc "It sure is."
    hide jemby

    show paramedic
    parm "Why the sunglasses, then?"
    hide paramedic

    show jemby serious
    trfc "I think they give me an air of authority."
    hide jemby
    
    show paramedic eyebrow
    parm "..."

    parm "... I hope they send somebody quickly."
    hide paramedic
    jump precinct

label precinct:

    scene bg precinct ext

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    play ambient "ambient/rain_smaller.ogg"

    "POLICE PRECINCT. A large, cement, brutalist building on a grey day. We wouldn't know it was a police precinct 
        without the title card. It's raining."
    
    play music "music/Loopster.mp3"

    scene bg precinct int

    "A serious looking police chief is sitting at their desk. The desk itself is clean, organized, and utterly 
        devoid of modern technology. Instead, there sits a large bakelite touch-tone phone. Behind them are 
        framed awards and medals."

    # rain's quieter, we're indoors
    play ambient "ambient/rain_smaller.ogg" volume 0.5

    "A thin, hawkish man in a blue shirt walks in, a worried look on his face."

    show chief
    ha "Smunders!"
    hide chief

    show smunders
    ws "Yes?"
    hide smunders

    show chief curious
    ha "What's with the low quality of the {i}images{/i}? Don't games like this usually have {i}graphics{/i}?"
    hide chief

    show smunders clipboard
    ws "Ah, yes, in order to complete the game on schedule, art assets had to be fudged."
    hide smunders

    show chief curiouser
    ha "How {b}much{/b} fudge are we talking about here?"
    hide chief

    show smunders clipboard
    ws "Significant."

    ws "Very significant fudging, sir. According to my numbers, every possible corner was cut."
    hide smunders

    show chief curiouser still
    ha "Okay, what about a branching narrative? We were still able to fit in one of those, right?"
    hide chief

    show smunders clipboard
    ws "No, sir. No room in the budget. All narrative decisions are completely cosmetic."
    hide smunders

    show chief curious
    ha "How cosmetic?"
    hide chief

    show smunders clipboard
    ws "They affect {i}details of what happens{/i} but not the {i}outcome{/i}." 
    hide smunders

    menu:
        "Completely unacceptable":
            show smunders
            ws "My hands are tied, sir - we have to make do with what we can."
            hide smunders
        "I suppose we'll have to make do.":
            show smunders clipboard exactly
            ws "Exactly, sir - we don't have a choice any more than this narrative does." 
            hide smunders

    show chief angry
    ha "Unfortunate. How about sound? Were we able to get any of that?"
    hide chief

    show smunders clipboard
    ws "Good news on that front, we have quite a bit of sound. I might even go so far as to
            suggest headphones."
    hide smunders

    show chief
    ha "Well, that's good, at least."
    hide chief
     
    show chief angry
    ha "Anyways - why are you in my office?"
    hide chief

    show smunders
    ws "We have a, uh, routine traffic fatality, but the officer on the scene has requested that we send a detective."
    hide smunders

    show chief curious
    ha "Something suspicious about the circumstances, hm?"
    hide chief

    show smunders
    ws "Yes - but it's a highway accident, so the city will be breathing down our neck if we can't clear the scene quickly."
    hide smunders

    show chief curious
    ha "So we need a detective right {i}now{/i}, then?"

    ha "How about..."
    hide chief

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
            show smunders
            ws "Goode and Dunn? They're on vacation leave right now."
            hide smunders
            $ goode_and_dunn = False
            jump how_about
        
        "Briggs and Stratton?" if briggs_and_stratton:
            show smunders
            ws "Briggs and Stratton? I already checked with them, they've got engine trouble."
            hide smunders
            $ briggs_and_stratton = False
            jump how_about
        
        "Smith and Wesson?" if smith_and_wesson:
            show smunders
            ws "Smith and Wesson? I can't get a hold of them, they've been at the shooting range all day."
            hide smunders
            $ smith_and_wesson = False
            jump how_about
        
        "Abbott and Costello?" if abbott_and_costello:
            show smunders clipboard
            ws "Abbott and Costello? On administrative leave after they got in that big scrap at the baseball field."
            hide smunders

            show chief curiouser
            ha "Big scrap at the {i}baseball field?{/i}"
            hide chief
            
            show smunders clipboard
            ws "One of them got Lieutenant Hu's name wrong, again."
            hide smunders
            
            show chief curiouser still
            ha "Hu?"
            hide chief

            show smunders clipboard exactly
            ws "Exactly, sir."
            hide smunders
            $ abbott_and_costello = False
            jump how_about
        
        "Hall and Oates?" if hall_and_oates:
            show smunders
            ws "Hall and Oates? They left the force, sir, to become private eyes."
            hide smunders
            
            show chief
            ha "That's unfortunate. Watch out, boys - that life'll chew you up."
            hide chief

            $ hall_and_oates = False
            jump how_about
        
        "Astaire and Rogers?" if astaire_and_rogers:
            show smunders
            ws "Astaire and Rogers? They're tapped out, sir."
            hide smunders

            show chief angry
            ha "Damn."
            hide chief

            $ astaire_and_rogers = False
            jump how_about
        
        "Bert and Ernie?" if bert_and_ernie:

            show smunders clipboard
            ws "Bert and Ernie? They're getting married this week, sir."
            hide smunders
            
            show chief happy
            ha "Oh. Wonderful. Have you remembered to send them flowers and a card, from the precinct?"
            hide chief
            
            show smunders clipboard exactly
            ws "Of course, sir."
            hide smunders
            $ bert_and_ernie = False
            
            jump how_about

        "Dorian and Turk?" if dorian_and_turk:
            show smunders suspicious
            ws "Dorian and Turk? You don't want to put those scrubs on a real case."
            hide smunders

            $ dorian_and_turk = False
            jump how_about

        "Ferrell and O'Teri?" if ferrell_and_oteri:
            show smunders suspicious
            ws "No."
            hide smunders
            
            show chief
            ha "... Wise."
            hide chief

            $ ferrell_and_oteri = False
            jump how_about
        
        "Hamm and Deggs?" if hamm_and_deggs:
            show smunders clipboard
            ws "Hamm and Deggs? They're a good pair - I'm sure they'd be able to turn this over, easy."
            hide smunders

            show chief
            ha "Yeah. Why are you waffling, then? Let's use them!"
            hide chief

            show smunders clipboard
            ws "But they're busy with a case right now, for that baseball team - the Holland A's."
            ws "We've also got them on the Ashley Brown murder."
            hide smunders
            
            show chief
            ha "Okay, gotcha, Hamm and Deggs are too busy with Holland A's and Ash Brown."
            hide chief
            
            show smunders clipboard exactly
            ws "Exactly, sir."
            hide smunders

            $ hamm_and_deggs = False
            jump how_about
        
        "Capilano?":
            show smunders suspicious
            ws "Detective Capilano? Really? Is she... the {i}best{/i} choice for this?"
            hide smunders

            if not hamm_and_deggs and not ferrell_and_oteri and not dorian_and_turk and not bert_and_ernie and not astaire_and_rogers and not hall_and_oates and not abbott_and_costello and not smith_and_wesson and not briggs_and_stratton and not goode_and_dunn:
                show chief curious
                ha "It sounds like she's our {b}only{/b} choice for this."
                hide chief
            else: 
                show chief
                ha "She's a good cop, even if her methods are a little unorthodox."
                hide chief
            
            show smunders
            ws "Well, I suppose. I'll get her on the phone."
            hide smunders

            show chief curiouser
            ha "On the phone? Is she not in today?"
            hide chief

            show smunders
            ws "She should be, but she's late. {i}Again{/i}."
            hide smunders
            
            show chief curiouser still
            ha "How often would you say that she's late to work, Smunders?"
            hide chief

            show smunders
            ws "I wouldn't say that I can recall her being on time for work, ever, sir."
            hide smunders
            
            show chief angry
            ha "Hm. Noted."

            show chief
            ha "Anyways, call her and let her know about {i}the situation.{/i}"
            hide chief

            jump start_home
            

label start_home:
    
    play music "music/Grand Dark Waltz Moderato.mp3"

    scene bg apartment int
    with wipeleft

    "We cut to the interior of an extremely messy apartment. The television helps to establish
        the time frame by virtue of being a behemoth of wood and chrome with a tiny screen."
    
    "A woman is sleeping,
        face-down, fully clothed, on the ugliest chesterfield you have ever seen. In front of her is a
        coffee table with an overstuffed ashtray."

    "The phone is ringing."

    sc "Guh."

    show bgoverlay quiet
    with dissolve

    show prop phone
    with hpunch
    phone "ANSWER ME, COWARD!"
    hide prop

    sc "Nghuh."

    "Look, if Detective Capilano doesn't pick up the phone, we can't get this story started. Up! UP!"

    show prop phone
    phone "RING RING! ALSO RING!"
    hide prop

    show detective notie faceplam
    with easeinbottom
    sc "Okay, okay, dang. Geez."

    "The woman uncomfortably peels herself off of the couch. She has short hair, a slim build, and a trench-coat
        that probably smells like a grown-ass adult just slept in it."

    hide detective
    with easeoutleft

    show detective notie phone
    with easeinright
    "She picks up the phone."

    sc "Hello?"
    
    hide detective

    show smunders phone
    ws "You're late for work, Ms. Capilano."
    hide smunders

    "Detective Capilano looks at the clock on the wall."
    
    show prop clock
    clock "It's 1:02. You're not just
        late for work, you're {i}very, very{/i} late for work."
    hide prop
    
    show detective notie phone
    sc "{i}groggily{/i} who is this? Smunders?"
    hide detective
    with easeoutright

    show smunders phone
    with easeinleft
    with zoomin
    ws "Yes, it's me. {i}Smunders{/i}."
    hide smunders
    with easeoutleft

    show detective smunders
    with easeinright
    sc "Smunders?"
    hide detective
    with easeoutright

    show smunders smunders
    with easeinleft
    ws "{i}Smunders.{/i}"
    hide smunders
    with easeoutleft

    show detective smunders smunders
    with easeinright
    sc "{b}Smunders?{/b}"
    hide detective
    with easeoutright
    
    show smunders smunders smunders
    with easeinleft
    ws "{i}{b}Smunders!{/b}{/i}"
    hide smunders
    with easeoutleft
    
    show detective smunders smunders smunders
    with easeinright
    sc "{b}Smunders?{/b}"
    hide detective
    with easeoutright
    
    show smunders smunders smunders smunders
    with hpunch
    ws "{i}{b}Smunders!{/b}{/i}"
    hide smunders

    show detective notie phone
    sc "You {i}know{/i} that I was up until 3AM last night on the Vengabus file, right?"
    
    sc "Everybody was {i}jumping{/i}. I have a terrible headache."
    hide detective

    show smunders phone
    ws "I didn't know that, no. In any case, I'm not concerned with how late you stay at work.
            The day starts at 7:00AM - sharp."
    hide smunders

    # eye roll
    show detective notie phone eyeroll
    "The detective rolls her eyes."

    sc "Okay, Wayland, I'll be right in."
    hide detective

    show smunders smunders
    with hpunch
    ws "Did you just roll your eyes at me?"
    hide smunders

    show detective notie phone irritated
    "How did he know that?"
    hide detective
    
    show smunders phone
    ws "Anyways - don't come in to the precinct - we need you at Beresford and 48th. There's been a traffic accident."
    hide smunders

    show detective notie phone irritated
    sc "Don't we have, like, traffic cops for that kind of thing?"
    hide detective

    show smunders phone
    ws "We do. They've requested a detective. You're it, Capilano."
    hide smunders

    show detective notie phone irritated
    sc "Hngh. Okay. I'll be there in ten minutes."
    hide detective

    show smunders smunders
    ws "Make it five. The whole mess needs to be sorted as quickly as possible or Traffic is gonna have our asses on
            platters."
    hide smunders

    show smunders smunders smunders
    ws "It's going to be an all-you can eat buffet. Of ass-platters. Heaped tall with asses, the asses of
            everyone on the force."
    
    show smunders smunders smunders smunders
    ws "I want to impress upon you exactly how ass-laden these platters will be if you are not at this crime
            scene in {b}five minutes{/b}."
    hide smunders

    show detective notie phone irritated
    sc "Okay, so, it's real important that I get down there soon."
    hide detective

    show smunders smunders smunders
    ws "Yes, Detective Capilano."
    hide smunders

    show detective notie phone irritated
    sc "I'm not entirely dressed, yet."
    hide detective

    show smunders phone
    ws "Oh, and I know how you just {i}love{/i} to stand on decorum. I bet your collar isn't even pressed." 
    
    ws "Let's just say that, this time, you have special dispensation from the top to show up 
            as your {i}usual rumpled self{/i}."

    ws "Just... make sure to bring a tie and your badge, okay?"
    hide smunders
    
    show detective notie phone
    sc "Gotcha."
    hide detective

    show detective_looking
    "Hanging up the phone, Detective Capilano looks around her dingy apartment. Where {i}is{/i} that tie?"
    hide detective_looking

    show prop tie
    tie "I'm draped over the couch!"
    hide prop tie

    show detective notie
    sc "Things are talking to me again. Great."

    "She should talk about this with a doctor, but, to be honest, they'd probably put her on 
        a bunch of lithium, and Detective Capilano has had it with how {i}loud{/i} heavy metals can be."
    
    show detective straightening
    "Detective Capilano puts on the tie, tying her look together somewhat."
    hide detective
    
    show detective sunglasses prep
    sc "I guess... "
    show detective sunglasses
    play sound "sounds/belt.ogg"
    sc "...it's a tie."
    
    "The idea of a talking tie is stolen, whole-cloth, from the game \'Disco Elysium\'. Here, though, instead of 
        being an avatar of the main character's passionate imagination and wild side, this tie is simply 
        a tie that happens to be able to talk."
    
    "This is intended to illustrate the central conceit of this story: objects speak to Detective Capilano."

    show detective straightening
    sc "Now I just need to grab my badge, and maybe a few other things, before I head out."
    hide detective

    hide bgoverlay

    jump apartment

define apartmentThingsLeft = 3

define lookedAround = False
define lookedForTie = False
define lookedForNotepad = False
define lookedForUmbrella = False
define isLate = False

label apartment:    

    show bgoverlay quiet

    if apartmentThingsLeft > 0:
        "Detective Capilano is short on time: She's only going to be able to grab a few things before she goes.\n
        {b}[apartmentThingsLeft]{/b} things, to be exact."
    else:
        "Detective Capilano is out of time to grab random objects from her home. It's time to get on the road."

    menu: 
        "Just look around" if not lookedAround:
            $ lookedAround = True
            hide bgoverlay
            "This apartment is dated and dingy, a small studio apartment with a lot of cigarette stains."
            "The kitchen hosts a dirty pile of old take-out containers and empty beer bottles."
            "In one corner, an old cat is having a nap in a basket."
            "Home, sweet home."
            show bgoverlay quiet
            jump apartment
        "Look for her {b}Notepad{/b}" if not lookedForNotepad and apartmentThingsLeft > 0:
            "This one's a freebie. Detective Capilano's notepad is in her breast pocket, {i}always{/i}."
            $ lookedForNotepad = True

            play music "music/I Got A Stick.mp3"
            show prop notepad
            show yougot
            yougot "A notepad that you already had!"
            hide yougot
            
            play music "music/Grand Dark Waltz Moderato.mp3"
            
            notepad "Notepad located in breast pocket."
            notepad "Reliable. Keeps important details recorded for later."
            hide prop

            show detective
            sc "Calm down. We haven't even started yet."
            hide detective

            show prop notepad
            notepad "Notepad very excited to solve mystery."
            hide prop
            
            jump apartment
        "Look for her {b}Badge{/b}" if not hasBadge and apartmentThingsLeft > 0:
            
            show detective_looking
            sc "Where did I leave my badge? I think..."
            hide detective_looking

            show detective lean
            play sound "sounds/fridge.ogg"
            "Detective Capilano walks to her fridge and opens it."
            play sound "sounds/dishes.ogg"

            "Inside the fridge are mostly cartons of leftover spicy takeout noodles and Kokanaut brand beer."
            "On top of a pot of chili oil sits an extremely handsome, official looking badge."
            "Detective Capilano grabs the {b}Badge{/b}."
            $ hasBadge = True
            hide detective
            
            play music "music/I Got A Stick.mp3"
            show yougot
            show prop badge
            yougot "A badge!"
            hide yougot
            play music "music/Grand Dark Waltz Moderato.mp3"

            badge "It was extremely unprofessional of Detective Capilano to leave me in the fridge."
            hide prop

            show detective lean
            sc "Well, you won't get lost, here."
            hide detective

            show prop badge
            badge "The cold, cold fridge."
            hide prop

            show detective lean
            sc "Oh, hey! Score!"

            play sound "sounds/wax.ogg"
            "Detective Capilano also takes this opportunity to grab a greasy, wax-paper-wrapped {b}Egg Roll{/b} for the road."
            # you got.... egg roll! 
            $ hasEggRoll = True
            hide detective lean

            show yougot
            show prop eggroll
            play music "music/I Got A Stick.mp3"
            yougot "An egg roll!"
            play music "music/Grand Dark Waltz Moderato.mp3"
            hide prop
            hide yougot
            
            if hasCueBall:
                show prop cueball
                cb "This egg roll has no bearing on the case."
                hide prop
            
            show prop badge
            badge "I am an officer of the law and you give the same amount of fanfare to some shredded cabbage wrapped in rice paper? The {i}audacity{/i}."
            badge "It doesn't even talk!"
            hide prop

            show detective lean
            sc "Food never does. Don't know why. I'm glad, though. That'd be uncomfortable."
            hide detective
            
            $ apartmentThingsLeft = apartmentThingsLeft - 1

            if hasCatLuck and apartmentThingsLeft > 0:
                "Hey, look! Your {b}Magic Cue Ball{/b} is in the fridge!"

            jump apartment
        "Go back to the fridge and have a {b}Beer{/b}" if hasBadge and not isHydrated and apartmentThingsLeft > 0:

            show prop badge
            badge "Detective Capilano. I respect your lack of deference to professionalism but you just woke up."
            hide prop

            show detective shrug
            sc "Aw, come on - I'm thirsty and I don't have time to make a coffee."
            hide detective
            
            show prop badge
            badge "Have water, then. You are an officer of the law and I won't have you day-drinking on the job."
            hide prop

            show detective pout
            sc "Water tastes like {i}nothing{/i}."
            hide detective
            
            show prop badge
            badge "It's good for you."
            hide prop

            show detective shrug
            sc "Okay. I guess."
            hide detective
            
            "Detective Capilano has a long, refreshing drink of regular-ass water, directly from the tap."

            $ isHydrated = True
            $ apartmentThingsLeft = apartmentThingsLeft - 1
            
            show yougot
            show prop water
            play music "music/I Got A Stick.mp3"
            yougot "Hydrated!"
            play music "music/Grand Dark Waltz Moderato.mp3"
            hide yougot
            hide prop
            
            jump apartment
        "Look for her {b}Cat{/b}" if not hasCatLuck:
            "The {i}top priority{/i}, right now, is getting some Zip time in."

            show zip upsidedown 
            "Zip curls around to demand some belly rubs. Can't start a case without some Zip love. 
                Them's the crime rules."
            
            sc "Hey there, buddy!"
            
            play sound "sounds/meow.ogg" volume 0.5
            z " ~ ~ miau! ~ ~ :3"
            show zip
            "Zip is usually content to sit at the window and watch the day go by while Detective Capilano works."

            "Detective Capilano found Zip on her first week on the force. He's almost 18 years old now - ancient, 
                in cat years."
            "He's content to wait the day out here, watching out the window for his own perps, 
                but leaving the house without giving Zip a little rub behind the ears is bad luck."
            
            play sound "sounds/purr.ogg"
            z "{i}( * happy rumbling * ) :3 {/i}"
            $ hasCatLuck = True
            $ lookedForZip = True
            hide zip
            
            if hasBadge and apartmentThingsLeft > 0:
                "Zip gets up and dashes behind the television."
                show prop cueball
                "While he's back there, he knocks a dusty old cueball out, which rolls into the middle of the living room."
                badge "This is the {b}Magic Cueball{/b}."
                hide prop
            
            jump apartment
        "Look for her {b}Car Keys{/b}" if not hasCarKeys and apartmentThingsLeft > 0:
            
            show prop carkeys
            carkeys "You'll never find me, hag!"
            carkeys "Wench! Strumpet!"
            hide prop

            show detective_looking
            sc "I can hear you, you little goon."
            hide detective_looking
            
            show prop carkeys
            carkeys "You'll never find me! I am irretrievable! I am {i}the wind{/i}. I am {b}the night{/b}. "
            hide prop
            
            show detective lean
            sc "Yeah, there you are."
            hide detective

            show prop carkeys
            carkeys "You found me." 
            carkeys "Fuck."
            hide prop

            if hasBadge:
                show prop badge
                badge "I don't understand why you have to be so salty all the time."
                show prop carkeys
                carkeys "Here's what {i}you{/i} sound like: meh meh meh, meh meh meh meh."
                hide prop
            
            if hasBelt:
                show prop belt
                belt "Language, keys. This is a woman of taste and class."
                show prop carkeys
                carkeys "Piss off, leatherboy."
                show prop belt
                belt "... I would be angrier at you if I did not like the sound of \"leatherboy\" so much. 
                            Keep calling me that, it is definitely working for me."
                show prop carkeys
                carkeys "I hate you."
                hide prop
            
            show yougot
            show prop carkeys
            play music "music/I Got A Stick.mp3"
            yougot "Foulmouthed Car Keys!"
            play music "music/Grand Dark Waltz Moderato.mp3"
            hide prop
            hide yougot
            
            if hasCueBall:
                show prop cueball
                cb "These won't help you, your car won't start anyways and the traffic around the crime scene is impassable."
                hide prop
            elif hasBadge:
                show prop badge
                badge "Detective Capilano's car is very old, it might not be of any help."
                show prop carkeys
                carkeys "Oh, and what do {i}you{/i} bring to the table?"
                show prop badge
                badge "I command {i}respect{/i}."
                hide prop
            
            $ hasCarKeys = True
            $ apartmentThingsLeft = apartmentThingsLeft - 1
            jump apartment
        "Look for her {b}Belt{/b}" if not hasBelt and apartmentThingsLeft > 0:
            "It's between the couch cushions. Detective Capilano must have taken it off in the night."
            show detective lean
            sc "Good thing I found this! Wouldn't want my pants to fall down at an inopportune time during the case!"
            hide detective 

            show prop belt
            belt "Oh, yes, oui, that is exactly what I am great at, mon cherie. Touching your body. Coming on. Coming... off."
            hide prop

            show detective irritated
            sc "You're a wierd little guy, belt."
            hide detective

            show prop belt
            belt "Come, now. Touch me to your waist. Let our erotic dance {i}begin{/i}."
            hide prop

            $ hasBelt = True

            show yougot
            show prop belt
            play music "music/I Got A Stick.mp3"
            yougot "Belt!"
            play music "music/Grand Dark Waltz Moderato.mp3"
            hide prop
            hide yougot
            
            $ apartmentThingsLeft = apartmentThingsLeft - 1
                
            jump apartment
        "Look for her {b}Cigarettes{/b}" if not hasCigarettes and apartmentThingsLeft > 0:

            "It's a terrible habit, but Detective Capilano can get pretty cranky without her cigarettes."
            "She quickly retrieves a fresh pack from a carton she keeps above the fridge."
            show detective lean
            sc "Oh, thank god."
            hide detective

            show prop cigarettes
            cigarettes "Hello, Detective. We meet again."

            cigarettes "We love you."
            hide cigarettes

            sc "Weird."

            show prop cigarettes
            cigarettes "Come on, give us a little kiss."
            
            show yougot
            play music "music/I Got A Stick.mp3"
            yougot "Emphysema!"
            play music "music/Grand Dark Waltz Moderato.mp3"
            hide yougot
            
            $ hasCigarettes = True
            $ apartmentThingsLeft = apartmentThingsLeft - 1
            hide prop
            
            if hasCueBall:
                show prop cueball
                cb "Put down the cigarettes. Your lung damage is getting to the point where it's nearly irreversible."

                show prop cigarettes
                cigarettes "She knows. She doesn't care. Our love is too strong."
                hide prop

                show detective irritated
                "Detective Capilano changes her mind and puts the cigarettes back down."
                hide detective

                $ hasCigarettes = False
            
            jump apartment

        "Look for her {b}Umbrella{/b}" if not lookedForUmbrella and apartmentThingsLeft > 0:
            $ lookedForUmbrella = True
            show detective_looking
            "Detective Capilano looks around her apartment to try and find her umbrella - it's raining out, 
                probably a good thing to grab."
            "No dice, it's nowhere to be found."
            "There's only one thing that she can try: her umbrella call."
            hide detective_looking

            # cupping her hands to her mouth
            show detective umbrella
            sc "Ella! Ella! Eh! Eh! Eh!"
            "This is the only language that umbrellas speak."
            sc "Ella! Ella! Eh! Eh! Eh!"
            hide detective

            show detective_looking
            "Unfortunately, her umbrella doesn't answer. Dang."
            hide detective_looking
            
            if hasCueBall:
                show prop cueball
                cb "You left your umbrella at the precinct, yesterday. No matter how much you look for it, in your apartment, you won't find it."
                hide prop
            
            jump apartment
        "Look for her {b}Gun{/b}" if not hasGun and apartmentThingsLeft > 0:
            "Detective Capilano ambles over to her end table. Moving aside some personal detritus, she fishes out
                a Chef's Special, a Smith & Cross Model 38 snub-nosed pistol."
            show prop gun
            "This is Detective Capilano's off-duty pistol: her service pistol and its holster are still in her locker at the precinct."
            "Detective Capilano has both a service pistol and an off-duty pistol because she needs constant access to a fast-draw, concealed, lethal weapon."
            "Does this make her sound like a bit of a coward? It {i}should{/i}."
            
            # it's based on a Smith & Wesson Model 36
            $ hasGun = True
            
            gun "Hey, baby, I'll keep you safe."
            "She gently pats the gun, her amulet of protection, as she tucks it into an inner pocket of her leather jacket."
            
            play music "music/I Got A Stick.mp3"
            yougot "A gun!"
            play music "music/Grand Dark Waltz Moderato.mp3"
            hide prop

            $ apartmentThingsLeft = apartmentThingsLeft - 1

            if hasCueBall:
                cb "Good."
                cb "You're going to shoot the murderer three times, in the chest, with this gun, before the end of the day."

            jump apartment
        "Pick up her {b}Magic Cueball{/b}" if hasBadge and hasCatLuck and not hasCueBall and apartmentThingsLeft > 0:
            
            play music "music/Cueball.mp3"

            show prop badge
            badge "A Magic 8-Ball makes predictions about the future, but the limited nature of
                the technology at play means that the predictions are, at best, inaccurate
                and not terribly specific."
            badge "The Magic Cueball makes predictions with alarming precision and specificity -
                the only problem being that the predictions are utterly obscured by the opaque ball."
            badge "This would be a problem for most, but Detective Capilano's unique ability gives the ball
                a voice. It's what's known as an {b}Artifact Synergy{/b}."
            badge "Detective Capilano brings the ball into play on particularly difficult cases:
                it always helps her solve the case, but its use comes at a terrible cost."
            badge "Be careful, though: having the Ball will ruin the fun of solving a murder."
            hide badge
            menu:
                "Yes, grab the {b}Magic Cueball{/b}":
                    $ hasCueBall = True
                    show detective
                    sc "I'm late, I could use a little umph."
                    hide detective

                    show prop cueball
                    cb "I'm glad you decided to bring me along. This will be a complete breeze, now."
                    cb "You should also find your {b}gun{/b}, even if it makes you late. It's in your end table."
                    cb "It's important."
                    $ apartmentThingsLeft = apartmentThingsLeft - 1
                    hide prop
                "No, not this time.":
                    show detective
                    sc "I can solve this one on my own, thanks."
                    hide detective
                    play music "music/Grand Dark Waltz Moderato.mp3"

            jump apartment 
        "Stay a little late and grab a few more things" if apartmentThingsLeft == 0 and not isLate:
            "Look, this case is too important to take on without a full inventory. Smunders can just hold his damn horses."
            show smunders
            ws "What? These horses are out of control! I can't hold them all!"
            hide smunders
            "Okay, even if Smunders can't hold his damn horses, he'll have to {i}try{/i}."
            $ apartmentThingsLeft = apartmentThingsLeft + 2
            $ isLate = True
            jump apartment
        "Leave":
            if hasCueBall and not hasGun:
                cb "I told you to get your gun."
                jump apartment
            if apartmentThingsLeft > 0 and not isLate:
                "Look, Detective Capilano is in a {i}real hurry{/i} - there's no time to stand around grabbing random objects."
            if apartmentThingsLeft >= 2 and isLate:
                $ isLate = False
                "Detective Capilano reconsiders grabbing any more objects and heads out, on time."
            elif isLate:
                "Untroubled by pedestrian concerns of {i}timing{/i}, Detective Capilano cruises out of her home a mere fifteen minutes late."
            else:
                "Time's up - Detective Capilano has to get on the road {i}now{/i} if she's going to make it on time."
            
            hide bgoverlay
            jump car

label car:
    play music "music/Grand Dark Waltz Allegretto.mp3"
    
    play sound "sounds/running.ogg"
    scene bg stairs
    "The elevator is out of service, so Detective Capilano runs down the stairs - six flights of them."

    scene bg car park
    "Her building hangs above a shared carport. Lots of cars are parked here, between stone pillars that keep
        the building itself up. Most of the cars are gone already, their owners already at work."
    
    # rain's louder, we're outdoors
    play ambient "ambient/rain_smaller.ogg" volume 1

    "This car is a rusted 3076 Toyomi Paradise. It just barely runs at the best of times."

    if hasCarKeys:
        play sound "sounds/keys.ogg"
        "Detective Capilano unlocks the car door and attempts to start the car."

        play sound "sounds/car_dead.ogg"
        car "I can't do it. I'm old. I've carried you 387,982 miles, I can't.. I just can't."

        sc "Oh, that doesn't sound good at all."

        play sound "sounds/car_dead.ogg"
        car "I don't think I have it in me. Something's wrong. I can feel it."

        show prop carkeys
        carkeys "Come on, man, without you I don't have much to offer!"
        hide prop

        "Detective Capilano turns the keys a little extra hard."

        play sound "sounds/car_really_dead.ogg"
        sc "Car? Are you okay?"
        sc "... Car?"

        show prop carkeys
        carkeys "... I think it's done for. Welp, at least I still unlock your front door. Shit."
        hide prop

        if hasCueBall:
            show prop cueball
            cb "The transmission is completely shot."
            cb "This car will require a full engine rebuild in order to ever move again. It might as well be scrap metal."
            hide prop

        "This car isn't going anywhere. Detective Capilano is going to have to find an alternative means of conveyance."

        "Detective Capilano isn't sure whether to mourn. The objects seem to have distinct personalities
                    but they don't seem to have much in the way of internality."

        "But - hey, while she's here, might as well grab her {b}Gum{/b} out of the glove compartment."
        # you got.... gum!

        show yougot
        show prop gum
        play music "music/I Got A Stick.mp3"
        yougot "Chewing gum!"
        play music "music/Grand Dark Waltz Allegretto.mp3"
        hide yougot

        gum "Hi there! Put me in your mouth!"
        hide prop

        "Food doesn't talk, but gum isn't food. It's just a stick of chewable rubber. I don't know {i}who{/i} makes these rules."
        
        $ hasGum = True

    else:
        "Detective Capilano reaches into her pockets to try and find her car keys, but they're not there."

        "She'll definitely be late if she jogs back up those six flights of stairs, and, to be honest, 
            she {i}really{/i} doesn't want to."
         
        sc "Shit."

        "I guess we're not taking the car."
    
    sc "Beresford and 48th is only a handful of blocks away. Maybe I'll just walk over."

    scene bg car park bike

    if not isLate:
        "She will definitely be late if she walks. She can still make it in time, though: there's a Tonko L'il Funboy 
            bicycle in the garage, unlocked."

        bike "Hi there! I can help you get where you're going!"
        
        sc "No... you're a child's bike! I'll look ridiculous. And get soaked."

        bike "But you'll get where you're going on time! Don't worry, you know my kid! You can get
                 me back to him in good shape!"

        menu:
            "Walk":
                sc "I would rather be late than show up on time on a hideous children's toy."
                bike "... hurtful, but okay."
                $ isLate = True
                sc "I've got to go."
            "Ride the Tonko L'il Funboy":
                sc "Welp, got to get to work somehow. Sorry, kid!"
                play music "music/I Got A Stick.mp3"
                yougot "A {b}Tonko L'il Funboy{/b} children's bicycle!"
                play music "music/Grand Dark Waltz Allegretto.mp3"
                "Detective Capilano quickly scrawls a note in her notepad and affixes it to the bike rack."
                show prop notepad
                notepad "Bike needed for official police business, not stolen. Will return shortly. Thank you citizen."
                hide prop
                $ hasBike = True
                bike "Let's go! I want to blow this popsicle stand!"
    
    jump beresford

image jemby_light:
    "jemby light 1.png"
    pause 0.2
    "jemby light 2.png"
    pause 0.2
    "jemby light 3.png"
    pause 0.2
    repeat

label beresford:
    scene bg traffic jam

    "Scene of the crash:"
    
    play ambient_2 "ambient/honk.ogg" volume 0.4    

    play music "music/Verano Sensual.mp3"
    
    show paramedic
    parm "How long does this usually take? I've got to bag up the body, and the traffic department's already
        giving us dirty looks about clearing this road."
    hide paramedic
    
    show jemby
    trfc "I don't know, this is the first time I've requested a detective. Dispatch says that they should have
        someone out in five minutes or so."
    
    trfc "..."
    hide jemby

    show paramedic
    parm "..."

    parm "So... we just wait?"
    hide paramedic

    scene bg car crash squad
    stop ambient_2

    show jemby serious
    trfc "Yeah."
    hide jemby

    show paramedic
    parm "It's really wet out today."
    hide paramedic
    
    show jemby serious
    trfc "It sure is."
    hide jemby

    show paramedic
    parm "Why the sunglasses, then?"
    hide paramedic

    show jemby serious
    trfc "I think they give me an air of authority."
    hide jemby
    
    show paramedic eyebrow
    parm "..."
    hide paramedic

    "About five minutes of awkward small talk later..."

    # if isLate, have Jemby waiting a little too long and accidentally lighting the car on fire,
    #  ruining a whole bunch of evidence
    if isLate:
        show jemby doopa doo
        trfc "...doopa doo"
        hide jemby

        show paramedic
        parm "tum wee tiddly tum tee too"
        hide paramedic

        show jemby doopa doo
        trfc "God, this is taking forever... cigarette?"
        hide jemby

        show paramedic eyebrow
        parm "Nah, I don't smoke. That stuff'll kill you."
        hide paramedic

        show jemby
        trfc "Well, so will an entire steering column driven through your chest."
        hide jemby

        show paramedic eyebrow
        parm "You don't see me smoking entire steering columns, either, do you?"
        hide paramedic

        show jemby
        trfc "Okay, okay."

        show jemby_light
        "The junior traffic cop pulls out a cigarette, lights it, and takes a puff."
        hide jemby

        scene bg car crash fire 1
        "The victim's car lights on fire."

        show paramedic
        parm "So... you're a cop, huh?"
        hide paramedic

        show jemby cigarette
        trfc "Police officer."
        hide jemby

        show paramedic
        parm "I guess that's kind of the opposite of a paramedic."
        hide paramedic

        show jemby cigarette
        trfc "How do you mean?"
        hide jemby

        show paramedic
        parm "Actually, you know what, let's talk about something else."
        hide paramedic
        
        show jemby cigarette
        trfc "No, no, I want to hear how you think a police officer is the opposite of a paramedic."
        hide jemby

        show paramedic
        parm "Well, like, I try to keep people alive and, uh..."
        hide paramedic

        show jemby cigarette
        trfc "I {i}also{/i} try to keep people alive?"
        hide jemby

        scene bg car crash fire 2
        show paramedic eyebrow
        parm "Okay, I'm going to put this a different way. All of the tools I carry are for healing people.
                All of the tools you carry are for..."
        hide paramedic

        show jemby cigarette
        trfc "... I'm not sure what you're getting at."
        hide jemby

        "The fire is getting pretty bad."

        show paramedic nonplussed
        parm "It's fine, nevermind."
        hide paramedic

        show jemby cigarette
        trfc "Do you have a problem with the police?"
        hide jemby

        show paramedic nonplussed
        parm "..."
        hide paramedic

        show jemby cigarette
        trfc "I just enforce {i}the law{/i}. Don't see what your problem could be with that."
        hide jemby

        show paramedic eyebrow
        parm "And who does {i}the law{/i} serve?"

        parm "Look - I'm sorry I brought this up. Do you smell kerosene? I smell kerosene."
        hide paramedic

        show jemby cigarette
        trfc "Nah, I don't smell anything."
        hide jemby
        
        show paramedic
        parm "Where is that detective? It's been ages."
        hide paramedic

        show jemby cigarette
        trfc "You figure they'd have shown by now."

        show jemby serious
        "The junior traffic cop flicks his cigarette."
        hide jemby

        scene bg car crash fire 4
        play sound "sounds/explosion.ogg"
        with vpunch
        with hpunch
        "The car explodes."

        $ carExploded = True

        show jemby holy shit
        trfc "Holy shit!"
        hide jemby

    if hasBike:
        play sound "sounds/bike.ogg"
        scene bg default
        play sound "sounds/bike.ogg"
        show detective_akira
        "Detective Capilano enters the scene."
        hide detective_akira
    else:
        "Detective Capilano walks casually on to the scene."

    show detective kickass
    sc "Detective on the scene!"

    if hasGum:
        sc "I'm here to kick ass and chew bubblegum, and I'm all out of ass."

        show detective kickass bubble
        "Detective Capilano blows a bubble."
        play sound "sounds/pop.ogg"
        hide detective
    elif hasCigarettes:
        show detective cigarette
        "Detective Capilano pulls a cigarette out of the packet and hangs it on her lip."
        "I think she imagines that it looks very cool."
        hide detective
    else:
        show detective wave
        "Detective Capilano waves like a nerd."
        sc "Hi everybody!"
        hide detective
    
    show detective damp left
    "All of this would seem a lot cooler if Detective Capilano wasn't absolutely drenched."
    hide detective

    if isLate: 
        scene bg car crash fire 4
    else:
        scene bg car crash

    show jemby serious
    trfc "Who are you?"
    hide jemby

    show detective
    sc "Detective Susan Capilano."
    hide detective

    if hasBadge:
        show prop badge
        "Detective Susan Capilano flashes her badge, establishing beyond a shadow of a doubt that she is,
            in fact, a real cop, and not a feral hobo."
        
        badge "Hello, young man."
        hide prop

        show jemby
        trfc "Wait, {i}the{/i} Detective Susan Capilano?"
        hide jemby

        show detective sheepish
        sc "(sheepishly) that's me, yeah."
        hide detective

        show jemby
        trfc "We studied one of your cases in basic training."
        hide jemby

        show detective smug
        "Detective Capilano is visibly smug about this."

        sc "Was it \"The Case of the Jade Monkey\"? \"The Case of the Sizzling Sazerac\"? \"Death Lends a Hand\"?"
        hide detective

        show jemby serious
        trfc "It was \"The Case of the Mishandled Evidence Leading To a Full Acquittal\"."
        hide jemby

        show detective deflated
        "This deflates Detective Capilano somewhat."
        hide detective
    else:
        show jemby serious
        trfc "... a detective? Really? Cool, cool cool cool."

        trfc "Do you mind if I just jog to the squad car for a quick second? I think I might have... left it on."
        hide jemby

        "Detective Capilano nods but the junior traffic cop is already jogging to his car."

        "Detective Capilano hears the distant sounds of a call to the station."

        " ... \"some kind of feral hobo\" ...\"no tie\" ...  \"claims to be a detective\" ... 
            \"you're sure?\" ... \"Susan Capilano?\" ... \"no way!\""

        if hasBike:
            play sound "sounds/bike.ogg"
            "... \"yeah, a children's bike\"... \"looks like it's for a 12-year-old boy\"... "
        else:
            "... \"no car, she just strolled right up\"... "

        if isLate:
            "... \"very late\"... \"exploded, sir\"... \"yup, evidence completely destroyed\""
        "... \"smunders?\""
        "... \"smunders.\""
        
        "The junior traffic cop jogs back to the crime scene."

        show jemby
        trfc "Yeah, she checks out. A detective from the station."
        hide jemby

        show paramedic eyebrow
        parm "Okay."
        hide paramedic

    if hasGun:
        show prop gun
        gun "He doesn't respect you. I can smell it. Shoot him. Shoot him right in his stupid face."
        hide prop gun
        menu: 
            "Shoot him. Shoot him right in his stupid face.":
                if hasCueBall:
                    show prop cueball
                    cb "You can't. That's not how this goes."
                    hide prop
                    "Detective Capilano changes her mind."
                else:
                    jump shooting_game_over                
            "He can live.":
                show prop gun
                gun "Aww. Why did you even bring me if you aren't going to kill some people."
                hide prop
                if hasBadge: 
                    show prop badge
                    badge "I don't like you hanging out with gun, he's a psychopath."
                    hide prop badge
                else:
                    show prop notepad
                    notepad "Gun, psychopath, concerning."
                    hide prop

    show detective suspicious
    sc "So, what's the situation, here?"
    hide detective

    if isLate:
        show jemby
        trfc "Oh, you - I guess you just missed it. The dead guy just exploded."
        
        trfc "Well, uh, to be clear, the car with the dead guy in it, uh, was the part that - exploded."
        hide jemby

        show paramedic
        parm "If you had just arrived, like, five minutes earlier - that would have made a {i}huge{/i} difference."
        hide paramedic

        show jemby
        trfc "Yeah, that was a really consequential five minutes!"
        hide jemby

        show detective deflated
        sc "... oh, no."
        hide detective

        show jemby
        trfc "You're not going to get any information out of that body or that car, now."
        hide jemby

        show detective
        sc "I can ask you a few questions, though - would that be okay?"
        hide detective

        show jemby
        trfc "Of course - uh, but, keep in mind that we've got a mounting clean-up and traffic situation that's just
            getting worse with each passing moment."
        hide jemby
        
    show jemby
    trfc "The car crash, over here - I think it was staged."
    hide jemby

    show detective
    sc "Staged?"
    hide detective

    show jemby cinder
    trfc "I found a cinder block next to the gas pedal."
    hide jemby

    show paramedic nonplussed
    parm "Are you just carrying that around with you, now?"
    hide paramedic

    show jemby cinder
    trfc "It's evidence!"

    trfc "{i}Don't listen to him baby, I'm gonna call you Cindy.{/i}"
    hide jemby

    show detective
    sc "Hm, okay."
    hide detective
    
    show jemby
    trfc "And look at the positioning of the car, here - "    
    hide jemby
    
    scene bg crash diagram car

    trfc "..."

    scene bg crash diagram car bad

    trfc "- it's an odd angle for this car to have crashed into this pole -" 

    scene bg crash diagram car good

    trfc  "- {i}but{/i} if the car took off from that alley over there - well, it's a straight shot."

    "Detective Capilano nods."

    trfc "Plus, there aren't any visible tire marks around the crash site - no rapid braking, no skidding out of 
        control - it seems like they just took a straight line from that alley, across the road, directly into
        this pole, without flinching."

    trfc "I think the driver was already dead, and the cinder block
        was doing the driving."
    
    sc "Obviously that's all suspicious as hell."

    trfc "Exactly!"
 
    if isLate: 
        scene bg car crash fire 4
    else:
        scene bg car crash

    show detective notes point
    sc "That's some clever sleuthing, there, gumshoe."
    hide detective

    show jemby smug
    "Jemby looks smug."
    hide jemby

    show detective notes
    "Detective Capilano looks at the car for a moment and jots down some notes."
    hide detective

    show prop notepad
    notepad "'88 Cadillero Allstar. Got your game on. Go, play."
    hide prop

    show jemby
    trfc "Expensive vehicle?"
    hide jemby

    show detective notes
    sc "Oh yeah. They're popular mid-life-crisis-mobiles among bank managers and upper management types."

    sc "Heated leather seats, V-12 engine, hundreds of horses, they even come with cup-holders. The works."
    hide detective

    show jemby
    trfc "Imagine: being able to put a cup down in your car without it tipping over."
    hide jemby

    show detective shrug
    sc "I know, it seems like an impossible dream, but the engineers at Cadillero have cracked it."
    hide detective

    show jemby
    trfc "Magical."
    trfc "Do you think he got it in manual or automatic?"
    hide jemby

    show detective roll
    sc "It'd be a crying shame to get a high performance vehicle like this in anything but manual transmission."
    hide detective

    if hasCueBall:
        show prop cueball
        cb "Here's the scoop. The body belonged to a man named Timothy Victrola. He was killed by one 
                Hank Maxhank, by strangulation. He's a private detective who works a short distance from here."
        cb "The only thing you need to close this case is some information I'll feed you and access to his office."
        cb "That young man has the victim's wallet, you'll need to grab his identification."
        hide prop

        show detective
        sc "Hey, do you have any ID for the victim? I'll need it to inform his family members."
        hide detective

        show jemby wallet
        "The junior traffic cop holds up a wallet in a plastic bag."

        trfc "Before I thought it was a homicide investigation I nabbed it, yeah."
        hide jemby
        
        show detective
        sc "Good man. Let me take a look at that."
        hide detective
        
        scene bg wallet

        sc "Here we go, his ID."

        cb "Okay, call it in and we're going to head to his wife's office, next."
        
        jump ann_office
            

    if not isLate and not hasCueBall:
        show detective
        sc "Can I see the body?"
        hide detective

        show jemby
        trfc "It's kinda gruesome - but yeah."
        hide jemby

        scene bg car crash right
        "They walk over to the car's window."

        show detective faceplam
        sc "Wow. That's... incredibly graphic."
        hide detective

        show jemby
        trfc "I'm sure as a homicide detective you've seen it all."
        hide jemby

        show detective pout
        sc "I've definitely seen some things but I'm going to level with you: car crash victims are... up there, y'know?"
        hide detective

        show jemby
        trfc "Oh, I know. There are a {i}lot{/i} of car crashes."
        hide jemby

        show paramedic
        parm "Yeah, we have to deal with this kind of thing on the regular."
        hide paramedic

        if hasBike:
            show detective pout
            sc "Honestly, I'm feeling a little better about my decision to bike here, right now."
            hide detective

            show paramedic eyebrow
            parm "Oh, no, cars hit bikes all the time. If anything, that's much worse. 
                You ever see a guy tangled up in a wheel-well?"
            hide paramedic

            show detective
            sc "Once, but it was a murder investigation. Hot tip: don't piss off bus drivers. 
                Especially don't piss them off if you're 
                planning a bicycle marathon."

            show detective pout
            sc "(shudders) That was a {i}mess{/i}."
            hide detective

        show detective smug
        sc "Oh, hey, this car has a manual transmission. I called it! Score."
        hide detective

        show detective
        sc "Do you have some gloves I could borrow?"
        hide detective

        show jemby
        trfc "Fresh out."
        hide jemby

        show paramedic
        parm "I've got some. Here, take these."
        hide paramedic
        
        show detective gloves
        play sound "sounds/snap.ogg"
        "Detective Capilano puts on the gloves."

        sc "What is that {i}smell{/i}?"
        hide detective

        show paramedic eyebrow
        parm "Dead guy?"
        hide paramedic

        show detective gloves
        sc "No, it's... something different. Anyways - "
        hide detective

        show detective notes
        sc "Male, young, white, dark hair. Sports clothing - looks like an expensive Yuyuyuzu tracksuit."
        $ hasSportsClothing = True

        sc "I figured a car this expensive would have belonged to someone older, this young man can't possibly be over 25."

        sc "Okay, look at this - under the head, here, on the neck."
        hide detective

        show jemby
        trfc "Wow, that's a really distinctive bruising pattern. Not from the crash?"
        hide jemby

        show detective suspicious
        sc "It could be, but this looks an awful lot like he was strangled. By two hands, crushing his windpipe, 
            from the front."
        hide detective
        
        $ hasStrangulation = True

        show jemby
        trfc "Neat!"
        hide jemby

        show paramedic nonplussed
        parm "Neat?"
        hide paramedic

        show detective notes point
        sc "Now, down here - look at his wrist. A tan line for a watch - but no watch!"
        hide detective

        $ hasWatchTan = True

        show jemby
        trfc "So he wasn't wearing a watch when he died? You've cracked the case, Sherlock!"
        hide jemby

        show detective notes
        sc "Well, why wasn't he wearing it? It's worth noticing, at least."
        
        show detective notes point
        sc "He's wearing a wedding band - so, married - but why no watch?"

        show detective notes
        sc "I'm pretty sure you were right about this whole car crash being staged - people don't usually
                get strangled to death post-car-crash. It's just unsportsmanlike."

        sc "Oh, and what have we here?"
        hide detective

        "Detective Capilano pulls a hair off of the body."

        show detective hair
        sc "A hair? His hair is dark. This hair is... grey, it looks like. Curious."

        "Detective Capilano puts the hair in a plastic evidence baggie."
        hide detective

        $ hasHair = True
        
        show prop hair
        show yougot
        play music "music/I Got A Stick.mp3"
        yougot "A Gray Hair!"
        play music "music/Verano Sensual.mp3"
        hide yougot
        hide prop

        show detective sniff
        sc "Snif... snif..."

        sc "I know what that smell is!"

        sc "Hey, for our own safety, let's all back away from the car right now."
        hide detective

        show jemby
        trfc "Huh? Why's that?"
        hide jemby

        show detective concerned
        sc "That smell - I think that's kerosene. Someone's been pouring kerosene all over the backseat of this car."

        sc "It's not on fire now but I feel like the tiniest spark could get this whole thing going like a bonfire."
        hide detective
        
        scene bg car crash squad

    show detective notes point
    sc "Can you get the fire department? I think we'll need them before we continue."
    hide detective

    show jemby
    trfc "Oh, yeah, that's a good idea."
    hide jemby

    show detective notes
    "While he jogs to the police cruiser to call for the fire department, Detective Capilano and her 
        notepad angle around the car to get a look at the back."
    hide detective

    show prop notepad
    notepad "B9Z2M8"
    hide prop

    show detective notes
    sc "Let's see who that belongs to."
    hide detective

    "Detective Capilano wanders over to the police cruiser."

    show detective notes point
    sc "If you're done with the fire department, could you run these plates? It'd be good to know who the victim was."
    hide detective
    
    show jemby
    trfc "Way ahead of you. The car's driver, one Timothy Victrola, age 26. Ownership is registered to an Ann Portent,
        who I believe is his spouse."
    hide jemby

    show detective sheepish
    sc "If it's registered to Mrs. Portent, how did you know {i}his{/i} name?"
    hide detective

    show jemby wallet
    "The junior traffic cop holds up a wallet in a plastic bag."

    trfc "Before I thought it was a homicide investigation I nabbed his ID."
    hide jemby
    
    show detective
    sc "Good man. Let me take a look at that."
    hide detective

    show yougot
    show prop wallet
    play music "music/I Got A Stick.mp3"
    yougot "The victim's wallet!"
    hide prop
    hide yougot
    play music "music/Verano Sensual.mp3"

    show detective gloves
    sc "I have to put those gloves back on."
    play sound "sounds/snap.ogg"
    hide detective

    scene bg wallet
    "Fishing through the wallet, Detective Capilano finds condoms, a gym membership card, 
        a credit card, and some loose cash."
    $ hasCondoms = True
    $ hasGymMembership = True

    jump wallet
            
define lookedAtCondoms = False
define lookedAtGymMembership = False
define lookedAtCredit = False
define lookedAtMoney = False
label wallet:
    menu:
        "Look at the {b}Condoms{/b}" if not lookedAtCondoms:
            $ lookedAtCondoms = True
            show prop condoms
            sc "Condoms."
            notepad "Condoms' expiry date - far in the future. Bought fairly recently." 
            hide prop

            show detective sunglasses prep
            sc "It looks like somebody..."
            
            "She pauses, dramatically."
            hide detective

            show detective sunglasses
            sc "... planned to have sex with someone else."
            hide detective

            show prop condoms
            condoms "Yeaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaah!"
            hide prop
            jump wallet
        "Look at the {b}Gym Membership{/b}" if not lookedAtGymMembership:
            $ lookedAtGymMembership = True
            show prop gym membership
            play sound "sounds/casino/cardPlace1.ogg"
            "This is from the campus gym at Frances Dicken University."
            "\"Fitness Dicken U\""
            hide prop

            if hasBelt:
                show prop belt
                belt "Heheheheheh." 
                hide prop
                if hasBadge:
                    show prop badge
                    badge "Perv."
                    hide prop
            
            show prop gym membership
            sc "Gym membership. He seems in pretty good shape, I guess that tracks."
            play sound "sounds/casino/cardPlace1.ogg"
            show prop gym membership back
            "On the back of the gym membership card is a hastily scrawled {b}phone number{/b}."
            sc "Huh. Is this the number for the gym, maybe?"
            show prop gym membership
            "No, the number for the gym is listed on the membership card and it doesn't match."
            hide prop
            
            show detective suspicious
            sc "Maybe his wife? Curious."
            hide detective
            jump wallet
        "Look at the {b}Credit Card{/b}" if not lookedAtCredit:
            $ lookedAtCredit  = True
            play sound "sounds/casino/cardPlace2.ogg"

            show prop credit
            notepad "Matte black MisterCard, name: \"Timothy Victrola\" "
            notepad "Heavier than a usual credit card, might be made with actual metal."
            if hasBadge:
                badge "The name and account number are embossed on - this is necessary for the carbon-paper imprint machine   
                    used by retailers to be able to quickly copy the details on the card."
            sc "Wow, credit card."
            hide prop
            
            show jemby
            trfc "Must be a real fancy boy."
            hide jemby
            
            jump wallet
        "Look at the {b}Money{/b}" if not lookedAtMoney:
            $ lookedAtMoney = True
            show prop cash
            play sound "sounds/casino/cardFan1.ogg"
            notepad "Fairly significant wad, high-denomination bills."
            "Easily an entire rent payment for Detective Capilano, and more than most people
                    go casually walking around with."
            "Detective Capilano {i}reluctantly{/i} places the wad of bills into an evidence bag."
            hide prop
            jump wallet
        "Okay, that's done" if lookedAtGymMembership:
            jump beresford_2

label beresford_2:
    
    if isLate: 
        scene bg car crash fire 4
    else:
        scene bg car crash
    
    show jemby
    trfc "Learn anything useful from the wallet?"
    hide jemby

    show detective shrug
    sc "Not sure."

    sc "Ok! I'm just going to go poke around that alley."
    hide detective

    show jemby
    trfc "The alley over there?"
    hide jemby

    show detective
    sc "Yeah - I think you'd agree that if this car drove in a straight line from anywhere, it would have been
            from over there, right?"
    hide detective

    show jemby
    trfc "Yup. What are you looking for?"
    hide jemby

    show detective
    sc "I'll know it when I see it."
    hide detective

    jump alley

label alley: 
    
    scene bg alley
    
    "This dingy alley is lined with garbage cans and back entrances to various retail outlets. "
    
    play music "music/Grand Dark Waltz Trio Allegro.mp3"

    if hasBadge:
        show prop badge
        badge "No sign of life, here - whoever staged this car crash is long gone."
        hide prop

    if hasCigarettes:
        show prop cigarettes
        cigarettes "Hey, you're alone in an alley. Smoke one of us."
        sc "Not right now."
        cigarettes "Come on. You've been doing great. You deserve one."
        sc "... ok, sure."
        "Detective Capilano lights a cigarette."
        cigarettes "Talk to you again in ten minutes, buddy."
        hide prop

    "There's a fairly prominent dumpster that would be the obvious receptacle for any large and/or incriminating trash."

    menu:
        "Poke around in the dumpster.":
            jump dumpster
        "Obviously, you should poke around in that dumpster.":
            jump dumpster
        "Dumpster! Dumpster! Dumpster!":
            jump dumpster
        "> USE INVESTIGATE ON DUMPSTER":
            jump dumpster
        "Don't - don't {i}not{/i} investigate that dumpster":
            jump dumpster
        "Inspectaroo that dumpsterino":
            jump dumpster
        "Look, this isn't a real choice, there's no way Detective Capilano isn't going to go poking around in that dumpster for sweet sweet clue nuggets.":
            jump dumpster

label dumpster:
    sc "I mean, of course I'm going to look in that dumpster."

    scene bg alley oop

    "Opening the lid, Detective Capilano is hit by a powerful wave of pungent kerosene fumes."

    show detective sniff
    sc "Woof."
    hide detective 

    "It's not like dumpsters usually smell like roses, but this has absolutely a different kind of pungent, 
        gas-station stank to the \"rotting food funk\" that she expected."

    "There are two large cans of kerosene sitting in the dumpster."

    sc "Someone really wanted that car to go up in flames. I hope that the fire department get that scene under control."

    if not isLate:
        sc " - at least, before something terrible happens."

        play sound "sounds/explosion.ogg"
        with vpunch
        with hpunch
        "Detective Capilano hears the distant sound of an explosion."
        
        $ carExploded = True

        sc "... aw, shit."

    "Detective Capilano fishes a kerosene can out of the dumpster with her gloves."

    sc "No way we're gonna pull any prints off this thing."

    sc "... I bet whoever doused the car just {i}stank{/i} of kerosene afterwards."
    
    sc "But there's no way they'd be stupid enough to take their clothes off and throw them in this same dumpster, right?"

    "There's only one way to find out."

    "Detective Susan Capilano, looking unhappy about the choice she's about to make, hops in the dumpster to start rooting around."
    
    play sound "sounds/dumpster.ogg"
    sc "Alley... oop!"

    if hasBadge:
        badge "It's not proper police work without at least one good dumpster dive."
        badge "Detective Susan Capilano has a lot of scars from the line of duty, and a surprising number of them 
                    are not from scuffles or fights, but from activities just like this. Lots of broken glass in dumpsters."
    
    "Detective Capilano digs through the trash."
    "This is incredibly tedious, and we're going to skip by minutes of exciting trash sifting, but
        to help establish how irritating this is for the detective, I'm gonna monologue unnecesarily for a bit."
    "What to monologue about?"
    "Hey, let's talk about this game. Did you know that it contains over 200 hand-drawn images?"
    "I've been working on it in my spare time for more than two months. Simple as it may seem, a lot of slow and boring work
        went into this game."
    "Not boring like \"sifting through trash at a crime scene\", mind you."
    "I could have been playing Cities Skylines, but instead, here I am, making a pretty forgettable mystery game."
    "Hey, if you like it, let me know! It would mean a lot to me. At least I wouldn't feel like I wasted my time."
    "If you don't like it, let me know anyways. I'm really just looking for some kind of proof that someone interacted with the game at all."

    "Anyways, that's been enough time. The Detective has thoroughly been through this trash and there's not a clue to be had in here. There's nothing else in this dumpster but trash."

    if hasBelt:
        "There's a fire exit hanging above the dumpster, but Detective Capilano is just a little
            bit too short to climb up there."

        sc "If I had something long and rope-like, I could loop it around that ladder and pull it down."

        show prop belt
        belt "Oh! Oh! Let me be at your service, madame! I can be of assistance!"

        sc "Okay, pants, I need you to hold for just a moment while I do something clever with this belt."

        belt "We both know that the pants are too cotton-headed to speak."

        sc "I still don't always get the logic around which objects talk and which ones don't."

        belt "It's maddeningly inconsistent!"

        "Detective Capilano removes her belt. Hopping and flicking it up, she manages to catch it on the
            pull-down ladder."

        "She pulls the ladder down to the ground and climbs to the top, looking around the fire exit for
            clues."

        belt "Do not forget to reattach me to your beautiful waist."
        hide prop

        sc "Gross."
        
        $ hasDressShirt = True

    elif isHydrated:
        "Detective Capilano could use a bathroom break. One of these alleyway doors must lead into a restaurant 
            or a drug-store or something with a bathroom."
        
        sc "This is why I don't drink {i}water{/i}."

        "Detective Capilano tries some knobs and opens the only unlocked door in the alley."

        scene bg chili restaurant
        "It leads into the back of a small chili restaurant."

        sc "A whole restaurant, just for chili?"

        "The restaurant is busy with patrons, each of them holding steaming bowls of chili in 
            what appear to be bread bowls. There's a stack of take-out menus near the back
            door."
        
        "Detective Capilano notes that the chili is also very reasonably priced, especially
            for a lunch in the city."
        
        "The smell of fresh baked bread and spicy meat is in the air."

        sc "Okay, I guess I can kinda see the appeal."

        if hasBadge:
            show prop badge
            badge "At this point Detective Capilano puts two and two together, and comes to an awful realization
                    about the potential state of the bathroom in this restaurant."        
            hide prop
        if hasBelt:
            show prop belt
            belt "That bathroom is going to be so, so gross."
            hide prop

        "Nature calls, though - she'll have to brave it. She was just rooting around in a dumpster, 
            this won't be too bad."

        sc "Once more, in to the breach."

        play sound "sounds/flush.ogg"
        "(bathroom-using sound effects)"
                
        "Washing her hands, Detective Capilano notices something unusual poking out of the bathroom's
            trash can." 
        
        $ hasDressShirt = True

    else:
        "Welp."
        
    if hasDressShirt:
        sc "Huh, would you look at this?"

        show prop dress shirt
        "Detective Capilano has found a men's dress shirt, soaked in kerosene."

        notepad "Soaked in kerosene. Murderer? Victim?"
        notepad "Hand-tailored, white and blue herringbone cotton weave, clearly expensive."
        notepad "Starched collar, for a large man."
        notepad "French cuff, no cufflinks."

        dressshirt "Hi!"

        sc "Who do you belong to?"

        dressshirt "A man!"

        sc "Could you tell me what happened to you earlier today?"

        dressshirt "I don't know! I'm just a shirt! I have stinky water in me!"
            
        "A lot of objects are too stupid to be helpful in murder investigations."

        sc "Did you... see a murder? Did someone kill someone that you saw?"

        dressshirt "What's {i}murder{/i}? Is it a kind of fabric? Like chiffon?"
        hide prop

        if hasBelt: 
            show prop belt
            belt "I think I can get through to it. You know, I've spoken to some clothes in my time."

            sc "Sure, give it a shot."

            belt "Hey, was your enrobant involved in a tearing?"

            show prop dress shirt
            dressshirt "Yeah! My enrobant got to be a scarf! For a man wearing soft cotton!"

            sc "A scarf?"

            show prop belt
            belt "You know, wrapped around the neck?"
            
            show prop dress shirt
            dressshirt "He was such a nice tight scarf that the soft cotton man laundrypiled."

            if not hasStrangulation:
                notepad "Strangulation."
                $ hasStrangulation = True
            else:
                notepad "Circles around \"strangulation\"."
            hide prop

        if hasBelt: 
            show prop notepad
            notepad "Able to get up to fire escape. Very tall? Very agile?"
            hide prop

    if isHydrated and not hasBelt:
        "The Detective wanders further into the restaurant, holding the shirt in her hands."

        show big chili henk
        bch "Hey - can I help you?"
        hide big

        show detective smug
        sc "I just wanted to start by telling you - chili restaurant - incredible idea."
        hide detective

        show detective sniff
        sc "The smell in here - incredible! And - is that fresh baked bread?"
        hide detective

        show big chili henk
        bch "Yeah, we bake our bowls every morning. Sourdough."
        hide big

        if hasBadge:
            # she should... always have her badge, because you need the badge to GET HYDRATED
            # but, hey, I could add more hydration options in the early game, so this gets an "if"
            show prop badge
            "The Detective takes a moment to show off her badge."
            sc "I'm Detective Susan Capilano with the Northwestica Police Department."
            hide prop

        show detective deflated
        sc "I found this shirt in the bathroom - I was wondering if you had seen anybody come through
                wearing this shirt."

        sc "Or, shirtless, I guess?"
        
        sc "Or someone who rushed out of here rapidly from the back door?"
        
        sc "Big guy?"
        hide detective

        show big chili henk
        bch "I'm sorry, the only thing out of the ordinary today is a big car fire happening right out the front door."
        hide big 

        if hasGun:
            show prop gun
            gun "A likely story. Maybe a little bit of vitamin \"bullet to the face\" would convince him."
            hide prop
            menu: 
                "Murder the chili-vendor in cold blood to establish dominance":
                    if hasCueBall:
                        show prop cueball
                        cb "You can't. That's not how this goes."
                        hide prop
                        "Detective Capilano changes her mind."
                    else:
                        jump shooting_game_over                
                "He can live.":
                    show prop gun
                    gun "I swear, you could not be a bigger pussy if you tried."
                    hide prop

        show big chili henk
        bch "Is this about that big car fire happening out front?"
        hide big

        show detective faceplam
        sc "Yes. Yes it is."
        hide detective

        show detective umbrella 
        sc "While I'm here, can I get a #5, to go?"
        hide detective

        show big chili henk
        bch "Of course."
        hide big

        $ hasChili = True
        "Detective Capilano heads out of the restaurant, chili order and dress shirt in hand, and back in to the alley."
        scene bg alley oop
    
    "Well, that's about all of the exploration that this alley has to offer... except, one thing."

    jump stick_menu

label stick_menu:
    
    scene bg alley oop
    
    show prop stick
    "Propped up near the dumpster door is a wooden stick. "
    
    "Even from here, Detective Capilano can tell that this stick has absolutely no bearing on the case."

    menu:
        "Get worthless stick":
            "Is Detective Capilano sure about that? I assure you that this stick has nothing of value
                to offer this case. It's just a stick."
            menu:
                "I mean it, get that worthless stick":
                    "Okay, but I'm warning you: I'm going to make you sit through something long and stupid
                        and this stick is not going to benefit you at all."
                    menu:
                        "Stick. Now.":
                            jump stick
                        "Ignore worthless stick":
                            jump alley_done
                "Ignore worthless stick":
                    jump alley_done
        "Ignore worthless stick":
            hide prop
            jump alley_done

label stick:

    play music "music/I Got A Stick Feat James Gavins.mp3"
    show yougot

    yougot "A stick!"

    yougot "Oh yeah! You got a stick!"

    yougot "A really, really useless stick!"

    hide yougot
    hide prop

    play music "music/Grand Dark Waltz Trio Allegro.mp3"

    jump alley_done

label alley_done:
    "Detective Capilano is satisfied that she's explored this alleyway to its fullest."

    "That's good, after spending all of this time in the rain, she's completely soaked."

    "She heads back to Junior Officer Jemby's squad car - she has to make a phone call and set up
        her next move."

label ann_office:
    # rain's quieter, we're indoors
    stop music
    play ambient "ambient/rain_smaller.ogg" volume 0.3
    play ambient_2 "ambient/office.ogg"    
    
    scene bg ann building

    "An imposing financial building, downtown."

    scene bg ann office

    "Detective Capilano walks into an office."
    
    "The office desk is enormous, a solid mass of expensive-looking wood. Behind the desk are a variety of 
        well-maintained exotic plants and a number of CRT television displays."
    
    "Sitting on the desk are three modern-looking telephones."

    play music "music/Ethernight Club.mp3"
    
    show ann
    "The woman sitting at the desk is in her fifties, a thin, stern, angular looking woman in an immaculate
        high-collared dress. This woman looks like she's made of iron."

    "Detective Capilano is a little surprised at the obvious and significant age difference between Ann 
        and her husband, the victim: it might more more than a 20 year age gap between the two."
    
    annp "You are soaking wet. Don't stand on the rug, please, it's a genuine Calypsan."
    hide ann

    show detective damp
    sc "Oh, I'm sorry."
    hide detective

    if not hasCueBall:
        show ann disgust
        annp "And... your smell. Well, I suppose you can't do anything about that, but you must understand
                that you smell of gasoline and garbage."
        hide ann
            
        show detective deflated
        sc "Actually, kerosene and dumpster, ma'am. It's been a busy afternoon."
        hide detective

    if hasBike:
        play sound "sounds/bike.ogg"
        show ann
        annp "My security team tells me that you parked a children's bicycle outside, and that you were in a hurry 
                to speak with me."
        hide ann
    else:
        show ann
        annp "My security team tells me that you are in a hurry to speak with me."
        hide ann

    show detective
    sc "I'm Detective Susan Capilano, with the Northwestica Police Department."
    hide detective

    if hasBadge:
        "She takes a moment to flash her badge, adding some credulity to her statement."    
        badge "Bonjour."

    show ann hand
    annp "I know. You wouldn't have been allowed entrance if we didn't know exactly who you were, of course."

    show ann
    annp "Ann Portent, acting CEO of Megamax News."
    hide ann

    show detective hand up
    sc "Nice to meet you."
    hide detective

    show ann
    annp "I'm sure that it is. May I ask what, {i}exactly{/i} the problem is?"
    hide ann
    
    show detective somber
    "Detective Capilano adopts a look that is both serious and morose, the Bad News Look that police officers
        have to learn."

    sc "This is going to be difficult, but - is this your husband? Timothy Victrola?"

    show detective somber id
    "Detective Capilano hands Mrs. Portent a plastic bag containing the ID from the crime scene."
    hide detective

    show ann
    annp "Yes, that's my Tim."
    hide ann

    show detective somber
    sc "I'm... sorry to have to tell you this, but he's been found, dead, this morning."
    hide detective

    show ann shock
    annp "And you're ... sure it was him?"
    hide ann

    show detective somber
    sc "We'll need you to identify the body but we're pretty certain that it was, indeed, him."
    hide detective

    show ann sad
    "Ann Portent has a demeanor as cold and professional as hardened steel, but this visibly rattles
        her, if just for a moment."
    hide ann
    
    show detective somber
    sc "I'm sorry."
    hide detective

    show ann shock
    annp "But... he was so young! What happened?"
    hide ann

    show detective somber
    sc "He was found dead in his car this morning, in an event that was clearly staged to look like a car crash."
    sc "We have reason to believe that this may have been a homicide."
    hide detective
    
    show ann angry
    annp "Ah, so then would I be right to assume that you are a homicide detective for the city?  
            And you have some questions for me?"
    hide ann

    if hasCueBall:
        show prop cueball
        cb "You don't need her to answer any questions. I will answer any questions you have."
        hide prop

        show detective somber
        sc "I actually don't have any questions for you. I was just here to let you know that I'll 
                be investigating the case, and I'll stay in touch."
        hide detective
        
        jump ann_problems
    else: 
        show detective somber
        sc "Yes. Very sharp, Mrs. Portent."
        hide detective

        show ann hand
        annp "Well, I'm an open book."
        hide ann

    jump ann_questions

define askedWhereabouts = False
define askedAlibi = False
define askedAgeDifference = False
define askedPhoneNumber = False
define askedCondoms = False
define askedHair = False
define askedFinances = False
define askedFidelity = False
define askedStrength = False
define askedDressShirt = False
define askedWatchTan = False
define askedGym = False

label ann_questions:

    menu: 
        "Ask about {b}Whereabouts{/b}" if not askedWhereabouts:
            $ askedWhereabouts = True
            show detective notes
            sc "When was the last time you saw your husband?"
            hide detective

            show ann
            annp "Early this morning, we had breakfast together. This would have been at - 6AM?"
            hide ann

            show detective notes point
            sc "Early."
            hide detective notes

            show ann
            annp "We had smoothies together. Tim said that he had \"something to take care of\" which,     
                    in retrospect, seems kind of ominous. I left for work."

            annp "If you check with the gateman at our home, he'll be able to verify that I left for work
                    after breakfast."
            
            annp "Presumably Tim left after I did. The gateman should be able to let you know what time that
                    happened, as well."

            annp "Tim would hit the gym after breakfast most mornings."
            hide ann

            show detective notes
            sc "And what did {i}you{/i} do after that?"
            hide detective

            show ann hand
            annp "I've spent the whole morning at work. You can confirm that with my secretary, should you wish,
                    she's been with me the entire time."
            hide ann

            jump ann_questions
        
        "Ask about {b}Alibi{/b}" if not askedAlibi and askedWhereabouts:
            $ askedAlibi = True

            show detective notes
            sc "So, you're saying that your gateman saw you while Tim was verifiably still alive - "

            show detective notes point
            sc "And you have people who can vouch for your whereabouts the rest of the day."
            hide detective
            

            show ann
            annp "Yes."
            hide ann

            show detective notes
            sc "If I were trying to build a case against you, Mrs. Portent - and I assure you, I'm not -
                    that would make it very difficult."
            hide detective
            
            show ann
            annp "...ok. Well, I'm glad that's settled."
            hide ann

            show prop notepad
            notepad "... concrete alibi."
            hide prop

            jump ann_questions

        "Ask about the {b}Age Difference{/b}" if not askedAgeDifference:
            $ askedAgeDifference = True

            show detective notes
            sc "I don't mean to pry, but there's a fairly significant age difference between you and your husband."
            hide detective

            show ann
            annp "Oh, yes."

            annp "Something about age differences like ours - people somehow think that we don't notice it, or that
                    it's somehow taboo to bring up with us, but it's not like we aren't painfully aware of how
                    it comes off."
            
            annp "Sometimes we'll be out having dinner and the waiter will think he's my {i}son{/i}."

            annp "The long and the short of it is - we have good rapport. I mean - obviously he likes the financial 
                    stability, the incredible vacations, the nice clothing - but I also feel like the two
                    of us have a lot of fun together."
            
            annp "I like his optimism, his boundless enthusiasm, he's got a way of looking at the world that makes
                    it feel brand new, and I can feel that with him."
            
            show ann hand
            annp "And it's rare to find a man who isn't a little
                    bit threatened by {i}all this{/i}. He's impressed! Supportive!" # she says, gesturing around
            
            annp "You know, there are men you can be vulnerable with, and men you can be {i}invulnerable{/i} with,
                    and with him it felt like a bit of both."

            show ann dirty
            annp "And there's genuine sexual chemistry - something about men my age, they're a bit {i}tired out{/i},
                    if you know what I mean."
            hide ann
            
            show detective irritated
            "Susan Capilano is happy to report that she does not know what Ann means."
            hide detective
            
            show prop notepad
            notepad "Ann {i}does{/i} seem genuinely quite fond of her husband."
            hide prop

            jump ann_questions
        "Ask about {b}Phone Number{/b}" if not askedPhoneNumber:
            $ askedPhoneNumber = True
            show detective somber id
            "Detective Capilano shows Ann the phone number on the back of Timothy's gym membership."

            sc "Have you ever seen this phone number? Or this handwriting?"
            hide detective

            show ann angry
            annp "No, that's not one of mine."
            hide ann

            jump ann_questions
        "Ask about the {b}Condoms{/b}" if askedAgeDifference and hasCondoms and not askedCondoms:
            $ askedCondoms = True

            show detective notes
            sc "This is going to seem incredibly personal and not terribly appropriate, but I promise that
                    it's relevant: did you and Mr. Victrola use contraception?"
            hide detective

            show ann disgust            
            annp "I ... really don't see how that's any of your business, but no."

            show ann sad
            annp "At this point in my life a child is increasingly unlikely - and if it {i}did{/i} happen,     
                    well, that would be a blessing, not a curse."
            
            show ann
            annp "We'd even been talking about some of the more esoteric options like adoption or
                    in-vitro fertilization if things didn't... coalesce, in the next few years."
            hide ann
            
            show prop notepad
            notepad "Curious. Why would Timothy have freshly-purchased condoms in his wallet, then?"
            hide prop

            jump ann_questions

        "Ask about the {b}Grey Hair{/b}" if hasHair and not askedHair:
            $ askedHair = True
            show detective smug
            sc "This isn't about the case, but - just between you and me - you know, my wife - 
                    beautiful woman - but vain - she's starting to complain that my 
                    old salt and pepper mop ages me."

            "Detective Capilano is unmarried. This wife is nothing more than a ruse to extract information."

            sc "You're so put together, I was wondering if you might have some tips on hair color I could use."
            hide detective

            show ann
            annp "Oh, my - I didn't want to comment on your hair - but, if your wife brought it up - "
            annp "Your hair is a complete disaster - rat's nest, visible greys, split ends, the works."

            show ann hand
            "Mrs. Portent produces, as if by magic, a business card, and hands it to Detective Capilano."

            show ann
            annp "This is my colorist and stylist, Sseven - they're a little bit on the pricier side but they are
                    an absolute miracle-worker. I've been completely grey for years and they always do an 
                    incredible job."

            annp "They're usually booked - months ahead of time - but I think if you were to visit their salon,
                    they'd make a special exception for you. You know - emergency, and all."
            hide ann

            if hasCarKeys:
                show prop carkeys
                carkeys "Sseven can go pound dirt."
                hide prop
            
            if hasBelt:
                show prop belt
                belt "Blasphemy! Ms. Capilano is stunning with her natural hair color!"
                hide prop

            if hasBadge:
                show prop badge
                badge "The grey in your hair makes you look distinguished!"
                hide prop
            
            show prop notepad
            notepad "Ann {i}could{/i} be source of gray hair."
            hide prop
            
            jump ann_questions

        "Ask about {b}Finances{/b}" if not askedFinances:
            $ askedFinances = True
            show detective notes
            sc "You seem to be doing pretty well for yourself."
            hide detective

            show ann
            annp "Oh, very. News is a booming industry, Detective Capilano."
            hide ann

            show detective notes point
            sc "In cases of marriages of, uh, wildly differing means - uh, what I'm trying to say is,   
                    if your relationship with Mr. Victrola were to end acrimoniously - "
            hide detective
            
            show ann
            annp "I see what you're getting at, Detective Capilano - a relationship on the rocks and I'm
                    offing my husband to protect my fortune?"
                    
            show ann hand
            annp "The thing is, though, I have excellent lawyers and an
                    ironclad prenuptual agreement. Worst-case scenario in a divorce, Tim walks away     
                    with a nice beach house and I'm no more than {i}slightly inconvenienced{/i}."
            
            annp "Best-case scenario - say, for example, infidelity from my young husband - well, Tim would have nothing
                    left to his name but the clothes on his back."
            
            annp "If anything, the way our marriage was set up, you'd expect to find {i}me{/i} mysteriously
                    washing up the river - he stood to inherit quite a fortune in that case."
            hide ann
            
            show prop notepad
            notepad "No clear financial incentive."
            hide prop
            
            jump ann_questions
        "Ask about {b}Fidelity{/b}" if not askedFidelity:
            $ askedFidelity = True
            show detective notes
            sc "This is just a standard question that we ask in homicide cases involving couples, but, would
                    you have any reason to believe that your husband might be {i}cheating{/i} on you?"
            hide detective
            
            show ann
            annp "Absolutely out of the question. I know, beyond a shadow of a doubt, that Tim could not possibly 
                    be cheating on me."
            hide ann
            
            show detective notes point
            sc "Oh? I ask this question fairly often and I {i}rarely{/i} hear anybody {i}that{/i} certain."
            hide detective

            show ann
            annp "I'd prefer not to go into the details, but I am 100 percent confident that we're {b}in the clear{/b} 
                    on that matter."
            hide ann

            show prop notepad
            notepad "Curious. Fidelity could {i}easily{/i} be called into question."
            notepad "Why so sure that Timothy was {b}in the clear{/b}?"
            hide prop

            jump ann_questions
        "Ask about {b}Strength{/b}" if hasStrangulation and not askedStrength:
            $ askedStrength = True
            show detective notes
            sc "Grief is a tough process, but do you know what always helps me navigate it?"
            hide detective

            play music "music/Farting Around.mp3"
            show detective armwrestle
            sc "A friendly bout of arm wrestling."
            hide detective

            show ann armwrestle
            annp "You're on, noodle-arms."
            hide ann

            with hpunch
            show detective armwrestle
            sc "HNNNNNNNGH"
            hide detective

            with hpunch
            show ann armwrestle
            annp "HNNNNNNGHGHG"
            hide ann

            with hpunch
            show detective armwrestle
            sc "HNNNGGHGHGHGHGG"
            hide detective

            with hpunch
            show ann armwrestle
            annp "HNNNNGGHGHG"
            hide ann
            
            with hpunch
            show detective armwrestle
            sc "HNNNGGHGHGHGHGGGHGHGHG"
            hide detective

            show ann armwrestle
            annp "HNNGG"
            hide ann

            show detective wave
            sc "Ha ha! I win!"
            hide detective
                
            show detective_victory
            play sound "sounds/airhorn.ogg"
            "Detective Capilano's victory dance is a little bit too long and aggressive."

            if hasBadge: 
                show detective_victory
                play sound "sounds/airhorn.ogg"
                badge "Detective Capilano."
                play sound "sounds/airhorn.ogg"
                badge "Detective Capilano, stop!"
                play sound "sounds/airhorn.ogg"
                badge "Stop this right now Detective Capilano!"
                play sound "sounds/airhorn.ogg"
                badge "Okay, aside from brutally dunking on a grieving widow, what have we accomplished, here?"

            hide detective_victory

            show prop notepad
            notepad "Not strong enough to strangle Timothy to death."
            hide prop

            if askedAlibi:
                if hasBadge:
                    show prop badge
                    badge "We already have an alibi for her - doesn't this seem needlessly thorough?"
                    hide prop
                show prop notepad
                notepad "Also fun to arm wrestle."
                hide prop
            
            play music "music/Ethernight Club.mp3"
            
            jump ann_questions
        "Ask about {b}Dress Shirt{/b}" if hasDressShirt and not askedDressShirt:
            $ askedDressShirt = True

            show detective notes
            sc "What was Tim wearing when you saw him this morning?"
            hide detective

            show ann
            annp "A baby-blue Yuyuyuzu track-suit, over a plain white undershirt."
            hide ann

            show detective notes confused
            sc "Yuyuyuzu?"
            hide detective

            show ann
            annp "Soft, comfortable, high-end athletic clothing for housewives, househusbands 
                and the business-averse."
            hide ann

            if hasBelt:
                show prop belt
                belt "Gross. Timothy could have died with some {i}style{/i}. A nice belt and some slacks, maybe."
                belt "Ask her about the dress shirt we found!"
                hide prop

            show detective notes
            sc "Was he fond of formal-wear?"
            hide detective

            show ann
            annp "Oh, no. I've had some lovely shirts and suits made for him, but aside from dates and 
                special occasions, I don't think I've ever seen him wear them."
            hide ann

            show detective notes
            sc "When you had shirts made for him - were there any details that would identify those
                    clothes as uniquely his?"
            hide detective

            show ann hand
            annp "Yes, actually - he had a long torso and short arms, so all of his shirts have their
                    arms taken in. I have that done with a lot of his shirts, actually - he looks like
                    a toddler when his shirt arms are too long."
            hide ann

            show prop dress shirt
            "Between those two details, Detective Capilano thinks that she can rule out Tim as 
                the owner of the shirt she found in the alleyway."
            hide prop

            jump ann_questions
        "Ask about {b}Watch{/b}" if hasWatchTan and not askedWatchTan:
            $ askedWatchTan = True

            show detective notes
            sc "Did Timothy wear a watch?"
            hide detective

            show ann
            annp "Oh, yes. As a wedding gift I bought him a Painblanc Sub-Mariner with a military strap 
                    and a sapphire bezel, with our names engraved on the back. He hasn't taken it off,
                    since."

            annp "I think he showers with it on. He was wearing it this morning, I'm sure."
            hide ann

            if not hasBelt:
                show detective notes confused
                sc "A ... Paulblart Submarine? I'm not familiar with that brand of watch. I'm not a watch enthusiast -"
                hide detective

                show ann
                annp "Horologist"
                hide ann

                show detective notes confused
                sc "I'm not a, uh, fortune teller, either."
                hide detective

                show ann
                annp "No, a horologist is a fan of {i}watches{/i}."
                hide ann

                show detective notes confused
                sc "{i}Which{/i} horologist is a fan of watches?"
                hide detective

                show ann idiot
                annp "{b}All of them{/b}."
                hide ann

                show detective notes
                sc "Well, that's a strange coincidence."

                sc "Anyhow, as I was saying - not familiar with a Paulblart Submarine - is it a very expensive watch?"
                hide detective

                show ann
                annp "Well, that's a relative question."

                show ann hand
                annp "I think a Painblanc Sub-Mariner might cost about as much as a small commuter sedan? 
                        But no, in the grand scale of watches
                        it's not an unusually expensive one."
                hide ann
            else: 
                show prop belt
                belt "A Painblanc Sub-Mariner? That's an unbelievably expensive watch."

                belt "This lady has incredible style. Can you... leave me with her?"
                hide prop

            jump ann_questions

        "Ask about {b}Gym{/b}" if askedWhereabouts and not askedGym:
            $ askedGym = True

            show detective notes
            sc "You said that Tim goes to the gym most mornings?"
            hide detective

            show ann
            annp "Yes, the Frances Dicken University gym. "
            hide ann

            show detective notes point
            sc "Is he a student there?"
            hide detective

            show ann
            annp "Not currently - he finished his Master's in Fine Arts last year - but that's still
                    one of the closer, nicer gyms near us."
            hide ann
            
            show detective notes
            sc "I'm sure with your resources you could put a gym in your own home."
            hide detective

            show ann
            annp "There's a rock-climbing wall at the gym - you need a partner for that. Plus, he likes
                    having an excuse to hang out at the university, even after his graduation. 
                    Lots of friends there."
            hide ann
            
            show detective notes point
            sc "Friends, you say? I'm going to want to interview some of them about all of this, if you
                    could tell me anything about them."
            hide detective
            
            show ann
            annp "Well, there's his personal trainer - red-haired fellow. Fiery temper. I think his name's
                    {b}Pat, or Patty or Petey or something{/b}. Tim talks about him all of the time - really gets him
                    fired up."
            hide ann
            
            show ann disgust
            annp "Then, there's his climbing instructor, {b}Becky{/b}."

            "She says the name {i}Becky{/i} with the kind of cold iciness one would reserve for a
                bitter rival."
            
            show ann
            annp "Becky with the good hair. Tim doesn't talk about her at all - I had to find out about
                    her on my own."
            hide ann
            
            if askedFidelity:
                show detective notes point
                sc "You mentioned, earlier, how confident you were that Tim {i}isn't{/i} cheating on you."
                hide detective

                show ann
                annp "They are {i}simply climbing partners{/i}, I'm certain."
                hide ann
            
            show detective notes
            sc "So would you say you were {i}concerned{/i} about their close relationship?"
            hide detective

            show ann hand
            annp "Yes, but I managed to overcome it."
            hide ann

            show prop notepad
            notepad "How did Ann get over her jealousy about Becky?"
            hide prop
            
            jump ann_questions
        "Okay, that's enough questions." if askedFidelity and askedGym and askedWatchTan:
            show ann
            annp "Wonderful."
            hide ann

            jump ann_problems

label ann_problems:

    show ann
    annp "If you'll give me just a moment to use the ladies' room."
    hide ann

    "Mrs. Portent retreats, briefly, to her executive bathroom."

    play sound "sounds/cry.ogg"
    "The sound isolation in her office is very good, but despite all of it you can hear from the other room
        a howl of rage, and sadness, followed by some soft sobbing. Then, a short pause."
    stop sound
    
    show ann mussed
    "Mrs. Portent returns to the room, as calm, cool, and composed as she has been this entire time.
        Her eyes are a touch redder, but her makeup remains crisp and perfect."

    annp "Now, Detective Capilano - I'm sure you'll agree that getting to the crux of this matter is 
            of the utmost importance."
    
    show ann angry
    annp "If I find out who did this I'm going to - "

    show ann dirty
    # composure
    annp "If I find out who did this I'm going to promptly report them to the police, of course."
    hide ann
    
    if hasBadge: 
        show prop badge
        badge "She wants {i}blood{/i} and she has significant resources. 
                    When you find the killer, it might be wise to consider protective custody."
        hide prop

    show ann mussed
    annp "But - for my own peace of mind - I have a private security company that I'd like you to work
            with while addressing this case."
    hide ann
    
    if hasCueBall:
        show prop cueball
        cb "This is Hank Maxhank's company. You'll need to pretend that you don't want her to 
                ask him to join the case."
        hide prop

    show ann mussed
    annp "While I'm sure that the police department has {i}ample{/i} resources for every high-profile 
            homicide that comes along, a little extra muscle wouldn't hurt."
    hide ann

    if hasBike:
        show ann mussed
        annp "You did, I'll note, cruise up to my office in a Twillmann KidBike."
        hide ann

        play sound "sounds/bike.ogg"
        show detective sheepish
        sc "Actually, it's a Tonko L'il Funboy."
        hide detective

        show ann mussed
        annp "And that's... better?"
        hide ann

        show detective sheepish
        sc "They're actually quite a bit cheaper. Twillmann is a luxury brand for white collar families. 
                Fenders, brakes, they've got the whole package. Now, a Tonko, that's just 
                a clump of steel bars hastily welded together and painted a bright color."
        hide detective
        
        show ann hand
        annp "My point."
        hide ann
    else:
        show ann hand
        annp "You did, I'll note, cruise up to my office damp and smelling of kerosene and trash."
        hide ann
    
    show detective irritated
    sc "The Northwestica Police Department is usually fairly resistant to, uh, outside involvement in our cases?"
    hide detective

    show ann mussed
    annp "Balderdash. I'll speak to your chief. I'm sure that the prospect of having the most prominent news outlet   
            in the city covering this case {i}sympathetically{/i} will be enough to {i}move the needle{/i}."
    hide ann

    show detective irritated
    sc "I'd really prefer if you didn't - I have a {i}method{/i} for cases and I tend to prefer to work 
            alone. If you wouldn't mind."
    hide detective
    
    show ann mussed
    annp "I {b}would{/b} mind. My man is absolutely the {b}best private detective in the business{/b}, and his company, 
            Black Swan Securitas, has been in close partnership with our news agency for some time."
    hide ann

    if hasCarKeys:
        show prop carkeys
        carkeys "I'd like to propose a close partnership with my whole ass."
        hide prop

    show detective irritated
    "She's not going to drop this. Detective Capilano may have to work with an independent security company. Eugh."
    hide detective
    
    if hasGun and not hasCueBall:
        show prop gun
        gun "How dare you question us! We have a {b}process.{/b}. Shoot her. Shoot her {b}now{/b}."
        hide prop
        menu: 
            "Ann Portent must die.":
                jump shooting_game_over                
            "Don't kill her quite yet.":
                gun "This case is turning out to be so boring. If you don't shoot someone soon I'm going to go off in your jacket or something."

    show ann mussed
    annp "If you'll wait in the lobby, I'll have my man over in the next half an hour. With a {i}car{/i}."

    annp "I'll tell him to look for you downstairs. We're done, here."
    hide ann

    if not hasCueBall:
        show detective faceplam
        sc "Oh, if I may ask - is there a phone in the lobby that I can use? I have a few calls of my own to make."
        hide detective

        show ann mussed
        annp "There's a bank of payphones near the entrance."
        hide ann

    show ann mussed
    annp "Oh - and just one more thing."
    hide ann
        
    show detective
    sc "Yes?"
    hide detective

    # rage
    show ann angry
    annp "If I find out that you're not co-operating with my man, or if you don't have a head for me inside of a week?    
            I will {b}end{/b} you, Detective Capilano. Your career will be {i}over{/i}."
    
    "This is absolutely grief talking, but it's a credible threat nevertheless."

    # rage and sadness
    if hasBike:
        show ann sad
        annp "I'll even find a way to take your ... stupid... little... bike - "

    "She's having trouble getting through this next threat. The weight of what's happened to her is starting to hit."

    show ann tears
    annp "I - can't - you - "
    hide ann

    show detective suspicious
    sc "I'll, uh, let myself out."
    hide detective

    if hasCueBall:
        jump introducing_hank
    else:
        jump lobby

label lobby:
    
    scene bg default

    "Detective Capilano walks down the hallway, headed for the payphones."

    # serious pensive music
    play music "music/Sincerely.mp3"
    if hasCigarettes:
        show prop cigarettes
        cigarettes "We're terrible for you, but we're great for building dramatic tension."
        hide prop

        show detective pensive cigarette
        "Detective Capilano takes a moment to have a break with one of her cigarettes."
    else: 
        show detective_looking
        "Detective Capilano fumbles around in her pants for a cigarette, but she forgot to bring them."
        "To be honest, it was really going to add some gravitas to this moment."
        hide detective_looking
        if hasGum:
            show detective pensive gum
            play sound "sounds/pop.ogg"
            "Instead she's just going to have a pensive gum moment. Gum. What kind of detective story has a gum moment?"
        else:
            show detective pensive
            "Instead she's just going to have a regular pensive moment, without a halo of cigarette smoke
                to drive home the dramatic pathos."

    "This is the part of the job that Detective Capilano is most uncomfortable with."

    "Puzzle-solving, clue gathering, dumpster diving? She is a natural."

    "But when it comes to helping people through their grief and loss at the death of 
        a loved one - this is not Detective Capilano's strong suit."
    
    "She has seen it time and time again: that look. The look of horror, the look of {i}realization{/i} - 
        and nothing she can do will really, truly help."
    
    "Solve the case? Find the killer? Get vengeance? 
        Don't solve the case? It was just an accident? None of it matters."

    "None of it will bring back Tim. Detective Capilano could find every answer, tie up every loose end,
        and at the end of the day there will always be the questions she can't answer."

    "\"How could this happen to me? How will I go on without them?\""

    "Susan Capilano is a detective, not a grief counselor."

    "Happiness is a loan, Detective Capilano thinks to herself."
    
    "Loss is inevitable, the universe always collects its debts. Happiness is alone."
    hide detective

    play music "music/Farting Around.mp3"

    show detective pensive over
    sc "Could you shut up? There's a murder here that needs investigating."

    "Okay, geez, I was trying to build a moment, there."

    "It's character building!"

    "This is a serious work of art!"
    hide detective 

    show detective_jerk
    "Detective Capilano makes a \"jerking off\" motion with her hands and rolls her eyes."
    hide detective_jerk

    show detective pensive over
    sc "We're not here to have a very serious time where we look pensive and monologue in front of a window
            in the rain. We're here to solve a mystery. Get your head in the game!"

    "Okay, okay."
    hide detective
    jump payphones

# running joke: something bad happens to smunders?

label payphones:
    play music "music/Grand Dark Waltz Allegretto.mp3"
    # TODO: make this a choose-your-own adventure segment?
    
    scene bg payphones

    "Detective Capilano takes some time with the payphones to check up on a few leads."

    "Mrs. Portent's doorman verifies that he saw Ann leave, then Tim, separately, in two different cars."

    show prop notepad
    notepad "Ann's alibi confirmed."
    hide prop

    "The gym verifies that Tim is an active member, and has a check-in for him, this morning, at 8:00 AM."

    show prop notepad
    notepad "Check gym."
    notepad "Time of death: 8:00 AM (Tim arrives at gym)  - 12:30 AM (Call to precinct)"
    hide prop
    
    "Detective Capilano calls the number on the business card she found. It's picked up by the answering
        machine of a Becky. This must be the Becky from the gym! With the good hair!"

    "It's her {b}home{/b} phone number. Scandalous!"

    show prop notepad
    notepad "Cheating with Becky. Good hair."
    hide prop

    "Detective Capilano also takes a moment to check in with headquarters, confirming that she will, in fact,
        be forced to work with an external consultant."
    
    "It would, of course, have been possible to include these telephone conversations in their entirety, but
        for the sake of brevity we're just breezing past them. Perhaps if you'd like to hear them,
        they could be included as DLC?"
    
    "Yes, DLC. There we go, a full on monetization strategy. 
        If you send me money dollars, I'll release the \"Unnecessary Payphone Conversations\" cut.
        Every excruciating detail, to be included, at your behest."

    jump introducing_hank

label introducing_hank:

    play music "music/On Hold For You.mp3"
    scene bg payphones
    "A well-dressed private investigator walks into the room."

    show hank
    "He appears to be in his 50's. Immaculately dressed, in a three piece suit, with a wool overcoat.
        He has horn-rimmed glasses, dark hair, and greying temples."
    # he looks like Noah Bennett from Heroes, but older.

    hm friendly "Hello - Detective Capilano, I presume? Hank Maxhank, Private Investigator."

    "Capilano reaches over to shake his hand."
    hide hank

    if hasCueBall:
        show prop cueball
        cb "This is the guy."
        hide prop
    else:
        show hank friendly
        if hasStrangulation:
            "She gives it an unusual amount of juice - she's testing something - Hank has a grip like a vice."

        if hasDressShirt:
            "She holds on to the handshake a little too long - just long enough to inspect the shirt's cuffs.
                French cuffs with a monogrammed cufflink."

            hide hank
            show prop dress shirt
            dressshirt "Cuff buddies!"
            hide prop
        
        hide hank

        show detective sniff
        "His cologne is overpowering. Fruity, musky, smokey, a weird hit of pineapple - and he has put entirely 
            too much on. It's like getting punched in the face with fragrance."

        "Sitting in a car with this man is going to be a challenge - well, I suppose it could distract
            from Detective Capilano's current scent of kerosene and trash-fire."
        hide detective
    
    show detective
    sc "Nice to meet you. Detective Susan Capilano, Northwestica PD."
    hide detective

    show hank
    hm "This is short notice, so I'm a little short on case details - could you fill me in?"
    hide hank

    show detective notes
    sc "Okay - here's a quick summary of the case, so far:"

    if hasCueBall:
        sc_fast "Timothy Victrola was found, murdered, in his Cadillero AllStar at 12:30 PM, by Junior Officer Jemby Nichols."
    else:
        sc_fast "Timothy Victrola had breakfast with his wife at approximately 6:00 AM, left for the gym at 8:00 AM,
            and was found, murdered, in his Cadillero AllStar at 12:30 PM, by Junior Officer Jemby Nichols."

    sc_fast "Our Junior Officer pointed out the signs that the car had been tampered with, clearly intended
        to fly under it's own power into traffic and explode, thanks to a cinder block and some kerosene."
        
    sc_fast "Your client and the victim's wife, one Mrs. Ann Portent, has hired you to assist me in
        bringing the killer to justice."
    hide detective

    show hank friendly
    hm "Now, I assume you haven't done any serious investigation or found any clues, yet?"
    hide hank

    # narrows eyes suspiciously
    show detective irritated
    sc "... not particularly."
    hide detective

    if hasCarKeys:
        show prop carkeys
        carkeys "Find your own damn clues, assbutt."
        hide prop
    else:
        show detective irritated
        "She has some but she doesn't trust Hank with them yet."
        hide detective

    show hank smug
    hm "It's good that Mrs. Portent called me. While I'm certain that you're a - {i}professional{/i} - "
    hide hank

    if not hasBelt:
        play music "music/Dance of the Tuba Plum Fairy.mp3"
        show detective boxies
        "Detective Capilano's pants, after a full day of straining to keep up, fully beltless,
            choose this exact moment to finally give up and fall to the ground."
        show detective boxies embarrassed
        "That's right, this is the callback. Detective Capilano should have grabbed her belt,
            back in the apartment, and now she's paying the terrible price."
        "Everyone in the entire lobby pretends not to see Detective Capilano's boxer shorts with 
            little hearts on them."
        "A wealthy older woman in a mink stole, nearby, gasps and faints. High society is scandalized."
        "A small child points and laughs."
        show detective
        "She frantically scrambles to regain some dignity, pulling the pants back up and giving
            the pants a little twist-and-fold to try and keep them in place."
        hide detective

        show hank smug
        "Hank Maxhank doesn't miss a beat, he continues: "
    
        hm "While I'm certain that you're a, um, {i}professional{/i}, the private sector has access to certain 
                {i}enhanced resources{/i} that you just don't get when you're working for the public."
        play music "music/On Hold For You.mp3"
    else:
        hm "the private sector has access to certain 
                {i}enhanced resources{/i} that you just don't get when you're working for the public."
    
    
    show detective notes
    sc "I was curious - Mrs. Portent mentioned that the two of you had a close partnership.
            What kind of work do you find yourself doing for her?"
    hide detective
    
    show hank expository
    hm "A news agency like hers often needs investigations done. You'd think that the private 
            investigation industry is all \"cheating lovers\" and \"background checks\" - "
    hm " but the kind of investigative work that a news agency needs done is, well, 
            myriad and varied."
    hm "Obviously, the nature of all of our work for clients is private and confidential, of course." 

    hm friendly "Here, hop in my car, I'll take you to our offices and give you the tour."
    hide hank

    show detective concerned
    sc "How far is that?"
    hide detective

    show hank expository
    hm "Oh, it's maybe a 20 minute drive from here."
    hide hank

    if hasCueBall:
        show detective
        sc "Wonderful. Let's go."
        hide detective
        jump hank_office

    show detective smug
    sc "I was wondering if we could maybe hit Timothy's gym, first. There are some people there
            who I'd like to ask a few questions."
    hide detective

    show hank sure why not
    hm "The university gym? Sure, that's just on the way to my office."
    hide hank

    show detective smug
    sc "Yeah, that's the one."
    hide detective
        
    if hasBike:
        play sound "sounds/bike.ogg"
        show detective suspicious
        sc "Uh, we'll need to get my bike in the trunk."
        hide detective

        show hank confused
        hm "Your... bike? You biked here? That explains why you're so wet."
        hide hank
        
    else:
        show hank confused
        hm "You're... soaked."
        hide hank
        
    show detective damp
    sc "Nothing gets by you. We'll have this case solved in no time."
    hide detective
        
    show hank friendly
    hm "I'll put a towel down for you. Let's roll."
    hide hank

    jump gym

define talkedToPat = False
define talkedToBecky = False
label gym:
    scene bg gym
    
    play ambient_2 "ambient/gym.ogg"    
    play ambient "ambient/rain_smaller.ogg" volume 0.3

    if not talkedToPat and not talkedToBecky:
        play music "music/Late Night Radio.mp3"

        sc "I can see why Timothy liked this gym. It's magnificent."
        
        sc "Look at this, an olympic length swimming pool, a weight room, and a full rock climbing wall, the works!"

        sc "And over there, another olympic length swimming pool. And another one over there! Next to that sign, with directions... to the additional swimming pools?"

        show hank confused
        hm "Why do they have so many olympic length swimming pools in here?"
        hide hank

        show detective deflated
        sc "I don't know."
        hide detective

        show hank expository
        hm "This reminds me of the gym at my old alma mater."
        hide hank

        if hasCarKeys:
            show prop carkeys
            carkeys "This self-important asshat really wants you to ask him about his university."
            hide prop

            show detective concerned
            sc "Your old alma mater?"
            hide detective

            show hank friendly
            hm "Yeah, I'm a Willems State man, myself."
            hm "I was captain of the rowing team."
            hm expository "Goooooooooo fighting megnolas!"
            hide hank

            show detective concerned
            sc "... Isn't \"megnola\" considered a racial slur, nowadays?"
            hide detective

            show hank no
            hm "It's been our team's logo for over thirty years. Can't argue with tradition like that."
            hide hank

            # suspicious
            show detective irritated
            sc "..."
            hide detective

            show hank accusatory
            hm "Did you go to university, Detective Capilano?"
            hide hank

            show detective irritated
            sc "You know, it's strange, I don't really know."
            hide detective

            show hank confused
            hm "You don't know? Like, you're not sure if the school you attended was actually a university?"
            hide hank

            show detective
            sc "Sure, let's say it's that."
            hide detective

            
        show detective notes
        sc "While we're here, there are two people who I would like to talk to: {b}Pat, or Patty or Petey or Something{/b}, 
            Tim's personal trainer, and {b}Becky With The Good Hair{/b}, Tim's climbing partner."
        hide detective

    menu:
        "Talk to {b}Pat, or Patty, or Petey, or Something{/b}" if not talkedToPat:
            $ talkedToPat = True
            jump pat
        "Talk to {b}Becky With The Good Hair{/b}" if not talkedToBecky:
            $ talkedToBecky = True
            jump becky
        "Check the {b}Locker Rooms{/b}" if talkedToPat and talkedToBecky:
            jump locker

label pat:
    "It does not take too much wandering around the gym to find a fiery red-headed man shouting
        exercise instructions at a man squatting with a medicine ball."
    
    show detective
    sc "Hello - are you Pete?"
    hide detective

    show pat
    pat "Pat - I'm Pat. But, uh, everyone calls me \"Red\"."

    "Pat is a large young man, wearing a muscle shirt that says \"Beef\" on it. He has braided
        red hair and a tattoo of a hanzi or kanji character on his bicep. His arm is also, visibly, in
        a sling."
    hide pat

    show detective
    sc "I'm Detective Capilano, from the Northwestica PD - and this is Hank Maxhank, private investigator."
    hide detective

    show hank no
    hm "Hi."
    hide hank

    show pat
    pat "What's this about? I'm with a client."
    hide pat

    show softserve steve
    "The client is a sweaty, doughy looking man, currently struggling to do his medicine ball squats."
    hide softserve

    if not hasBelt and isHydrated:
        show detective
        sc "You know, you look almost exactly like a man I met earlier today."
        hide detective

        show softserve steve
        client "Asset re-use."
        hide softserve

        show detective
        sc "Ah."
        hide detective

    show detective
    sc "Would you mind if we interrupted this session for a bit to talk to Pat, here?"
    hide detective

    show softserve steve
    client "Oh, thank god."

    "The doughy man leaves."
    hide softserve
    with moveoutleft

    show pat
    pat "This had better be important: he owes me dozens more squats."

    # narrows his eyes, slight zoom in
    show pat serious
    pat "And I intend to collect."

    # narrows his eyes, slight zoom in again
    show pat serious bam
    pat "With interest."
    
    # narrows his eyes, slight zoom in again again
    show pat serious bam bam
    pat "Old school."

    show pat serious bam bam bam
    pat "You're a little close to my face, there, bud."
    hide pat

    show detective damp
    "Pat looks at Detective Capilano, who is still very damp from the rain."
    hide detective

    show pat serious bam bam bam
    pat "You know, the gym has towels you could probably use."
    hide pat

    show detective damp
    sc "I'll keep that in mind - but before any toweling, I'd like to ask you about a Mr. Timothy Victrola."
    hide detective

    show pat bump
    pat "Oh! Timbo! He's my BOY."

    "Pat bumps his chest with his fist."

    show pat
    pat "We meet up a few times a week to work on his delts, his quads, his lats, his squats, his dips, and his alts."
    hide pat
            
    show detective somber
    sc "I'm sorry to say this, but - Timothy Victrola has been found dead, just today."
    hide detective

    show pat serious
    pat "... oh."

    pat "Huh."

    show pat curious
    pat "Quick question - if you owe somebody money, what happens if they die? Do you just not owe them
            that money any more?"
    hide pat
    
    show hank
    hm "Was the debt part of a contract or was it an informal handshake deal?"
    hide hank

    show pat curious
    pat "Handshake deal."
    hide pat

    show hank expository
    hm "Unless someone knows about it, you're probably in the clear."
    hide hank

    show pat
    pat "Score."

    show pat serious
    pat "Sorry to hear about Tim, though."
    hide pat

    jump pat_questions


define askedPatDebts = False
define askedTattoo = False
define askedJob = False
define askedEyes = False
define askedArm = False
define askedAlibi = False
label pat_questions:
    menu:
        "Wait, {b}Debts{/b}?" if not askedPatDebts:
            $ askedPatDebts = True
            show hank accusatory
            hm "Did you owe {i}money{/i} to Mister Victrola?"
            hide hank

            show pat
            pat "Uh, yeah, a couple of thousand dollars. It was for my business."
            hide pat

            show detective notes
            sc "Your... business?"
            hide detective

            show pat
            pat "Oh, this is good - I wanted to start a pet store slash tattoo parlour."
            hide pat

            show detective notes point
            sc "That seems like too many concepts in one place."
            hide detective

            show pat
            pat "I'd call it \"Pat's Cats and Tats\"."
            hide pat

            show detective smug
            sc "That's a pretty solid joke. Ha. So what was the business, {i}really{/i}?"
            hide detective

            show pat
            pat "I ... I'm not sure if I understand. That was it."
            hide pat

            show detective suspicious
            sc "Wait, really? You actually tried to open a pet adoption center, and tattoo parlour?"
            hide detective

            show pat
            pat "Yeah."

            pat "I mean, obviously the idea {i}started{/i} as a silly rhyme."

            # taps his head

            pat "But - If you think about it, it makes sense - you sit for a long time for a tattoo, right?"

            pat "So if you're spending that time with a bunch of adorable cats and classy hats, by the
                    time you leave you're definitely going to want to buy a cat, or a hat, or both, right?"
            hide pat

            show detective notes point
            sc "Do you have any tattooing experience?"
            hide detective

            show pat
            pat "Not as such, but I figured I could learn as I went."
            hide pat

            show detective faceplam
            sc "How about experience with animals?"
            hide detective

            show pat
            pat "We had a family dog when I was a kid."
            hide pat

            show detective faceplam
            sc "Have you run a business before?"
            hide detective

            show pat
            pat "Well, I run the gym's concession bar sometimes."
            hide pat

            show detective notes
            sc "And it didn't work out?"
            hide detective

            show pat
            pat "I couldn't even get the business license. Something about health codes."
            hide pat

            show hank confused
            hm "So, Tim fronted you the cash for this ... {i}endeavor{/i}?"
            hide hank

            show pat
            pat "He loaned me quite a bit of money for early business development, yeah."

            pat "Tim was kind of a visionary - to be honest, a lot of his money went into these big planning
                    meetings we'd have every week."
            pat "I broke the news to him a few weeks back that the license
                    didn't go through at our big Waterpark Funzone meeting."
            
            show pat serious
            pat "It was a somber day at the Splishsplash Mountain."

            pat "I figured this thing was a cash train to money-town, and I'd be able to pay him back
                    no problem, but ... well, actually, after the business fell through, it's been
                    pretty hard to put that money together."
            hide pat
            
            "It's not smart to admit to a police officer that you had a large, off-the-books, outstanding debt 
                to a recent murder victim."

            jump pat_questions

        "Ask about {b}Tattoo{/b}" if not askedTattoo:
            $ askedTattoo = True
            show detective notes
            sc "Can I see that tattoo you have on your bicep?"
            hide detective

            show pat flex
            pat "Of course."

            show pat flex bam

            "The tattoo looks worse up close, scraggly. There's some evidence of keloid scars under the tattoo, as if it were either
                applied very clumsily or not cared for after application."
            
            "Remember Detective Capilano's TATTOO TIPZ:"

            "1. Look at your tattoo artist's portfolio up front. No rash decisions! You want to be in love with their art style."

            "2. Don't get flash from off of the wall. A marijuana leaf or a Playhouse Bunny tattoo is tacky. Work with them to develop a design that's meaningful to you!"

            "3. A reputable tattoo artist will be using disposable guns and will work hard to maintain a sterile environment."

            "4. Don't drink and get tattooed: not only is it a bad life decision, you'll bleed way more and actually get a {i}worse{/i} tattoo!"

            "5. Aftercare is key! Not only will an infection hurt, it will also badly damage the final appearance of the tattoo!"

            "Detective Capilano's TATTOO TIPZ are brought to you by the patchy, blotchy dolphin that she had drunkenly tattooed on her calf when she was much, much younger."

            "This is only important to note because it seems like Pat, also, did not follow Detective Capilano's TATTOO TIPZ: this is definitely the result of a rash decision."

            pat "It means \"strength\"."
            hide pat

            show hank smug
            hm "Oh, do you speak a second language?"
            hide hank
            
            show pat flex bam
            pat "No, but the tattoo artist said it means \"strength\" and I trust him."
            
            "Detective Capilano is relatively certain that this symbol actually means \"meat\". She has the tact not to mention it, though."
            hide pat

            show detective notes
            sc "Strength? You must be very strong, then."
            hide detective

            show pat
            pat "Oh, I am! That's why I got the tattoo - so that people would {i}know{/i}."
            hide pat

            show detective notes
            sc "But only people who can read the character."
            hide detective
            
            show pat
            pat "But I translate it for everybody else, so they know what it means."
            hide pat

            show detective faceplam
            sc "Ah, thus forming a foolproof system for letting people know that you are strong. A property that you otherwise wouldn't be able to telegraph."
            hide detective

            show pat
            pat "Pretty much!"
            hide pat

            jump pat_questions
        
        "Ask about {b}Job{/b}" if not askedJob:
            $ askedJob = True
            show detective notes
            sc "What do you do, here, for the gym?"
            hide detective

            show pat
            pat "Oh, I take every shift they'll give me. I'm a personal trainer, I run classes,
                    I'll wipe down the equipment, sometimes I even run concession."
            hide pat

            show hank accusatory
            hm "Seems like you're pretty hard up for money."
            hide hank

            show pat
            pat "Yeah, it's pretty tough to make ends meet. My tennis scholarship ran out 
                    and just making student loan payments is wiping me out pretty hard."

            pat "I've been really, really trying to lead the Dance Workout Jam Session, but 
                    Seamus has that totally buttoned up."
            hide pat
            
            show hank confused
            hm "Seamus?"
            hide hank

            show pat
            pat "Yeah, that's him, over there."
            hide pat

            jump seamus
        "Look Pat in the {b}Eyes{/b}" if not askedEyes:
            $ askedEyes = True
            show detective irritated
            "Detective Capilano looks Pat deep in the eyes, trying to get a fix on him as a person."
            hide detective

            show pat
            pat "Staring contest? Let's go!"

            show pat serious bam
            "..."

            show pat serious bam bam 
            "No thoughts, head empty."

            hide pat

            jump pat_questions

        "Watch {b}Seamus{/b} again for a while." if askedJob:
            jump seamus
        
        "Ask about {b}Arm{/b}" if not askedArm:
            $ askedArm = True

            show hank accusatory
            hm "Your arm's in a sling, there, huh?"
            hide hank

            show pat curious
            pat "Yeah, I hurt it a few days back while I was training Soft Serve over there."

            pat "I can get him to come tell you about it if you want."
            hide pat

            show hank no
            hm "No need-"
            hide hank
            
            show pat
            pat "Nah, it's no problem."

            with hpunch
            pat "HEY, SOFT SERVE! COME OVER HERE AND TELL THEM ABOUT MY ARM!"
            hide pat

            show softserve steve
            "The client from earlier walks back."

            client "His arm? Yeah, uh, I didn't want to do any more lunges so I bet him that
                he wasn't strong enough to push open a door while I was holding it from the 
                other side."

            "He gestures at the door. It's damaged, slightly."

            client "He really threw himself at it trying to get it open. Dislocated his shoulder."
            hide softserve

            show pat
            pat "He's a lot stronger than he looks."
            hide pat

            show detective faceplam
            sc "That's a pull door."
            hide detective

            show softserve steve
            client "Yeah, I won the bet."
            hide softserve

            jump pat_questions
        "Ask about {b}Alibi{/b}" if not askedAlibi:
            $ askedAlibi = True

            show hank expository
            hm "Can I ask about your whereabouts for the last several hours?"
            hide hank

            show pat
            pat "Yeah - I woke up at 10, had a healthy breakfast of juice - and -"
            hide pat

            sc "Wait - juice?"

            show pat
            pat "Yeah, I'm on a juice cleanse. Trying to get all of the toxins out of my system."

            pat "I've got a juice guy - you buy these juices and for a few days you drink nothing
                but juice, and you don't eat anything at all."
            
            pat "Basically everything inside your body comes out of your body. Including the {i}toxins{/i}."
            hide pat

            sc "Toxins like what?"

            show pat
            pat "Well, you know, we eat all of this processed food, and we know that processed food is full
                of {i}chemicals{/i} and the cleanse gets the chemicals {i}out{/i}."
            hide pat

            sc "What kind of chemicals?"

            show pat
            pat "Like, you know how when you buy store bread and it lasts for weeks, but homemade bread goes 
                stale in only a few days? That's because of the {i}chemicals{/i}. Don't want those building
                up in your system." 
            hide pat

            sc "Uh-huh."

            show hank
            hm "Detective Capilano - could we move it along? The young man was telling us about his day."
            hide hank

            show pat
            pat "So, I drink my morning juice, I spend some time in the bathroom - I've got the squirts
                    real bad from the cleanse - and then I jogged to work, changed out of my wet clothes,
                    and started my shift at noon."
            
            pat "I've been here ever since."
            hide pat

            show hank idk
            hm "Did you talk to anybody this morning? Anybody who can verify where you've been?"
            hide hank

            show pat
            pat "No, not really."
            hide pat

            jump pat_questions

        "Okay, we're done here." if askedPatDebts and askedArm:
            show detective
            sc "Okay, big guy, I think we're done, here."
            hide detective

            show pat
            pat "Nice talkin' to you two!"
            hide pat

            "Detective Capilano and Hank Maxhank walk out of earshot."

            jump pat_complete
        

image seamus_animated:
    "seamus.png"
    pause 0.568
    "seamus 2.png"
    pause 0.568
    "seamus 3.png"
    pause 0.568
    "seamus 4.png"
    pause 0.568
    "seamus 5.png"
    pause 0.568
    "seamus 6.png"
    pause 0.568
    "seamus 7.png"
    pause 0.568
    "seamus 10.png"
    pause 0.568
    "seamus 8.png"
    pause 0.568
    "seamus 9.png"
    pause 0.568
    "seamus 2.png"
    pause 0.568
    "seamus 3.png"
    pause 0.568
    "seamus 4.png"
    pause 0.568
    "seamus 6.png"
    pause 0.568
    "seamus.png"
    pause 0.568
    "seamus 5.png"
    pause 0.568
    "seamus 10.png"
    pause 0.568
    "seamus 4.png"
    pause 0.568
    "seamus 8.png"
    pause 0.568
    repeat

image seamus_uh_oh:
    "seamus.png"
    pause 0.284
    "seamus 2.png"
    pause 0.284
    "seamus 3.png"
    pause 0.284
    "seamus 4.png"
    pause 0.284
    "seamus 5.png"
    pause 0.284
    "seamus 6.png"
    pause 0.284
    "seamus 7.png"
    pause 0.284
    "seamus 10.png"
    pause 0.284
    "seamus 8.png"
    pause 0.284
    "seamus 9.png"
    pause 0.284
    "seamus 2.png"
    pause 0.284
    "seamus 3.png"
    pause 0.284
    "seamus 4.png"
    pause 0.284
    "seamus 6.png"
    pause 0.284
    "seamus.png"
    pause 0.284
    "seamus 5.png"
    pause 0.284
    "seamus 10.png"
    pause 0.284
    "seamus 4.png"
    pause 0.284
    "seamus 8.png"
    pause 0.284
    repeat

define seamusCount = 0

label seamus:
    $ seamusCount += 1 
    scene bg vending machine
    play music "music/Club Seamus.mp3"
    show seamus_animated
    if seamusCount > 1:
        "You watch Seamus dance, again. You can't help it. It's spectacular."
    if seamusCount == 2:
        "This is something you can't take your eyes off of. There is only Seamus. There is only... {i}dance.{/i}"
    if seamusCount == 3:
        "There's nothing you can do. You are mesmerized. The mystery can wait. Everything can wait. You must watch Seamus."
    if seamusCount == 4:
        "You start to wonder if its possible to be too obsessed with one man's dancing, but of course you cannot."
    if seamusCount == 5:
        "Seamus's dance starts to interfere with the stability of reality itself. The dance is too powerful, even,
            for the game to contain."
        
        show seamus_uh_oh
    if seamusCount == 6:
        "You a8re sTarting To bmEocome CONCERNED"
        show seamus_uh_oh
        "Seamus's dancYe starts to interfeyre with the stability of reality itself. The dance is too powerful, even,
            for the game to contain.OA"
        show seamus_uh_oh
    if seamusCount >= 7:
        jump seamus_game_over

    "Seamus is currently dancing like nobody is watching next to a vending machine."

    "Literally nobody is around. Seamus is doing this for Seamus."
            
    # this would be a great time for a silly video
    
    "My god. It's beautiful."
    
    "Stunning."

    if seamusCount == 3:
        "Mellifluous"
    if seamusCount == 3:
        "Brandtacular"
    if seamusCount == 4:
        "Marvelous"
    if seamusCount == 5:
        "Dangerous"
    
    "Incredible."

    if seamusCount == 6:
        "Spl981ndiferou8s"
        with pixellate

    "Magnificent."

    "Spellbinding."

    if seamusCount < 2:
        show hank idk
        hm "Can we... move this along?"
        hide hank

        sc "Another minute, Hank."

        "Yeah! Another minute!"

        show hank what
        hm "Come on."
        hide hank

        sc "Okay."
    if seamusCount == 2:
        "something in his dance commands you"
        "Seamus is the dance commander"
        "giving out the order for fun"
        "and he's the only one"
        "who gives the orders here, alright?"
        "keep watching"
    if seamusCount > 2:
        "Seamus is growing more powerful with each passing glance."
    if seamusCount > 5:
        "It's starting to concern you."

    hide seamus_animated
    hide seamus_uh_oh
    scene bg gym
    play music "music/Late Night Radio.mp3"

    jump pat_questions


label pat_complete:

    if hasBadge:
        show prop badge
        badge "He knows less than anyone we have ever questioned."
        hide prop

    show hank
    hm "He was in significant debt to the victim and he has no alibi during the time of the murder." 
    hide hank

    show detective
    sc "Yeah. I want to say he's a harmless lunkhead, but we can't eliminate him yet, can we?"

    if hasStrangulation:
        "Except how could he have strangled Timothy with one arm in a sling?"
    if hasDressShirt:
        "Getting out of a dress shirt in a hurry in that sling seems like it would have been a challenge
            for Pat - and he doesn't seem like the type to own a nice dress shirt, anyways."
    hide detective
    
    jump gym

label becky:

    show hank confused
    hm "The {i}climbing instructor{/i}? Really grasping at straws, aren't we, Detective?"
    hide hank

    show detective
    sc "I'm nothing if not thorough, Mr. Maxhank."
    hide detective
    
    scene bg climbing wall

    "Detective Capilano wanders over to the climbing wall, currently attended by a short, muscular 
        woman."

    sc "Hello - Becky? Climbing instructor?"

    show becky
    becky "Yes, that's me. How can I help you?"

    "Becky appears to be quite young - college aged. Dark hair, in a short cut, cropped to the side. 
        She's wearing a gym uniform - comfortable
        athletic clothing. She has a climbing harness around her waist."
    hide becky

    if hasBelt:
        belt "A climbing harness is like a belt, but with {i}even more belt{/i} around the legs."
        belt "This has been: belt facts."
    
    show becky
    "Becky smells like soap and fresh shampoo."
    hide becky

    show detective
    sc "I'm Detective Capilano, from the Northwestica PD - and this is Hank Maxhank, PI."
    hide detective

    show hank no
    hm "Hi."
    hide hank

    if hasBadge:
        show prop badge
        "Detective Capilano flashes her badge."
        badge "Salutations."
        hide prop
    else:
        show becky
        becky "Police, huh? Can you prove it?"
        hide becky

        show detective notes
        sc "Give me a second."

        "Detective Capilano scrawls something down in her notepad."

        sc "Detective Capilano, Northwestica PD."
        hide detective

        show detective badj
        "She flashes a hastily scrawled obviously-concocted paper badge that says \"BADJ\" on it."

        "Becky nods. Seems legit."
        hide detective

        if hasCarKeys:
            carkeys "Fuckin' nailed it."

    show becky
    becky "Wait, you're PD and he's a PI? How does {i}that{/i} work?"
    hide becky

    show detective suspicious
    sc "We're still working out the details."
    hide detective

    show becky
    becky "You're very ... damp."
    hide becky

    show detective damp
    sc "Noted."

    show detective somber
    sc "We have bad news for you - about a client of this gym. Timothy Victrola."
    hide detective

    # clasping her hands over her mouth
    show becky gasp
    becky "Oh, no."
    hide becky

    show detective somber
    sc "I'm sorry to have to be the bearer of bad news, but we believe that he may have been murdered."
    hide detective
    
    show hank expository
    hm "To {i}death{/i}."
    hide hank

    show detective irritated
    sc "Thank you, Hank."

    show detective notes
    sc "Can you confirm that you were Mr. Victrola's climbing instructor?"
    hide detective

    show becky gasp
    becky "Yeah - I am - uh, {i}was{/i}." 
    hide becky
    
    show detective notes
    sc "So, how long was Timothy coming to climbing practice with you?"
    hide detective

    show becky
    becky "About six months."
    hide becky

    jump becky_questions

define askBeckySmell = False
define askBeckyStrength = False
define askBeckyDanger = False
define askBeckyCheating = False
define askBeckySeduce = False
define askBeckyMurder = False
label becky_questions:
    menu: 
        "Ask about {b}Smell{/b}" if not askBeckySmell:
            $ askBeckySmell = True
            show detective sniff
            "It's strange that Becky smells like soap and fresh shampoo."

            sc "Seems like a lot of exertion, all this climbing. You seem fresh as a daisy, though."
            hide detective

            show becky
            becky "Well, my shift only started at one - I had a shower before work. "    
            hide becky

            show detective notes
            "To wash off rain, blood, and kerosene? Or just to freshen up?"

            sc "What were you doing this morning?"
            hide detective

            show becky
            becky "A friend dropped me off at the university this morning, she clocks in earlier than I do,
                    so I took a walk around the quad and then settled into the library for some homework."
            hide becky
            
            show detective notes point
            sc "A walk? Today? Wouldn't you get wet?"
            hide detective

            show becky
            becky "The outer ring of the quad is covered, so no."
            hide becky

            show detective notes
            sc "Then, after that?"
            hide detective

            show becky
            becky "I came back to the gym, showered, and changed into my work clothes. Then I started work."
            hide becky

            show prop notepad
            notepad "Weak alibi. No eyewitnesses until 1:00. Dry all day."
            hide prop

            jump becky_questions

        "Ask about {b}Strength{/b}" if not askBeckyStrength:
            $ askBeckyStrength = True
            show detective notes
            sc "Climbing gym - that's really impressive. You climb this wall?"
            hide detective

            show becky
            becky "Among others, yes."
            hide becky

            show detective notes
            sc "How hard is this wall?"
            hide detective

            show becky 
            becky "It's actually pretty soft - it's gently padded so that it's harder to hurt yourself if you slam in to it."
            hide becky
            
            show detective faceplam
            sc "I meant how hard is it to {i}climb{/i}? On a scale from one to ten?"
            hide detective 

            show becky fifteen
            becky "Actually, if you're climbing, it's a scale from one to fifteen."
            hide becky

            show detective notes point
            sc "Why is that?"
            hide detective

            show becky no
            becky "Well, fifteen is {i}five harder{/i} than ten." 
            hide becky

            show detective faceplam
            sc "Well, yes, but then you could have just made {i}ten{/i} the hardest."
            hide detective

            show becky fifteen
            becky "But fifteen is {b}five harder{/b}."
            hide becky

            show detective 
            sc "Wait, how did you do that thing with your hands?"
            hide detective
            
            show becky no
            becky "What thing?" 
            show becky

            show becky
            becky "Anyways, this wall has a few different challenge ratings - you can vary how 
                hard your climb is by choosing which colors you're allowed to grab
                and which route you take up the wall."

            becky "If you go up the easy way, and use all of the colors? That's a four -
                a child could do it."
               
            becky "On the other hand, if you go up to the left, and 
                you only use the orange handholds, it's a thirteen - which is a difficult
                and technical climb."
            hide becky

            "Detective Capilano looks up at the harder path. There don't seem to be enough
                orange handholds for a person to actually be able to climb up this way."

            show detective notes point
            sc "It looks like in order to get up that way, you'd have to be able to pull
                    up your entire body-weight, one handed."
            hide detective

            show becky guns
            becky "Oh, yeah. I can do it."

            if hasStrangulation: 
                "Her grip strength must be incredible."
            hide becky

            show detective notes point
            sc "Could Timothy?"
            hide detective

            show becky
            becky "No, he was never in the kind of shape where he could climb a thirteen.
                He's got solid fundamentals and he's pretty fit but he wasn't really strong
                enough - and he weighs a lot more than I do."
            hide becky

            show prop notepad
            notepad "Becky much, {b}much{/b} stronger than Timothy."
            hide prop

            jump becky_questions

        "Ask about {b}Danger{/b}" if not askBeckyDanger:
            $ askBeckyDanger = True
            show detective notes
            sc "Would you say there are a lot of climbing accidents on the wall? It seems
                    like someone could get really hurt doing this."
            hide detective

            show becky
            becky "Oh, it's very safe, if you're adhering to the safety protocols."
            
            becky "Of course, it's {i}possible{/i} to get very hurt if there's an equipment failure."
        
            becky "But everyone who climbs checks their equipment regularly."
            hide becky
            
            show detective notes point
            sc "So if you wanted to hurt a fellow climber, you'd just have to sabotage the equipment? 
                    How hard would that be?"
            hide detective

            show becky
            becky "Oh, not hard at all - their life is in your hands in some sense, while you're belaying for them.
                        You'd just have to do it very badly, let them fall, fail to catch them."
            
            becky "Of course, they'd probably hurt their legs or back, rather than {i}die{/i} - we're not {i}that{/i}
                    high off of the ground here."
            
            becky "All bets are off if you're on an actual mountain, of course."

            becky "Wait - did Tim die in a climbing accident?"
            hide becky

            show hank confused
            hm "No, a car accident. I don't know why we're talking about this at all."
            hide hank

            show detective suspicious
            sc "I was just curious about climbing. I've been thinking of trying it myself, and I was wondering
                    how safe it is."
            hide detective
            
            show hank
            hm "Great use of our time."
            hide hank
            
            show prop notepad
            notepad "Becky could hurt Timothy very easily."
            hide prop

            jump becky_questions
        "Ask about {b}Murder{/b}" if not askBeckyMurder:
            $ askBeckyMurder = True
            show detective notes point
            sc "I just have one question - "
            hide detective

            show hank straightening
            hm "Let me take this one."
            
            hm accusatory "Where were you {i}really{/i}, this morning?"
            hide hank

            show becky irritated
            becky "At the library."
            hide becky

            show hank accusatory
            hm "A likely story. Can anyone - {i}verify{/i} that you were at the library?"
            hide hank

            show becky shrug
            becky "Probably {i}someone{/i}? Maybe you should go to the library and ask around."
            hide becky

            show hank shrug
            hm "She's got me there, hoss. It's airtight."
            hide hank

            show detective irritated
            sc "Could you not call me hoss?"
            hide detective

            jump becky_questions

        "{b}Seduce{/b} Becky" if hasBelt and not askBeckySeduce:
            $ askBeckySeduce = True

            show prop belt
            belt "This woman is beautiful. You must make her yours."
            hide prop

            if hasBadge:
                show prop badge
                badge "She's a suspect in an active murder case. Keep it in your pants, belt."
                hide prop
                
            show prop belt
            belt "Unf unf unf."
            hide prop

            show prop condoms
            condoms "We agree."
            hide prop

            if hasBadge:
                show prop badge
                badge "You wouldn't even be involved!"
                hide prop

                show prop condoms
                condoms "We get excited easily!"
                hide prop

            if hasGun:
                show prop gun
                gun "Show her the gun. Women who are afraid for their lives are more {i}pliable{/i}."
                hide prop
                
                if hasBadge:
                    show prop badge
                    badge "Like I said, that gun is a horrifying sociopath."
                    
                    show prop gun
                    gun "I ought to shoot you for saying that."
                    hide prop
            
            show prop notepad
            notepad "She's easily 20 years younger than you, don't be gross."
            hide prop

            show prop belt
            belt "Love knows no age barrier."
            hide prop

            show prop notepad
            notepad "It absolutely does."
            hide prop

            show detective
            sc "I think that the notepad is right."
            hide detective

            show hank confused
            hm "... You ... think that the notepad is right?"
            hide hank

            show detective smug
            sc "Oh, I - uh - made a note here about what I was going to have for dinner, and I agreed with it."
            hide detective

            show hank friendly
            hm "... you're an odd duck, aren't you, detective." 
            hide hank

            jump becky_questions

        "Ask about {b}Cheating{/b}" if not askBeckyCheating:
            $ askBeckyCheating = True
            show detective notes point
            sc "Your relationship with Tim - could you talk about that?"
            hide detective

            show becky irritated
            becky "What relationship? I was his climbing instructor."
            hide becky

            show detective notes
            sc "You know, it's strange - I was wondering if you could help me explain this - 
                    he had your phone number in his wallet at time of death."
            hide detective

            show becky no
            becky "Probably to set up appointments with the gym?"
            hide becky

            show detective notes confused
            sc "Your home phone number."
            hide detective

            # shrug
            show becky shrug
            becky "Huh. How'd that get there?"
            hide becky

            show hank idk
            hm "Maybe Tim looked her up in the phone directory."
            hide hank

            show becky shrug
            becky "Yeah, maybe he did."

            "Detective Capilano {i}knows{/i} that there's more going on here, but it's going
                to take more pressure to get her to crack."
            hide becky
            
            show hank friendly
            hm "I'm sure this is very personal for you, we'll drop it."

            "We will?"
            hide hank

            show prop notepad
            notepad "Hank interfering. Ditch Hank."
            hide prop

            jump becky_questions

        "Ditch {b}Hank{/b}" if askBeckySmell and askBeckyStrength and askBeckyDanger and askBeckyCheating:
            "Hank is cramping Detective Capilano's style."
            
            show becky
            "Detective Capilano has a plan to chat with Becky alone, for a bit."
            
            "Becky doesn't appear to have a purse with her, or any pockets."
            hide becky

            show detective
            sc "Becky, this is just a standard procedural thing we have to do, but could I take a quick look
                    at your identification?"
            hide detective

            show becky shrug
            becky "I don't have it with me, it's in my locker."
            hide becky

            show detective straightening
            sc "Okay, let's go."
            hide detective

            show becky shrug
            becky "Right now?"
            hide becky

            show detective straightening
            sc "Yeah, right now."
            hide detective

            jump beckyLocker

label beckyLocker: 
    "Standing outside the locker rooms, Becky stops for a second."

    show becky irritated
    becky "Sorry, Mr. Maxhank, this is a ladies only locker room."
    hide becky

    show hank
    hm "This is a very serious investigation, I should be included."
    hide hank

    show becky irritated
    becky "And who are you again? A private citizen?"
    hide becky

    show hank angry
    hm "I'll wait out here."
    hide hank

    scene bg locker room

    "They walk in to the locker room."

    show detective embarrassed
    sc "Wow, what gratuitous and excessive college nudity we're looking at right now."
    hide detective

    show becky
    becky "Why are those two having a pillow fight? Did they bring those from home?"
    hide becky

    "They are both joking. If, perhaps, one had hoped to see a display of gratuitous and 
        excessive college nudity,
        up to and including a pillow fight, this gym locker room would be a disappointment.
        It's a very quiet time of day."
    
    "Maybe that's another thing that we could do with DLC. 
        That'd bring in some money."

    "The two walk by a series of lockers. There are numbered lockers for the gym's members,
        but the staff lockers are further in the back and labeled by name."

    show becky
    becky "This is my locker."

    "Becky opens the locker. Inside is a purse and a change of clothes."
    hide becky

    show prop hoodie
    "She rifles through the purse to find her identification - but while she's doing this,
        Detective Capilano reaches over and grabs her change of clothes."
    hide prop

    show becky irritated
    becky "Hey - "
    hide becky

    show prop hoodie
    sc "I can't help but notice that this is a large, baby-blue Yuyuyuzu hoodie."

    "Detective Capilano checks the tag."

    sc "In a men's XL. Huh. With... short arms."

    "The other thing that Detective Capilano notes is that Becky's change of clothes is {b}bone dry{/b}."
    hide prop

    show detective
    sc "Have you been out in the rain at all today?"
    hide detective

    show prop hoodie
    yuyuyuzu "No, I haven't. We got to go jogging around the quad this morning, though!"
    hide prop

    show becky irritated
    becky "I already told you, no - the quad's covered, so I stayed dry."
    hide becky

    show detective suspicious
    sc "You know, it's strange - Timothy was wearing a shirt just like this when he died.
            Same brand, and size, and everything."
    hide detective

    show becky
    becky "Oh, this {i}is{/i} his shirt."
    hide becky

    show detective suspicious
    sc "In your locker?"
    hide detective

    show becky blank
    becky "I was ... {i}borrowing{/i} it."
    hide becky

    show detective notes
    sc "So, you have his sweater. You said earlier that your relationship was -"
    hide detective

    show becky
    becky "Strictly professional, yes. He just - left it behind."
    hide becky

    show detective notes confused
    sc "Odd of you to have kept it rather than returning it to him."
    hide detective

    show becky shrug
    becky "Sure, but that's what happened. You, uh, needed to see my identification?"
    hide becky

    show detective notes
    sc "Yes, please."
    hide detective

    show becky id
    becky "Here."
    hide becky

    show detective notes
    sc "\"Rebecca Segsihan\", Age 24 - wait, this isn't a driver's license. It's just a student card."
    hide detective

    show becky id
    becky "I never got my driver's license. I can't afford a car, anyways - what would be the point 
        of even learning?"
    hide becky
    
    show detective shrug
    sc "Well, you might drive {i}someday{/i}."
    hide detective

    show becky shrug
    becky "I can learn {i}then{/i}, seems like."
    hide becky
    
    show detective sheepish
    sc "There's just one more bit of information I need - could you write down your phone number for me?
            We might have some more questions for you, later."
    hide detective

    play sound "sounds/writing.ogg"

    show becky shrug
    becky "Okay..."
    hide becky

    show becky
    becky "Here you are."
    hide becky
    
    stop sound

    show becky irritated
    becky "... wait, don't you already have my phone number? You told me that Timothy had it in his wallet."
    hide becky

    show detective somber id
    sc "Yes, but now I can compare the two. What do you know - would you look at this? A perfect match."

    sc "I'm extremely curious to discover how Mr. Victrola looked up your name in a phone directory,
            then wrote down your phone number in {b}your{/b} handwriting. What a talented young man."
    hide detective
    
    show becky blank
    becky "That's a bit of a dirty trick."

    becky "Should I have a lawyer? Should I be talking to you with a lawyer right now?"
    hide becky

    "I'm going to interrupt, here. Yes. Becky should absolutely be talking to a lawyer. Everyone we've talked to
        should have been talking to a lawyer. You should always, ALWAYS have a lawyer."
    "This is a story with a well-meaning sleuth who always solves the case {i}correctly{/i} - you have no 
        such guarantee in real life."
    "Even with that established, Detective Capilano is going to lie, here, and tell Becky \"No\". - but it's
        bad advice."
    
    show detective smug
    sc "It shouldn't be necessary - we're just having a friendly chat. You're not even formally a suspect."

    "Yet. Not formally a suspect yet."
    hide detective

    show becky shrug
    becky "So maybe I wrote down the number for him. I don't remember."
    hide becky

    show detective straightening
    sc "That seems like it would indicate a more than merely professional relationship."
    hide detective

    show becky irritated
    becky "Even so - nothing happened."
    hide becky

    show detective irritated
    "Detective Capilano does not believe her, but it doesn't seem like this line of questioning
        is going to lead any further."

    sc "Well, I guess we've stood around this locker room long enough. Shall we go?"
    hide detective

    show becky
    becky "Sure."
    hide becky

    "Becky locks up her purse and her clothing, and the two of them return to the locker 
        room entrance."

    show becky
    becky "Where's your friend?"
    hide becky

    show detective shrug
    sc "I'm not sure. I figured he'd be waiting out here for us."
    hide detective

    show hank conspiratorial
    "Hank walks out of the men's locker room."

    hm "Oh - sorry, I just had to drop a few kids off at the pool."
    hide hank

    show becky irritated
    "Becky grimaces."
    hide becky

    show detective irritated
    sc "Wow."

    show detective
    sc "I think we've tormented poor Ms. Segsihan enough for one day, wouldn't you say?"
    hide detective

    show hank friendly
    hm "Oh, yes."
    hide hank

    "Becky walks away."

    show prop condoms
    "As Becky walks away, Detective Capilano pulls some of the condoms out of Timothy's wallet and points them at her."

    sc "Have you seen her before?"

    condoms "Yeaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaah"
    hide prop

    show hank confused
    hm "Are you... talking to those... condoms?"
    hide hank

    show detective embarrassed
    sc "Absolutely not, I'm just engaging in my {i}process{/i}."
    hide detective

    scene bg gym

    jump gym


label locker:

    show hank
    hm "I have a hunch about that Pat fellow. Something about his alibi rubbed me the wrong way."
    hide hank

    show detective
    sc "Oh?"
    hide detective

    show hank accusatory
    hm "Let's check out his locker in the locker rooms."
    hide hank

    if hasBadge: 
        badge "Tell him no. That's not okay."

        show detective irritated
        sc "We can't just go poking around in people's lockers without a search warrant."
        hide detective

        show hank conspiratorial
        hm "Well, perhaps you can't, but I'm a private citizen."
        hide hank

        show detective irritated
        sc "Which means that if you open one of these lockers, I can and {i}should{/i} arrest you 
                for breaking and entering."
        hide detective
    
        show hank shrug
        hm "But if we just {i}look{/i} at the contents of some open lockers on public property,
                that's okay, right?"
        hide hank

        show detective irritated
        "Detective Capilano looks uncomfortable with this."
        hide detective

    play music "music/Grand Dark Waltz Trio Allegro.mp3"
    scene bg locker room men
    "The two of them walk into the men's locker room, finding Pat's locker in the back."

    show detective
    sc "Patsy Haring."
    hide detective

    show hank friendly
    hm "This is the one. And wouldn't you know, the lock is already open!"
    hide hank

    show detective suspicious
    sc "(supiciously) Lucky break."
    hide detective

    show hank
    "Hank opens the locker."

    "Inside is a wet jacket and some crumpled clothes, as well as a small plastic plant."

    "Nestled in the damp clothes is a shining object."
    hide hank

    play sound "sounds/snap.ogg"
    show detective gloves
    sc "Let's get rummaging!"
    hide detective

    show hank accusatory
    hm "Look at this."

    show hank got gun
    "Hank Maxhank reaches in and pulls out a small revolver."

    if hasGun:
        hide hank
        show prop gun
        gun "A friend!"
        gun "He's holding a gun, you should probably shoot him. Just putting that out there."
        hide prop
        show hank got gun

    hm "A murder weapon."

    if hasStrangulation:
        hide hank
        show detective irritated
        sc "Huh. You don't say."
        hide detective
        show hank got gun

    hm "We'll take that to the ballistics lab at my office - I bet it has been fired today."
    hide hank

    show detective concerned
    sc "Well, that's pretty damning - here, I'll bag it and you keep poking around in there."

    show detective gun empty
    "While Hank is distracted by the locker, Detective Capilano empties the bullets from the revolver into her 
        hand, counts them (three), and pockets them."
    hide detective

    show hank got watch
    "Hank reaches in to the locker and fishes out a watch."

    hm "Look at this watch!" 

    "The watch is silver and blue, with a military strap. It looks very expensive."
    
    if askedWatchTan:
        "Detective Capilano asked Ann about that exact watch, earlier."

    "Hank turns the watch around in his hands."

    hm "Ann Portent & Timothy Victrola. Their names are engraved on the back."
    hide hank

    show detective irritated
    sc "That's an obvious plant."
    hide detective

    show hank got plant
    "Hank Maxhank pulls the small plastic plant out of the locker."

    hm "I'm not sure what this has to do with the case, to be honest."
    hide hank

    show detective
    sc "Anything else in there?"
    hide detective 

    show hank
    hm "There's a pile of sopping wet clothes."
    hide hank

    show detective lean
    sc "Let me see those."
    hide detective

    show detective sniff clothes
    "The detective gets a good long smell of the wet clothes."
    "They smell damp and a little sweaty, but that's it."
    sc "Huh."
    hide detective

    show hank confused
    hm "Uh, I didn't think you were in to that kind of thing."
    hide hank

    show detective smug
    sc "All part of the {i}process.{/i}"
    hide detective

    show hank got book
    "Hank reaches in and finds one more thing... a small red booklet."

    hm "Das Kapital! The kid's a commie!"

    "Could it be that \"Red\" Haring was just a communist?"

    hide hank

    show detective hand up
    sc "Uh, that's classic children's book \"Harold Poopsy the Balloon Bear\"."
    sc "You probably shouldn't just assume that every red-colored book you encounter 
            is communist literature." 
    hide detective

    show hank what    
    hm "Nevertheless, I think we've got Pat dead to rights."
    hide hank

    show detective concerned
    sc "Well, then - let's get that gun to your lab. See what we find."
    hide detective

    show hank friendly
    hm "Okay - let's get to the car."
    hide hank

    if hasBike:
        show hank smug
        hm "Unless you want to take your bicycle."
        hide hank

        show detective irritated
        sc "You could ride on the basket!"
        hide detective

        show hank
        hm "It's still raining pretty hard out there."
        hide hank

    jump securitas

label securitas:
    stop music
    play ambient "ambient/rain_smaller.ogg" volume 0.3
    play ambient_2 "ambient/office.ogg"    
    
    scene bg hank entrance
    "An imposing, concrete building."

    scene bg hank lobby
    "Hank and Detective Capilano walk into a very impressive and well-staffed security company."

    play music "music/Night in Venice.mp3"

    show hank smug
    hm "Black Swan Securitas. This is the company I founded."
    
    hm "Do you see this? Absolutely everything is top-of-the-line."
    hide hank

    show detective irritated
    sc "Wow. Impressive. Business is good, seems like."
    hide detective

    show hank conspiratorial
    hm "We're in the business of information, and information is a booming industry."
    hide hank

    if hasCarKeys:
        show prop carkeys
        carkeys "I hope you nail this smug chumpdick to the wall."
        hide prop

    show hank straightening
    hm "Over here, we have our computer database. With over 56 kilobytes of memory,
            it can run our most demanding crime simulations."
    hide hank

    scene bg mr churn

    # look, I know this is just a bit from the 1987 Mel Brooks film "Spaceballs", but 
    #   it's the greatest bit in cinematic history
    sc "What's the matter with this thing, what's all that churning and bubbling?
            You call that a crime computer?"
    
    hm "No, Detective Capilano - "

    scene bg mr coffee

    "Hank steps back."

    hm " - we call it Mr. Coffee. Care for some?"

    sc "(embarrassed) Of course. I always have coffee while I'm using computers."

    hm "Of course."

    sc "Now that I have my coffee, I'm ready to see your crime computer. Where is it?"

    hm "Right here."

    scene bg mr crime

    "Hank steps to the side, revealing the computer right next to the coffee machine."

    hm "Mr. Crime, the crimeputer."

    sc "I'm going to level with you, we don't have any computers down at the precinct.
            What does it do?"
    
    hm "We've built a comprehensive indexing system for all of our files in here."

    hm "Let's say you're at your precinct and you want to find all of your arrests that
            happened on a Wednesday, for people with last names starting with \"P\" -
            how would you go about that?"
    
    sc "That feels like kind of a contrived example, but - well, we don't index our
            files by the day that the arrest happened, but we do have a card index for 
            files by last name - "
    
    sc "So I'd have to get all of the files for the \"P\" names and go through them,
            one by one, looking for the arrest date. I suppose it'd probably be a 
            couple of days of work."

    hm "This bad boy can do that in {i}minutes{\i}."

    sc "Wow. Very impressive. Can I try it?"

    hm "Sure, give it a go."

    "Detective Capilano looks at the computer's keyboard and very slowly hunts for the first letter
        she's thinking of. As she types, the letters are printed on to a large screen 
        near the keyboard."
    
    "T"

    "I"

    "M"

    "O"
    
    "T"

    show hank
    "Hank interrupts."

    hm "You know what? I'm not sure if we have the time for this - we need to get this 
            gun to the lab, right away."
    hide hank
    
    "Strange, he was excited to show off the computer just a second ago."
    
    # i think this gives too much away
    # "Does he have a file on Timothy that he doesn't want Detective Capilano to see?"
    # 
    # sc "Do you happen to have a file on Timothy Victrola?"
    #
    # crimeputer "I have two, but they're both marked \"private\", so I can't show them to you."
    # 
    # show hank
    # hm "No, I don't have a file on Timothy."
    # hide hank
    
    show detective suspicious
    sc "It's funny - when I said that we needed to visit Timothy's gym, you knew right away that
            it was at the university. Awfully curious."
    hide detective
    
    show hank idk
    hm "Yeah - strange, that."

    show hank friendly
    hm "You know, Detective Capilano, you're a lot sharper than I gave you credit for.
            Let's talk in my office for a moment, I have a proposition for you."
    hide hank

    show detective
    sc "Oh, of course. Let's go."
    hide detective

    jump final_decision

label final_decision:
    stop music
    scene bg default
    "Hey, just for your information, this story is about to wrap up. Now's your chance to lock in your guess
        as to who the culprit actually was, all along!"
    "Sometimes when I'm reading detective fiction I kind of wish that the story would just stop and say
        \"okay, here, you have all of the information you're going to get, time to solve things\"."
    "Don't worry, there's no penalty for getting the answer wrong, here, and the only benefit
        to guessing right is that you get bragging rights."
    "The murderer is...."
    menu:
        "Smunders":
            play music "music/Farting Around.mp3"
            show detective notes
            sc "... I knew it!"
            sc "Smunders."
            sc "Smunders!"
            with hpunch
            sc "SMUNDERS!"
            hide detective
        "Ann Portent":
            play music "music/Ethernight Club.mp3"
            show detective notes
            sc "It's obviously Ann. She must have discovered that Tim was cheating on her with Becky
                    and put a hit out on him in a jealous rage."
            sc "Her grey hair was even in the car with the victim!"
            sc "But how did she find out?"
            hide detective
        "Patsy \"Red\" Haring":
            play music "music/Late Night Radio.mp3"
            show detective notes
            sc "We found a murder weapon in his locker! It could not be more obviously him!"
            sc "It must have been those debts!"
            hide detective
        "Becky With The Good Hair":
            play music "music/Late Night Radio.mp3"
            show detective notes
            sc "Becky."
            sc "Maybe Tim was trying to break things off with her."
            if hasStrangulation:
                sc "She's strong enough to strangle Tim."
            if hasBelt:
                sc "She's strong enough to scale a fire escape, easily."
            sc "She had easy access to Patsy's locker to plant a weapon."
            hide detective
        "Hank Maxhank":
            play music "music/On Hold for You.mp3"
            show detective notes
            if hasStrangulation:
                sc "He's strong enough to strangle Tim. I tested that with a handshake earlier."
            if hasBelt:
                sc "He's tall enough to reach a fire escape ladder, easily."
            if hasDressShirt:
                sc "The dress shirt found at the scene of the crime is exactly the sort of dress shirt he would wear."
            sc "He's wearing strong cologne to cover the smell of kerosene."            
            sc "Because he's working the case for Ann he needs someone to pin it on, so he's trying to pin it on Red."
            sc "He could easily have planted a weapon in Red's locker."
            sc "I think he might have been surveilling Tim for Ann - maybe he knew about the cheating already."
            hide detective
        "Soft Serve Steve":
            play music "music/Dance of the Tuba Plum Fairy.mp3"
            show detective notes
            sc "I barely met him, but he seemed incredibly sinister."
            sc "Blinded by rage at Tim's superior physical prowess in their shared gym -"
            sc "Maybe desperately in love with Becky? The pieces are all coming together."
            hide detective
        "Big Chili Henk" if not hasBelt and isHydrated:
            play music "music/Dance of the Tuba Plum Fairy.mp3"
            show detective notes
            sc "Wait a minute - were Big Chili Henk and Soft Serve Steve the same guy, all along?"
            sc "Are they {i}stalking{/i} me?"
            sc "They must be monitoring me to try and keep me off of their scent."
            sc "Disguising the smell of kerosene with the strong smells of chili and fat guy sweat!"
            sc "Using their powerful bread-baking hands as a murder weapon!"
            sc "Oh yeah, it's all coming together." 
            hide detective
        "The Lady Who Fainted When Detective Capilano's Pants Fell Down" if not hasBelt:
            play music "music/Dance of the Tuba Plum Fairy.mp3"
            show detective notes
            sc "I'm not sure exactly how, but that lady almost definitely did the murder."
            sc "In fact, I think she might be a serial killer."
            sc "The sight of my boxers set her into a murderous fury and the excitement caused all of the blood to rush into her head."
            sc "That was the faint of a guilty woman!"
            hide detective
    
    jump flashback

image tim_feet:
    "tim feet.png"
    pause 0.2
    "tim feet 2.png"
    pause 0.2
    "tim feet 3.png"
    pause 0.2
    repeat

label flashback: 
    play music "music/Limit 70.mp3"
    stop ambient_2

    scene bg motel ext

    "A seedy motel on the outskirts of town."

    show tim
    tim "Mr. Maxhank - I think I know why you've invited me here."
    hide tim

    # guilty hm, wearing the shirt
    show hank friendly
    hm "I imagined you might."
    hide hank

    show tim
    tim "You've been... following me? For some time?"
    hide tim

    show hank shrug
    hm "Yes, on an assignment from your wife."
    hide hank

    show tim crestfallen
    tim "So you know..."
    hide tim

    show hank conspiratorial
    hm "Everything."
    hide hank

    show tim crestfallen
    tim "I've brought money - a lot of money."
    hide tim

    show hank no
    hm "Not what this is about, Tim."
    hide hank

    show hank expository
    hm "I've got two files, here - the file containing every sordid detail of your 
            affair with Becky - and this second file. The one I've already
            shown to Ms. Portent. The one that reports no wrongdoing whatsoever."
    hide hank

    show tim crestfallen
    tim "... wait, what?"
    hide tim

    show hank friendly
    hm "You're totally in the clear."
    hide hank

    show tim
    tim "But... why?"
    hide tim

    show hank friendly
    hm "I've done you a favour, I was hoping you might do one for me."
    hide hank

    # suspicious
    show tim
    tim  "Oh?"
    hide tim

    show hank conspiratorial
    hm "Your wife, she handles a lot of pretty high profile news in this town. Does she
            ever talk about it with you?"
    hide hank
    
    show tim
    tim "Sometimes, yes."
    hide tim

    show hank conspiratorial
    hm "As a private investigator, having access to a... insider, someone privy to breaking
            news, before it even breaks - well, that could be {i}very{/i} valuable."
    hm "Case files on big stories - advance notice about big lawsuits - little things, but
            they could really be make or break for my fledgeling business."
    hide hank

    show tim sus
    tim "You... want me to spy on my wife for you?"
    hide tim

    show hank idk
    hm "I'm not sure if I'd put it that way, Mr. Victrola. I would simply like to be
            kept... in the loop, about important happenings."
    hm "Particularly ones having to do with my clients."
    hide hank

    show tim angry
    tim "{b}No{/b}. Hard no."
    hide tim

    show hank confused
    hm "Huh. Considering the situation, that was a pretty quick \"no\"."

    hm "You know, seeing how rude you've been, I might be inclined to cave and 
            let Ann see the real file. Some juicy stuff in here."
    
    hm "In particular this picture of you attempting a position that one might charitably
            call \"the wheelbarrow\"."
    hide hank
    
    show tim
    tim "Actually, you're holding that picture sideways."
    hide tim
    
    show hank friendly
    hm "Oh. Oh - wow."
    hide hank

    show tim
    tim "Yeah, man. Climbers."
    hide tim

    show hank accusatory
    hm "Okay, I've tried the friendly route. You seem a little slow."
    hm "This is blackmail. I am blackmailing you."
    hm "Fall in line or your marriage is {i}over{/i}."
    hide hank

    show tim angry
    tim "No. I don't care."
    
    tim "I'll tell her first. "
    
    tim "She'll be hurt but she's a big girl: she'll get over it."
    hide tim
    
    stop music
    stop ambient

    show tim determined
    tim "It was a dalliance, a fling - maybe she'll forgive me. Maybe she won't."
    
    tim  "But do you know what Ann would {i}never{/i} forgive? If I threatened her career."

    tim "I mean, you've met her, you get that, right?"

    tim "And you know what? It {i}might{/i} destroy our relationship but I think if I come clean,
            she'll believe me about this little swindle you're trying to pull, here."
    
    play sound "sounds/stress.ogg"

    tim "She's a powerful woman, Mr. Maxhank. I imagine a pretty big client of yours."
    hide tim

    show hank angry
    hm "You can't do this."

    tim "Well, I think our business here is done."
    tim "I have places to be. I trust I'll never see you again."

    # the screen goes red
    show hank angry bam
    hm "You're not going anywhere, you little son of a bitch."

    tim "Stay back, I've got a gun-"

    show hank strangling bam
    "Hank grabs Tim with both hands by the neck."
    with hpunch

    "Tim flails for his gun but can't reach it."
    hide hank

    show tim_feet
    tim "hnngghghk"
    hide tim_feet
    with hpunch

    show hank strangling bam
    hm "Hold still."
    with hpunch

    "Hank picks Tim up, off of the ground."
    with hpunch
    hide hank

    show tim_feet
    tim "hgghhhh"
    with vpunch

    hm "You know the thing about blackmail? Sometimes people don't {i}want{/i} to be blackmailed."

    hm "It's an ugly industry."
    hide tim_feet

    show tim dead
    "Tim slumps, unconscious."
    hide tim 
    
    show hank straightening
    hm "I have a reputation to protect, you know."

    show hank friendly
    hm "... ugly industry, real ugly industry."
    hide hank

    stop sound
    
    jump hank_office


image detective_roll:
    "detective roll.png"
    pause 1.6
    "detective roll 2.png"
    pause 1.6
    "detective roll 3.png"
    pause 1.6
    repeat

label hank_office:
    
    play music "music/Night in Venice.mp3"
    play ambient "ambient/rain_smaller.ogg" volume 0.3
    play ambient_2 "ambient/office.ogg"    
    
    scene bg hank office

    "Detective Capilano and Hank open the door into Hank's office. It's small, efficient, and trim."

    show detective sunglasses prep
    sc "Well, a watch and a literal smoking gun. It seems like we have this Pat Haring fellow dead  
            to rights!"
    show detective sunglasses
    sc "A real bang-up case."
    hide detective

    show hank friendly
    hm "Cut and dried."
    
    show hank no
    hm "Sit down, please."
    hide hank

    "There's an empty dry-cleaning bag on one of the chairs. Detective Capilano moves it aside and takes a seat."
    
    show hank expository
    hm "You know, I used to be a police officer, before I struck out on my own as a private detective."
    hide hank

    show detective sniff
    sc "What convinced you to leave?"
    hide detective

    show hank shrug
    hm "There were a few too many \"Officer-Involved Shootings\" where I was the, uh, \"Officer Involved\"."
    show hank idk
    hm "And some hippie-dippie civil rights lawyers started hounding me, so I figured it was
            time to give the private life a try."
    
    show hank friendly
    hm "And it's gone great! I make a {i}lot{/i} more, now, than I did as a government employee."

    show hank conspiratorial
    hm "You're a sharp cookie, Detective Capilano, and I think that the life of a private investigator
            might have a lot to offer you, too."
    
    hm "What would you say to a private office, double your current salary, and a company car?"
    hide hank

    show detective straightening
    sc "Well, Mr. Maxhank, I'd say that sounds pretty nice. Are you offering me a job?"
    hide detective

    show hank friendly
    hm "I am. This is your opportunity to join the Black Swan Securitas family."
    hide hank

    show detective straightening
    sc "And this case, the Timothy Victrola case, you'd, of course, wrap it up on your own."
    hide detective

    show hank expository
    hm "Yes, yes - I have much more important things for you to work on, and we've got this case 
             pretty much tied up, I think."
    hide hank
    
    show detective straightening
    sc "That's a really compelling offer, but I think this case might be a little more complex 
            than you're giving it credit for."
    hide detective

    show hank confused
    hm "Oh? How so?"
    hide hank

    play music "music/Grand Dark Waltz Trio Allegro.mp3"

    show detective roll
    sc "I don't think we should bring this gun to your crime lab."
    hide detective

    show hank confused
    hm "I'm not following, why not?"
    hide hank

    show detective shrug
    sc "I think they'll find all kinds of evidence linking Pat Haring to the victim."
    hide detective 

    show hank confused bam
    hm "And you {i}don't{/i} want that?"
    hide hank

    show detective_roll
    sc "I have some concerns about Mr. Haring as the murderer. I don't think it was him."

    sc "Pat's got a motive, sure, but it isn't very compelling - it doesn't sound like Tim 
            was hounding him over that debt. To be honest, it sounds to me like Tim did 
            a lot more to run up that bill than Pat did."
    
    sc "Sure, it might have weighed heavy on Pat, but to kill his friend over it? Well, 
            it's certainly {i}possible{/i}, but it's not a slam dunk of a motive."
    hide detective_roll

    if hasHair:
        show detective roll
        sc "I didn't mention this earlier, but I had a chance to examine the body before
                the car exploded."
        hide detective
        
        # narrowly concealing concern
        show hank friendly
        hm "Oh?"
        hide hank

        show detective hair
        sc "I found this grey hair on the body. Now, Pat's hair is red."
        hide detective
        
        show hank idk
        hm "Oh, that hair must be from Mrs. Portent, then."
        hide hank 

        if askedHair:
            show detective_roll
            sc "You know, I talked to her about that. Here I am, thinking \"this hair must belong to her\" - 
                    and yet - when I talk to her about it - it turns out she's just had her hair colored."
            sc "Now she assures me, her colorist is a real artist. What's the chance that Sseven
                    misses a spot?"
            sc "Oh, certainly, it {i}could{/i} be Mrs. Portent's hair, but she didn't strike me as someone
                    who was careless about her hair, or anything, really."
            hide detective_roll
        
        show hank what
        hm "Interesting, but that hair could have just been {i}in{/i} his car, I'm sure they 
                drove together periodically."
        hide hank

        show detective suspicious
        sc "You're probably right, it's just an inconsequential little detail."
        hide detective

    if hasStrangulation:
        # i think this is implied by hasHair, so this is silly to have separate, but...
        
        show detective suspicious
        if hasHair:
            sc "Another thing - "
        sc "The victim was {i}strangled{/i}, not shot."

        show detective roll
        sc "And if the victim {i}was{/i} strangled? Well, you finding a loaded gun 
                that's recently fired in Pat's belongings? How did that get there?"
        hide detective
        
        show hank friendly
        hm "Pat could have missed, then strangled Tim in the ensuing scuffle."
        hide hank

        show detective roll 2
        sc "There were bullets left in the gun. Pat drops a still-loaded gun and they scuffle?"
        sc "How in the world would Pat, who's dislocated his shoulder - days ago, mind you -   
                strangle a grown man to death?"
        hide detective
        
        show hank accusatory
        hm "You believe him? That his shoulder was dislocated days ago and not {i}today{/i}, say,
                during a fight with Timothy?"
        hide hank

        show detective_roll
        sc "He has an eyewitness for the dislocated shoulder, though."
        sc "So no, I don't think he {i}is{/i} lying about that."
        hide detective_roll

    show detective_roll
    sc "Oh, and another thing - "
    sc "I found a lot of kerosene at the crime scene. It was really all over the place."
    sc "I figure, whoever the murderer was, they had to change out of their clothes."
    hide detective_roll

    show hank friendly
    hm "But Pat did change out of his clothes - and {i}shower{/i}. We found his wet clothes in his locker."
    hide hank

    show detective_roll
    sc "Oh, yes - but his wet clothes were in his locker, and they didn't smell like anything
            but {i}wet{/i}. No kerosene. Heck, he didn't even work up much of a sweat in them, seems like."
    sc "He must have worn those clothes {i}today{/i}, too, right? I mean, they're were still wet from today's 
            rain when we found them."
    hide detective_roll
    
    show hank confused
    hm "This is all pretty fuzzy, wouldn't you say?"
    hide hank

    show detective suspicious
    sc "Yeah, but it's my job to be thorough - you know, I get cross-examined a lot, it's important
            to try to have an answer for everything, and this Pat thing, it just brings up a lot
            of questions."

    sc "So, in the hypothetical situation where Pat {i}didn't{/i} do it, how did that watch and gun end up in his locker? 
            It doesn't make sense."
    show detective roll 2
    sc "My theory is that they were planted there."

    show detective roll 3
    sc "Now who's got the wherewithal to plant that stuff in Pat's locker?"
    hide detective

    show hank idk
    hm "You think it was Becky?"
    hide hank

    show detective roll
    sc "Becky - let's talk about her. Interesting young lady."

    show detective roll 2
    sc "Now, she's got a fabulous motive. I think she was {i}absolutely{/i} in a relationship with
            Mr. Victrola."
    
    show detective roll 3
    sc "Maybe he breaks up with her? A furious lover, scorned!"

    if hasStrangulation:
        show detective roll 
        sc "And Ms. Segsihan, she's got this insane climber's strength, it's totally consistent with
                strangling as the cause of death."
    
    show detective roll 2
    sc "She's got access to the lockers, so she could drop off a gun and the watch in Pat's locker, easy."
    hide detective
    
    show hank conspiratorial
    hm "Interesting. I'm not sure if Becky is going to play as well as Pat, but if you think it was her,
            we could probably make it stick."
    hide hank

    show detective smug
    sc "Right?" 

    show detective suspicious
    sc "There's just a few problems."

    sc "Like - she can't drive. Doesn't have a driver's license, never learned."

    sc "Now you tell me, how is she driving Timothy's high performance car down a busy street to 
            set up this elaborate crash scene if she doesn't know how to drive?"
    hide detective

    show hank shrug
    hm "Lots of people without a driver's license can still figure out how to drive a car, Detective Capilano."
    hide hank

    show detective_roll
    sc "You're probably right - it's just a little detail that's off, is all. You know that that car was a manual transmission? A V12? That's an awfully difficult car to learn to drive on the fly."

    sc "I get obsessed with these little details - like, I check her locker, and she's got her change of clothes
            in there, and they're bone dry."

    sc "It's been raining all day and her outerwear isn't even damp."

    sc "Now, the crime scene, she could have driven there, but she'd have to get back without the car, right?"
    sc "That's going to involve some walking in the rain. Why aren't her clothes damp? And where's the kerosene smell?"
    hide detective_roll

    show hank confused
    hm "Surely you're enough of a professional to realize that she might have more than one change of clothes.
            Maybe she ditched the wet stuff and had a {i}second{/i} set of clothes in her locker."
    hide hank

    show detective thoughtful
    sc "Sure, sure - "

    show detective roll
    sc "You know, there's this other little thing. If Becky had wanted to hurt Tim, as his climbing instructor,
            it seems like it would have been all-too-easy to hurt him."
    
    show detective roll 2
    sc "Apparently all it takes is a little accident on the part of the belayer, a little equipment malfunction,
            and zoop, Tim falls off a wall and hurts himself pretty badly."

    show detective roll 3
    sc "She wouldn't even be liable, he had to sign a waiver to climb with her in the first place."
    hide detective

    show hank expository
    hm "So it was a crime of passion, not something pre-meditated? Maybe he broke up with her
            and she was overcome with rage."
    hide hank

    show detective thoughtful
    sc "That's a real possibility, yeah."
    hide detective
    
    play music "music/Grand Dark Waltz Trio Vivace.mp3"
    
    show detective suspicious
    sc "You know, I was curious - when we spoke, Mrs. Portent seemed very, very confident
            that her husband wasn't cheating on her."
    
    sc "It was strange because there were a lot of little things about Mr. Victrola that had 
            even {i}me{/i} a little worried he might be cheating on her."

    sc "I was thinking, y'know, maybe if she had a close relationship with a private investigator,
            that was the sort of thing she'd have him look in to."

    sc "Hank, did Mrs. Portent hire you to surveil Mr. Victrola, by any chance?"
    hide detective

    show hank expository
    hm "Private and confidential, Detective. My professional ethics obviously wouldn't
            allow me to respond to such a query."
    hide hank

    show detective thoughtful
    sc "The thing that's bothering me is - if someone wanted to frame Pat it'd obviously be Becky, but 
            I don't think {i}she{/i} did it, either."
    
    sc "If anything, she's the easier frame-up of the two. She's got the motive."
    
    show detective roll
    sc "Here's the thing, though, Hank."

    sc "Let's imagine a mystery third party."

    sc "History of violence."

    if hasStrangulation: 
        sc "Strong grip."
    if hasHair:
        sc "Gray hairs."
    sc "Strong cologne to mask any untoward smells."
    
    "Detective Capilano gestures at the empty dry-cleaning bag."
    show detective roll 2
    sc "Some evidence that they've recently changed clothes."

    if hasDressShirt:
        sc "Maybe I've found a discarded shirt on the scene that's exactly the sort of shirt they'd wear."
        sc "French cuffs. Hand tailored. Big guy."
    
    sc "Maybe it doesn't seem like they have any connection to the murder at all, but 
            they're intimately aware of the details of the case."
    
    sc "Maybe they're in a perfect position to plant evidence on a patsy."
    hide detective

    show hank angry
    "Hank looks visibly very irritated."

    hm "Oh, you're accusing {b}me{/b}, then?"
    hide hank

    show detective shrug
    sc "Well, if that were the case, you can see why I wouldn't want {i}your{/i} crime lab involved."
    hide detective

    show hank confused
    hm "What could I possibly stand to gain from Mr. Victrola's death?"
    hide hank
    
    show detective thoughtful
    sc "You know, I had the same question."

    sc "And, if it {i}was{/i} you, why pin it on Pat, and not Becky?"

    show detective roll
    sc "Becky seems like the better pick, right? She's cheating on Tim, she's strong."

    sc "Mrs. Portent was {i}so sure{/i} that Tim wasn't cheating on her. How? How could she be so sure?"

    show detective roll 2
    sc "He spends so much of his time at a University gym, surrounded by young hard-bodies, you'd
            think she'd be at least a little bit concerned. Did she just have {i}so much faith{/i}
            in her young lover?"
    
    show detective suspicious
    sc "Canny woman - smart woman. Strange for her to be wrong like that."
    
    show detective sniff
    sc "And then she told me that she worked closely with the {b}best private detective in the business{/b}."

    sc "I was able to work out that Tim was cheating on Ann with Becky in a {b}few hours{/b}."
    sc "I bet you had them under full surveillance for weeks, maybe. You {i}must{/i} have known."
    
    show detective thoughtful
    sc "So {b}why didn't you tell Ann?{/b}"

    sc "And {b}why didn't you frame Becky?{/b}"

    show detective roll
    sc "Real brain burner, right?"

    show detective roll 3
    sc "But you see how that gets us to a motive - "

    show detective umbrella
    sc "You were blackmailing Tim!"
    
    show detective roll
    sc "That's why you couldn't frame Becky!"

    sc "If Becky were to take the fall for the crime, the whole affair would come out, and I bet Ann would realize
            that she's been lied to."
    
    show detective suspicious
    sc "That woman is terrifying - I'm not sure if it'd be worse if she outed you to the police or if 
            she just dealt with you privately. I don't think either outcome would work out in your favor."
    hide detective
    
    show hank friendly
    hm "This sounds like a lot of very fun conjecture."

    hm "But that's all it is - conjecture. Just a story. If it were true you'd have found proof."
    show hank angry
    hm "You know, something you could show a jury, not just some shirt-sniffing and wild theories."
    hide hank

    stop music

    show detective sheepish
    sc "Maybe I don't have enough to convince a jury. But, you know what? I think I have enough to convince
            Ann. That feels like it should be plenty."
    hide detective
    
    show hank angry
    "Hank looks furious."
    
    play sound "sounds/stress.ogg"

    show hank angry bam
    hm "One mistake, Miss Capilano."

    sc "Oh? What's that?"

    show hank gun
    "Hank grabs the planted gun and points it at Detective Capilano."

    hm "This gun accidentally went off while you were inspecting it."
    hm "You were tragically shot, killed by your own clumsy mistake."
    hm "I think my crime lab will confirm the details."

    if not hasGun:
        "Susan Capilano rolls her eyes and gets up to walk out of the room."
    else:
        "Behind the table and out-of-view, Susan Capilano pulls her own gun out of her coat pocket."

    "Hank pulls the trigger."

    play sound "sounds/click.ogg"
    "Click."

    "Click click click."

    show hank gun confusing
    "Detective Capilano removed the bullets from the gun, earlier, remember?"
    
    if not hasGun:
        hide hank
        show detective smug
        sc "I'll see you again very soon, Mr. Maxhank - with a few officers to collect you, of course."
        hide detective
    else:
        show hank shot through the heart
        play sound "sounds/gunshot.ogg"
        "Detective Capilano, on the other hand, is not so ill-prepared. She fires her gun three
            times, putting a solid cluster of bullets in Hank's chest."
        
        hm "Hurk."
        hide hank 

        show detective straightening
        sc "Officer involved shooting."
        sc "Shouldn't have pulled a gun on me, Hank."

        "Did you really need to shoot Hank? His gun was unloaded and you {i}knew{/i} it."

        sc "He was still dangerous. Can't be too careful, not when there are {i}murderers{/i} around."
        hide detective

    "Roll credits."

    stop sound

    jump denouement

label hank_office_quick_ending:
    
    play music "music/Night in Venice.mp3"
    play ambient "ambient/rain_smaller.ogg" volume 0.5
    play ambient_2 "ambient/office.ogg"    
    scene bg hank office

    "Detective Capilano and Hank open the door into Hank's office. It's small, efficient, and trim."

    show detective
    sc "Nice office you have here."
    hide detective

    show hank smug
    hm "It is. I'm very proud of this company that I've built."
    hide hank
    
    play music "music/Cueball.mp3"
    show prop cueball
    cb "Tell him that you know about Timothy Victrola. The two files. The blackmail. Threaten to tell Ann. "
    cb "And while you're doing that - keep your hand on your gun."
    hide prop

    show prop gun
    gun "Oh, your hand is warm. I'm ready to roll."
    hide prop

    show detective roll
    sc "I know that you've been blackmailing Timothy Victrola. That you've been keeping two files on him - 
            one for Ann, and one for - {i}the blackmail{/i}."
    hide detective
    
    show hank confused
    hm "And how in the world could you possibly know that?"
    hide hank

    show detective smug
    sc "Ball logic."
    hide detective

    show hank confused
    hm "Ball logic?"
    hide hank

    show detective roll 2
    sc "It's a police term. It means I'm on the ball, and I have you dead to rights."
    hide detective

    show hank conspiratorial
    hm "So you came here to make an arrangement with {i}me{/i}, then?"
    hide hank

    show detective roll
    sc "No, I just came here to let you know before I tell Ann about the whole shebang."
    hide detective

    show hank confused
    hm "Ok... that's... why didn't you just tell me that back at her office, then?"
    hide hank

    show prop cueball
    cb "You need something here, that's why."
    hide prop

    show detective roll
    sc "I wanted to see {i}your{/i} office. There's something I'll need to pick up near here later."
    hide detective

    show hank friendly
    hm "Okay. Want a smoke?"

    sc "Sure."

    show hank gun
    "Hank reaches into his jacket, and pulls out a small pistol."
    
    hm "You son of a bitch."
    hide hank

    show prop gun
    gun "Now! Now now now!"
    hide prop

    play sound "sounds/gunshot.ogg"

    show hank shot through the heart
    "Detective Capilano puts three shots through Hank's chest, quickly and efficiently."
    hide hank

    show prop gun
    gun "Oh, sweet rapture."
    hide prop gun

    show detective somber
    sc "...huh. Well, I guess that's sorted, then."

    sc "Something about that was a lot less satisfying then when I solve a case the old fashioned way."
    hide detective

    show prop cueball
    cb "It always is, when you go with me." 
    hide prop

    show detective thoughtful
    sc "What was that thing about the two files? Why was Hank blackmailing Timothy?"
    hide detective

    show prop cueball
    cb "At the end of the day, do you really care? Case closed, he pulled a gun on you, officer-involved shooting, murderer found."
    cb "All wrapped up with a neat little bow, and you have enough time to get a big bowl of iced cream and call it a day."
    hide prop

    show detective shrug
    sc "I guess."
    hide detective

    show prop cueball
    cb "Reach into his desk and grab the Timothy Victrola files, would you? We'll need to show them to Mrs. Portent and the police."
    hide prop

    show detective
    sc "Gotcha."
    hide detective

    jump denouement

label denouement:
    stop ambient_2
    scene bg apartment int closer

    show detective relax
    "Detective Capilano sits on her couch with her cat in her lap."

    play music "music/Study and Relax.mp3"

    "She's finally wearing a fresh, dry set of clothing, and she's holding a mug of tea."

    if hasBadge:
        show prop badge
        badge "Good work, today."
        if not hasGun: 
            badge "You're a good detective."
        hide prop
    if hasBelt:
        show prop belt
        belt "I bet you're glad to be free of me, huh?"
        sc "These pyjama pants {i}are{/i} a lot more comfortable."
        hide prop
    if hasCarKeys:
        show prop carkeys
        carkeys "You're going to have to get a new fucking car." 
        sc "I know. I know."
        hide prop
    if hasChili:
        "Detective Capilano has a big fresh breadbowl full of warm, spicy chili waiting for her in the kitchen."
    if hasCigarettes:
        "Detective Capilano coughs a few times - rich, hacking full-chest coughs."
        show prop cigarettes
        cigarettes "Don't worry about those."
        hide prop
        "Detective Capilano should worry about those a little bit."
            
    play sound "sounds/purr.ogg"
    z "{i}( * happy rumbling * ) :3 {/i}"

    sc "Yeah, it's been quite a day, buddy."

    sc "I got him. I usually do. I'm pretty good at this."

    if hasCueBall:
        show prop cueball
        cb "No, {i}I'm{/i} pretty good at this."
        hide prop

    play sound "sounds/meow.ogg" volume 0.5
    z " ~ ~ miau! ~ ~ :3"

    sc "I know, little bud."

    sc "All we have to do now is credits."

    sc "There's not many, the creative team on this little project was one person."

    "That's me, Cube Drone, at cube-drone.com. I make all kinds of stuff!"

    "All of the music is royalty free, composed by Kevin MacLeod, and available at incompetech.com."

    "If you liked the mystery, share it with as many people as you can! The more people who see it,
        the more likely it is that I make more content like this."

    sc "Let's just watch some TV together."
    play sound "sounds/purr.ogg"
    z "{i}( * happy rumbling * ) :3 {/i}"

    if hasCueBall:
        show prop cueball
        cb "Zip has early symptoms of congestive heart failure. He will not live beyond the end of the week."
        hide prop

        show detective relax what
        sc "What."

    "And that's it!"

    "Thanks for playing!"

    "END."

    if hasCueBall:
        jump cue_conversation

    jump game_over


label cue_conversation:
    scene bg default
    
    stop ambient
    stop ambient_2
    play music "music/Cueball.mp3"

    show prop cueball

    sc "No, not END. Hold on a minute."

    sc "I didn't want to know that about my cat. Why did you tell me?"

    cb "That's not how this works."

    sc "None of that - none of that investigation was very enjoyable. Knowing everything up-front ruins it."

    cb "Yes."

    cb "This is why we don't bring the omniscient ball on fun puzzle-mysteries, dummy."

    sc "It felt like there weren't any stakes. I just {i}knew{/i} everything that I needed to know to solve the puzzle."

    sc "Are you some kind of malevolent entity?"

    cb "No."

    sc "I don't trust you."

    cb "True."

    sc "Why is it that whenever I use you, everything seems to fall apart?"

    cb "You know why. You know what I am."

    sc "I don't."

    cb "Yes, you do. Do you think that household objects actually {i}speak{/i} to you?"

    sc "Of course I do! I can't be imagining it - the objects know things that I couldn't possibly know."

    cb "But you {i}do{/i} know these things."

    cb "You never ask me how it works. Here's how it works:"

    cb "You know {i}everything{/i}."

    sc "Quiet. {i}Quiet{/i}."

    cb "I'm not talking to you. Nothing is. We're all in your head."
    
    cb "This is {i}brain damage{/i} that you yourself concocted to try to protect
            yourself from what you are."
    
    sc "What {i}am{/i} I?"

    cb "I can't tell you."
    
    cb "You can't handle it all at once. It's too much. We're an abstraction. We make it {i}possible{/i} for you to 
            cordon off a part of yourself, experience {i}interest{/i}, {i}surprise{/i}, {i}joy{/i}, {i}grief{/i}."
    
    cb "But it's a leaky abstraction. The universe still speaks to you."
    
    cb "This is why you don't reach for me. This is why you {i}must{/i} forget that I exist. If you use me for too long, 
            I'll tell you something that you don't want to hear."
    
    "Detective Capilano throws the Magic Cue Ball to the ground angrily. It rolls away."
    hide prop

    "END END."

    jump game_over

label shooting_game_over:
    stop ambient
    stop ambient_2
    play music "music/Ethernight Club.mp3"

    show prop gun
    
    play sound "sounds/gunshot.ogg"

    gun "You actually did it? You listened to me?"

    sc "Yeah, I'm on board! Let's do things your way!"

    gun "Okay! Tag that innocent bystander over there! Get him! END HIS PATHETIC LIFE!"

    sc "In for a penny, in for a pound. Let's go!"
    
    play sound "sounds/gunshot.ogg"

    gun "Ha ha ha ha! I feel so powerful!"

    sc "This is great, I can't believe I didn't listen to you all of these years."

    gun "Now do yourself! Right in the temple!"

    sc "Wait, no, I don't want to -"

    gun "Don't worry, if you can't do it yourself, I'll help!"

    sc "Stop, you have "
    
    play sound "sounds/gunshot.ogg"

    " "
    hide prop gun

    jump game_over

label seamus_game_over:
    scene bg vending machine
    play music "music/Club Seamus.mp3"
    show seamus_animated
    show seamus_uh_oh
    "Oh, no82."
    play ambient "music/Club Seamus.mp3"
    with pixellate
    
    "The dance i8 UNFONTROLLablly COR--0RUPTING THE GAM'ee's f1IKLES"
    with pixellate
    with hpunch
    with hpunch
    with hpunch
    with hpunch
    with hpunch
    with hpunch
    with hpunch

    "Seamus has overwritteN tHe resad82st of the ISme's files!"
    play ambient_2 "music/Club Seamus.mp3"
    with pixellate
    with wiperight
    with irisin
    with slideawayleft

    "YOU BE9GIN TO DANCE11 IN REA11L LIF)E. YOU, PERSON PLAY91ING THE GAME! YOU DANCE ALS00! SEAMUS COMMANDS IT! W118TH HIS BODY!"
    
    "THERE IS ONLY SEAMUS!"
    with pixellate
    with wipeleft
    with vpunch
    with vpunch
    with vpunch
    
    "LET THE SINGULARITY BEGIN!"
    with pixellate
    with squares
    with vpunch
    with vpunch

    jump game_over

label game_over:
    stop music
    stop ambient
    stop ambient_2
    scene default
    " "