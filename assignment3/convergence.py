'''Pengyu Xue 260927847'''
def taylor_sum(k,n):
    if (k > 1) or (k <= -1):#If k is not between -1 and 1, a ValueError should be raised instead.
        raise ValueError()
    lim = 0 # start with 0
    for i in range(1,n+1): #add each term from 1 to nth term
        coe=-(-1)**i
        dif=k**i/i
        lim = lim + coe*dif
    return lim
import matplotlib.pyplot as plt #import the graphic module
x_value=[]
for i in range(10):#negative values in the x-axis
    x_value.append(-(i/10))
for i in range(1,11): #positive values in the x-axis
    x_value.append(i/10)
x_value.sort() #sort in order
colors=['b','#f97306','g','r'] #hex value for orange color
n=[1,3,5,9] # order of each line
lab=['n=1','n=3','n=5','n=9'] #the label of each line
for i in n: #4 lines
    y_value=[]  
    for x in x_value:
        y_value.append(taylor_sum(x,i)) #add the appropriate value into the y_value list
    plt.plot(x_value,y_value,colors[n.index(i)],label='{}'.format(lab[n.index(i)]))# plot each line, give colors and labels
plt.title('Taylor sum vs ln(x+1)') #add title to the graph
import math #need import math to calculate ln(x+1)
log_value=[]
for x in x_value:
    log_value.append(math.log(x+1)) # add the appropriate value into log_value list
plt.plot(x_value,log_value,'k',label='ln(x+1)',linewidth=2) #plot the ln(x+1) line
plt.savefig("taylorsum.png") #save to the file
plt.show()    # show the graph