import random
stages = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========''',

'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',

'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',

'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',

'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',

'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',

'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   
'''
print(logo)
word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar'
             'coyote crow deer dog donkey duck eagle ferret fox frog goat' 
             'goose hawk lion lizard llama mole monkey moose mouse mule'
             'newt otter owl panda parrot pigeon python rabbit ram rat raven'
             'rhino salmon seal shark sheep skunk sloth snake spider'
             'stork swan tiger toad trout turkey turtle weasel whale'
             'wolf wombat zebra').split()

chosen_word = random.choice(word_list)
print(f'your random word is {chosen_word}')

word_length = len(chosen_word)
lives = 6
display = []

for letter in range(word_length):
    display+="_"  

end_of_game = False

while not end_of_game:
    guess = input('Guess  a letter:\n').lower()
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        lives-=1
        if lives == 0:
            end_of_game = True
        print('you lose')
        
    if '_' not in display:
        end_of_game = True
        print('you win')
print(stages[lives])

    
    
