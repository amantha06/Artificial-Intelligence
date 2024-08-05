def check():
    for i in range(0,3):
        if number_grid[0][i] == number_grid[1][i] == number_grid[2][i] == "X"  \
        or number_grid[i][0] == number_grid[i][1] == number_grid[i][2] == "X"  \
        or number_grid[0][0] == number_grid[1][1] == number_grid[2][2] == "X"  \
        or number_grid[2][0] == number_grid[1][1] == number_grid[0][2] == "X":
            print(p1 + " won!")
            return True


        elif number_grid[0][i] == number_grid[1][i] == number_grid[2][i] == "O" != " " \
        or number_grid[i][0] == number_grid[i][1] == number_grid[i][2] == "O" != " " \
        or number_grid[0][0] == number_grid[1][1] == number_grid[2][2] == "O" != " " \
        or number_grid[2][0] == number_grid[1][1] == number_grid[0][2] == "O" != " ":
            print(p2 + " won!")
            return True

            
    return False




p1 = input("Who is Player 1? ")
p2 = input("Who is Player 2? ")

number_grid = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]



done = check()


while done == False:
    
    print(number_grid[0])
    print(number_grid[1])
    print(number_grid[2])
    
    
    countX = 0
    countO = 0
    for i in number_grid:
        countX += i.count("X")
    for z in number_grid:
        countO += z.count("O")

    went = False
    
    while went != True:
        try:
            if countX == countO:
                x1 = int(input("Where do you want to place your marker " + p1 + " please give X coordinate: "))  
                y1 = int(input("Where do you want to place your marker " + p1 + " please give Y coordinate: "))
                
                number_grid[y1][x1] = "X" 
                went = True

            elif countX > countO:
                x2 = int(input("Where do you want to place your marker " + p2 + " please give X coordinate: "))
                y2 = int(input("Where do you want to place your marker " + p2 + " please give Y coordinate: "))
                
                number_grid[y2][x2] = "O"
                went = True
        except IndexError:
            print("Index Error; please enter in a value from 0-2 for the coordinates")
        except ValueError:
            print("Please enter an int not a string")
        done = check()
if done == True:
    print(number_grid[0])
    print(number_grid[1])
    print(number_grid[2])
