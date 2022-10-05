'''Pengyu Xue 260927847'''
import random
from dungeon_helpers import get_directions, get_directions_message, get_next_coordinate

class Player():
    def __init__(self, name):
        self.name = name #set the name to initial
        self.health = 10 #set the initial health t 10
       
    def get_name(self): #return the name
        return self.name
    
    def get_health(self):#return the health 
        return self.health
        
    def set_health(self, health):
        if health < 0: #if health < 0, raise the ValueError
            raise ValueError('Health less than 0')
        else: #otherwise, unchange
            self.health = health

class Dungeon():
    def __init__(self, map_filename, num_traps):
        self.dungeon_map = Dungeon.read_map_file(self, map_filename) #local name lis is the return of read_map_file
        lis = Dungeon.read_map_file(self, map_filename) #shorter name
        for i in lis:
            if len(i) == len(lis):# check if the length of each sublist equal to the length of the list or not
                continue
            else:
                raise ValueError('non-square grid')
        if len(lis) < 4: #if the length of the list is less than 4, then it means the number of rows less than 4
            raise ValueError('Not a 4x4 grid')
        else:
            for i in lis:#if the length of the sublist in the list is less than 4, then it means the number of columns less than 4
                if len(i) < 4:
                    raise ValueError('Not a 4x4 grid')
        for i in lis:
            for j in i: #if the character is 'x' , '*' , 'T', then continue
                if j == 'x' or j == '*' or j == 'T':
                    continue
                else: # if the character is not 'x' , '*' , 'T', then raise the error
                    raise ValueError('invalid character')
        Tr = 0 #the number of treasure
        for i in lis:
            Tr = Tr + i.count('T')
        if Tr == 0 :#if the treasure number is zero, then raise error
            raise ValueError('no treasure')
        n_emp = 0
        for i in lis:
            n_emp = n_emp + i.count('*')# count the number of empty space
        if num_traps < 0:# if the number of traps less than 0, raise error
            raise ValueError('number of traps less than 0')
        if n_emp < num_traps:## if the number of empty space less than traps less, raise error
            raise ValueError('empty space is less than number of traps')
        self.num_traps = num_traps
        self.add_traps()#recall the add_traps method
        
    def read_map_file(self, filename):
        fi = open(filename, 'r') #open file
        fil = fi.readlines() #gives a list of string
        self.dungeon_map=[]
        for i in fil:#split each string into sublist and add to a list
            i=i.rstrip('\n')
            self.dungeon_map.append(list(i))
        return self.dungeon_map
    
    def get_coords_of_empty_spaces(self):
        lis = self.dungeon_map
        emp_sp = []
        for i in lis:
            for j in i:
                if j == '*':
                    tup = lis.index(i) ,i.index(j) #tuple the empty space
                    emp_sp.append(tup)
        return emp_sp
    
    def get_char_at(self, coord):
        lis = self.dungeon_map#recall the list of sublist
        coor = lis[coord[0]][coord[1]] # the character at this place
        return coor 
            
    def visit_square(self, coord, player):    
        chac = Dungeon.get_char_at(self,coord) # call get_char_ at method, returns a character
        plr = Player(player) # class Player, set plr as object of Player
        if chac == 'T': # if the character is T, then game over
            print('Game over, Treasure found')
            return True
        if chac == '*' or chac == 'x':#if the character is * or x, nothing happens
            return False
        if chac == '^':#if the character is ^, lose one health
            plr.get_health = plr.get_health - 1
            if plr.get_health == 0: #if health is 0, dead , game over
                print('Game over, Player dead')
                return True
                    
    def enter(self, player):
        cur_coord = self.get_starting_coordinate()
        num_moves = 0
        
        while True:
            game_over = self.visit_square(cur_coord, player)
            if game_over:
                break # end of game
            
            print(get_directions_message(self.dungeon_map, cur_coord))
            chosen_direction = input("Where would you like to go?\n>")
            valid_directions = get_directions(self.dungeon_map, cur_coord)
            if chosen_direction not in valid_directions:
                print("Invalid direction.")
                continue
            
            cur_coord = get_next_coordinate(cur_coord, chosen_direction)
            num_moves += 1
    
    def get_starting_coordinate(self):
        empty_spaces = self.get_coords_of_empty_spaces()
        return random.choice(empty_spaces)
    
    def add_traps(self):
        coords_of_empty_spaces = self.get_coords_of_empty_spaces()
        while self.num_traps > 0:
            coord = random.choice(coords_of_empty_spaces)
            self.dungeon_map[coord[0]][coord[1]] = '^'
            coords_of_empty_spaces.remove(coord)
            self.num_traps -= 1

name = input("Please enter player name:\n> ")
player = Player(name)
dungeon = Dungeon("d1.txt", 4)
dungeon.enter(player)