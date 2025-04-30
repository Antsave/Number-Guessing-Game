
def levelEasy(num:int, guess:int):
        if (num == guess):
            return 1
        elif (num > guess):
            return 2
        else:
             return 3