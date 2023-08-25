"""Puppy Simulator: This program uses State patterns to allow the user to feed and play with the puppy.
Written by: Ayar Maw, Rayna Maruyama (group 9)
Date: December 6, 2022
Functions:
    N/A
"""

import puppy
import check_input

def main():
    
    print("congratulations on your new puppy!")
    p = puppy.Puppy()

    choice = 0
    while choice != 3:
        
        #prompt the user to chose feed or play with the puppy
        choice = check_input.get_int_range("What would you like to do?: \
                                                        \n1. Feed the puppy \
                                                        \n2. Play with the puppy \
                                                        \n3. Quit \
                                                        \nEnter Choice: ", 1, 3)
        if choice == 1:
            print()
            print(p.give_food())    
           
        elif choice == 2:
            print()
            print(p.throw_ball())
           
        elif choice == 3:
            break
        else:
            print("invalid")        
            
    

main()