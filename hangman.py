import hangman_words
import hangman_art
import random
import os

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
guessed_letters = []

print(hangman_art.logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # clear screen for mac
    os.system('clear') 

    # clear screen for windows
    # os.system('clr')

    if guess in display:
      print(f"You have already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
  
    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose.\nThe word was {chosen_word}.")
        if guess not in guessed_letters:
          guessed_letters.append(guess)

    #Join all the elements in the list and turn it into a String.
    print(f"\n{' '.join(display)}" + 
    f"     \n\nYour wrong guessed letters: {' '.join(guessed_letters)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
