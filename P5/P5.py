#!/usr/bin/env python
# coding: utf-8

# In[4]:


from math import sqrt
A = int(input("Ingrese el coeficiente de la variable cuadrática\n"))
B = int(input("Ingrese el coeficiente de la variable lineal\n"))
C = int(input("Ingrese el término independiente\n"))

x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)  

x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A) 

print("Las soluciones de la ecuación son:")
print(x1)
print(x2)


# In[ ]:




