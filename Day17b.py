import sys

# Open file and load as array a:
a = []
f = open('input17b.txt')
for line in f:
    a.append(line.rstrip('\n'))
f.close()

inputstring = a[0]



class Map:
    def __init__(self, height, width, player_x, player_y, paths):
        self.height = height
        self.width = width
        self.x = player_x
        self.y = player_y
        self.paths = paths
        self.highpoint = 5
        self.depth = 0
        self.rockcounter = 1

        self.stuff = ['|.......|','|.......|','|.......|','|.......|','|.......|','|.......|','|.......|','#########']
        self.stuffghost = []
    

    def move(self, direction):
        self.get_high_point()
        if direction == 'add':
            self.stuff.insert(0, '|.......|')
        if direction == 'rock1':
            self.stuff.insert(self.highpoint -3, '|..@@@@.|')
            self.stuff.insert(self.highpoint -3, '|.......|')
            self.stuff.insert(self.highpoint -3, '|.......|')
            self.stuff.insert(self.highpoint -3, '|.......|')
        if direction == 'rock2':
            self.stuff.insert(self.highpoint -3, '|...@...|')
            self.stuff.insert(self.highpoint -3, '|..@@@..|')
            self.stuff.insert(self.highpoint -3, '|...@...|')
            self.stuff.insert(self.highpoint -3, '|.......|')
        if direction == 'rock3':
            self.stuff.insert(self.highpoint -3, '|..@@@..|')
            self.stuff.insert(self.highpoint -3, '|....@..|')
            self.stuff.insert(self.highpoint -3, '|....@..|')
            self.stuff.insert(self.highpoint -3, '|.......|')
        if direction == 'rock4':
            self.stuff.insert(self.highpoint -3, '|..@....|')
            self.stuff.insert(self.highpoint -3, '|..@....|')
            self.stuff.insert(self.highpoint -3, '|..@....|')
            self.stuff.insert(self.highpoint -3, '|..@....|')
        if direction == 'rock5':
            self.stuff.insert(self.highpoint -3, '|..@@...|')
            self.stuff.insert(self.highpoint -3, '|..@@...|')
            self.stuff.insert(self.highpoint -3, '|.......|')
            self.stuff.insert(self.highpoint -3, '|.......|')
        if direction == 'down':
            if self.checkdown() == True:
                # print('Blocked Turn To #!')
                self.turntostone()
            else:
                # print('Move Down')
                self.movedown()
                pass
        if direction == '>':
            # print('push right')
            if self.checkright() == True:
                pass
                # print('Blocked Right')
            else:
                # print('Move Right')
                self.moveright()
                pass
        if direction == '<':
            # print('push left')
            pass
            if self.checkleft() == True:
                pass
                # print('Blocked left')
            else:
                # print('Move left')
                self.moveleft()
                pass

     
    def moveleft(self):
        self.stuffghost = self.stuff[:]
        self.cleanats()
        xx = 0
        yy = 0
        # put @ for new position in Ghost.
        for x in self.stuff:
            yy=0
            for y in x:
                if y == '@':
                    list1 = list(self.stuffghost[xx])
                    # print(list1)
                    list1[yy-1] = '@'
                    self.stuffghost[xx] = ''.join(list1)
                yy+=1
            xx+=1
        
        #copy gost over stuff
        self.stuff = self.stuffghost





    def checkleft(self):
        # Make sure there are no # immediatly right of @s
        blocked = False
        xx = 0
        yy = 0
        for x in self.stuff:
            yy = 0
            for y in x:
                # print(y)
                if y == '@':
                    if self.stuff[xx][yy-1] == '#' or self.stuff[xx][yy-1] == '|':
                        blocked = True
                yy+=1
            xx+=1
            # input()
        # print(blocked)
        # input()
        return blocked

    
    def moveright(self):
        self.stuffghost = self.stuff[:]
        self.cleanats()
        xx = 0
        yy = 0
        # put @ for new position in Ghost.
        for x in self.stuff:
            yy=0
            for y in x:
                if y == '@':
                    list1 = list(self.stuffghost[xx])
                    # print(list1)
                    list1[yy+1] = '@'
                    self.stuffghost[xx] = ''.join(list1)
                yy+=1
            xx+=1
        
        #copy gost over stuff
        self.stuff = self.stuffghost





    def checkright(self):
        # Make sure there are no # immediatly right of @s
        blocked = False
        xx = 0
        yy = 0
        for x in self.stuff:
            yy = 0
            for y in x:
                # print(y)
                if y == '@':
                    if self.stuff[xx][yy+1] == '#' or self.stuff[xx][yy+1] == '|':
                        blocked = True
                yy+=1
            xx+=1
            # input()
        # print(blocked)
        # input()
        return blocked


    def turntostone(self):
        self.stuffghost = self.stuff[:]
        self.cleanats()
        xx = 0
        yy = 0
        # put @ for new position in Ghost.
        for x in self.stuff:
            yy=0
            for y in x:
                if y == '@':
                    list1 = list(self.stuffghost[xx])
                    # print(list1)
                    list1[yy] = '#'
                    self.stuffghost[xx] = ''.join(list1)
                yy+=1
            xx+=1
        
        #copy gost over stuff
        self.stuff = self.stuffghost[:]
        #init next rock
        if self.rockcounter%5 == 0:
            self.move('rock1')
        if self.rockcounter%5 == 1:
            self.move('rock2')
        if self.rockcounter%5 == 2:
            self.move('rock3')
        if self.rockcounter%5 == 3:
            self.move('rock4')
        if self.rockcounter%5 == 4:
            self.move('rock5')
        self.rockcounter +=1
        # get rid of blank top
        del self.stuff[0]
        del self.stuff[0]
        del self.stuff[0]
        # del self.stuff[0]
        self.get_high_point()

    
    
    
    def movedown(self):
        self.stuffghost = self.stuff[:]
        self.cleanats()
        xx = 0
        yy = 0
        # put @ for new position in Ghost.
        for x in self.stuff:
            yy=0
            for y in x:
                if y == '@':
                    list1 = list(self.stuffghost[xx+1])
                    # print(list1)
                    list1[yy] = '@'
                    self.stuffghost[xx+1] = ''.join(list1)
                yy+=1
            xx+=1
        
        #copy gost over stuff
        self.stuff = self.stuffghost



    def cleanats(self):
        xx = 0
        yy = 0
        for x in self.stuffghost:
            yy = 0
            for y in x:
                if y=='@':
                    list1 = list(self.stuffghost[xx])
                    # print(list1)
                    list1[yy] = '.'
                    self.stuffghost[xx] = ''.join(list1)
                else:
                    pass

                yy+=1
            xx+=1
    
    def checkdown(self):
        # are all the @ symbols above . or @ spaces
        blocked = False
        xx = 0
        yy = 0
        for x in self.stuff:
            yy = 0
            for y in x:
                # print(y)
                if y == '@':
                    if self.stuff[xx+1][yy] == '#':
                        blocked = True

                yy+=1
            xx+=1
            # input()
        # print(blocked)
        # input()
        return blocked


    def print_map(self):
        for x in self.stuff:
            print(x)
    
    def print_map_ghost(self):
        for x in self.stuffghost:
            print(x)

    def get_high_point(self):
        count = 0
        # print(self.stuff)
        for x in self.stuff:
            # print(x)
            if '#' in x:
                self.highpoint = count
                break
            count+=1
        return self.highpoint

    def get_depth(self):
        self.depth = len(self.stuff) - self.get_high_point()
        return self.depth
    
    def getrockcount(self):
        return self.rockcounter


m = Map(4, 4, 0, 0, [1,2,4])



m.move('rock1')
m.print_map()
input()
print(m.getrockcount())

inputstringindex = 0
inplen = len(inputstring)
# using the above will allow us to repeat over using mod.
while m.getrockcount() < 2023:
    # cycle detection
    if inputstringindex%inplen == 0:
        m.print_map()
        input()
    m.move(inputstring[inputstringindex%inplen])
    # m.print_map()
    # input()
    m.move('down')
    # m.print_map()
    # input()
    print(m.getrockcount())
    inputstringindex += 1

print(f'The answer is {m.get_depth()} -1')

# while True:
#     m.print_map()
#     print(f'The highest rock:{m.get_high_point()} from top. It sits at {m.get_depth()} from bottom.')
    
#     direction = input("Enter A Command:")
#     m.move(direction)
    
# The correct answer was 3133