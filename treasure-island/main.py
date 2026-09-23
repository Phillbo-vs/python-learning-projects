print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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


step1 = input('You wake up on a strange island with no memory of how you arrived\n'
    'In front of you stands an ancient stone temple.\n'
    'Above the entrance are the words:\n'
    "Only those who can understand the island may claim what lies within.\n"
    'You enter the temple.\n'
    'At the end of a dark hallway, you find two doors.\n'
    'One is on the RIGHT.\n'
    'One is on the LEFT.\n'
    'A stone tablet between them reads:\n'
    '"One path follows the hand that greets a king."\n'
    'The other follows the hand that holds your heart.\n'
    '"Choose the path that sailors once called the path of good fortune."\n'
    'Which door do you choose?\n'
    '(Right or Left)\n').lower()
if step1 == 'left':
    print("Well done!\n")
    step2 = input('You enter a mysterious forest.\n'
                    'After walking for hours, you reach a wide river.\n'
                    'The water is completely still.\n'
                    'You notice enormous footprints beside the riverbank.\n'
                    'Then you see a shadow moving beneath the water.\n'
                    'A second stone tablet appears:\n'
                    '"The river is hungry,\n'
                    'but the patient traveller shall pass.\n'
                    'The foolish traveller fights the current.\n'
                    'The wise traveller waits for the river to reveal its secret."\n'
                    'You look across the river.\n'
                    'The shadow beneath the water is getting closer.\n'
                    'What do you do?\n'
                    '(Swim or Wait)\n').lower()
    if step2 == 'wait':
            print("Well done!\n")
            step3 = input('You wait.\n'
                                'Eventually, the shadow disappears.\n'
                                'The river begins to glow, and an ancient bridge rises from beneath the water.\n'
                                'You cross safely.\n'
                                'On the other side, you discover a giant chamber containing three portals.\n'
                                '🔴 RED\n'
                                '🔵 BLUE\n'
                                '🟡 YELLOW\n'
                                'A final inscription appears:\n'
                                '**"Three lights stand before you.\n'
                                'Red burns with anger.\n'
                                'Blue sleeps beneath the deepest sea.\n'
                                'Yellow shines like the sun.\n'
                                'The treasure was never meant for those who seek darkness or destruction.\n'
                                'Seek instead the colour that brings light to the world."\n'
                                'Which portal do you choose?\n'
                                '(Red, Blue or Yellow)\n').lower()
            if step3 == 'yellow':
                print('You step through the yellow portal.\n'
                      'The moment you enter, the entire chamber fills with golden light.\n'
                      'The walls begin to glow, revealing ancient paintings of the island.\n'
                      'At the centre of the room, a stone chest rises from the ground.\n'
                      'You slowly walk towards it and place your hand on the lid.\n'
                      'The chest opens.\n'
                      'Inside lies a magnificent treasure, untouched for thousands of years.\n'
                      'Gold coins, precious jewels, and an ancient golden crown shine before you.\n'
                      'But beside the treasure, you find one final message:\n'
                      '"The greatest treasure belongs to those who understand the island."\n'
                      'You smile.\n'
                      'You have solved every riddle and survived every challenge.\n'
                      '🏆 YOU FOUND THE TREASURE! 🏆\n'
                      '🌟 CONGRATULATIONS! 🌟\n'
                      'You are the true treasure hunter of the island!')
            elif step3 == 'red':
                print('You step through the red portal.\n'
                      'Suddenly, the chamber becomes unbearably hot.\n'
                      'Flames rise from the ground around you.\n'
                      'You hear a deep voice echo through the chamber:\n'
                      '"You chose anger and destruction."\n'
                      'The red light becomes brighter and brighter.\n'
                      'You try to escape, but the portal has disappeared.\n'
                      'The temple shakes violently.\n'
                      'You made the wrong choice.\n'
                      '💀 GAME OVER 💀\n'
                      'The treasure remains hidden.\n')

            elif step3 == 'blue':
                print('You step through the blue portal.\n'
                      'Suddenly, you find yourself deep beneath the ocean.\n'
                      'You look around and see an enormous underwater kingdom.\n'
                      'A mysterious voice whispers:\n'
                      '"You chose the path of the deepest sea."\n'
                      'You swim towards a distant light, but it slowly disappears.\n'
                      'The water becomes darker and darker.\n'
                      'You realise that the treasure is not here.\n'
                      '💀 GAME OVER 💀\n'
                      'The ocean keeps its secrets.')
            else:
                print('You hesitate and choose none of the portals.\n'
                      'The three lights suddenly disappear.\n'
                      'The chamber falls completely silent.\n'
                      'The temple has decided that you are not ready.\n'
                      '💀 GAME OVER 💀')
    else:
         print('You jump into the river and begin swimming.\n'
                    'At first, the water is calm.\n'
                    'Then everything goes silent.\n'
                    'You look beneath the surface...\n'
                    'Two enormous eyes stare back at you.\n'
                    'The shadow you saw earlier wasn\'t a shadow at all.\n'
                    'Something massive rises from the depths.\n'
                    'You made the wrong choice.\n'
                    '💀 GAME OVER 💀\n'
                    'Sometimes the wisest thing to do is simply wait.\n')
else:
    print('You push open the Wrong door.'
    'For a moment, nothing happens.'
    'Then you hear a deep rumble beneath your feet.'
    'The symbols on the door begin to glow red.'
    'You suddenly realize...'
    'You chose the path of misfortune.'
    'The floor disappears beneath you, and darkness consumes the room.'
    '💀 GAME OVER 💀'
    'The island has claimed another traveller.')