'''Pengyu Xue 260927847'''
def dec_to_bin(dec_string): #define the function from decimal to binary
    dec_=[]
    dec_string=int(dec_string)
    while dec_string>0:
        rem=int(dec_string)%2 #reminder of the binary number divide by 2
        dec_.append(rem)#add the reminder to the list
        dec_string=(dec_string-rem)/2 #to make sure x is still a integer not a float
    dec_=dec_[::-1] #the order should be reversed
    dec_str=''
    for i in dec_: #add the value from list into a string
        dec_str+=str(i)
    deci=int(dec_str) #convert the string to integer
    return deci

def bin_to_dec(bin_string):#define the function from binart to decimal
    bina=[]
    for i in bin_string:
        bina.append(i)#add the value into a list
    bina=bina[::-1]#reverse the order
    bin_=0 #this function is an addition, so the origin is zero
    bin_1 = 0
    for i in bina:
        if i == '1' or i == '0':
            bin_1 += int(i)*(2**(bin_)) #convert the string to integer value , and sum up the value, when i is 0, bin_1 remain unchanged, if i is 1, then do the
            bin_ += 1
        else: # there is value not equal to 1 or 0 in the list
            return None
    return bin_1
def menu():
    while True: #run until there is a break statement
        inp=input("""Options:
 1) Binary to Decimal
 2) Decimal to Binary
 3) Exit program
Enter your choice:""") #input the choice of user
        if inp=='1':
            binary=input('Please enter the binary number:')
            print(binary,'in decimal is', bin_to_dec(binary))
        if inp=='2':
            decimal=input('Please enter the decimal number:')#ask the user to input a decimal
            print(decimal, "in binary is", dec_to_bin(decimal)) #recall the dec_string function
        if inp=='3':
            print('Goodbye.')
            break #this break statement will shut the program

menu()
