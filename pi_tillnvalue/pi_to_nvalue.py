#pi=(Diameter of circle)/(circumference of circle)
#Chudnovsky Algorithm

import math
from decimal import *


#Define factorial using recursion
def factorial(n):
    
    if not n:
        return 1
    return n*factorial(n-1)


#Define k
#k=number of decimal places.
#k iterations give k-1 decimal places. so, we use, k=k+1
def iter_k(k):
    k=k+1
    getcontext().prec=k
    sum1=0
    for k in range(k):
        first = factorial(6*k)*(13591409+545140134*k)
        down = factorial(3*k)*(factorial(k))**3*(640320**(3*k))
        sum1 += (first)/down
    return Decimal(sum1)

#get value of pi
def pi_value(k):

    it1= iter_k(k)
    up = 426880*math.sqrt(10005)
    pi = Decimal(up)/it1
    return pi    

#main function
def first():
    
    k=int(input("Enter the decimal place value: "))
    result=pi_value(k)

    print("The pi value till {} decimal places is - {} ".format(k,result))



if __name__=='__main__':
    first()



   