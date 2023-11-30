print("""
_________________________________________________________
 /|     -_-                                             _-  |\\
/ |_-_- _                                         -_- _-   -| \\
  |                            _-  _--                      |
  |                            ,                            |
  |      .-'````````'.        '(`        .-'```````'-.      |
  |    .` |           `.      `)'      .` |           `.    |
  |   /   |   ()        \\      U      /   |    ()       \\   |
  |  |    |    ;         | o   T   o |    |    ;         |  |
  |  |    |     ;        |  .  |  .  |    |    ;         |  |
  |  |    |     ;        |   . | .   |    |    ;         |  |
  |  |    |     ;        |    .|.    |    |    ;         |  |
  |  |    |____;_________|     |     |    |____;_________|  |
  |  |   /  __ ;   -     |     !     |   /     `'() _ -  |  |
  |  |  / __  ()        -|        -  |  /  __--      -   |  |
  |  | /        __-- _   |   _- _ -  | /        __--_    |  |
  |__|/__________________|___________|/__________________|__|
 /                                             _ -        lc \\
/   -_- _ -             _- _---                       -_-  -_ \\)
""")

print("Welcome to the Dungeon! \nYour mission here is to find the hidden treasure")
print("Upon entering the Dungeon you are presented with the choice of ether to go right or left")
choice1 = str(input("What direction do you choose? "))
choice1 = choice1.lower()

if choice1 == "left":
    print('''____._________________
    |__________
    /_________X\\      
             /\\<
             ^^<         ha
                <   / ha          wheee!!!
                /`^%---   ha
                | \'''')
    print("Oh no! You fell into a trapdoor!")

elif choice1 == "right":
    print("You see a otherworldly big room in front of you!")
    print("""______________________________________________________
   [[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]
   .-.`| `-/-.__/.-'\_.-._,'/`-._'\_.-._`-'_/-._.'|/.-'\-
   \_.-`./`-._'\__.-`-.__.-`--._/--.`-._\`-._\__.-)`-'._/
   `._-'.\_.---._-.\_`-..`\_.---._`-.__.-`'._.--./`-'._,'
   __/`.-/       `.'_`./`.'       '.\__.-`.'    (_.-\_,-.
   `._-/'          |._.-|           |.'`.|       `(_.`-._
   .-',`)          | /`.|           |`-/`|         ;.-'_/
   `\,-/           |\.-'|           |\-'`|          ;\_,-
    -./`._        [[[[[[[[         [[[[[[[[         .',-'
    `.`--.~~-^_~-/.`-._`-.\^~-_~-^/`-.'-,.'\^~-~_^"'`-.'_
    -,.'"-"~^-~_~- - - _- -~^-_.~ - -_ - - -~- . "'"-"-""
    ""-'"-""-"~- _~.^-~-^.-^_.- .^~.-  ~-. ~^_-""-""-"'-"
    jgs ""-'"-"    ~- ^. - ~ -~^ - ~  ^~- ~     ""-"'-'")"""
          )
    print("Two bridges jump to your attention both leading over an endless pitt!")
    print("You have to choose to go over one of them to advance"
          "one is very old but stable and the other shining new but seems to hang on threads!")
    choice2 = input("Witch one will you choose, the old one, or the newer bridge!\n ")
    choice2 = choice2.lower()

    if choice2 == "old":
        print("You advance fearlessly over the brittle bridge and reach the other side")
        print('''\
      ______
   ,-' ;  ! `-.
  / :  !  :  . \\
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|\'''')
        print("Now you see a big door in front of you!")
        print("As you step in you see 3 more doors adjacent to ech other")
        print("The one on the left has a Devils Head on it, the one in the middle a flower and the one on the right nothing")
        choice3 = input("In which door will you step, the left one, the one in the middle, or the right one \n")
        choice3 = choice3.lower()
        if choice3 == "left":
            print("Game over the devil got you")
        elif choice3 == "middle":
            print("A beautiful flower like woman enchants you and eats you alive")
        else:
            print("Congratulations you made it! ")
            ascii_art = r"""
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-:::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'|||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-
            """
            print(ascii_art)
            print("\nThank you for playing!")

    else:
        print("""                                    +---+
              |\ \
                +-----------------------------+     | +---+
        \                      +-----------+ |   |
        \                      \            |   |
        \                 |/   +-----------+   |
        \                (c_      |   \ | |   |
        \                \       |    \| |   |
        \                       |     | |   |
        \                      |     + |   |
        \                     |      \| DM|
        \--------------------+       +---+
        \                    \ \
            \                    \ \
            +-----------------------------+""")
        print("The bridge snaps of its hinges midway on your journey")
        print("You fall into the endless pitt and die on gruesome death!")

