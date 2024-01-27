import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import pyplot
import math
r_e=4.6239
ga=1.4
AR=5.8
MF=3.33183
n=10000
nb=1#1-n^2
d=(MF-1)/n
M=np.zeros(n)
AR=np.zeros(n)
meyer=np.zeros(n)
mach=np.zeros(n)
alpha=np.zeros(n)
x=np.zeros(n)
x1=np.zeros(n)
y1=np.zeros(n)

f1=2/(ga+1)
f2=(ga-1)/2
f3=(ga+1)/(2*(ga-1))
f4=(ga+1)/(2*(ga-1))
f5=(ga+1)/(ga-1)

for i in range(n):
    M[i]=1+(i*d)
    print(M[i])

for j in range(n):
    AR[j]=(1/M[j])*((f1*(1+(f2*M[j]*M[j])))**f4)
    

for k in range(n):
    meyer[k]=(f5**0.5)*(math.atan((1/f5)*(M[k]*M[k]-1))**0.5)-(math.atan(((M[k]**2-1)**0.5)))

for l in range(n):
    mach[l]=math.asin(1/M[l])

for i in range(n):
    alpha[i]=mach[i]-meyer[i]

for j in range(n):
    x[j]=(M[j]*math.sin(alpha[j])*AR[j])/5.8
    x1[j]=(1-(1-x[j]))/math.sin(alpha[j])*r_e*math.cos(alpha[j])
    y1[j]=(1-(1-x[j]))/math.sin(alpha[j])*r_e*math.sin(alpha[j])
    print(x1[j])
    print(y1[j])
    
plt.plot(x1,y1)
plt.show()
data = pd.DataFrame({'drag': x1,'time': y1})
    
    
plt.plot(x1,y1)
plt.show()
data = pd.DataFrame({'drag': x1,'time': y1})
file_name = 'billy_got_molested.xlsx'
data.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')
    
    
