import random
import hangman_art
import hangman_words

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

display = []

for letter in range(len(chosen_word)):
    display.append("_") 
print(display)

lives = 6



while "_" in display:
    print("")
    print()
    print()
    
    guess = input("guess a letter:").lower()
    
    if guess in display:
        print(f"You already guessed {guess} try again")
    
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
    print(f"{' '.join(display)}")    

            
    if guess not in display:
        print(f"You guessed {guess}, thats not in the word. You lose a life ")
        lives=lives-1
    print(hangman_art.stages[lives])
    
    if lives ==0:
        print("you lose")
        break
    
print(f"{' '.join(display)}")    
if "_" not in display:
    print("you win")
    


