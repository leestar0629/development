class Stack :
    def __init__(self):
        self.value=[]
    def push(self,number):
        self.value.insert(0,number)
    def pop(self):
        if len(self.value)==0:
            print(-1)
        else:
            print(self.value.pop(0))
    def top(self):
        if len(self.value)==0:
            print(-1)
        else:
            print(self.value[0])

    def empty(self):
        if len(self.value)==0:
            print(1)
        else:
            print(0)
    def size(self):
        print(len(self.value))


ex=Stack()
a=int(input())
for x in range(a):
    i=(input()).split()
    if i[0]=='push':
        ex.push(int(i[1]))
    elif i[0]=='top':
        ex.top()
    elif i[0]=='size':
        ex.size()
    elif i[0]=='empty':
        ex.empty()
    elif i[0]=='pop':
        ex.pop()