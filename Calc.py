def addition(a,b):
    print(a,"+",b,"=",a+b)
def multiple(a,b):
    print(a,"X",b,"=",a*b)
def subtraction(a,b):
    print(a,"-",b,"=",a-b)
def divide(a,b):
    print(a,"/",b,"=",a/b)

def values():
    a=int(input("Enter 1st No: "))
    b=int(input("Enter 2nd No: "))
    return a,b

def calc():
    i="y"
    while (i=="y" or i=="Y"):
        print(">>>>>>>MENU<<<<<<<")
        print("1. ADD\n2. SUBTRACT\n3. MULTIPLY\n4. DIVIDE")
        choice=int(input("Enter Your Choice: "))
        if choice is 1:
            a,b=values()
            addition(a,b)
        elif choice is 2:
            a,b=values()
            subtraction(a,b)
        elif choice is 3:
            a,b=values()
            multiple(a,b)
        elif choice is 4:
            a,b=values()
            divide(a,b)
        else:
            print("INVALID INPUT!")
        i=input("Continue [Y/N]: ")

def main():
    print(">>>>>>>>>>>>>> PROGRAM FOR CALCULATOR USING FUNCTIONS <<<<<<<<<<<<<<<")
    calc()

main()
