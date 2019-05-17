# housekeeping

import random
yourScore = 0
cpuScore = 0
terminator = 'done++'
choice = ''
rockPaperOrScissors = ['rock','paper','scissors']
def sanitizeUserInput():
    while True:
        print('Choose between rock, paper, and scissors (or done++ to exit)!')
        decision = input()
        decision.lower()
        if decision != 'rock' and decision != 'paper' and decision != 'scissors' and decision != 'done++':
            print('Please enter "rock", "paper", or "scissors".')
        else:
            return decision
            break
def determineWinner(a,b):
    if a == 'rock' and b == 'rock':
        print('\nYou picked:\n' + a + '\n' + 'CPU picked:\n' + b + '\nDraw!!!')
        return 'draw'
    if a == 'rock' and b == 'paper':
        print('\nYou picked:\n' + a + '\n' + 'CPU picked:\n' + b + '\nCPU wins!!!')
        return 'CPU'
    if a == 'rock' and b == 'scissors':
        print('\nYou picked:\n' + a + '\n' + 'CPU picked:\n' + b + '\nYou win!!!')
        return 'You'
    if a == 'paper' and b == 'rock':
        print('\nYou picked:\n' + a + '\n' + 'CPU picked:\n' + b + '\nYou win!!!')
        return 'You'
    if a == 'paper' and b == 'paper':
        print('\nYou picked:\n' + a + '\n' + 'CPU picked:\n' + b + '\nDraw!!!')
        return 'draw'
    if a == 'paper' and b == 'scissors':
        print('\nYou picked:\n' + a + '\n' + 'CPU picked:\n' + b + '\nCPU wins!!!')
        return 'CPU'
    if a == 'scissors' and b == 'rock':
        print('\nYou picked:\n' + a + '\n' + 'CPU picked:\n' + b + '\nCPU wins!!!')
        return 'CPU'
    if a == 'scissors' and b == 'paper':
        print('\nYou picked:\n' + a + '\n' + 'CPU picked:\n' + b + '\nYou win!')
        return 'You'
    if a == 'scissors' and b == 'scissors':
        print('\nYou picked:\n' + a + '\n' + 'CPU picked:\n' + b + '\nDraw!!!')
        return 'draw'
    

# ask user for their choice

try:
    while choice != terminator:
        choice = sanitizeUserInput()
        
# calculate winner

        cpuChoice = rockPaperOrScissors[random.randint(0,2)]
        winner = determineWinner(choice, cpuChoice)

# determine tally
        
        if winner == 'You':
            yourScore = yourScore + 1
        if winner == 'CPU':
            cpuScore = cpuScore + 1
        print('CPU Score: ' + str(cpuScore) + ' Your Score: ' + str(yourScore))
        print('')
            

# closing remarks

    print('Thank you for playing my rock paper scissors game!')
except KeyboardInterrupt:
    print('Ctrl+C entered, program terminating...')
