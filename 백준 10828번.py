import sys
a=int(sys.stdin.readline())
ex=[]
for x in range(a):
    key=sys.stdin.readline().split()

    if key[0]=='push':
        ex.append(key[1])
    elif key[0]=='top':
        if len(ex)==0:
            print(-1)
        else:
            print(ex[-1])
    elif key[0] =='size':
        print(len(ex))
    elif key[0]=='empty':
        if len(ex)==0:
            print(1)
        else:
            print(0)
    elif key[0]=='pop':
        if len(ex)==0:
            print(-1)
        else:
            print(ex.pop())