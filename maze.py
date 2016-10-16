#File: maze.py
#Name: Sean Siow

from graphics import*
from random import*

class MyStack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if self.stack != []:
            return self.stack.pop()
        else:
            return None
    def isEmpty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)

class Cell:
    def __init__(self):
        self.N = True
        self.S = True
        self.E = True
        self.W = True
        self.visited = False
        self.isFirst = False
        self.isLast = False
        self.isKey = False

    def hasAllWalls(self):
        return self.N and self.S and self.E and self.W

class Maze:
    def __init__(self, dim):
        self.size = dim
        totalCells = dim*dim
        self.grid = [[Cell() for i in range(dim)]for j in range(dim)]
        visitedCells = 0
        x = randrange(1,dim)
        y = randrange(1,dim)
        self.grid[x][y].isFirst = True
        self.entranceX = x
        self.entranceY = y
        cellStack = MyStack()
        self.cellSize = 500/dim
        self.visited = []
        self.path = []
        self.pathKey = []
        self.pathEnd = []
        
        while visitedCells < totalCells:
            neighbors = self.tryVisit(x,y)
            if len(neighbors) >= 1:
                newX, newY, direc = choice(neighbors)
                if direc == 'east':
                    self.grid[x][y].E = False
                    self.grid[newX][newY].W = False
                elif direc == 'west':
                    self.grid[x][y].W = False
                    self.grid[newX][newY].E = False
                elif direc == 'north':
                    self.grid[x][y].N = False
                    self.grid[newX][newY].S = False
                elif direc == 'south':
                    self.grid[x][y].S = False
                    self.grid[newX][newY].N = False
                self.grid[x][y].visited = True
                cellStack.push((x,y))
                x,y = newX,newY
                self.grid[x][y].visited = True
                visitedCells += 1
            else:
                if cellStack.isEmpty():
                    break
                else:
                    x,y = cellStack.pop()
        x = randrange(1,dim)
        y = randrange(1,dim)
        if (x,y)== (self.entranceX,self.entranceY):
            while (x,y) == (self.entranceX,self.entranceY):
                x = randrange(1,dim)
                y = randrange(1,dim)
        self.grid[x][y].isLast = True
        self.exitX = x
        self.exitY = y
        x = randrange(1,dim)
        y = randrange(1,dim)
        if (x,y)== (self.entranceX,self.entranceY) or (x,y) == (self.exitX,self.exitY):
            while (x,y) == (self.entranceX,self.entranceY) or (x,y) == (self.exitX,self.exitY):
                x = randrange(1,dim)
                y = randrange(1,dim)
        self.KeyX = x
        self.KeyY = y

    def tryVisit(self, x, y):
        neighbors = []
        if x+1 < self.size and self.grid[x+1][y].hasAllWalls():
            neighbors.append((x+1,y,'east'))
        if x-1 >= 0 and self.grid[x-1][y].hasAllWalls():
            neighbors.append((x-1,y,'west'))
        if y+1 < self.size and self.grid[x][y+1].hasAllWalls():
            neighbors.append((x,y+1,'north'))
        if y-1 >= 0 and self.grid[x][y-1].hasAllWalls():
            neighbors.append((x,y-1,'south'))
        return neighbors

    def draw(self, win):
        for x in range(self.size):
            for y in range(self.size):
                cell = self.grid[x][y]                
                if cell.E == True:
                    wall = Line(Point(x*self.cellSize+self.cellSize+10, y*self.cellSize+self.cellSize+10), Point(x*self.cellSize+self.cellSize+10, y*self.cellSize+10))
                    wall.setFill('Black')
                    wall.draw(win)
                if cell.W == True:
                    wall = Line(Point(x*self.cellSize+10, y*self.cellSize+self.cellSize+10), Point(x*self.cellSize+10, y*self.cellSize+10))
                    wall.setFill('Black')
                    wall.draw(win)
                if cell.N == True:
                    wall = Line(Point(x*self.cellSize+10, y*self.cellSize+self.cellSize+10), Point(x*self.cellSize+self.cellSize+10, y*self.cellSize+self.cellSize+10))
                    wall.setFill('Black')
                    wall.draw(win)
                if cell.S == True:
                    wall = Line(Point(x*self.cellSize+10, y*self.cellSize+10), Point(x*self.cellSize+self.cellSize+10, y*self.cellSize+10))
                    wall.setFill('Black')
                    wall.draw(win)
                if (x,y) in self.pathKey:
                    square = Rectangle(Point((x)*self.cellSize+self.cellSize/5,y * self.cellSize+self.cellSize/5),
                                       Point((x+1) * self.cellSize-self.cellSize/5 ,(y+1) * self.cellSize-self.cellSize/5))
                    square.move(10,10)
                    square.setFill('Blue')
                    square.draw(win)
                if (x,y) in self.pathEnd:
                    square = Rectangle(Point((x)*self.cellSize+self.cellSize/5,y * self.cellSize+self.cellSize/5),
                                       Point((x+1) * self.cellSize-self.cellSize/5 ,(y+1) * self.cellSize-self.cellSize/5))
                    square.move(10,10)
                    square.setFill('Purple')
                    square.draw(win)
                if cell.isFirst == True:
                    square = Rectangle(Point((x)*self.cellSize+self.cellSize/5,y * self.cellSize+self.cellSize/5),
                                       Point((x+1) * self.cellSize-self.cellSize/5 ,(y+1) * self.cellSize-self.cellSize/5))
                    square.move(10,10)
                    square.setFill('Green')
                    square.draw(win)
                if cell.isLast == True:
                    square = Rectangle(Point((x)*self.cellSize+self.cellSize/5,y * self.cellSize+self.cellSize/5),
                                       Point((x+1) * self.cellSize-self.cellSize/5,(y+1) * self.cellSize-self.cellSize/5))
                    square.move(10,10)
                    square.setFill('Red')
                    square.draw(win)
                if (x,y) == (self.KeyX,self.KeyY):
                    square = Rectangle(Point((x)*self.cellSize+self.cellSize/5,y * self.cellSize+self.cellSize/5),
                                       Point((x+1) * self.cellSize-self.cellSize/5 ,(y+1) * self.cellSize-self.cellSize/5))
                    square.move(10,10)
                    square.setFill('Yellow')
                    square.draw(win)

    def Explore(self, x, y):
        if (x,y) == (self.exitX,self.exitY):
            self.path += [(x,y)]
            return True
        if (x,y) in self.visited:
            return False
        self.visited += [(x,y)]
        if x-1 >= 0 and not self.grid[x][y].W:
            if self.Explore(x-1,y):
                self.path += [(x,y)]
                return True
        if x+1 <= self.size-1 and not self.grid[x][y].E:
            if self.Explore(x+1,y):
                self.path += [(x,y)]
                return True
        if y-1 >= 0 and not self.grid[x][y].S:
            if self.Explore(x,y-1):
                self.path += [(x,y)]
                return True
        if y+1 <= self.size-1 and not self.grid[x][y].N:
            if self.Explore(x,y+1):
                self.path += [(x,y)]
                return True
        return False



def main():
    print("*********************************************************************")
    print("This program will generate a maze with its solution.")
    print("The maze will be of size n*n, where the user will input the value for n")
    print("The green box in the maze is the starting point")
    print("The yellow box in the maze is the key to the exit")
    print("The red box in the maze is the exit point")
    print("The blue boxes represents the path from the start to the key")
    print("The purple boxes represents the path from the key to the exit")
    print("*Note: The purple boxes will overlap with the blue ones since it takes the same path near the key")
    print("*Note: To see output, run program through an IDE (I used IDLE)")
    print("*********************************************************************")
    dim = eval(input("Insert Dimension for Maze\n(Must be less than 48 and greater than 2!): "))
    m = Maze(dim)
    m.exitX,m.exitY,m.KeyX,m.KeyY = m.KeyX,m.KeyY,m.exitX,m.exitY
    win = GraphWin("Maze", 550+m.cellSize,550+m.cellSize)
    m.Explore(m.entranceX,m.entranceY)
    m.pathKey = m.path
    m.path = []
    m.visited = []
    m.exitX,m.exitY,m.KeyX,m.KeyY = m.KeyX,m.KeyY,m.exitX,m.exitY
    m.Explore(m.KeyX,m.KeyY)
    m.pathEnd = m.path
    m.draw(win)
main()
