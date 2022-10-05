'''Pengyu Xue 260927847'''
def create():
    # code here.
    dict={} #empty dictionary
    inp = input('Enter polynomial:')# ask the user to input a polynomial
    inp=inp.split()
    for i in range(len(inp)): #inp is a list, so use len to check the length of inp, shows a integer
        #for i, go through the list by index
        key=inp[i].split('x')[1]
        val=inp[i].split('x')[0] #split('x') will leave only integers, and 'd[something] = something' will add the value into the dictionary, we represent the power after each coefficients
        dict[key] = val #add value following the key to the empty dictionary
    return dict 

def display(polynomial):      
    # code here. #recall the dictionary
    for key in polynomial:#for each key value in the polynomial from input of create()
        if polynomial[key]=='-0.0' or polynomial[key]=='0.0': #print another thing if the key is 0
            print('0.00x0', end='')
            break
        else:
            final='{:.2f}'.format(float(polynomial[key])) + 'x' + key #change the string to integer and then change it to two decimal pointss; polynomial[key] recalls the relavent value stored in the dictionary; these are strings, add them up together 
            print(final,end=' ') #print the string one after another, prevent starting a new line
    print()# skip a line
        
def derivative(polynomial, order=1):    
    # code here.
    dict={}#empty dictionary
    power=[] # a list which collect all the power value
    coe=[] #a list which collect all the coefficiant value
    fin_p=[]#a list which collect all the power after derivation
    fin_c=[]#a list which collect all the coefficiant after derivation
    for p in polynomial.keys(): #collect all the power in the dictionary keys
        power+=[p]
    for c in polynomial.values():#collect all the power in the dictionary values
        coe+=[c]
    order = int(user_input) #change the order number
    while order>0: #if order = 0, then it won't run
        order = order - 1 #reduce one each time, to control how many times the while loop will run
        for i in range(len(power)):
            coe[i] = str(float(power[i])*float(coe[i])) # the relavent coefficiants have the same index as the power, derivation of coefficiant
            power[i] = str(int(power[i]) - 1) #derivation of power
    for po in power: #collect the power after derivation
        fin_p += [po]
    for co in coe:#collect the coefficiants after derivation
        fin_c += [co]
    for i in fin_c:# for situation that key value is 0
        if i == '0':
            dict={'0':"0"}
        else: #add related value following the index to the dictionary created at the beginning
            for i in range(len(fin_p)):
                dict[fin_p[i]] = fin_c[i] 
        return dict  #return the dictionary

def integrate(polynomial):    
    # code here.
    dict={} #an empty dictionary
    dic={}
    for key in polynomial: #the key value in polynomial
        power= int(key)+1 # integrate of power
        coe= str((1/power)*float(polynomial[key]))# integrate of coefficient, and convert to string format
        power=str(power)#convert to string format
        dic[power] = (coe) #add the relavent coefficient value with power value into the dictionary
    for i in dic: # in the dictionary, check all the value
        dict[i]= dic[i]#add value following the index number into the dictionary
    return dict #return the dictionary


polynomial = create() #this function will ask the user to input a polynomial and store as a dictionary 
display(polynomial) #recall the display() function
user_input = input('Enter order of derivative: ')
print('Derivative: ')
display(derivative(polynomial, order=int(user_input)))
print('Integral: ')
display(integrate(polynomial))