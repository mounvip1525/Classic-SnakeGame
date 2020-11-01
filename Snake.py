import curses
from random import randint

curses.initscr()#for initialising all module from curses library
curses.noecho()#preventing the default key entires
curses.curs_set(0)#prevent the default cursor's existence which can interupt the game
win = curses.newwin(30,60,0,0)#y,x columns,rows,starting point cordinates
win.keypad(1)#initialise the keypad for the new window created
win.border(0)#prevent the double border
win.nodelay(1)#returns -1 if no key is pressed

ESC = 27
key = curses.KEY_RIGHT#initial key when the game starts
snake=[(5,10),(5,9),(5,8)]#y,x cordinate form
food = (10,30)
score = 0
win.addch(food[0],food[1],'o')

while key!= ESC:
    win.addstr(0,2,'Score = ' + str(score) + ' ')
    win.timeout(100) # 100 milliseconds

    prev_key = key
    event = win.getch()#get the character entered from keyboard
    key = event if event !=1 else prev_key

    if key not in [curses.KEY_UP,curses.KEY_DOWN,curses.KEY_LEFT,curses.KEY_RIGHT,ESC]:   # (only) keys, arrow keys that we use for playing 
        key = prev_key

    #claculating the next cordinates
    y = snake[0][0]
    x = snake[0][1]

    if key == curses.KEY_DOWN:  y +=1
    if key == curses.KEY_UP:    y -=1
    if key == curses.KEY_RIGHT: x +=1
    if key == curses.KEY_LEFT:  x -=1
    snake.insert(0,(y,x))

    #end game if snake hits the border or if snake overlaps itself(checking for every element ecept for te head)
    if(y==0 or x==0 or x==59 or y==29 or snake[0] in snake[1:]):break

    #check if snake has eaten the food
    if snake[0] == food:
        score += 1
        food = ()
        while food == ():
            food = (randint(1,18),randint(1,58))
            if food in snake:#for preventing the the new cordinates to be created within the list of the snake's cordinates
                food = ()
        win.addch(food[0],food[1],'o')
    else:
        #moving the snake
        last = snake.pop()
        win.addch(last[0],last[1],' ')

    win.addch(snake[0][0],snake[0][1],'-')

curses.endwin()#return back to the normal command line
print(f'Score = {score}')
