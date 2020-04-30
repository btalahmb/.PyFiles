#ppictureGrid.py

grid =[['.','.','.','.','.','.'],
       ['.','0','0','.','.','.'],
       ['0','0','0','0','.','.'],
       ['0','0','0','0','0','.'],
       ['.','0','0','0','0','0'],
       ['0','0','0','0','0','.'],
       ['0','0','0','0','.','.'],
       ['.','0','0','.','.','.'],
       ['.','.','.','.','.','.']]

def picture():

    gridLength = len(grid)
    inLength = len(grid[0])

    for i in range(len(grid)):
        if ((len(grid[i])) == inLength):
            inLength = len(grid[i])
        else:
            print('List contains inner lists of variable lengths')
    for i in range(inLength):
        for j in range(gridLength):
            print(grid[0][i],grid[1][i],grid[2][i],grid[3][i],grid[4][i],grid[5][i],grid[6][i],grid[7][i],grid[8][i])
            
picture()