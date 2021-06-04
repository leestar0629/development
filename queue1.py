a=int(input())
queue=[]
for x in range(a):
    key=input().split()
    if key[0] == 'push':
        queue.append(key[1])
    elif key[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif key[0] == 'size':
        print(len(queue))
    elif key[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif key[0]=='front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif key[0]=='back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
