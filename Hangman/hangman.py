print("HANGMAN")
print("The game will be available soon.")
import random
word_list = ["python", "java", "javascript", "php"]
word_r = random.choice(word_list)
word_1 = list(word_r)
word_2 = word_1[0:3]
word_3 = "".join(word_2)
hidden_word = str(input("Guess the word " + word_3 + ": "))
if hidden_word == word_r:
    print("You survived!")
else:
    print("You lost!")