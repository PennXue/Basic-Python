'''Pengyu Xue 260927847'''
n = int(input('Enter n:')) #ask to input one intege
non_prime=[] #list of number that are not prime
prime=[]#list of number that are prime
list_n=[]
for i in range(4,n): #exclude 0 to 3
    list_n.append(i)
for num in list_n: #check the prime numbers in n
    for i in range(2,num):
        if num%i ==0:
            non_prime.append(num)
non_prime = list(set(non_prime)) #leave the number that are not prime, only once in the list
for i in non_prime:#remove the number that are not prime out of the list
    list_n.remove(i) # all the prime number in one list
# above this line, everything is to find the prime numbers    
list=[] # empty list to collect all the sets
for i in list_n: # run by every prime number
    for a in range(2,i): #start from 2 to i
        b = i - a # b is the difference of i and a
        if i>b>a: # follow the condition i > b > a 
            list.append([a,b,i]) # the format will be lists in list
for i in list: #the method to seperate each list
    for a in i:
        print(a, end=' ') #print them with a space behind
        if i.index(a) == 2: # when it is the last integer in the list, skip a line
            print()   
            
        
