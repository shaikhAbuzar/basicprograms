rv = True
exp = []

def paraextract(expr):
    para = ['(','{','[',']','}',')']
    for i in expr:
        if i in para:
            exp.append(i)

def paracheck(i,op):
    global rv
    if exp[0] == ')' or exp[0] == ']' or exp[0] == '}':
        return False
    while rv:
        if exp[i] == '{' or exp[i] == '[' or exp[i] == '(' :
            rv = paracheck(i+1,exp[i])
        if (op == '(' and exp[i] == ')') or (op == '[' and exp[i] == ']') or (op == '{' and exp[i] == '}'):
                exp.pop(i)
                exp.pop(i-1)
                return True
        if (op == '(' and (exp[i] == '}' or exp[i] == ']')) or (op == '[' and (exp[i] == '}' or exp[i] == ')')) or (op == '{' and (exp[i] == ')' or exp[i] == ']')):
                return False

if __name__ == "__main__":
    expr = list(input())
    paraextract(expr)
    if paracheck(1,exp[0]):
        print('true')
    else:
        print('false')