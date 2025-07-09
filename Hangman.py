from random import choice

words = ['python', 'computer', 'mouse', 'vancouver', 'canada']
incorrect_letters = []
correct_letters = []
attempts = 5
matches = 0
game_finished = False

def choose_word(words):
    chosen_word = choice(words)
    unique_letters = len(set(chosen_word))
    return chosen_word, unique_letters

def ask_for_letter():
    chosen_letter = ''
    is_valid = False
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    while not is_valid:
        chosen_letter = input('Enter a letter: ').lower()
        if chosen_letter in alphabet and len(chosen_letter) == 1:
            is_valid = True
        else:
            print('You did not enter a valid letter.')

    return chosen_letter

def show_board(chosen_word):
    hidden_list = []

    for letter in chosen_word:
        if letter in correct_letters:
            hidden_list.append(letter)
        else:
            hidden_list.append('_')

    print(' '.join(hidden_list))

def check_letter(chosen_letter, hidden_word, lives, hits):
    end = False

    if chosen_letter in hidden_word:
        correct_letters.append(chosen_letter)
        hits += 1
    else:
        if chosen_letter not in incorrect_letters:
            incorrect_letters.append(chosen_letter)
            lives -= 1
        else:
            print('You already guessed that letter.')

    if lives == 0:
        end = lose()
    elif hits == unique_letters:
        end = win(hidden_word)

    return lives, end, hits

def lose():
    print('You have run out of lives.')
    print('The hidden word was: ' + word)
    return True

def win(discovered_word):
    show_board(discovered_word)
    print('Congratulations! You guessed the word:')
    return True

# Start the game
choose_word(words)
word, unique_letters = choose_word(words)

while not game_finished:
    show_board(word)
    print('\n')
    print('Wrong letters: ' + '-'.join(incorrect_letters))
    print(f'Lives: {attempts}')
    letter = ask_for_letter()

    attempts, finished, matches = check_letter(letter, word, attempts, matches)

    game_finished = finished
