
        import numpy as np
        import random
        import csv
        m=int(input(\"Enter no. of rows : \"))
        n=int(input(\"Enter no. of column : \"))
        p=np.random.random((m,n))
        p
        with open(new_file.csv,w+) as my_csv:
            csvWriter = csv.writer(my_csv,delimiter=',')
            csvWriter.writerows(p)
      
