#!/usr/bin/env python
# coding: utf-8

# In[19]:


tamaño = int(input("tamaño del triángulo: "))

for i in range(1, tamaño + 1):
    for j in range(i):
        print("* ", end="")
    print()

for i in range(1, tamaño):
    for j in range(tamaño - i):
        print("* ", end="")
    print()


# In[ ]:





# In[ ]:




