
#1
for x in range(0,151):
    print(x)

#2
for x in range(0,1001,5):
    print(x)

#3
count=[]
for x in range(1,101):
    if x%10==0:
        count.append('Coding Dojo')
    elif x%5==0:
        count.append('Coding')
    else:
        count.append(x)
print(count)

#4
y=0
for x in range(0,500001):
    if x%2!=0:
        y+=x
print(y)

#5
for x in range (2018,0,-4):
    print(x)

#6
lownum = 6
highnum = 24
mult = 3
for x in range(lownum,highnum,1):
    if x%mult==0:
        print(x)



