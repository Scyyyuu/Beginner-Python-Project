print ("=== Welcome To Ragnarok! ===")
Username = input ("Username: ")
import random 
User_ID = random.randint (1,1000) #shows a random id number for player
print (f"Player ID: {User_ID}")
print ()
print (f"Welcome {Username} To Ragnarok!")
Instruction = "Ragnarok is an Idle RPG python game inspired by AFK Arena and Idle Hero in Google Play Store."
print (Instruction)

experience = 0
Mage_class = ["Wands", "Spellbook", "Orb"]
ragnarok_class = ['MAGE', 'KNIGHT', 'MARKSMAN', 'TANK']
player_class = input (f"Choose a class from {ragnarok_class}: ").upper()

if player_class == 'MAGE':
    print ("You chosee the Mage Class")

elif player_class == 'KNIGHT':
    print ("You chosee the Knight Class")

elif player_class == 'MARKSMAN':
    print ("You chosee the Marksman Class")

elif player_class == 'TANK':
    print ("You chosee the Tank Class")

print ()
Start = 1
Farm_num = int (input ("Type a number to start farming: "))
print ("Per number you type is equivalent to amount of farming experience (type x to stop)")

for Farm in range (Start, Farm_num):
    print (Farm, end= ",")
