print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice = input('You\'re at a cross road! Where do you want to go? Type "left" or "right"\n').lower()
if choice == "left":
    choice1=input('You\'ve come to a lake. There is an island in the middle of the lake. What do you want to do? Type "swim" to swim across or "wait" for a boat\n').lower()
    if choice1 == "swim":
        print("Attacked by trout! GAME OVER.\n")
    elif choice1 == "wait":
        choice3 = input("Your are in front of three mysterious door! Which door do you want to choose red, blue or yellow\n").lower()
        if choice3 == "red":
            print("Burned by fire! GAME OVER\n")
        elif choice3 == "yellow":
            print("Congratulations! You WON The TREASURE!\n")
        elif choice3 == "blue":
            print("Eaten by beasts! GAME OVER\n")
        else:
            print('You chose a door that don\'t exist! GAME OVER\n')
    else:
        print("Wrong choice! GAME OVER\n")

elif choice.lower() == "right": 
    print("You fell into a hole! GAME OVER\n")

else:
    print("Wrong Way!GAME OVER\n")
   