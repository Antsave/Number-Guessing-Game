def levelHard(num: int, guess: int):
    if num == guess:
        return 1  # Correct guess

    diff = abs(num - guess)

    if guess < num:  # Too low
        if diff <= 10:
            return 2  # Hot (too low)
        elif diff <= 50:
            return 3  # Warm (too low)
        else:
            return 4  # Cold (too low)
    else:  # Too high
        if diff <= 10:
            return 5  # Hot (too high)
        elif diff <= 50:
            return 6  # Warm (too high)
        else:
            return 7  # Cold (too high)
