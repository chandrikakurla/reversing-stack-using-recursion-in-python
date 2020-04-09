def CreateStack():
    stack=[]
    return stack
def isEmpty(stack):
    if len(stack)==0:
        return True
    else:
        return False
def pop(stack):
    if not isEmpty(stack):
        return stack.pop()
    else:
        print("stack is empty")
        return
def push(stack,data):
    stack.append(data)
def insert_bottom(stack,obj):
    if isEmpty(stack):
        push(stack,obj)
    else:
        temp=pop(stack)
        insert_bottom(stack,obj)
        push(stack,temp)
def rev(stack):
    if not isEmpty(stack):
        temp=pop(stack)
        rev(stack)
        insert_bottom(stack,temp)
def print_Stack(stack):
    for i in range(len(stack)-1,-1,-1):
        print(stack[i],end=' ')
if __name__=="__main__":
    stack=CreateStack()
    push(stack,1)
    push(stack,2)
    push(stack,3)
    push(stack,4)
    push(stack,5)
    print("before reversing stack")
    print_Stack(stack)
    rev(stack)
    print("\nafter reversing stack")
    print_Stack(stack)






