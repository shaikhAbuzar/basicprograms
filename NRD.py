def left_shift(a,q):
    m=""
    n=""
    for i in range(len(a)):
        if(i==len(a)-1):
            m=m[:]+q[0]
        else:
            m=m[:]+a[i+1]
    for i in range(len(q)):
        if(i==len(q)-1):
            n=n[:]+""
        else:
            n=n[:]+q[i+1]
    return m,n
    
def toBin(n):
    st=bin(n)
    s=st[2:]
    return s

def zadd(n,count):
    st=str(n)
    s=st[::-1]
    for i in range(count-len(st)):
        s=s[:]+"0"
    st=s[::-1]
    return st

def negative(n):
    s=" "
    for i in range(len(n)):
        if n[i]=="0":
            s=s[:]+"1"
        elif n[i]=="1":
            s=s[:]+"0"
    m=int(s,2)+1
    return zadd(toBin(m),len(n))

def binAdd(a,b):
    m=0
    s=''
    m=int(a,2)+int(b,2)
    s=toBin(m)
    if len(s)>len(a):
        s=s[1:]
    return s

def nonRestoringDivision(dividend,divisor):   
    q=toBin(dividend)
    a=toBin(0)
    b=toBin(divisor)
    
    count=len(q)
    q=zadd(q,count)
    a=zadd(a,count)
    b=zadd(b,count)
    print('\n Q=',q)
    print(' A=',a)
    print(' B=',b)
    
    neg_b=negative(b)
    print('-B=',neg_b,'\n')
    #prinnting in Tabular format
    print('   A           Q         Operation\n')
    for j in range(len(q)):
        #Left Shift
        a,q=left_shift(a, q)
        print(' ',a,'    ',q,end="   ---->Shift Left")
        print()
        #Addition or Subtraction of B
        if(a[0]=='0'):
            a=binAdd(a,neg_b)
            print(' ',a,end=' ')
            print("    ",q,end="   ----> A->A-B")
        elif(a[0]=='1'):
            a=binAdd(a,b)
            print(' ',a,end=' ')
            print("    ",q,end="   ----> A->A+B")
        print()
        '''Assigning value to q'''
        if a[0]=='0':
            for i in range(len(q)):
                if i==len(q)-1:
                    q=q[:]+'1'
            print(' ',a,end=' ')
            print("    ",q,end="  ----> Q-->1\n\n")
        elif a[0]=='1':
            for i in range(len(q)):
                if i==len(q)-1:
                    q=q[:]+'0'
            print(' ',a,end=' ')
            print("    ",q,end="  ----> Q-->0\n\n")

    #if the remainde ris negative
    if a[0]=='1':
        a=binAdd(a, b)
    print("Binary Quotient :",q)
    print("Binary Remainder:",a,'\n')
    print("Decimal Quotient :",int(q,2))
    print("Decimal Remainder:",int(a,2))

def main():
    print(">>>>>>>>>>>Program For Non-Restoring Division<<<<<<<<<<<<")
    print('Enter the value of Q:',end=' ')
    q=int(input())
    print('Enter the value of B:',end=' ')
    b=int(input())    
    nonRestoringDivision(q,b)
    
main()
