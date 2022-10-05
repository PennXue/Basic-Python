'''Pengyu Xue 260927847'''
valid_t=[] #vaild temputer list, set before while loop therefore to stop the repeatation values
while True: #if vaild is True then run, and it will always run until there is a break statement
    temp=[] #start as empty list at the beginning of every run
    enter = input('Enter readings:') #ask to enter the value
    if enter != 'stop':
        enter_list = enter.split(",")#split the string into the list
        for i in enter_list:
            temp_int=int(i)#change it to a integer
            temp.append(temp_int) #list the temputers in the empty list
        for t in temp:#check if it is valid value
            if t > -70 and t < 50:
                valid_t.append(t)#add valid value into the new list
    if enter == 'stop':
        break #stop the loop if the input is 'stop'
if valid_t==[]: # no valid values in the list
    print('Really broken sensor!')
else: # using the method to print two decimal points in float format
    print('Temperatures today: maximum was', '{0:.2f}'.format(float(max(valid_t))), 'degrees, minimum was','{0:.2f}'.format(float(min(valid_t))),"degrees, average was", '{0:.2f}'.format(float(sum(valid_t)/len(valid_t))), ' degrees.')