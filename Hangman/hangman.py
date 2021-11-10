import random
print("HANGMAN")
words = ["python", "java", "javascript", "php"]
word_r = random.choice(words)
word_list = list(word_r)
str_null = len(word_r) * "-"
list_null = list(str_null)
for i in range(10):
    enter_letter = str(input("Input a letter: "))
    if enter_letter in word_list:
        if word_list.count(enter_letter) >= 2:
            index = word_list.index(enter_letter)
            list_null[index] = enter_letter
            word_list[index] = "-"
        index = word_list.index(enter_letter)
        list_null[index] = enter_letter
    else:
        print("That letter doesn't appear in the word")
    print(''.join(list_null))
print("Thanks for playing!")
print("We'll see how well you did in the next stage")