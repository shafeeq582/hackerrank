reg=None
stack=list()
n=int(input())
sins=list()
i=0

def machine(ins,reg,stack):
    if ins[0]=='PUSH':
        stack.insert(0,int(ins[1]))
        
    elif ins[0]=='STORE':
        p=stack.pop(0)
        reg=p
        
    elif ins[0]=='LOAD':
        stack.insert(0,reg)
        
        
    elif ins[0]=='PLUS':
        x=stack.pop(0)
        y=stack.pop(0)
        z=x+y
        stack.insert(0,z)
        
    elif ins[0]=='TIMES':
        x=stack.pop(0)
        y=stack.pop(0)
        z=x*y
        stack.insert(0,z)
        
    elif ins[0]=='IFZERO':
        k=stack.pop(0)
        if k==0:
            m=int(ins[1])
            machine(sins[m-1],reg,stack)
            
    else:
        print(stack[0])
        
    

while i<n:
    ins=list(input().split())
    sins.append(ins)
    i+=1
    machine(ins,reg,stack)
