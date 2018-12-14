import random

r = 'r'
p = 'p'
s = 's'

print 'Welcome to the Rocks,Papers & Scissors!'

win = random.choice(["You Win!",'Congratulations',':)','Hallellujiah!','Victory!!'])
loss = random.choice(['You Lose..',':(','Tough Luck Mate!','Better Luck Next Time!'])
tie = random.choice(['Ah!A Tie','It\'s a Tie','We have a Tie'])

while True:
    cpu = random.choice([r,p,s])

    user = input ('Take your Pick.\nRocks,Papers or Scissors??')
    print cpu
    
    if user == cpu :
        print tie
    elif user == r and cpu == p:
        print loss
    elif user == r and cpu == s:
        print win
    elif user == p and cpu == r:
        print win
    elif user == p and cpu == s:
        print loss
    elif user == s and cpu == p:
        print win
    elif user == s and cpu == r:
        print loss
    
