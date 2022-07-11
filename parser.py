import collections
fp = open(r'F:\Python\Python\design (4)\Mike (2)\Mike\design.nodes')
line = fp.readline()
nodes=collections.defaultdict(list)
cnt = 1
while line:
    
    (key,val,val1)=line.split()
    nodes[int(cnt)].append(val)
    nodes[int(cnt)].append(val1)
    line = fp.readline()
    cnt += 1

     
fp.close()

fp = open(r'F:\Python\Python\design (4)\Mike (2)\Mike\design.pl')

line = fp.readline()
pl=collections.defaultdict(list)
cnt = 1
while line:
    string1=line.replace(':', "")  
    (key,val,val1,val2)=string1.split()
    pl[int(cnt)].append(key)
    pl[int(cnt)].append(val)
    pl[int(cnt)].append(val1)
    line = fp.readline()
    cnt += 1

    
fp.close()


fp = open(r'F:\Python\Python\design (4)\Mike (2)\Mike\design.nets')
line = fp.readline()
string1=line.replace(":", "")
a=string1.split()
NumNets=a[1]

line=fp.readline()
string1=line.replace(":", "")
a=string1.split()
NumPins=a[1]
line=fp.readline()
nets=collections.defaultdict(list)
cnt = 0
while line:
    string1=line.replace(":", "")
    (key,val)=string1.split()
    for i in range(int(val)):
        line=fp.readline()
        (key1,val1)=line.split()
        nets[int(cnt)].append(key1)
    line = fp.readline()
    cnt += 1



fp.close()


fp = open(r'F:\Python\Python\design (4)\Mike (2)\Mike\design.scl')
line = fp.readline()
string1=line.replace(":", "")
a=string1.split()
NumRows=a[1]



scl=collections.defaultdict(list)
cnt = 0

for line in fp:
    if line.strip() == 'CoreRow Horizontal':
        line = fp.readline()
        string1=line.replace(":", "")
        (key1,val)=string1.split()
        scl[int(cnt)].append(val)
        line = fp.readline()
        string1=line.replace(":", "")
        (key1,val)=string1.split()
        scl[int(cnt)].append(val)
        cnt += 1
        if key1== 'Sitewidth':
            cnt += 1
            break
        
    


fp.close()
print(pl)


