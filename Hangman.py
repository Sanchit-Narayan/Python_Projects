import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

from hangman_arts import logo
print(logo)

lives = 6
#print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You have already used this letter")
        continue

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            print(stages[0])
            print("You lose")
            print("The word was:", chosen_word)
            end_of_game = True
        else:
            if lives == 6:
                print(stages[6])
            elif lives == 5:
                print(stages[5])
            elif lives == 4:
                print(stages[4])
            elif lives == 3:
                print(stages[3])
            elif lives == 2:
                print(stages[2])
            elif lives == 1:
                print(stages[1])
   
        lives -= 1
        
    print(f"{' '.join(display)}")

    if "_" not in display:
      end_of_game = True 
      print("You Won")

    
