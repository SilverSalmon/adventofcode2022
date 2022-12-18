


class Map:
    def __init__(self, height, width, player_x, player_y, paths):
        self.height = height
        self.width = width
        self.x = player_x
        self.y = player_y
        self.paths = paths
        self.highpoint = 5
        self.depth = 0

        self.stuff = ['|.......|','|.......|','|.......|','|.......|','|.......|','|.......|','|.......|','#########']
        self.stuffghost = []
    

    def move(self, direction):
        self.get_high_point()
        if direction == 'add':
            self.stuff.insert(0, '|.......|')
        if direction == 'rock1':
            self.stuff.insert(self.highpoint -3, '|..@@@@.|')
        if direction == 'rock2':
            self.stuff.insert(self.highpoint -3, '|...@...|')
            self.stuff.insert(self.highpoint -3, '|..@@@..|')
            self.stuff.insert(self.highpoint -3, '|...@...|')
        if direction == 'rock3':
            self.stuff.insert(self.highpoint -3, '|..@@@..|')
            self.stuff.insert(self.highpoint -3, '|....@..|')
            self.stuff.insert(self.highpoint -3, '|....@..|')
        if direction == 'rock4':
            self.stuff.insert(self.highpoint -3, '|..@....|')
            self.stuff.insert(self.highpoint -3, '|..@....|')
            self.stuff.insert(self.highpoint -3, '|..@....|')
            self.stuff.insert(self.highpoint -3, '|..@....|')
        if direction == 'rock5':
            self.stuff.insert(self.highpoint -3, '|..@@...|')
            self.stuff.insert(self.highpoint -3, '|..@@...|')
        if direction == 'down':
            if self.checkdown() == True:
                print('Blocked Turn To #!')
                self.turntostone()
            else:
                print('Move Down')
                self.movedown()
                pass
        if direction == '>':
            print('push right')
            if self.checkright() == True:
                print('Blocked Right')
            else:
                print('Move Right')
                self.moveright()
                pass
        if direction == '<':
            print('push left')
            if self.checkleft() == True:
                print('Blocked left')
            else:
                print('Move left')
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
        print(blocked)
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
        print(blocked)
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
        self.stuff = self.stuffghost


    
    
    
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
        print(blocked)
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


m = Map(4, 4, 0, 0, [1,2,4])


m.print_map()
m.move('rock1')
m.print_map()
m.move('down')
m.print_map()
m.move('down')
m.print_map()
m.move('down')
m.print_map()
m.move('down')
m.print_map()
m.move('rock2')
m.print_map()
m.move('down')
m.print_map()
m.move('down')
m.print_map()
m.move('down')
m.print_map()
m.move('down')
m.print_map()
m.move('rock3')
m.print_map()
m.move('down')
m.print_map()
m.move('down')
m.print_map()
m.move('down')
m.print_map()



while True:
    m.print_map()
    print(f'The highest rock:{m.get_high_point()} from top. It sits at {m.get_depth()} from bottom.')
    
    direction = input("Enter A Command:")
    m.move(direction)
    