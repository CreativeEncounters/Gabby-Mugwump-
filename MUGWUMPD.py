import random

print "MUGWUMP-D!\n"
print "Instructions: \n"
print "2 Players race to see who will find"
print "the horrid creature, THE MUGWUMP, first."
print "Take turns and guess the location of the Mugwump on your grid."
print "The first to find the Mugwump wins."
print "The loser will be haunted by the Mugwump forever;)\n"
print "Created by: Gabby\n"

def prettyprintgrid(grid):
    row = 0
    print "  0 1 2 3 4"
    for line in grid:
        print row,
        row += 1
        for point in line:
            print point,
        print ""

def straightdistance(r1, c1, r2, c2):
    rdiff = r1 - r2
    cdiff = c1 - c2

    rdiff = abs(rdiff)
    cdiff = abs(cdiff)

    if rdiff > cdiff:
        return rdiff
    else:
        return cdiff
   
grid1 = []
grid2 = []

turn = 2

mugr = random.randint(0,4)
mugc = random.randint(0,4)

#construct grids
for i in range(0,5):
    grid1.append(['.','.','.','.','.'])
    grid2.append(['.','.','.','.','.'])

    

#game loop
while True:

    #Turns 
    if turn == 2:
        turn = 1
        print "Player 1's turn: \n"
        prettyprintgrid(grid1)

    elif turn == 1:
        turn = 2
        print "Player 2's turn: \n"
        prettyprintgrid(grid2)

    row = raw_input("Row: ")
    row = int(row)
    col = raw_input("Colum: ")
    col = int(col)

    #If user finds Mugwump
    if row == mugr and col == mugc:
        
        if turn == 1:
            grid1[mugr][mugc] = 'O'
            prettyprintgrid(grid1)
            print "\nPlayer 1 WON!\n"
            print " You found the evil Mugwump! Congrats! This calls for a feast!"
            print "You are a hero!"
            print "\nPlayer 2, YOU LOSE!\n"
            print " You were going to let this evil creature run about through the city!"
            print "The Mugwump will now haunt you forever."
        elif turn == 2:
            grid2[mugr][mugc] = 'O'
            prettyprintgrid(grid2)
            print "\nPlayer 2 WON!\n"
            print " You found the evil Mugwump! Congrats! This calls for a feast!"
            print "You are a hero!"
            print "\nPlayer 1, YOU LOSE!\n"
            print " You were going to let this evil creature run about through the city!"
            print "The Mugwump will now haunt you forever."
        break

    #If user doesn't find Mugwump
    else:
        if turn == 1:
            grid1[row][col] = 'X'
        elif turn == 2:
            grid2[row][col] = 'X'
            
        print "You hear digging",straightdistance(row, col, mugr, mugc),"tiles away. The Mugwump is near!\n"


        
