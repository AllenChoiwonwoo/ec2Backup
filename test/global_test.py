pageToGo = 0



def next1pg():
    global pageToGo
    pageToGo = pageToGo+1
    print(pageToGo)
    next5pg()

def next5pg():
    global pageToGo
    pageToGo = pageToGo+5
    print(pageToGo)

def next10pg():
    global pageToGo
    pageToGo = pageToGo + 10
    print(pageToGo)
    next1pg()

while pageToGo < 154:
    next10pg()
    # next1pg()
