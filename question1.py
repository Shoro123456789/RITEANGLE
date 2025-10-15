from collections import Counter
sum=0
sum_of_products=0
combos=set()
total_sum=0
#for a in range(1,8):
#    for b in (10,20):
#        for c in range(1,9):
#            print(str(a)+str(b)+str(c))
#            sum += int(str(a)+str(b)+str(c))
 #           sum_of_products += a*b*c
#            combos+=1
#print(sum)
#print(sum_of_products)
#print(combos)
#print(str(sum/sum_of_products))
a,b,c=1,10,1
while len(combos)!=792:
    sum=int(str(a)+str(b)+str(c))
    if sum not in combos:
        combos.add(sum)
        total_sum+=sum
        sum_of_products += a*b*c
    a+=1
    b+=1
    c+=1
    if a==9:
        a=1
    if b==21:
        b=10
    if c==10:
        c=1
print(total_sum)
print(sum_of_products)
print(str(total_sum/sum_of_products))