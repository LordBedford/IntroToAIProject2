#Peter Marchese

import random

#Function to generate a map
def mapGen(d):
    #Check if d is a multiple of 3
    if d % 3 != 0:
        print("d is not a multiple of 3. Please try again using a d value that is a multiple of 3")
        return

    #Initiate map with all 1 chars for regular cell
    map = [[0 for i in range(d)] for j in range(d)]

    #Add characters to top row
    tracker = 0
    for i in range(len(map[0])):
        if tracker == 0:
            map[0][i] = 2
            tracker = 1
        elif tracker == 1:
            map[0][i] = 1
            tracker = 2
        else:
            map[0][i] = 3
            tracker = 0

    #Add characters to bottom row
    tracker = 0
    for i in range(len(map[d-1])):
        if tracker == 0:
            map[d-1][i] = 5
            tracker = 1
        elif tracker == 1:
            map[d-1][i] = 4
            tracker = 2
        else:
            map[d-1][i] = 6
            tracker = 0

    #Add pits
    pits_per_row = d / 3 - 1
    placed_pits = 0
    for i in range(len(map)-1):
        if i == 0:
            continue
        j = 0
        while placed_pits != pits_per_row:
            if random.randint(1,d) == 1 and map[i][j] != 7:
                map[i][j] = 7
                placed_pits += 1
            j += 1
            if j >= d:
                j = 0
        placed_pits = 0
    return map
#print(mapGen(9))