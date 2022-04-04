#Game: Hangman

import random
import string
from words import words

def get_valid_word(words):
  word = random.choice(words) #choose a random word
  while " " or "-" in word:
    word = random.choice(words) #make sure it's valid

  return word.upper()

def hangman():
  word = get_valid_word(words)
  word_letters = set(word) #letters in the word
  alphabet = set(string.ascii_uppercase)
  used_letters = set() #what the user has guessed
  lives = 7

  while len(word_letters) > 0 and lives > 0: #keeps the user guessing until there's no letter left in the word
    # ' '.join(["a", "b", "cd"]) --> 'a b cd'
    print(f"You have {lives} lives left, and you have used these letters: ", ' '.join(used_letters))

    #what current word is
    word_list = [letter if letter in used_letters else "-" for letter in word]
    print("Current word: ", ' '.join(word_list))
  #get user input as a guess
    user_input = input("Guess a letter: ").upper()
    if user_input in alphabet - user_input:
      used_letters.add(user_input)
      if user_input in word_letters:
        used_letters.remove(user_input)

      else:
        lives = lives - 1
        print(f"The letter {user_input} is not in the word. Lives left: {lives}")
  
    elif user_input in used_letters:
      print("You've already used that letter. Try again!")
    else:
      print("Invalid character. Try again!")

  if lives == 0:
    print(f"Sorry, you died. The word was: {word}")
  else:
    print(f"Congratulations! You've guessed the word: {word}")

hangman()
