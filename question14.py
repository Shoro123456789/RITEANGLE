proportions = [45,45]
counter=0
for i in range(1,proportions[0]+1):
    for j in range(1,proportions[1]+1):
        for x_offset in range(0,proportions[0]):
            for y_offset in range(0,proportions[1]):
                if i>j:
                    if i+x_offset<=proportions[0] and j+y_offset<=proportions[1]:
                        print(str(i)+","+str(j))
                        counter+=1
print("Total count: "+str(counter))