#1
def countdown(x):
    c=[]
    for x in range(x,-1,-1):
        c.append(x)
    print(c)

#2
def pnr(x):
    print(x[0])
    return(x[1])

#3
def fpl(x):
    return x[0] +len(x)

#4
def vgts(x):
    nl=[]
    if len(x)<2:
        return 'false'
    else:
        for a in x:
            if a>x[1]:
                nl.append(a)
        print(len(nl))
        return nl

#5
def lv(s,v ):
    l=[]
    for a in range(0,s):
        l.append(v)
    return l
