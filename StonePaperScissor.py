import random

lst = ['Stone', 'Paper', 'Scissor']
rdm = random.choice(lst)
lose = 0
won = 0
tie = 0

print('Welcome to the Game!!!')
print('STONE PAPER SCISSOR')
print()

for i in range(11):

    print('Choose any one of three!')
    a = int(input('1. Stone\n2. Paper\n3. Scissor\n'))
    print('Computer Chooses:', rdm)

    if a == 1 and rdm == lst[0]:
        print('Tie')
        tie += 1
        print("Computer's Score:", lose, "Your Score:", won)

    elif a == 1 and rdm == lst[1]:
        print('You Lose')
        lose += 1
        print("Computer's Score:", lose, "Your Score:", won)

    elif a == 1 and rdm == lst[2]:
        print('You Won')
        won += 1
        print("Computer's Score:", lose, "Your Score:", won)

    elif a == 2 and rdm == lst[0]:
        print('You Won')
        won += 1
        print("Computer's Score:", lose, "Your Score:", won)

    elif a == 2 and rdm == lst[1]:
        print('Tie')
        tie += 1
        print("Computer's Score:", lose, "Your Score:", won)

    elif a == 2 and rdm == lst[2]:
        print('You Lose')
        lose += 1
        print("Computer's Score:", lose, "Your Score:", won)

    elif a == 3 and rdm == lst[0]:
        print('You Lose')
        lose += 1
        print("Computer's Score:", lose, "Your Score:", won)

    elif a == 3 and rdm == lst[1]:
        print('You Won')
        won += 1
        print("Computer's Score:", lose, "Your Score:", won)

    elif a == 3 and rdm == lst[2]:
        print('Tie')
        tie += 1
        print("Computer's Score:", lose, "Your Score:", won)

    else:
        print('You have type wrong input.')

print('Times you won:', won, '\nTimes you lose:', lose, '\nTies:', tie)

if won == lose:
    print("It's a tie match!")

elif won > lose:
    print("Congratulations! You won the match!")

elif won < lose:
    print("Oops! You lose the match!")

else:
    print("Error!!!")
