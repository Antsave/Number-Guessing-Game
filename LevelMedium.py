def levelMedium(num:int, guess:int):
        if (num == guess): # if user guess number corectly
            return 1
        elif (num > guess): # If you need to guess higher.
            if ((guess + 10) >= num): # If your guess is Hot (within 10)
                 return 2
            else:# If your guess needs to go higehr but not within 10 
                 return 3
        else:
             if ((guess -10)<= num): # if user guess is hot
                  return 4
             else: # if user guess needs to go lower but not within 10
                  return 5
             