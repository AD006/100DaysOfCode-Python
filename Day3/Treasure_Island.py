#Treasure Island Game
print("Welocme to the Treasure Island Game \nYour mission is to find the treasure")
choice1=input('You are at a cross road. \nWhere do you want to go? Type "left" or "right"?\n').lower()

if choice1=="left" :
  choice2=input('Great you choose the right direction. You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim\n').lower()
  if choice2=="wait" :
    choice3=input('Great you reached here.\nThere is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?Type "red" to choose red door. Type "yellow" to choose yellow door. Type "blue" to choose blue door.\n').lower()
    if choice3=="red":
      print('''Game Over.....Wrong Door \n
  ___ _ __ _ __ ___  _ __ 
 / _ \ '__| '__/ _ \| '__|
|  __/ |  | | | (_) | |   
 \___|_|  |_|  \___/|_|   ''')
    elif choice3=="yellow" :
      print('''You find it \n
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
            /______/______/______/______/______/______/______/______/______/______/______/
            *******************************************************************************
            ''')
    elif choice3=="blue" :
      print('''Game Over.....Wrong Door\n
  ___ _ __ _ __ ___  _ __ 
 / _ \ '__| '__/ _ \| '__|
|  __/ |  | | | (_) | |   
 \___|_|  |_|  \___/|_|   ''')
  else :
    print('''Sharks are here. Game over... \n
                (`.
                 \ `.
                  )  `._..---._
\`.       __...---`         o  )
 \ `._,--'           ,    ___,'
  ) ,-._          \  )   _,-'
 /,'    ``--.._____\/--''
''')
else:
  print('''Wrong direction... Game over \n
 _____     _    _____   ____  /_ /,
| ,-, )  /'_`\ |_   _| |  __| \ \>
| `-'<  | (_) |  | |   |  _|   ) )__ ,_
|_|`\_\  \___/   |_|   |_|    (_.-'_)__|''')

