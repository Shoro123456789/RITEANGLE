import numpy as np
from scipy.integrate import quad
#a=13
def f(x):
    return (m*(x-1)+2)**2
def g(x):
    return ((1/m)*(x-2)+1)**2
closest=0.0
#had to test multiple ranges to find 4 values of a (2.0001, 6),(6,8),(8,10)
for a in np.arange(6,8,0.00001):
    m=(a-2)/(12-1)
    result1, error = quad(f, 1, 12)
    result2, error2 = quad(g, 2, a)
    #print(str(result1)+" "+str(result2))
    #print(str(np.abs(np.pi*(result1-result2))))
    if np.abs(np.pi*(result1-result2))<50.0 and np.abs(np.pi*(result1-result2))>closest:
        closest=np.abs(np.pi*(result1-result2))
        best_a=a
        print("Best a so far: "+str(best_a)+" with area: "+str(closest))
        best_result1=result1
        best_result2=result2
print("Final Best a: "+str(best_a)+" with area: "+str(closest))
print("Final integrals: "+str(np.pi*best_result1)+" and "+str(np.pi*best_result2))
