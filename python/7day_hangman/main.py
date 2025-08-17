import random
stages = [r'''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========
 ''', r'''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========
 ''', r'''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========
 ''', r'''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========
 ''', r'''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========
 ''', r'''
    +---+
    |   |
    O   |
        |
        |
        |
  =========
 ''', r'''
    +---+
    |   |
        |
        |
        |
        |
  =========
''']


print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
''')


word_list = ["kon", 'fibi', 'astronauta', 'mops', 'pies']

word = random.choice(word_list)

placerholder = ""
word_lenght = len(word)
for position in range(word_lenght):
    placerholder += "_"
print(placerholder)

lives = 6

game_over = False
correct_letters = []

while not game_over:
    char = str(input("Guess a letter: ").lower())

    display = ""
    for letter in word:

        if letter == char:
            display += letter
            correct_letters.append(char)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(lives)
    print(display)

    if char not in word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose")

    if "_" not in display:
        game_over = True
        print("You win")

    print(stages[lives ])


