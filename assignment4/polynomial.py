import matplotlib.pyplot as plt
import numpy as np

class Polynomial:
    def __init__(self):
        self.power2coeff = {} # an empty dictionary
    
    def add_term(self, coeff, power):
        self.power2coeff[power] = coeff #assign each power with coeff value into the dictionary

    def __str__(self):# will be called when print(self)
        result = ''
        for power, coeff in self.power2coeff.items():
            result += '{:.2f}x{} '.format(coeff, power)
        return result
    def evaluate(self,x):
        result = 0 #set result to zero
        for k in self.power2coeff.keys(): #go through the keys in self.power2coeff
            each = self.power2coeff[k]*x**k #do the math operation 
            result = result + each # add up each term
        return result # return the integer
    def add(self,other_poly):
        for keys in other_poly.power2coeff.keys():
            if keys in self.power2coeff.keys(): #the key from other_ploy dictionary, which also exist in self dictionary
                self.power2coeff[keys] = self.power2coeff[keys] + other_poly.power2coeff[keys] #add the coefficient together
            else:#the key from other_ploy dictionary, which doesn't exist in self dictionary
                self.power2coeff[keys] = other_poly.power2coeff[keys]
        return self
    def plot(self, a , b , N , filename):
        x_value = np.linspace(a, b, num=N) #a numpy array of N number in interval (a,b) with even space
        y_value = Polynomial.evaluate(self,x_value) # call the function evaluate in class Polynomial to operate the x_value to get y_value
        plt.plot(x_value,y_value) #plot the two arrays 
        plt.title('Polynomial:{}'.format(str(self))) # add the title 
        plt.savefig("{}".format(filename)) # save with the filename 
        plt.show() #show the diagram
    def integrate(self,a,b):
        result={} # set an empty dictionary 
        for power, coefficient in self.power2coeff.items():  
            result[power + 1] =  coefficient / (power + 1)#method from assignment 2, to assign each power with coefficient value into the dictionary after integration
        self.power2coeff = result #set the self.power2coeff of the class to the integrated dictionary
        final = Polynomial.evaluate(self,b) - Polynomial.evaluate(self,a) # the method of integration, f(upper limit)-f(lower limit)
        result_2={} #after assigned the value for final, set the self.power2coeff back to its origin
        for power, coefficient in self.power2coeff.items():  
            result_2[power - 1] =  coefficient * (power) #method of derivation 
        self.power2coeff = result_2 # set the self.power2coeff of the class back to origin by using the inverse method: derivation
        return final
    def trapz_integrate(self,a,b,N):
        dx = (b-a)/N #divide interval(a,b) to N, to get even spaced delta x-value
        area = 0.0
        x = a #start with a
        for k in range(N):
            anew = (dx/2)*(Polynomial.evaluate(self,x)+Polynomial.evaluate(self,x+dx)) #operation of each trapezoid 
            area = area + anew #add to the area
            x = x + dx # assign new x-value for next run
        return area # return of value of area, integer 