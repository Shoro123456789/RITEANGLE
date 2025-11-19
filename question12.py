import numpy as np
from scipy import stats
counter=0
for HH in range(0,100):
    for MM in range(0,60):
        for SS in range(0,60):
            sample=np.array([],dtype=int)
            for i in list(str("{0:0=2d}".format(HH))):
                sample=np.append(sample,int(i))
            for i in list(str("{0:0=2d}".format(MM))):
                sample=np.append(sample,int(i))
            for i in list(str("{0:0=2d}".format(SS))):
                sample=np.append(sample,int(i))
            #stat= stats.mode(sample)
            #print(str(stat.count)+","+str(stat.mode))
            #if stat.count==2:
            #    counter+=1
            #    print(str(HH)+":"+str(MM)+":"+str(SS)+"     count:"+str(counter))
            if len(np.unique(sample))==2:
                counter+=1
                print(sample)
                print("count:"+str(counter))
print(counter)