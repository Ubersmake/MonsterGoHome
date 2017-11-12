# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Bus Driver")
define s = Character("Shopkeeper")

# The game starts here.

label start:

    $ communication = 0
    $ care = 0

    $ browsedMagazines = False
    $ browsedSnacks = False
    $ askedAboutTrain = False

    jump i1

label i1:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    "Your breath lingers in the morning air on your way to the bus stop."

    "There are fewer cars this early in the day."

    "The crows overhead chirp and cry with little competition from the world below them."

    "As the sun begins its lazy ascent the world begins to blend together in the same luminous haze."

    "It only takes a few minutes to walk from home to the bus stop."

    "Like most mornings, someone is already there."

    "You don't know his name, but you've seen him many times before."

    "Every time you've kept to yourself. Every time he has responded in kind."

    "Today he has a red knit cap on. A plaid scarf covers most of his neck and some of his mouth. It doesn't stop his breath from appearing in the crisp morning."

    menu:

        "A long overcoat covers the rest of him. He keeps his hands in his pockets. Like you."

        "Say \"Good morning\".":
            $ communication += 1
            jump goodmorning

        "Say nothing.":
            jump nothing

label goodmorning:

    "You try to say something, but the words never quite leave your lips."

    jump i2

label nothing:

    "You wonder if you should say something, but the words never appear in your head."

    "The birds have more to say, but not by much."

    jump i2

label i2:

    "Occasionally he pulls his phone out from his pocket. Each time he frowns before putting it away."

    "You wait in silence for a little while longer before the bus arrives."

    menu:

        "The sun has long since set by the time you return."

        "It was a long day at the office.":
            jump office

        "It's been a long day of classes.":
            jump classes

        "It was a long day.":
            jump longday

label office:

    menu:

        "Reviews are scheduled for the end of the month."

        "Maybe it's time to go":
            $ care += 1
            jump i3

        "Maybe you'll stick around just a little bit longer.":
            jump i3

label classes:

    menu:

        "There are a few tests around the corner."

        "Maybe you'll study some more tonight.":
            jump i3

        "Maybe you'll take it easy for once.":
            $ care += 1
            jump i3

label longday:

    "Errant thoughts race through your mind, all of which go nowhere."

    menu:

        "It hurts to think. It's been that sort of day."

        "You wonder where you're going with your life.":
            jump i3

        "You wonder what tomorrow will bring.":
            $ care += 1
            jump i3

label i3:

    "The lights guide the way home, casting dim warm circles on the cold concrete."

    jump ii1

label ii1:

    "A few blocks later you pass by another stop and spot a small monster sitting on a bench."

    "It notices you with its unblinking eye, a glowing red circle that takes up most of its body."

    "\"Body\" is a generous word. The amorphous blob is a perfect sphere most of the time. Patches of tiny needles shift and extend here and there as it \"breathes\"."

    menu:

        "If it stood up off the bench the monster would barely reach up to your knees."

        "It's been a while since you've seen a monster.":
            jump seen

        "It's been a while since you've read about monsters.":
            jump read

label seen:

    "There used to be more of them, but they mostly keep to themselves these days."

    jump ii2

label read:

    "There used to be more of them, but that was a long time ago."

    jump ii2

label ii2:

    menu:

        "It continues to eye you."

        "Wave your hand.":
            $ communication += 1
            jump wave

        "Continue walking.":
            jump walk

label wave:

    "The monster does its best to imitate you."

    jump ii3

label walk:

    "As you pass by you hear a keening noise."

    "You look back and see that the monster has moved to the base of the bus sign."

    jump ii3

label ii3:

    "A tendril or spine appears from the top of the creature and touches the schedule posted near the base of the sign."

    "For people, even children, it would be easy to read."

    menu:

        "You're not sure what compels you to approach."

        "Maybe it was curiosity.":
            $ communication += 1
            jump ii4

        "Maybe it was fear.":
            jump ii4

label ii4:

    "You look into the monster's one eye and part of you feels like you're slipping away."

    "Instinctively you grab onto the nearest thing to brace yourself."

    "As you turn your head you notice that your hand is near the monster's tendril, and that it is seemingly pointing at the map."

    "It's waiting at the wrong stop."

    menu:

        "You look down and wonder how the monster must feel."

        "It must be scared.":
            $ care += 1
            jump iii1

        "It must be lonely.":
            $ communication += 1
            jump iii1

label iii1:

    "As the evening wears on you find yourself waiting at a disused bus stop a little closer to home."

    "The sign has script you can't read, but the monster seems excited."

    menu:

        "You're still not sure if it can communicate, but the movement of spines across its otherwise smooth body seem to betray its feelings."

        "It seems thankful.":
            jump iii2

        "It seems relieved.":
            jump iii2

label iii2:

    "Another bus comes by. This one seems more dilapidated than the others around the neighborhood."

    "The door opens and the monster squeezes to fit through."

    "The driver stares at you with its cold eyes."

    "From far away it would look like any other bus driver. The same tan uniform. The same tan hat with the name and logo of the transit company stitched on the front."

    "From the sidewalk it stares through you with its vacant, milky eyes."

    "Another keening noise scrapes across your mind. When you recover you notice the driver looking at the monster."

    menu:

        b "\"Get on,\" he says without any emotion."

        "Get on.":
            jump board

        "Step back.":
            jump endinga

label board:

    "The doors shut behind you and the monster eagerly sits on one of the seats."

    jump iii3

label iii3:

    "You stare out the window at the houses slipping into and out of view."

    "Before you can ruminate on how you ended up on a strange bus with a strange monster the bus stops in front of a rather large station."

    "The driver speeds off leaving you and the monster in the orange glow of a brick building out of place and time."

    jump iv1

label iv1:

    "The monster is clearly more familiar with the station than you are."

    "Through the front door is a platform lined with benches. Beyond that is a rail that seems to stretch on forever."

    menu:

        "You sit down and watch the monster talk to something behind a window. It slides back to you and presents a ticket."

        "Take it cautiously.":
            $ communication += 1
            jump caution

        "Take it angrily.":
            jump anger

label caution:

    "You weren't aware that humans were allowed here."

    jump iv2

label anger:

    "You weren't pleased to be somewhere you shouldn't."

    jump iv2

label iv2:

    "The clock on the other side of the platform ticks away."

    "You notice that one of the kiosks has someone behind it."

    jump kiosk

label kiosk:

    menu:

        "Without anything else to do you approach. The woman behind it seems human."

        "Browse through the magazines." if browsedMagazines == False:
            $ browsedMagazines = True
            jump kioskMagazines

        "Browse through the snacks." if browsedSnacks == False:
            $ browsedSnacks = True
            jump kioskSnacks

        "Ask about the train." if communication >= 3 and askedAboutTrain == False:
            $ askedAboutTrain = True
            jump shopkeeper1

        "Walk away":
            jump iv3


label kioskMagazines:

    "Most of them are out of place. Some seem plucked out of the previous century. Others are printed on impossible paper."

    jump kiosk

label kioskSnacks:

    menu:

        "There are assorted candies and chocolates."

        "Buy something for yourself.":
            jump snacksForYourself

        "Buy something for the monster.":
            jump snacksForMonster

        "Buy something for the both of you." if care >= 2:
            jump snacksForBoth

label snacksForYourself:

    "After some pointing and a brief exchange you have something sweet in your pocket."

    jump kiosk

label snacksForMonster:

    "After some pointing and a brief exchange you have something you hope the monster will like."

    jump kiosk

label snacksForBoth:

    "After some pointing and a brief exchange you have something sweet to split between yourself and the monster."

    jump kiosk

label shopkeeper1:

    menu:

        s "\"A human?\" she softly exclaims. \"We don't get too many of you around here.\""

        "You're human.":
            jump shopkeeperHuman

        "You're human?":
            jump shopkeeperNotHuman

label shopkeeperHuman:

     s "She smiles. \"Human enough.\""

     jump shopkeeper2

label shopkeeperNotHuman:

    s "She laughs. \"Human enough.\""

    jump shopkeeper2

label shopkeeper2:

    menu:

        s "\"What brings you out here? Nothing beyond but the Sidereal.\""

        "\"I'm here with the...monster?\"":
            $ communication += 1
            jump shopkeeperNotMonster

        "\"I'm here with the monster.\"":
            jump shopkeeperMonster

label shopkeeperNotMonster:

    "She notices the creature sitting on the bench."

    s "\"Ahh. Well, I guess you don't have any better words for us.\" She shrugs."

    s "\"Qu'arn. No. Don't try to pronounce it. No one over there can \"speak\" anyway.\""

    jump shopkeeper3

label shopkeeperMonster:

    "She takes note of the creature sitting on the bench."

    s "\"Qu'arn.\" She shrugs."

    s "\"Don't bother trying to pronounce it. No one over there can \"speak\" anyway.\""

    jump shopkeeper3

label shopkeeper3:

    menu:

        s "\"Not too many of them here. A little difficult for them to blend in.\""

        "\"What about you?\"":
            jump shopkeeperYou

        "\"You seem to be doing well.\"":
            jump shopkeeperWell

label shopkeeperYou:

    "She smiles."

    "For a moment you glimpse a toothy grin stretching from ear to ear, but only for a moment."

    s "\"It's a job, I guess.\""

    jump shopkeeper4

label shopkeeperWell:

    "She chuckles."

    "For a moment you glimpse a toothy grin stretching from ear to ear, but only for a moment."

    s "\"Thanks.\""

    jump shopkeeper4

label shopkeeper4:

    menu:

        "\"You ever been?\""

        "\"No.\"":
            $ communication += 1
            jump shopkeeperNo

        "\"No.\" (Lie.)":
            jump shopkeeperLie

label shopkeeperNo:

    "She laughs a bit."

    s "\"Of course not. Very few people go.\""

    s "\"It'll seem unsettling at first, but most of us feel the same way about this place when we first arrive.\""

    jump shopkeeper5

label shopkeeperLie:

    "You see a flash of that unsettling grin again."

    s "\"You don't have to be so...human.\""

    s "\"It's not so bad.\""

    jump shopkeeper5

label shopkeeper5:

    "She turns around and, after going through some drawers, produces a worn down book about as large as a cheap paperback."

    "The binding is worn down in several places, and the corners of every other page seem to have been bent in both directions."

    s "\"We don't make too many of these anymore. So just...bring it back, OK?\""

    "She opens up the book to a specific page after blowing off the thin layer of dust that had accumulated on the front cover."

    s "\"There's a phrasebook of sorts near the end. No one \"speaks\" over there, so the gestures it tells you to make are a little out of date.\""

    s "\"There's some history near the front, but what you really want is this.\""

    "She points to maps printed on a few dozen pages before closing the book and sliding it toward you."

    s "\"We smile, too.\""

    "As she says that you can feel the vibrations of the approaching train in your bones."

    jump kiosk

label iv3:

    "The monster, which has since moved from the seat to the edge of the platform, seems excited."

    "The train arrives in a plume of white smoke."

    "You board with the monster with the ticket in your hand. After entering the cabin you notice the ticket is gone."

    "The cabin is empty. Before you can take your seat the train begins to accelerate in a cacophony of smoke and screeching."

    "Outside the world seems to fade away into a distant void."

    jump v1

label v1:

    "You wonder why they call it the Sidereal when you pass through a tunnel and emerge in a truly different place."

    "Whenever you turn the sky seems to turn with you."

    "Here the stars are fixed in place. Off in the distance are two tiny suns set in front of a nebulous pink sky."

    menu:

        "You notice a series of spines emerging and retracting from the monster. Its gaze is set toward the horizon that isn't there."

        "\"Is this home?\"":
            jump endingb

        "\"Welcome home.\"":
            jump endingb

label endinga:

    "You step back. The driver shakes his head. The doors close and the bus slowly speeds away."

    menu:

        "You can see the monster looking at you from the rear window before the bus turns the corner."

        "You wonder if the monster made it home.":
            jump end

        "You wonder if you should go home.":
            jump end

label endingb:

    "Welcome to the Sidereal."

label end:

    "To Be Continued."

    # This ends the game.

    return
