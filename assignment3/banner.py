'''Pengyu Xue 260927847'''
def search_lines(txt): #this function returns a dictionary of all letters with corresponding sublist
    f=open("banner_letters.txt",'r')#open the file , and read mode
    fx=f.readlines() #fx is a list of string
    a=[] #all the lines 
    for i in fx:
        x=i.rstrip('\n')
        a.append(x) # all the lines with \n removed 
    letters='abcdefghijklmnopqrstuvwxyz'
    let_s=list(letters) #list of all letters
    number=[]
    for i in range(182): #total of 182 lines
        number.append(i)
    numb=number[::7] # list of all numbers with a space of 7
    dic={} #the dictionary of each letter, have the respresented lines
    for le in let_s:
        let=[]
        ind = let_s.index(le) # index of le in let_s
        start = numb[ind] # the number of the starting line in the file
        for i in range(start,start+7):
            let.append(a[i]) # a list of string of each le in let_t
        dic[le] = let # add to the dictionary
    # above is to set the dictionary
    t=list(txt)#list the txt string into a list
    di={}
    for i in t:
        di[i]=dic[i]#add the appropriate lines with the letter into the dictionary
    return di 
def make_banner(text):
    if text.isalpha() is False: #if the characters in the string are not all alpha, then raise the error
        raise ValueError("All characters in text must be alphabetic.")
    txt=text.lower() #change all letters into lowercase
    dic = search_lines(txt) # returns a dictionary
    t=list(txt)#list the txt string into a list
    di={}
    string = ''
    for i in t:#add the appropriate lines with the letter into the dictionary
        di[i]=dic[i]
    for i in range(7):#each letter contains 7 lines
        for z in t:#each letter in the string
            d = di[z]#the string for each line
            string = string + d[i] + ' '#add each line together,  but end with a space behind
        string = string + '\n'#after the first line, start a new line
    return print(string) #return a string which exclude the string'\n', but start a new line
    
    
