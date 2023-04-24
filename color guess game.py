import random
colors=['red','blue','green','yellow', 'voilet', 'black']
print('the list of colors are:',colors)
while True:
    color=colors[random.randint(0,len(colors)-1)]
    guess =input('i am thinking about a color, can you guess it?')
    while True:
        if color==guess.lower():
            break
        else:
            guess=('nope, try again;')
    print('you guessed it| I am thinking about ',color)
    play_again=input('Lets play again? Type "no" to quit ')
    if play_again.lower()=='no':
        break
print('It was fun, thanks for playing')
