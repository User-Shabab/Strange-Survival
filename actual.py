import random
import time

def credits():
    nok0 = True
    nok1 = True
    while nok0:
        while nok1:
            time.sleep(1)
            border()
            print("CREDITS:")
            time.sleep(1)
            print("  ")
            time.sleep(1)
            print("Wu Ming: Main and overall developer; Development\n"
            "Pingu: Ideas for introduction script; Innovation\n"
            "Phoenix: Ideas for breakoff and repeat functions; Innovation\n")
            nok1 = False
    
def border():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def dead():
    print('''
    You lose all your lives, hence ending the game.
          _______     
         /       \    
        | (X) (X) |   
         \   ^   /    
          !|||||!     
         '\_____/'    

    ''')
    print(" ")
    credits()


def life_x():
    if lives == 3:
        print(f"---¥¥¥~~~You have {lives} lives left.~~~¥¥¥---\n")
    if lives == 2:
        print(f"---¥¥~~~You have {lives} lives left.~~~¥¥---\n")
    if lives == 1:
        print(f"---¥~~~You have {lives} lives left.~~~¥---\n")
    if lives == 0:
        print(f"---~~~You have {lives} lives left.~~~---\n")

def win():
    runs0 = True
    runs1 = True
    while runs0:
        while runs1:
            print(" ")
            print(" ")
            print("Well done!!! You have lived through, and won the game!")
            print("Thank you for playing the game")
            border()
            credits()
            runs1 = False
            
def dayR1(l):
    time.sleep(2)
    print("After a few days you go to your grandfather's grave to give a visit.")
    print("It's in Athens, Greece.")
    print("You are in Istanbul, do you fly there or drive there?")
    time.sleep(2)
    ans = input("Type 'y' for flying and 'n' for driving_")
    print(" ")
    border()
    time.sleep(2)
    # 2 lives
    if ans == 'y':
        print("You were killed by anti aircraft guns.")
        print("You then lost another life by being shot by the soldiers.\n")
        l = l - 2
        time.sleep(2)
        print(f"--~~~You have {l} lives left.~~~--")
        return l
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DEAD
    elif ans == 'n':
        time.sleep(2)
        print("You arrive and mourn.")
        print("You also realise that you accidentally prayed to the wrong grave, in Ulaanbatar, a very hisotrical city.")
        time.sleep(2)
        print("However, from locals, your pet horse was involved with something paranormal around here, so do you stay?")
        time.sleep(2)
        ans = input("Type 'y' for Istanbul and 'n' for Ulaanbatar_")
        time.sleep(2)
        border()
        if ans == 'y':
            time.sleep(2)
            print("You go back to Istanbul")
            print("As you land in Istanbul and get out of the car,")
            time.sleep(2)
            print("You suddenly see a person in full black running at you with a knife.")
            time.sleep(2)
            print("What do you do?")
            time.sleep(2)
            ans = input("Type 'y' for Taekwondo-Jitsu, 'n' for Hybrid martial arts, or 'p' for running away_")
            time.sleep(2)
            border()
            time.sleep(2)
            if ans == 'y':
                print("He throws the knife at you and you lose a life.")
                l = l - 1
                time.sleep(2)
                print("Suddenly you wake up in a coffee shop and get drowned in coffee by the same man.")
                l = l - 1
                time.sleep(2)
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DEAD
            elif ans == 'n':
                time.sleep(2)
                print("You're a bit rusty, but you successfully fend off the man, who runs away, dropping the knife.")
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~RETURN TO MAIN CODE
            elif ans == 'p':
                time.sleep(2)
                print("The man chases you down, and stabs you to death, making you lose a life.")
                print("The bleeding and loss of blood also take away another life, coz why not, I'm outta ideas here.")
                time.sleep(2)
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DEAD
                l = l - 2
                time.sleep(2)
        elif ans == 'n':
            #1 lives
            print("Your pet horse kills you because it wanted to go back home, and pet food sucks there.")
            time.sleep(2)
            l = l - 1
            print(f"--~~~You have {l} lives left.~~~--\n")
            # coconut number was chosen depending on how many lines there were in code at that time
            print("Suddenly, out of no where, you notice 355 coconuts being thrown at you.")
            print("You have about 100 baskets that can fit 2 coconuts each, and about 140 hungry crabs in your pocket.")
            print("Do you risk your life by trying to fend off from this coconut attack, or retreat and hide?")
            ans = input("Type 'y' for fend off, 'n' for hide_")
            border()
            chance = random.randint(1, 10)
            if chance >= 7 and ans == "y":
                print("Well done! You successfully collect all the coconuts and the crabs eat the rest.")
                print("However, as you're walking back to the city, you see a man, who must've been hurt by coconuts.")
                ans = input("Type 'y' to help him, or 'n' to leave him_")
                border()
                time.sleep(2)
                if ans == "y":
                    print("What a kind heart you have, yet such an unlucky fate...")
                    time.sleep(2)
                    print("The man was dead all along, and you have awoken and disturbed his evil soul.")
                    time.sleep(2)
                    print("You have started the zombie apocalypse in Mongolia, and lose all your lives,")
                    print("because he bites you and turns you into the walking dead as well\n")
                    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DEAD
                    l = 0
                if ans == "n":
                    print("The man, named Billy George Jay, nearly died, but survived in the end.")
                    print("He seeks long term revenge on you now. Way to go, making enemies eh?")
                    #MADE ENEMY FOR THE FUTURE
                    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~RETURN TO MAIN CODE
                    time.sleep(2)
            elif chance < 7 and ans == "y":
                print("Despite your hardest efforts, there were 2 coconuts left, which hit you on the head at light speed.\n")
                time.sleep(2)
                l = l - 1
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DEAD
                print(f"--~~~You have {l} lives left.~~~--\n")
            elif ans == "n":
                time.sleep(2)
                print("Your coward-like action got you kicked out of Mongolia and shot on the way back.")
                l = l - 1
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DEAD
                print(f"--~~~You have {l} lives left.~~~--\n")

    return l

def dayR2(l):
    ######################### STILL IN CONSTRUCTION
    print("Suddenly, you wake up into an ancient land, and a higher life form appears in front of you...\n")
    print('''
        ::::::::|/''"""'""""-:;:::::::       
        :::::|-`               "-;::::       
        ::::;_       _,,._       ¬;:::       
        ::::_       .::::::,       '::       
        :::::       :::::::;.       |:       
        ::::: ,.      ¬:::::;.       :       
        :::;           ,,:::::;      :       
        ::.  :.:        .::::::, _::,:       
        ::   :|:,      _:::::::::::-;:       
        ::-.;::|:      ¬::::::: |::;.:       
        ::;:_'---'     ;;'"¬--   :::::       
        ::; '|          ;     :  |::::       
        ::| ,:___..`           _; ::::       
        :::..::: '             -" ::::       
        :::;'::                  /::::       
        ::::,''              .__::::::       
        ::::;.            ._::::::::::       
        ::::;           __::::::::::::       
        :::::;_____    '::::::::::::::       
        :::::::::::;,   ::::::::::::::       
        ::::::::::::;   ¬:::::::::::::       
        ::::::::::::/ '  ::: :::::::::       
        ::::::::|-::        ::::::::::       
        ::::#-""- :::      .'::|"---""       
        :|-'  ___,:::,    .|.¬- __,.::       
                  
            - Ernest Khalimov, Gigachad
    ''')
    time.sleep(2)
    return l
    

def dayR3():
    pass
    # still in development...
    # print("You get bored waiting at a gas station,")
    # print("So now you can either play something on your phone,")
    # print("Or listen to some downloaded music on  an mp3")
    # ans = input("Type in 'y' for games, and 'n' for music_")
    # border()
    # lives = 0
