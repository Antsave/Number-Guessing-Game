from randN import randN
from LevelEasy import levelEasy
from LevelMedium import levelMedium
from LevelHard import levelHard
import LevelEasy
def main():
    #Main start of game asking for levels.
    #print(randN(1,10))
    
    print("Hello! Welcome to the number Guessing Game!\n")
    print("We have 5 options please enter the number that coresponds with the option you would like to choose. \n")
    while (True): # while loop to break 
        
        print("Option 1: Guess a number 1 - 3\n")
        print("Option 2: Guess a number 1 - 10\n")
        print("Option 3: Guess a number 1 - 50\n")
        print("Option 4: Guess a number 1 - 100\n")
        print("Option 5: Guess a number 1 - 1000\n")
        print("Option 6: Quit Program")
        choice = int(input("Enter your selection ")) #Gets user input
        match choice:
            case 1:
                randNum = randN(1,3) # Calls random number function
                while(True): 
                    guess = int(input("Guess a number 1 - 3\n"))
                    result =  levelEasy(randNum, guess)
                    match result:
                        case 1:
                            print("Congratulations You win ")
                            break
                        case 2: 
                            option = int(input("Incorrect. Press 1 to try again\n Press 2 to quit. "))
                            if (option == 1):
                                print("Guess Higher")
                                continue
                            elif(option == 2):
                                print("Quitting Level")
                                break
                            else:
                                print("Invalid Input! Guess again!")
                            
                        case 3:
                            option = int(input("Incorrect. Press 1 to try again\n Press 2 to quit. "))
                            if (option == 1):
                                print("Guess Lower")
                                continue
                            elif(option == 2):
                                print("Quitting Level")
                                break
                            else:
                                print("Invalid Input! Guess again!")
            case 2:
                 randNum = randN(1,10) # Calls random number function
                 while(True): 
                    guess = int(input("Guess a number 1 - 10\n"))
                    result =  levelEasy(randNum, guess)
                    match result:
                        case 1:
                            print("Congratulations You win ")
                            break
                        case 2: 
                            option = int(input("Incorrect. Press 1 to try again\n Press 2 to quit. "))
                            if (option == 1):
                                print("Guess Higher")
                                continue
                            elif(option == 2):
                                print("Quitting Level")
                                break
                            else:
                                print("Invalid Input! Guess again!")
                            
                        case 3:
                            option = int(input("Incorrect. Press 1 to try again\n Press 2 to quit. "))
                            if (option == 1):
                                print("Guess Lower")
                                continue
                            elif(option == 2):
                                print("Quitting Level")
                                break
                            else:
                                print("Invalid Input! Guess again!")
            case 3:
                randNum = randN(1,50) #calls random number 
                print(randNum)
                while(True):
                    guess = int(input("Guess a number 1 - 50 \n"))
                    result = levelMedium(randNum, guess)
                    match result:
                        case 1:
                            print("Congratulations You win ")
                            break 
                        case 2:
                           option = int(input("Incorrect. Press 1 to try again\n Press 2 to quit. "))
                           if (option == 1):
                               print("You're Hot! Guess Higher! ")
                               continue
                           elif(option == 2):
                               print("Quitting Level")
                               break
                           else:
                               print("Invalid input. Guess again!")
                               continue
                        case 3: 
                            option = int(input("Incorrect. Press 1 to try again\n Press 2 to quit. "))
                            if (option == 1):
                               print("You're Cold! Guess Higher! ")
                               continue
                            elif(option == 2):
                               print("Quitting Level")
                               break
                            else:
                               print("Invalid input. Guess again!")
                               continue
                        case 4:
                            option = int(input("Incorrect. Press 1 to try again\n Press 2 to quit. "))
                            if (option == 1):
                               print("You're Hot! Guess Lower! ")
                               continue
                            elif(option == 2):
                               print("Quitting Level")
                               break
                            else:
                               print("Invalid input. Guess again!")
                               continue
                        case 5:
                             option = int(input("Incorrect. Press 1 to try again\n Press 2 to quit. "))
                             if (option == 1):
                               print("You're Cold! Guess Lower! ")
                               continue
                             elif(option == 2):
                               print("Quitting Level")
                               break
                             else:
                               print("Invalid input. Guess again!")
            case 4:
                randNum = randN(1,100) #calls random number 
                print(randNum)
                while(True):
                    guess = int(input("Guess a number 1 - 100 \n"))
                    result = levelMedium(randNum, guess)
                    match result:
                        case 1:
                            print("Congratulations You win ")
                            break 
                        case 2:
                           option = int(input("Incorrect. Press 1 to try again\n Press 2 to quit. "))
                           if (option == 1):
                               print("You're Warm! Guess Higher! ")
                               continue
                           elif(option == 2):
                               print("Quitting Level")
                               break
                           else:
                               print("Invalid input. Guess again!")
                               continue
                        case 3: 
                            option = int(input("Incorrect. Press 1 to try again\n Press 2 to quit. "))
                            if (option == 1):
                               print("You're Cold! Guess Higher! ")
                               continue
                            elif(option == 2):
                               print("Quitting Level")
                               break
                            else:
                               print("Invalid input. Guess again!")
                               continue
                        case 4:
                            option = int(input("Incorrect. Press 1 to try again\n Press 2 to quit. "))
                            if (option == 1):
                               print("You're Warm! Guess Lower! ")
                               continue
                            elif(option == 2):
                               print("Quitting Level")
                               break
                            else:
                               print("Invalid input. Guess again!")
                               continue
                        case 5:
                             option = int(input("Incorrect. Press 1 to try again\n Press 2 to quit. "))
                             if (option == 1):
                               print("You're Cold! Guess Lower! ")
                               continue
                             elif(option == 2):
                               print("Quitting Level")
                               break
                             else:
                               print("Invalid input. Guess again!")


            case 5:
                 randNum = randN(1,1000) #calls random number 
                 print(randNum)
                 while(True):
                    guess = int(input("Guess a number 1 - 1000 \n"))
                    result = levelMedium(randNum, guess)
                    print(result)
                    match result:
                        case 1:
                            print("Congratulations You win ")
                            break 
                        case 2:
                           option = int(input("Incorrect. Press 1 to try again\n Press 2 to quit. "))
                           if (option == 1):
                               print("You're Hot! Guess Higher! ")
                               continue
                           elif(option == 2):
                               print("Quitting Level")
                               break
                           else:
                               print("Invalid input. Guess again!")
                               continue
                        case 3: 
                            option = int(input("Incorrect. Press 1 to try again\n Press 2 to quit. "))
                            if (option == 1):
                               print("You're Warm! Guess Higher! ")
                               continue
                            elif(option == 2):
                               print("Quitting Level")
                               break
                            else:
                               print("Invalid input. Guess again!")
                               continue
                        case 4:
                            option = int(input("Incorrect. Press 1 to try again\n Press 2 to quit. "))
                            if (option == 1):
                               print("You're Cold! Guess Lower! ")
                               continue
                            elif(option == 2):
                               print("Quitting Level")
                               break
                            else:
                               print("Invalid input. Guess again!")
                               continue
                        case 5:
                             option = int(input("Incorrect. Press 1 to try again\n Press 2 to quit. "))
                             if (option == 1):
                               print("You're Hot! Guess Lower! ")
                               continue
                             elif(option == 2):
                               print("Quitting Level")
                               break
                             else:
                               print("Invalid input. Guess again!")
                        case 6:
                             option = int(input("Incorrect. Press 1 to try again\n Press 2 to quit. "))
                             if (option == 1):
                               print("You're Warm! Guess Lower! ")
                               continue
                             elif(option == 2):
                               print("Quitting Level")
                               break
                             else:
                               print("Invalid input. Guess again!")
                        case 7:
                             option = int(input("Incorrect. Press 1 to try again\n Press 2 to quit. "))
                             if (option == 1):
                               print("You're Cold! Guess Lower! ")
                               continue
                             elif(option == 2):
                               print("Quitting Level")
                               break
                             else:
                               print("Invalid input. Guess again!")




                        
    
        
if __name__ == "__main__":
    main()