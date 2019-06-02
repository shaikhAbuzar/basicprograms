def Total(a):
    Sum=0
    for i in range(len(a)):
        Sum+=a[i]
    return Sum

proc=[]
btime=[0]
stime=[]
atime=[]
wtime=[]
tatime=[]
value=[]
n=int(input('Enter total No of Inputs: '))

for i in range(n):
    print('Process No',i+1,':',end=' ')
    a=input()
    proc.append(a)

for i in range(n):
    print('Burst Time Value',i+1,':',end=' ')
    b=int(input())
    btime.append(b)

temp_b=btime.copy()
btime=btime[1:]
tq=int(input('Enter the Time Quantum: '))

for i in range(n):
    atime.append(0)
    stime.append(0)
    wtime.append(0)
    tatime.append(0)

print('\n>>>>>>GANTT CHART<<<<<\n')
j=k=p=0
l=Total(btime)
for i in range(4*l):
    k = int(i / 2)
    if i%2 == 1:
        m = k % n
        if btime[m] == -1:
            continue
        if btime[m] <= tq:
            stime[m] = atime[p]
            wtime[m] += (stime[m] - atime[m])
            atime[m] = atime[p] + btime[m]
            btime[m] = -1
            p = m
        if btime[m] > tq:
            stime[m] = atime[p]
            wtime[m] += (stime[m] - atime[m])
            atime[m] = atime[p] + tq
            btime[m] = btime[m] - tq
            p = m
        value.append(stime[p])
        print('|', proc[m], end='')
    else:
        print('',end=' ')
value.append(atime[p])
print('|')

for i in range(2*len(value)):
    if i % 2 == 1:
        print(' ', end=' ')
    else:
        print('{:02d}'.format(value[j]), end=' ')
        j += 1
print('\n')

print('WAITING TIME = START TIME - ARRIVAL TIME')
for i in range(n):
    print(proc[i],'=',wtime[i])
total=Total(wtime)
print('Average Waiting Time: ',total/n,'\n')

print('TURN AROUND TIME = WAITING TIME + BURST TIME')
for i in range(n):
    print(proc[i],'=',wtime[i],'+',temp_b[i+1],'=',temp_b[i+1]+wtime[i])
    tatime.append(int(temp_b[i+1]+wtime[i]))
total=Total(tatime)
print('Average Turn Around Time: ',total/n,'\n')
