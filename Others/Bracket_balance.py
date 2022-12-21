stack=[]
def isbalanced(into):
    for i in range(0,len(into)):
        if into[i]=="(":
            stack.append(")")
        elif into[i]=="{":
            stack.append("}")
        elif into[i]=="[":
            stack.append("]")
        else:
            if(len(stack)>0):
                a=stack.pop()
                if a == into[i]:
                    pass
            else:
                print("false")
                return 0
        if (i == (len(into)-1) and len(stack)==0):
            print("true")

s=input("Enter value: ")
isbalanced(s)
