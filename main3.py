import random
class FruitQuiz:
    def __init__(self):
        self.fruits = {
            "apple" : "red",
            "banana" : "yellow",
            "grape" : "green",
        }
    def quiz(self):
        while(True):
            fruit , colour = random.choice(list(self.fruits.items()))
            print(f"\n What is the colour of {fruit}?")
            user_answer = input("Your answer:").lower()
            if user_answer == colour:
                print("Correct!")
            else:
                print(f"Wrong! The correct answer is {colour}.")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                print("Thanks for playing!")
                break

