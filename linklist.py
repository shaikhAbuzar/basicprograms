linkedList=[1,2,3,4,5,6]
while True :
    print('MENU')
    print('1.ADD AT BEGINING\n2.ADD IN MIDDLE\n3.ADD IN ENDING')
    print('4.REMOVE FROM BEIGINING\n5.REMOVE FROM MIDDLE\n6.REMOVE FROM END')
    print('7.DISPLAY LIST\n8.EXIT')
    choice = int(input('Enter Your Choice: '))
    if choice == 1:
        val = input('Enter the element to add: ')
        linkedList.insert(0,val)
        print(val,'Added Successfully')
    elif choice == 2:
        val = input('Enter the element to add: ')
        pos = int(input('Enter the position of element from 0: '))
        linkedList.insert(pos,val)
        print(val,'Added Successfully at position',pos)
    elif choice == 3:
        val = input('Enter the element to add: ')
        linkedList.append(val)
        print(val,'Added Successfully')
    elif choice == 4:
        val = linkedList.pop(0)
        print(val,'Removed')
    elif choice == 5:
        pos = int(input('Enter position: '))
        val = linkedList.pop(pos)
        print(val,'Removed from',pos)
    elif choice == 6:
        val = linkedList.pop()
        print(val,'Removed')
    elif choice == 7:
        for i in linkedList:
            print(i,'-->',end=' ')
        print('NULL')
    else:
        break