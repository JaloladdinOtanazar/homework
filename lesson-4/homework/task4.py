import random
def game():
    num = random.randint(1, 100)
    attempts = 10
    while attempts > 0 :
        guess_a_number = int(input("Enter your guess: "))
        if guess_a_number > num:
            print("too high")
        elif guess_a_number < num:
            print("too low")
        
        else:
            print("you are right")
            break
        attempts -= 1

    if attempts == 0:
        print("you lost")
        
    play_again = input("Want to play again? (Y/N): ").lower()
    if play_again == 'y':
        game()

        
game()
