print('Welcome to Hangman')

import random

class Hangman:
    
    def __init__(self, word_list, num_lives =5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.list_letters = []
        self.num_lives = 5
        self.word_list = word_list
        print(f"The mystery word has {len(self.word)} characters")
        print(' '.join(self.word_guessed))
       

    def ask_letter(self):
        letter = input('Guess a letter: ')
        if len(letter) != 1:
            print('Please, enter just one character')
            self.ask_letter()
        elif letter.lower() in self.list_letters:
            print('You have already guessed this letter')
            self.ask_letter()
        else:
            self.list_letters.append(letter)
            letter = letter.lower()
            self.check_letter(letter)
    
    def check_letter(self, letter):
        letter_positions = [index for index, value in enumerate(self.word) if value == letter]
        letter_values = [value for index, value in enumerate(self.word) if value == letter]
        if len(letter_positions) >0:
            for index, value in enumerate(letter_positions):
                self.word_guessed[value] = self.word[value]
            updated_guesses = ' '.join(self.word_guessed)
            print(updated_guesses)
            if '_' in updated_guesses:
                self.ask_letter()
            else:
                print('Congratulations, you won!')
        else:
            self.num_lives += -1
            if self.num_lives < 1:
                print('No more lives left, you lose')
            else:
                print(f'Wrong, you have {self.num_lives} lives left')
                self.ask_letter()
        
        
def play_game(word_list):
    game = Hangman(word_list, num_lives = 5).ask_letter()

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)