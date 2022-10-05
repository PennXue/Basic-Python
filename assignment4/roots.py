from math import log
import numpy as np
import matplotlib.pyplot as plt
num_iter = 100 # a large number which could help to approcimate the real root
def secant(f, a, b, num_iter, epsilon=1e-6):
    a_n, b_n = a, b
    for i in range(num_iter):
        slope =  (f(b_n) - f(a_n)) / (b_n - a_n)
        x_sec = a_n - f(a_n) / slope  #x-intercept of secant
        f_xsec = f(x_sec)
        if f(a_n) * f_xsec < 0:
            a_n, b_n = a_n, x_sec
        elif f(b_n) * f_xsec < 0:
            a_n, b_n = x_sec, b_n
        elif abs(f_xsec) < epsilon:
            #print("Found solution.")
            return x_sec
        #else:
            #print("Root is not in the interval.")
        #    return None
    return a_n - f(a_n) / slope
# function f(t) of t, which v is set to be 335
def f(x): # given the value for u, M0, m and g
    return 2510*(log(2.8*10**6/(2.8*10**6 - ((13.3*10**3)*x)))) - (9.81*x) - 335
print('The time when the rocket reaches the speed of sound (335 m/s):', secant(f, 0, 150, num_iter),'s') # interval is [0, 150]
# function v(t) of t, which exclude the sound speed
def v(x): # given the value for u, M0, m and g
    return 2510*(log(2.8*10**6/(2.8*10**6 - ((13.3*10**3)*x)))) - (9.81*x)
x_value = np.arange(150+1) #interval include 150 
y_value = np.array([v(x) for x in x_value])# start with the list of appropriate y_value operated by v(x_value), and then change it to an array
plt.plot(x_value, y_value) #plot into the diagram
plt.ylabel('The speed of the rocket') #label a title to y-axis
plt.xlabel('Time measured from liftoff') #label a title to x-axis
plt.title('Speed of rocket at different time') #label a title to diagram
plt.savefig("rocket.png")# save to "rocket.png"
plt.show() #show the image