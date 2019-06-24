import random
import numpy as np
lst=[]
while len(lst)<16:
  if len(lst)==0:
    lst.append(random.randint(100,200))
  else:
    lst.append(random.randint(100,200))
    if abs(lst[-1]-lst[-2]) != 5:
      lst.pop()
    else:
      continue
array=np.array(lst)
array1=array.reshape((8,2))
print(array1)s