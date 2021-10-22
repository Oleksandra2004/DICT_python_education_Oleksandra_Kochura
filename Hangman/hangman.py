print("HANGMAN")
print("The game will be available soon.")
import random
hidden_word = str(input("Guess the word: "))
word_list = ["python", "java", "javascript", "php"]
word_r = random.choice(word_list)
if hidden_word == word_r:
    print("You survived!")
else:
    print("You lost!")
