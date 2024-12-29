def add(n1,n2):
    '''adds'''
    return n1+n2
def sub(n1,n2):
    '''subtracts'''
    return n1-n2
def multiply(n1,n2):
    '''multiplies'''
    return n1*n2
def divide(n1,n2):
    '''divides'''
    return n1/n2

func={'+':add,
      '-':sub,
      '*':multiply,
      '/':divide}

def calc():
    ch=True
    num1=float(input("Number 1: "))
    print("Pick an operation")
    for key in func:
        print(key)

    while ch==True:
        opr=input()
        num2=float(input("Number 2: "))

        operation=func[opr]
        ans=operation(num1,num2)
        print(f"{num1} {opr} {num2} = {ans}")
        op=input(f"Enter 'y' to continue with {ans} and 'n' to start a new calculation 'ex' to exit : ")
        if op=='y':
            num1=ans
            print("Enter next operator:")
        elif op=='n':
            ch=False
            calc()    
        else:
            ch=False        

calc()