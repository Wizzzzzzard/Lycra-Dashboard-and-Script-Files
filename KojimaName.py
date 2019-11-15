from random import seed
from random import randint
import time
import sys

def dice_roll(dice_num, dice_side):
    seed(a = time.gmtime())
    for _ in range(dice_num):
        value = randint(1, dice_side)
    return value

def wait(seconds):
    i = 0
    while i < 1:
            time.sleep(seconds)
            i +=1

# Section 1: Determines how many names you'll have

print("Section 1: Determining How Many Names You Have\n")
print("Kojima often creates characters that have many alternate names, so we must first figure out how many names you will have.")

x = dice_roll(1,6)
if x <6:
    NameNum = 1
    print("You have one name!")
elif x == 6:
    NameNum = 6
    print("You have one name + six other alternative names!")
else:
    print("Error: The random number generator has been compromised by the Patriots!")

wait(2)

# Gathers the answers to Section 2 of the Quiz

print("\n\n\n")
print("Section 2: Personal Information\n")
print("Kojima’s characters have names that are directly related to their own character traits. \nThis information will make sure your name fits your personality")

Sec2Quest1a = input("\nWhat is your firstname? ")
Sec2Quest1b = input("\nWhat is your surname? ")
Sec2Quest1 = Sec2Quest1a + " " + Sec2Quest1b
Sec2Quest2 = input("\nWhat do you do at your occupation? ")
Sec2Quest2a = input("\nCondense the verb in your answer into a single -er noun. (e.g. if you are a sheep farmer, your answer will be “farmer”) ")
Sec2Quest3 = input("\nWhat was your first pet’s specific species/breed? If you never had a pet, please answer with an animal you wish you owned. ")
Sec2Quest4 = input("\nWhat’s your most embarrassing childhood memory? Be specific. ")
Sec2Quest4a = input("\nCondense this story into two words. ")
Sec2Quest5 = input("\nWhat is the object you’d least like to be stabbed by? ")
Sec2Quest6 = input("\nWhat is something you are good at? (Verb ending in -ing) ")
Sec2Quest7 = input("\nHow many carrots do you believe you could eat in one sitting, if someone,like, forced you to eat as many carrots as possible? ")
Sec2Quest8 = input("\nWhat is your greatest intangible fear? (e.g. death, loneliness, fear itself) ")
Sec2Quest9 = input("\nWhat is your greatest tangible fear? (e.g. horses) ")
Sec2Quest10 = input("\nWhat is the last thing you did before starting this worksheet? ")
Sec2Quest11 = input("\nWhat condition is your body currently in? (single word answer) ")
Sec2Quest12 = input("\nFavorite state of matter? ")
Sec2Quest13 = input("\nA word your name kind of sounds like? (e.g. Brian -> Brain) ")
Sec2Quest14 = input("\nWhat is your Zodiac sign? ")
Sec2Quest15 = input("\nIf you had to define your personality in one word, what would it be? ")

wait(2)

# Gathers the answers to Section 3 of the Quiz

print("\n\n\n")
print("Section 3: Kojima Information\n")
print("Kojima character names reflect his own idiosyncrasies. He can’t help himself. ")

Sec3Quest16 = input("\nWho is your favorite film character? (NOTE: must be played by Kurt Russell) ")
Sec3Quest17 = input("\nWhat is the last word of the title of your favorite Kubrick film? ")
Sec3Quest18 = input("\nWhat is the first word in the title of your favorite Joy Division album? ")
Sec3Quest19 = input("\nWhat is a scientific term you picked up from listening to NPR once? ")
Sec3Quest20 = input("\nWhat is a piece of military hardware you think looks cool even though war is bad? ")
Sec3Quest21 = input("\nWhat is something you’d enjoy watching Mads Mikkelsen do? ")
Sec3Quest21a = input("\nPlease condense into one word. ")

wait(2)

# Gathers the answers to Section 4 of the Quiz

print("\n\n\n")
print("Section 4: Determining Your Name Conditions\n")
print("Sometimes, a character will have a plot-based condition that affects their name.\nYou, too, might have a condition that affects your name.\nConditions can stack, so please make note of how many your name has.")
Name = Sec2Quest1
print("\nThe Man Condition")
x = dice_roll(1,4)
if x <=3:
    ManNum = 0
    ManCond = ""
    print("You do not have this condition.")
    Name = Name + ManCond
elif x == 4:
    ManNum = 1
    print("You have this condition. Your last name will include the suffix-man. \nIf your name already has -man at the end of it, I guess you’re just going to have -manman at the end of your name.")
    ManCond = "man"
    Name = Name + ManCond
else:
    print("Error: The random number generator has been compromised by the Patriots!")

print("\nThe Condition Condition")
x = dice_roll(1,8)
if x <=5:
    CondNum = 0
    CondCond = ""
    Name = CondCond + Sec2Quest1
    print("You do not have this condition.")
elif x == 6:
    CondNum = 6
    print("You’re big. Your name must have “Big” at the beginning of it")
    CondCond = "Big"
    Name = CondCond + Sec2Quest1
elif x == 7:
    CondNum = 7
    print("You are older than you once were. Your name must have “Old” at the beginning of it.")
    CondCond = "Old"
    Name = CondCond + Sec2Quest1
elif x == 8:
    CondNum = 8
    print("You are how you currently are.")
    CondCond = ""
    Name = Sec2Quest11 + Sec2Quest1
else:
    print("Error: The random number generator has been compromised by the Patriots!")

print("\nThe Clone Condition")
x = dice_roll(1,12)
if x <=11:
    CloneNum = 0
    print("You do not have this condition.")
    CloneCond = ""
elif x == 12:
    CloneNum = 12
    CloneCond = input("You are a clone of someone else, or you have been brainwashed into becoming a mental doppelganger of someone else. Findsomeone who has completed this worksheet and replace 50% ofyour Kojima name with 50% of their Kojima name.")
    Name = Name + CloneCond
else:
    print("Error: The random number generator has been compromised by the Patriots!")

print("\nThe Kojima Condition")
x = dice_roll(1,100)
if x !=69:
    KojimaNum = 0
    print("You do not have this condition.")
elif x == 69:
    KojimaNum = 1
    print("Oh no. You are Hideo Kojima. Hideo Kojima created you and is also you. \nYou are the man who created himself and there is nothing you can do about it. \nYou’re in Kojima’s world—your world—and that’s just the breaks, pal. \nStop this worksheet now. \nYou’re Hideo Kojima.Go do the things that Hideo Kojima does.")
    Name = "Hideo Kojima"
else:
    print("Error: The random number generator has been compromised by the Patriots!")

wait(2)

# Decides Your Name category

print("\n\n\n")
print("Section 5: Determining Your Name Category\n")
print("Kojima names fall into a finite number of categories.This section will determine the category in which your name belongs. \nNOTE:If you have a name + 6 alternate names, you will do this section once to find your true name,\nand then you will have an alternate name in every other category.")

x = dice_roll(1,20)
if x == 1:
    NameCat = 1
    print("You have a NORMAL NAME.")
elif x > 1 and x < 7:
    NameCat = 2
    print("You have an OCCUPATIONAL NAME")
elif x > 6 and x < 11:
    NameCat = 3
    print("You have a HORNY NAME")
elif x > 10 and x < 14:
    NameCat = 4
    print("You have a THE NAME")
elif x > 13 and x <18:
    NameCat = 5
    print("You have a COOL NAME")
elif x == 18 or x == 19:
    NameCat = 6
    print("You have a VIOLENT NAME")
elif x == 20:
    NameCat = 7
    print("You have a NAME THAT LACKS SUBTEXT")
else:
    print("Error: The random number generator has been compromised by the Patriots!")

wait(2)

# This step takes places if you have a Normal Name
if NameNum == 6 or NameCat == 1:
    print("\n\n\n")
    print("Section 6: NORMAL NAME\n")
    print("Kojima’s early work includes lots of characters that have names that are widely considered to be “normal.” \nWas this just because, in the early years, he didn’t have the power to say,\n“I’m Hideo Kojima, I can name someone Die-Hardman if I want to” without people questioning him? \nProbably.")
    NormalName = Name
    print("NORMAL NAME: Your name is " + str(NormalName) + ". That’s your name. \nYour Kojima name is probably just your actual name. Sorry if you were expecting something wild")
    Name = NormalName
    wait(2)
# This step takes place if you have an Occupational Name
if NameNum == 6 or NameCat == 2:
    print("\n\n\n")
    print("Section 7: OCCUPATIONAL NAME\n")
    print("Kojima’s characters tend to be driven by the work that they do.That often carries over to their names. You, too, can be nothing more than your job.")
    x = dice_roll(1,4)
    if x == 1:
        Name = Sec2Quest15 + Sec2Quest2a
        OccupationalName = CondCond + Name + CloneCond + ManCond
        print("OCCUPATIONAL NAME: Your name is " + str(OccupationalName) + ". That’s your Kojima name")
    elif x == 2:
        Name = Sec2Quest6 + Sec2Quest2a
        OccupationalName = CondCond + Name + CloneCond + ManCond
        print("OCCUPATIONAL NAME: Your name is " + str(OccupationalName) + ". That’s your Kojima name")
    elif x == 3:
        Name = Sec2Quest13 + Sec2Quest2a
        OccupationalName = CondCond + Name + CloneCond + ManCond
        print("OCCUPATIONAL NAME: Your name is " + str(OccupationalName) + ". That’s your Kojima name")
    elif x == 4:
        Name = Sec3Quest16 + Sec2Quest2a
        OccupationalName = CondCond + Name + CloneCond + ManCond
        print("OCCUPATIONAL NAME: Your name is " + str(OccupationalName) + ". That’s your Kojima name")
    Name = OccupationalName
    wait(2)
# This step takes place if you have a horny name
if NameNum == 6 or NameCat == 3:
    print("\n\n\n")
    print("Section 8: HORNY NAME\n")
    print("Kojima’s characters and stories are irrevocably horny. Weirdly horny, sure, but horny nonetheless.")
    x = dice_roll(1,4)
    if x == 1:
        Name = Sec2Quest12 + Sec2Quest3
        HORNYName = CondCond + Name + CloneCond + ManCond
        print("HORNY NAME: Your name is " + str(HORNYName) + ". That’s your Kojima name")
    elif x == 2:
        Name = "Naked " + Sec2Quest3
        HORNYName = CondCond + Name + CloneCond + ManCond
        print("HORNY NAME: Your name is " + str(HORNYName) + ". That’s your Kojima name")
    elif x == 3:
        Name = Sec2Quest6 + Sec2Quest3
        HORNYName = CondCond + Name + CloneCond + ManCond
        print("HORNY NAME: Your name is " + str(HORNYName) + ". That’s your Kojima name")
    elif x == 4:
        Name = Sec2Quest14 + Sec2Quest3
        HORNYName = CondCond + Name + CloneCond + ManCond
        print("HORNY NAME: Your name is " + str(HORNYName) + ". That’s your Kojima name")
    Name = HORNYName
    wait(2)
# This step takes place if you have a the name
if NameNum == 6 or NameCat == 4:
    print("\n\n\n")
    print("Section 9: THE NAME\n")
    print("Kojima loves to make people have names that start with the word “The” and they usually symbolise fears or unstoppable forces. \nYou are now that unstoppable force.")
    x = dice_roll(1,4)
    if x == 1:
        Name = "The" + Sec2Quest8
        THEName = CondCond + Name + CloneCond + ManCond
        print("THE NAME: Your name is " + str(THEName) + ". That’s your Kojima name")
    elif x == 2:
        Name = "The" + Sec2Quest9
        THEName = CondCond + Name + CloneCond + ManCond
        print("THE NAME: Your name is " + str(THEName) + ". That’s your Kojima name")
    elif x == 3:
        Name = "The" + Sec2Quest4a
        THEName = CondCond + Name + CloneCond + ManCond
        print("THE NAME: Your name is " + str(THEName) + ". That’s your Kojima name")
    elif x == 4:
        Name = "The" + Sec3Quest20
        THEName = CondCond + Name + CloneCond + ManCond
        print("THE NAME: Your name is " + str(THEName) + ". That’s your Kojima name")
    Name = THEName
    wait(2)
# This step takes place if you have a cool name
if NameNum == 6 or NameCat == 5:
    print("\n\n\n")
    print("Section 10: COOL NAME\n")
    print("Kojima loves to be cool. \nSometimes,his idea of cool is a bit strange, but it is always cool to Hideo Kojima, and that’s what matters.")
    x = dice_roll(1,6)
    if x == 1:
        Name = Sec3Quest21a + Sec3Quest17
        COOLName = CondCond + Name + CloneCond + ManCond
        print("COOL NAME: Your name is " + str(COOLName) + ". That’s your Kojima name")
    elif x == 2:
        Name = Sec3Quest21a + Sec3Quest18
        COOLName = CondCond + Name + CloneCond + ManCond
        print("COOL NAME: Your name is " + str(COOLName) + ". That’s your Kojima name")
    elif x == 3:
        Name = Sec3Quest21a + Sec3Quest19
        COOLName = CondCond + Name + CloneCond + ManCond
        print("COOL NAME: Your name is " + str(COOLName) + ". That’s your Kojima name")
    elif x == 4:
        Name = Sec3Quest21a + Sec2Quest6
        COOLName = CondCond + Name + CloneCond + ManCond
        print("COOL NAME: Your name is " + str(COOLName) + ". That’s your Kojima name")
    elif x ==5:
        Name = Sec3Quest21a + Sec2Quest8
        COOLName = CondCond + Name + CloneCond + ManCond
        print("COOL NAME: Your name is " + str(COOLName) + ". That’s your Kojima name")
    elif x == 6:
        Name = Sec3Quest21a + Sec2Quest13
        COOLName = CondCond + Name + CloneCond + ManCond
        print("COOL NAME: Your name is " + str(COOLName) + ". That’s your Kojima name")
    Name = COOLName
    wait(2)
# This step takes place if you have a violent name
if NameNum == 6 or NameCat == 6:
    print("\n\n\n")
    print("Section 11: VIOLENT NAME\n")
    print("Sometimes, a Kojima name can be very threatening and violent, like Sniper Wolf, or The Fury. \nNow you can also be threatening and violent.")
    x = dice_roll(1,4)
    if x == 1:
        Name = Sec2Quest5 + Sec3Quest19
        VIOLENTName = CondCond + Name + CloneCond + ManCond
        print("VIOLENT NAME: Your name is " + str(VIOLENTName) + ". That’s your Kojima name")
    elif x == 2:
        Name = Sec2Quest5 + Sec2Quest12
        VIOLENTName = CondCond + Name + CloneCond + ManCond
        print("VIOLENT NAME: Your name is " + str(VIOLENTName) + ". That’s your Kojima name")
    elif x == 3:
        Name = Sec2Quest5 + Sec3Quest20
        VIOLENTName = CondCond + Name + CloneCond + ManCond
        print("VIOLENT NAME: Your name is " + str(VIOLENTName) + ". That’s your Kojima name")
    elif x == 4:
        Name = Sec2Quest5 + Sec2Quest9
        VIOLENTName = CondCond + Name + CloneCond + ManCond
        print("VIOLENT NAME: Your name is " + str(VIOLENTName) + ". That’s your Kojima name")
    Name = VIOLENTName
    wait(2)
# This step takes place if you have a name that lacks subtext
if NameNum == 6 or NameCat == 7:
    print("\n\n\n")
    print("Section 12: NAME THAT LACKS SUBTEXT\n")
    print("Sometimes, Kojima gives up and just names a character exactly what they are. \nCongratulations. You are exactly what you do.")
    Name = Sec2Quest10
    SUBTEXTName = CondCond + Name + CloneCond + ManCond
    print("SUBTEXT NAME: Your name is " + str(SUBTEXTName) + ". That’s your Kojima name")
    Name = SUBTEXTName
    wait(2)
else:
    print("Error: The random number generator has been compromised by the Patriots!")

if NameCat == 1:
    Name = NormalName
elif NameCat == 2:
    Name = OccupationalName
elif NameCat == 3:
    Name = HORNYName
elif NameCat == 4:
    Name = THEName
elif NameCat == 5:
    Name = COOLName
elif NameCat == 6:
    Name = VIOLENTName
elif NameCat == 7:
    Name = SUBTEXTName
else:
    Name = Name 

if KojimaNum == 1:
    Name = "Hideo Kojima"
else:
    Name = Name

print("\n\n\n")
print("Section 13: Explaining Your Name\n")
print("Kojima’s characters know that their names are meaningful, and they will tell you it completely unprompted. \nYou, too, must explain your name to any potential friends, foes, or shadowy government institutions.")
print("\n")
print("Use the following blank to fill in your monologue. \nExplain your Kojima name to the best of your ability. \nFeel free to draw from personal experience,friendships you’ve had, \nor just say some guy on the internet made you fillout an 11-page worksheet to gain this name. \nHere’s a start:")
print("Hi, I’m " + str(Name) + ", and if you’re wondering how I got this name, well, let me tell you. I ")
NameExplain = input("")

file1 = open("KojimaName.txt","a+")
L = ["NORMAL NAME: " + NormalName + "\n", "OCCUPATIONAL NAME: " + OccupationalName + "\n", "HORNY NAME: " + HORNYName + "\n", "THE NAME: " + THEName + "\n", "COOL NAME: " + COOLName + "\n", "VIOLENT NAME: " + VIOLENTName + "\n", "NAME WITH NO SUBTEXT: " + SUBTEXTName + "\n" + "\nHi, I’m " + str(Name) + ", and if you’re wondering how I got this name, well, let me tell you. I " + NameExplain + "\n\n"]
file1.writelines(L)