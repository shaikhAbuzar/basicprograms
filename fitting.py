jobs=[]#Book's Blocks
cand=[]#Book's Jobs
temp=[]
best=[]
first=[]
worst=[]
print(">>>>>>>>>>>>PROGRAM FOR BEST, FIRST, WORST FIT<<<<<<<<<<<<")
#USER INPUT
nj=int(input('Enter the No. of Blocks: '))
nc=int(input('Enter the No. of Jobs: '))

print("\nValue For Jobs")
for i in range(nc):
    print("Job No.",i+1,':',end=' ')
    val=int(input())
    cand.append(val)

print("\nValue For Blocks")
for i in range(nj):
    print("Block No.",i+1,':',end=' ')
    val=int(input())
    jobs.append(val)
    
copy=cand.copy()

#FIRST FIT
for i in range(len(cand)):
    for j in range(len(jobs)):
        if(cand[i]<=jobs[j]):
            temp.append(jobs[j])
    i=0
    while i<len(temp):
        if temp[i] not in first:
            first.append(temp[i])
            break
        else:
            i+=1
    temp.clear()
    
#WORST FIT
for i in range(len(cand)):
    for j in range(len(jobs)):
        if(cand[i]<=jobs[j]):
            temp.append(jobs[j])
    temp.sort(reverse=True)
    i=0
    while i<len(temp):
        if temp[i] not in worst:
            worst.append(temp[i])
            break
        else:
            i+=1
    temp.clear()
    
#BEST FIT
copy.sort()
for i in range(len(copy)):
    for j in range(len(jobs)):
        if(copy[i]<=jobs[j]):
            temp.append(jobs[j])
    temp.sort()
    i=0
    while i<len(temp):
        if temp[i] not in best:
            best.append(temp[i])
            break
        else:
            i+=1
    temp.clear()
    
#OUTPUT
i=0
print('\nOUTPUT FOR BEST FIT:')
print('JOBS     BLOCKS')
while i<len(best):
    print(copy[i],'---->>',best[i])
    i+=1
print('\nOUTPUT FOR FIRST FIT:')
i=0
print('JOBS     BLOCKS')
while i<len(first):
    print(cand[i],'---->>',first[i])
    i+=1
print('\nOUTPUT FOR WORST FIT:') 
i=0
print('JOBS     BLOCKS')
while i<len(worst):
    print(cand[i],'---->>',worst[i])
    i+=1
