import collections
from typing import Collection
import matplotlib.patches as patches
from numpy.lib.function_base import append
from shapely.geometry import Polygon
import numpy 
import numpy as np
from collections import Counter
import math 
from copy import deepcopy
from numpy import array, dot
import operator
import pandas as pd 

np.set_printoptions(threshold=np.inf)
fp = open(r'F:\Python\Python\design (4)\Mike (2)\Mike\design.nodes')
line = fp.readline()
global nodes
nodes=collections.defaultdict(list)
cnt = 1
NumNodes=0
#getting data from design nodes
while line:
    
    (key,val,val1)=line.split()
    nodes[int(cnt)].append(key)
    nodes[int(cnt)].append(val)
    nodes[int(cnt)].append(val1)
    if(key=='NumNodes'):
        NumNodes=val1
    line = fp.readline()
    cnt += 1

     
fp.close()





fp = open(r'F:\Python\Python\design (4)\Mike (2)\Mike\design.pl')

line = fp.readline()
global pl
pl=collections.defaultdict(list)
cnt = 1
#getting data from design pl
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
global nets
nets=collections.defaultdict(list)
cnt = 0
Net_Degree=collections.defaultdict(list)
#getting data from design nets
while line:
    string1=line.replace(":", "")
    (key,val)=string1.split()
    Net_Degree[cnt].append(int(val))
    for i in range(int(val)):
        line=fp.readline()
        (key1,val1)=line.split()
        nets[int(cnt)].append(key1)
    line = fp.readline()
    cnt += 1


fp.close()

nets_adj=[]
for i in range(int(NumNets)):
    for j in range(len(nets[i])):

        
        val=nets[i][j]
        
        nets_adj.append(val)
    



fp = open(r'F:\Python\Python\design (4)\Mike (2)\Mike\design.scl')
line = fp.readline()
string1=line.replace(":", "")
a=string1.split()
NumRows=a[1]


global scl
scl=collections.defaultdict(list)
cnt = 0
#getting data from design scl
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


def lists_overlap(a, b):
    for i in a:
        if i in b:
            return True
    return False


def Enquiry(lis1):
    if len(lis1) == 0:
        return 0
    else:
        return 1


from shapely.geometry import Polygon
import random
import matplotlib.patches as patches
from matplotlib.patches import Circle, Rectangle, Arc, Ellipse
from statistics import mean
  
import numpy as np
import matplotlib.pyplot as plt
#setting subplots
fig, ax = plt.subplots()


ax.yaxis.grid(True, which='major')
ax.yaxis.grid(True, which='minor')


x_min_HPWL=[]
x_max_HPWL=[]
y_min_HPWL=[]
y_max_HPWL=[]

def Total_Perimeter_Wire_length(ptc_list,ax):
    total_perimeter_wire_lenght=0
    for i in range(len(nets)):
        for j in range(len(nets[i])):
            
            x_min_HPWL.append(int(ptc_list[nets[i][j]][0]))
            x_max_HPWL.append(int(ptc_list[nets[i][j]][1]))
            y_min_HPWL.append(int(ptc_list[nets[i][j]][2]))
            y_max_HPWL.append(int(ptc_list[nets[i][j]][3]))

        xminHPWL=min(x_min_HPWL)
        xmaxHPWL=max(x_max_HPWL)
        yminHPWL=min(y_min_HPWL)
        ymaxHPWL=max(y_max_HPWL)
        x=[xminHPWL,xminHPWL,xmaxHPWL,xmaxHPWL]
        y=[yminHPWL,ymaxHPWL,ymaxHPWL,yminHPWL]
        HPWL=(xmaxHPWL-xminHPWL)+(ymaxHPWL-yminHPWL)
        total_perimeter_wire_lenght+= HPWL

        '''
        checking if nets are calculated correctly
        #ax.add_patch(patches.Polygon(xy=list(zip(x,y)), fill=False,label='label',facecolor='red',color = 'green',clip_on=False))
        '''
        x_min_HPWL.clear()
        x_max_HPWL.clear()
        y_min_HPWL.clear()
        y_max_HPWL.clear()
    
    return total_perimeter_wire_lenght
         
            

y_min=100
y_max=180
x_min=0
x_max=100
plt.xlim(x_min,x_max)
plt.ylim(y_min,y_max)

global patch_list
patch_list=collections.defaultdict(list)
ptc_cnt=1

cnt=3

#random placement
for i in range((int(nodes[1][2])-int(nodes[2][2]))):
    index_x=nodes[cnt][0]
    rx = random.randint(x_min,x_max-int(nodes[cnt][1]))
    ry = random.randint(y_min,y_max-int(nodes[cnt][2]))
    x = [rx,rx,rx+int(nodes[cnt][1]),rx+int(nodes[cnt][1])]
    y = [ry,ry+int(nodes[cnt][2]),ry+int(nodes[cnt][2]),ry]
    patch_list[nodes[cnt][0]].append(rx)
    patch_list[nodes[cnt][0]].append(rx+int(nodes[cnt][1]))
    patch_list[nodes[cnt][0]].append(ry)
    patch_list[nodes[cnt][0]].append(ry+int(nodes[cnt][2]))

    
    
    centerx =mean(x)
    centery =mean(y)

    plt.text(centerx, centery,nodes[cnt][0])
    ax.add_patch(patches.Polygon(xy=list(zip(x,y)), fill=False,label=nodes[cnt][0],facecolor='red',color = 'red'))
    cnt+=1
    ptc_cnt+=1

#I/O pin placement for Random placement
cnt=(int(nodes[1][2])-int(nodes[2][2]))+1
for i in range(int(nodes[2][2])):
    x=pl[cnt+i][1]
    
    y=pl[cnt+i][2]
    
    patch_list[nodes[cnt+i+2][0]].append(int(x))
    patch_list[nodes[cnt+i+2][0]].append(int(x))
    patch_list[nodes[cnt+i+2][0]].append(int(y))
    patch_list[nodes[cnt+i+2][0]].append(int(y))
    testCircle = Circle((int(x),int (y) * 1), radius = 1 * 1, color = 'blue', lw = 2, fill = True, zorder=0,clip_on=False)
    ax.add_patch(testCircle)
    
    
TPWL=Total_Perimeter_Wire_length(patch_list,ax)




global overlaps_list

overlaps_list=collections.defaultdict(list)


notoverlaps=0
def overlaps(patc_list):
    
    overlaps=0
    cnt=3
    i=0
    j=0
    
    while(i<(int(nodes[1][2])-int(nodes[2][2]))):

        
        j=i+1
            
        while(j<(int(nodes[1][2])-int(nodes[2][2]))):
            
            if(patc_list[nodes[cnt+i][0]][0] >= patc_list[nodes[cnt+j][0]][1] or patc_list[nodes[cnt+j][0]][0] >= patc_list[nodes[cnt+i][0]][1]):
                j+=1
                
           
            elif(patc_list[nodes[cnt+i][0]][3] <= patc_list[nodes[cnt+j][0]][2] or patc_list[nodes[cnt+j][0]][3] <= patc_list[nodes[cnt+i][0]][2]):
                j+=1
          

            else:                
                overlaps_list[overlaps].append(i+1)
                overlaps_list[overlaps].append(j+1)
                overlaps=overlaps+1
                j+=1
            
                         
        i+=1

    return overlaps
            

overlaps1=overlaps(patch_list)


print("STATS")
print("Overlaps before legalization",overlaps1)
   

global nodes_list

nodes_list=collections.defaultdict(list)
i=0
cnt=0
while(i<len(nodes)-2):
    
    str1=nodes[cnt+3][0]
    nodes_list[str1]=cnt
    cnt+=1
    i+=1

pins=collections.defaultdict(list)
#I/0 Pins list

cnt=33
for i in range(8):
    pins[nodes[cnt][0]]=1
    cnt+=1




i=0
cnt=0
global node_weight
node_weight=collections.defaultdict(list)
#calculating how many edges each node has

while(i<len(nodes)-2):
    node_cnt=0
    string_node=nodes[cnt+3][0]
    
    
    for j in range (len(nets)):
        for k in range(len(nets[j])):
            if(string_node==nets[j][k]):
                node_cnt+=1
        
    node_weight[string_node]=node_cnt  
    cnt+=1
    i+=1

#Adjacency_Matrix NxN

counter=0
N = 30
M = 8
Adjacency_Matrix = numpy.zeros(shape=(N,N))
cnt=8
for i in range(len(nets)-8):
    for j in range(len(nets[cnt])-1):
        for k in range(len(nets[cnt])-j-1):
            Adjacency_Matrix[int(nodes_list[nets[cnt][j]])][int(nodes_list[nets[cnt][k+1]])] = 2/((node_weight[nets[cnt][j]])) + 2/((node_weight[nets[cnt][k+1]]))
            
    
    cnt+=1



#Pin Connection Matrix M x N

Pin_Connection_Matrix = numpy.zeros(shape=(N,M))
cnt=0
for i in range(M):
    for j in range(len(nets[cnt])-1):
        for k in range(len(nets[cnt])-j-1):
            Pin_Connection_Matrix[int(nodes_list[nets[cnt][j]])][int(nodes_list[nets[cnt][k+1]])-30] = 2/((node_weight[nets[cnt][j]])) + 2/((node_weight[nets[cnt][k+1]]))
            
    cnt+=1        


#Degree Matrix N x N
Degree_Matrix= numpy.zeros(shape=(N,N))
Deg_Adj=0
Deg_Pin=0
for i in range(N):
    
    for j in range(N):
        Deg_Adj=Deg_Adj + Adjacency_Matrix[i][j]
    
    for k in range(M):
        Deg_Pin=Deg_Pin + Pin_Connection_Matrix[i][k]
    
    Degree_Matrix[i][i]=Deg_Adj+Deg_Pin


#Laplacian Matrix N x N

Laplacian_Matrix= numpy.zeros(shape=(N,N))

Laplacian_Matrix=Laplacian_Matrix-Adjacency_Matrix





i=0
j=0
cnt=0
ar='1'




#rows for legalization
global rows_leg
global rows_leg1
global rows_leg2_min
global rows_leg2_max
global rows_3rd_detailed
rows_leg=collections.defaultdict(list)
for i in scl:
    rows_leg[i].append(int(scl[i][0]))
    rows_leg[i].append(int(scl[i][1]))
    rows_leg[i].append(0)


rows_leg1=rows_leg.copy()
rows_TPWL=deepcopy(rows_leg)
rows_leg2_min=deepcopy(rows_leg)
rows_leg2_max=deepcopy(rows_leg)
rows_3rd_detailed=deepcopy(rows_leg)
rows_4th_detailed=deepcopy(rows_leg)


for i in range(len(rows_leg2_max)):
    rows_leg2_max[i][2]=x_max




fig_leg, ax_leg = plt.subplots()

plt.xlim(x_min,x_max)
plt.ylim(y_min,y_max)


ax_leg.yaxis.grid(True, which='major')
ax_leg.yaxis.grid(True, which='minor')
ax_leg.patches_leg=ax.patches.copy()




cnt=0
p=0


global patch_list_leg1
patch_list_leg1=collections.defaultdict(list)






#first legalization algo
for i in range(len(ax_leg.patches_leg)-8):
    j=0
    x_min1=ax_leg.patches_leg[j].get_path().vertices[1][0] #It will change
    x_max1=ax_leg.patches_leg[j].get_path().vertices[2][0]
    y_min1=ax_leg.patches_leg[j].get_path().vertices[0][1]
    y_max1=ax_leg.patches_leg[j].get_path().vertices[1][1]
    height1=ax_leg.patches_leg[j].get_path().vertices[1][1]-ax_leg.patches_leg[j].get_path().vertices[0][1]
    min1=ax_leg.patches_leg[j].get_path().vertices[1][0]#setting first patche's x_min as min
    
    for j in range(len(ax_leg.patches_leg)):
        
        x_min1=ax_leg.patches_leg[j].get_path().vertices[1][0] #It will change
        x_max1=ax_leg.patches_leg[j].get_path().vertices[2][0]
        y_min1=ax_leg.patches_leg[j].get_path().vertices[0][1]
        y_max1=ax_leg.patches_leg[j].get_path().vertices[1][1]
        height1=ax_leg.patches_leg[j].get_path().vertices[1][1]-ax_leg.patches_leg[j].get_path().vertices[0][1]
       
        # If another patch has a smaller x_min it becomes the patch to be placed
        if (x_min1 < min1):
            
            x_min1=ax_leg.patches_leg[j].get_path().vertices[1][0] #It will change
            x_max1=ax_leg.patches_leg[j].get_path().vertices[2][0]
            y_min1=ax_leg.patches_leg[j].get_path().vertices[0][1]
            y_max1=ax_leg.patches_leg[j].get_path().vertices[1][1]
            height1=ax_leg.patches_leg[j].get_path().vertices[1][1]-ax_leg.patches_leg[j].get_path().vertices[0][1]
            min1=ax_leg.patches_leg[j].get_path().vertices[1][0]
            break
        break
   
   
    

    ptc_cnt=3
    #find the selected patch and store its place for other functions
    for t in range(len(patch_list)-8):
        name=nodes[ptc_cnt][0]
        
        if(x_min1==patch_list[nodes[ptc_cnt][0]][0] and x_max1==patch_list[nodes[ptc_cnt][0]][1] and  y_min1==patch_list[nodes[ptc_cnt][0]][2] and  y_max1==patch_list[nodes[ptc_cnt][0]][3]):
            
            name=nodes[ptc_cnt][0]
            ptc_cnt+=1
            break
        else:
            ptc_cnt+=1





    #checking from first row
    k=0
    row_cnt=0
    x_min_leg=(rows_leg[k][2]-x_min1)**2
    x_max_leg=(rows_leg[k][2]-x_max1)**2
    y_min_leg=(rows_leg[k][0]-y_min1)**2
    y_max_leg=(((rows_leg[k][0])+height1)-y_max1)**2
    sum_leg=x_min_leg+x_max_leg+y_min_leg+y_max_leg
    sqrt_leg1=math.sqrt(sum_leg)
    
    #get the nearest row for selected cell based on euclidean distance
    for k in range(len(rows_leg)):
        x_min_leg=(rows_leg1[k][2]-x_min1)**2
        x_max_leg=(rows_leg1[k][2]- x_max1 )**2
        y_min_leg=(rows_leg1[k][0]-y_min1)**2
        y_max_leg=(((rows_leg1[k][0])+height1)-y_max1)**2
        sum_leg=x_min_leg+x_max_leg+y_min_leg+y_max_leg
        sqrt_leg=math.sqrt(sum_leg)
        
        if(sqrt_leg<sqrt_leg1):
            row_cnt=k
            sqrt_leg1=sqrt_leg
    
    
    
    
    

    x_place=x_max1-x_min1
    y_place=y_max1-y_min1
    x = [rows_leg1[row_cnt][2] , rows_leg1[row_cnt][2] , rows_leg1[row_cnt][2] + x_place , rows_leg1[row_cnt][2] + x_place]
    y = [rows_leg1[row_cnt][0] ,rows_leg1[row_cnt][0] +y_place , rows_leg1[row_cnt][0]+y_place,rows_leg1[row_cnt][0]]
    patch_list_leg1[name].append(int(rows_leg1[row_cnt][2]))
    patch_list_leg1[name].append(int(rows_leg1[row_cnt][2]) + int(x_place))
    patch_list_leg1[name].append(int(rows_leg1[row_cnt][0]))
    patch_list_leg1[name].append(int(rows_leg1[row_cnt][0]) + int(y_place))
    ax_leg.add_patch(patches.Polygon(xy=list(zip(x,y)), fill=False,label='Label',facecolor='red',color='red'))
 

    centerx =mean(x)
    centery =mean(y)
    
    plt.text(centerx, centery,name)
    cnt+=1
    rows_leg[row_cnt][2]=rows_leg[row_cnt][2] + x_place
    del ax_leg.patches_leg[j]

#I/O pins for 1st legalization   
cnt=(int(nodes[1][2])-int(nodes[2][2]))+1
for i in range(int(nodes[2][2])):
    x=pl[cnt+i][1]
    
    y=pl[cnt+i][2]
    patch_list_leg1[nodes[cnt+i+2][0]].append(x)
    patch_list_leg1[nodes[cnt+i+2][0]].append(x)
    patch_list_leg1[nodes[cnt+i+2][0]].append(y)
    patch_list_leg1[nodes[cnt+i+2][0]].append(y)
    testCircle = Circle((int(x),int (y) * 1), radius = 1 * 1, color = 'blue', lw = 2, fill = True, zorder=0,clip_on=False)
    ax_leg.add_patch(testCircle)
   

twpl_after_leg_1=Total_Perimeter_Wire_length(patch_list_leg1,ax)
overlaps_after1=overlaps(patch_list_leg1)
print("Overlaps after 1st legalization :",overlaps_after1)
print("TWPL after 1st legalization legalization is :",twpl_after_leg_1)





fig_TWPL, ax_TWPL = plt.subplots()
ax_TWPL.yaxis.grid(True, which='major')
ax_TWPL.yaxis.grid(True, which='minor')
plt.xlim(x_min,x_max)
plt.ylim(y_min,y_max)



#TPWL Legalization
TPWL_list=[]
global patch_list_TWPL_leg
patch_list_TWPL_leg=collections.defaultdict(list)
ax_TWPL.patches_leg=ax.patches.copy()
global ax_TWPL_list
ax_TWPL_list=collections.defaultdict(list)

for i in range(30):
    cnt_TWPL=[]
    x_min_TPWL=[]
    x_max_TPWL=[]
    y_min_TPWL=[]
    y_max_TPWL=[]
    j=0
    
    min1=ax_TWPL.patches_leg[j].get_path().vertices[1][0]#setting first patche's x_min as min
    
    for j in range(len(ax_TWPL.patches_leg)):
        
        x_min1=ax_TWPL.patches_leg[j].get_path().vertices[1][0] #It will change
        x_max1=ax_TWPL.patches_leg[j].get_path().vertices[2][0]
        y_min1=ax_TWPL.patches_leg[j].get_path().vertices[0][1]
        y_max1=ax_TWPL.patches_leg[j].get_path().vertices[1][1]
        height1=ax_TWPL.patches_leg[j].get_path().vertices[1][1]-ax_TWPL.patches_leg[j].get_path().vertices[0][1]
       
        # If another patch has a smaller x_min it becomes the patch to be placed
        if (x_min1 < min1):
            
            x_min1=ax_TWPL.patches_leg[j].get_path().vertices[1][0] #It will change
            x_max1=ax_TWPL.patches_leg[j].get_path().vertices[2][0]
            y_min1=ax_TWPL.patches_leg[j].get_path().vertices[0][1]
            y_max1=ax_TWPL.patches_leg[j].get_path().vertices[1][1]
            height1=ax_TWPL.patches_leg[j].get_path().vertices[1][1]-ax_TWPL.patches_leg[j].get_path().vertices[0][1]
            min1=ax_TWPL.patches_leg[j].get_path().vertices[1][0]
            del_index=j
            break
        break
    #text for cells in legalized plot
  

    ptc_cnt=3
    #find the selected patch and store its place for other functions
    for t in range((int(nodes[1][2])-int(nodes[2][2]))):
        name=nodes[ptc_cnt][0]
        
        if(x_min1==patch_list[nodes[ptc_cnt][0]][0] and x_max1==patch_list[nodes[ptc_cnt][0]][1] and  y_min1==patch_list[nodes[ptc_cnt][0]][2] and  y_max1==patch_list[nodes[ptc_cnt][0]][3]):
            
            name=nodes[ptc_cnt][0]
            
            break
        else:
            ptc_cnt+=1
    
    for k in range(len(rows_TPWL)):
        total_perimeter_wire_lenght=0
        
        
        for m in range(len(nets)):
            
            if name in  nets[m]:
                for n in range(len(nets[m])):
                    index=nets[m][n]
                    if(index != name):
                        x_min_TPWL.append(int((patch_list[index][0])))
                        x_max_TPWL.append(int((patch_list[index][1])))
                        y_min_TPWL.append(int((patch_list[index][2])))
                        y_max_TPWL.append(int((patch_list[index][3])))
                    else:
                        x_place=x_max1-x_min1
                        y_place=y_max1-y_min1
                        
                        x_min_TPWL.append(int(rows_TPWL[k][2]))
                        x_max_TPWL.append(int(rows_TPWL[k][2]) + int(x_place))
                        y_min_TPWL.append(int(rows_TPWL[k][0]))
                        y_max_TPWL.append(int(rows_TPWL[k][0]) + int(y_place))

               
                xminTPWL=min(x_min_TPWL)
                xmaxTPWL=max(x_max_TPWL)
                yminTPWL=min(y_min_TPWL)
                ymaxTPWL=max(y_max_TPWL)    
                HPWL=(xmaxTPWL-xminTPWL)+(ymaxTPWL-yminTPWL)
                total_perimeter_wire_lenght+= HPWL
                x_min_TPWL.clear()
                x_max_TPWL.clear()
                y_min_TPWL.clear()
                y_max_TPWL.clear()

        cnt_TWPL.append(total_perimeter_wire_lenght)
        total_perimeter_wire_lenght=0
        
    
    minpos = cnt_TWPL.index(min(cnt_TWPL))     
          
       
    cnt_TWPL.clear()
 

    x_place=x_max1-x_min1
    y_place=y_max1-y_min1
    x = [rows_TPWL[minpos][2] , rows_TPWL[minpos][2] , rows_TPWL[minpos][2] + x_place , rows_TPWL[minpos][2] + x_place]
    y = [rows_TPWL[minpos][0] ,rows_TPWL[minpos][0] +y_place , rows_TPWL[minpos][0]+y_place,rows_TPWL[minpos][0]]
    patch_list_TWPL_leg[name].append(int(rows_TPWL[minpos][2]))
    patch_list_TWPL_leg[name].append(int(rows_TPWL[minpos][2]) + int(x_place))
    patch_list_TWPL_leg[name].append(int(rows_TPWL[minpos][0]))
    patch_list_TWPL_leg[name].append(int(rows_TPWL[minpos][0]) + int(y_place))
    ax_TWPL.add_patch(patches.Polygon(xy=list(zip(x,y)), fill=False,label='Label',facecolor='red',color='red'))
 

    centerx =mean(x)
    centery =mean(y)
    
    plt.text(centerx, centery,name)
    cnt+=1
    rows_TPWL[minpos][2]=rows_TPWL[minpos][2] + x_place
    del ax_TWPL.patches_leg[j]

#I/O pins for TWPL legalization   
cnt=(int(nodes[1][2])-int(nodes[2][2]))+1
for i in range(int(nodes[2][2])):
    x=pl[cnt+i][1]
    
    y=pl[cnt+i][2]
    patch_list_TWPL_leg[nodes[cnt+i+2][0]].append(x)
    patch_list_TWPL_leg[nodes[cnt+i+2][0]].append(x)
    patch_list_TWPL_leg[nodes[cnt+i+2][0]].append(y)
    patch_list_TWPL_leg[nodes[cnt+i+2][0]].append(y)
    testCircle = Circle((int(x),int (y) * 1), radius = 1 * 1, color = 'blue', lw = 2, fill = True, zorder=0,clip_on=False)
    ax_TWPL.add_patch(testCircle)


 




TWPL_length=Total_Perimeter_Wire_length(patch_list_TWPL_leg,ax_TWPL)
overlaps_leg1=overlaps(patch_list_TWPL_leg)
print('Overlaps after TWPL legalization:',overlaps_leg1)
print("TWPL after TWPL legalization is : ",TWPL_length)


fig_leg2, ax_leg2 = plt.subplots()

plt.xlim(x_min,x_max)
plt.ylim(y_min,y_max)


ax_leg2.yaxis.grid(True, which='major')
ax_leg2.yaxis.grid(True, which='minor')
ax_leg2.patches_leg=ax.patches.copy()

p=0


#Second legalization algorithm


for i in range((len(ax_leg2.patches_leg))//2):
    
    #Left legalizatiion
    j=0
    x_min1=ax_leg2.patches_leg[j].get_path().vertices[1][0] #It will change
    x_max1=ax_leg2.patches_leg[j].get_path().vertices[2][0]
    y_min1=ax_leg2.patches_leg[j].get_path().vertices[0][1]
    y_max1=ax_leg2.patches_leg[j].get_path().vertices[1][1]
    height1=ax_leg2.patches_leg[j].get_path().vertices[1][1]-ax_leg2.patches_leg[j].get_path().vertices[0][1]
    min1=ax_leg2.patches_leg[j].get_path().vertices[1][0]#setting first patche's x_min as min
    
    for j in range(len(ax_leg2.patches_leg)):
        
        x_min1=ax_leg2.patches_leg[j].get_path().vertices[1][0] #It will change
        x_max1=ax_leg2.patches_leg[j].get_path().vertices[2][0]
        y_min1=ax_leg2.patches_leg[j].get_path().vertices[0][1]
        y_max1=ax_leg2.patches_leg[j].get_path().vertices[1][1]
        height1=ax_leg2.patches_leg[j].get_path().vertices[1][1]-ax_leg2.patches_leg[j].get_path().vertices[0][1]
        
        # If another patch has a smaller x_min it becomes the patch to be placed
        if (x_min1 < min1):
            
            x_min1=ax_leg2.patches_leg[j].get_path().vertices[1][0] #It will change
            x_max1=ax_leg2.patches_leg[j].get_path().vertices[2][0]
            y_min1=ax_leg2.patches_leg[j].get_path().vertices[0][1]
            y_max1=ax_leg2.patches_leg[j].get_path().vertices[1][1]
            height1=ax_leg2.patches_leg[j].get_path().vertices[1][1]-ax_leg2.patches_leg[j].get_path().vertices[0][1]
            min1=ax_leg2.patches_leg[j].get_path().vertices[1][0]
            break
        break  
    
    
    
    ptc_cnt=3
    for t in range(len(patch_list)-8):
        name=nodes[ptc_cnt][0]
        
        if(x_min1==patch_list[nodes[ptc_cnt][0]][0] and x_max1==patch_list[nodes[ptc_cnt][0]][1] and  y_min1==patch_list[nodes[ptc_cnt][0]][2] and  y_max1==patch_list[nodes[ptc_cnt][0]][3]):
            
            name=nodes[ptc_cnt][0]
            ptc_cnt+=1
            break
        else:
            ptc_cnt+=1   


    for k in range(len(rows_leg2_min)):
        if(rows_leg2_min[k][2]+(x_max1-x_min1)>rows_leg2_max[k][2]):
            rows_leg2_min[k][2]=100000
    #checking from first row
    k=0
    row_cnt=0
    x_min_leg=(rows_leg2_min[k][2]-x_min1)**2
    x_max_leg=(rows_leg2_min[k][2]- x_max1 )**2
    y_min_leg=(rows_leg2_min[k][0]-y_min1)**2
    y_max_leg=((rows_leg2_min[k][0])-y_max1)**2
    sum_leg=x_min_leg+x_max_leg+y_min_leg+y_max_leg
    sqrt_leg1=math.sqrt(sum_leg)
    
    #get the nearest row for selected cell based on euclidean distance
    for k in range(len(rows_leg2_min)):
        x_min_leg=(rows_leg2_min[k][2]-x_min1)**2
        x_max_leg=(rows_leg2_min[k][2]- x_max1 )**2
        y_min_leg=(rows_leg2_min[k][0]-y_min1)**2
        y_max_leg=((rows_leg2_min[k][0])-y_max1)**2
        sum_leg=x_min_leg+x_max_leg+y_min_leg+y_max_leg
        sqrt_leg=math.sqrt(sum_leg)
        
        if(sqrt_leg<sqrt_leg1):
            row_cnt=k
            sqrt_leg1=sqrt_leg
            
    x_place=x_max1-x_min1
    y_place=y_max1-y_min1
    x = [rows_leg2_min[row_cnt][2] , rows_leg2_min[row_cnt][2] , rows_leg2_min[row_cnt][2] + x_place , rows_leg2_min[row_cnt][2] + x_place]
    y = [rows_leg2_min[row_cnt][0] ,rows_leg2_min[row_cnt][0] +y_place , rows_leg2_min[row_cnt][0]+y_place,rows_leg2_min[row_cnt][0]]
    ax_leg2.add_patch(patches.Polygon(xy=list(zip(x,y)), fill=False,label='Label',facecolor='red',color='red'))
    p+=1

    centerx =mean(x)
    centery =mean(y)
    
    plt.text(centerx, centery,name)
    
    cnt+=1
    rows_leg2_min[row_cnt][2]=rows_leg2_min[row_cnt][2] + x_place
    del ax_leg2.patches_leg[j]

    
    #Right legalizatiion
    
    j=0
    x_min1=ax_leg2.patches_leg[j].get_path().vertices[1][0] #It will change
    x_max1=ax_leg2.patches_leg[j].get_path().vertices[2][0]
    y_min1=ax_leg2.patches_leg[j].get_path().vertices[0][1]
    y_max1=ax_leg2.patches_leg[j].get_path().vertices[1][1]
    height1=ax_leg2.patches_leg[j].get_path().vertices[1][1]-ax_leg2.patches_leg[j].get_path().vertices[0][1]
    max1=ax_leg2.patches_leg[j].get_path().vertices[2][0]#setting first patche's x_min as min
    
    for j in range(len(ax_leg2.patches_leg)):
        
        x_min1=ax_leg2.patches_leg[j].get_path().vertices[1][0] #It will change
        x_max1=ax_leg2.patches_leg[j].get_path().vertices[2][0]
        y_min1=ax_leg2.patches_leg[j].get_path().vertices[0][1]
        y_max1=ax_leg2.patches_leg[j].get_path().vertices[1][1]
        height1=ax_leg2.patches_leg[j].get_path().vertices[1][1]-ax_leg2.patches_leg[j].get_path().vertices[0][1]
        max1=x_max1
        # If another patch has a smaller x_min it becomes the patch to be placed
        if (x_max1 > max1):
            
            x_min1=ax_leg2.patches_leg[j].get_path().vertices[1][0] #It will change
            x_max1=ax_leg2.patches_leg[j].get_path().vertices[2][0]
            y_min1=ax_leg2.patches_leg[j].get_path().vertices[0][1]
            y_max1=ax_leg2.patches_leg[j].get_path().vertices[1][1]
            height1=ax_leg2.patches_leg[j].get_path().vertices[1][1]-ax_leg2.patches_leg[j].get_path().vertices[0][1]
            max1=ax_leg2.patches_leg[j].get_path().vertices[2][0]
            break
        break
    
    
 
    ptc_cnt=3
    for t in range(len(patch_list)-8):
        name=nodes[ptc_cnt][0]
        
        if(x_min1==patch_list[nodes[ptc_cnt][0]][0] and x_max1==patch_list[nodes[ptc_cnt][0]][1] and  y_min1==patch_list[nodes[ptc_cnt][0]][2] and  y_max1==patch_list[nodes[ptc_cnt][0]][3]):
            
            name=nodes[ptc_cnt][0]
            ptc_cnt+=1
            break
        else:
            ptc_cnt+=1     

    for k in range(len(rows_leg2_min)):
        if(rows_leg2_max[k][2]-(x_max1-x_min1)<rows_leg2_min[k][2]):
            rows_leg2_max[k][2]=100000
    #checking from first row
    k=0
    row_cnt=0
    x_min_leg=(rows_leg2_max[k][2]-x_min1)**2
    x_max_leg=(rows_leg2_max[k][2]- x_max1 )**2
    y_min_leg=(rows_leg2_max[k][0]-y_min1)**2
    y_max_leg=((rows_leg2_max[k][0])-y_max1)**2
    sum_leg=x_min_leg+x_max_leg+y_min_leg+y_max_leg
    sqrt_leg1=math.sqrt(sum_leg)
    
    #get the nearest row for selected cell based on euclidean distance
    for k in range(len(rows_leg2_max)):
        x_min_leg=(rows_leg2_max[k][2]-x_min1)**2
        x_max_leg=(rows_leg2_max[k][2]- x_max1 )**2
        y_min_leg=(rows_leg2_max[k][0]-y_min1)**2
        y_max_leg=((rows_leg2_max[k][0])-y_max1)**2
        sum_leg=x_min_leg+x_max_leg+y_min_leg+y_max_leg
        sqrt_leg=math.sqrt(sum_leg)
        
        if(sqrt_leg<sqrt_leg1):
            row_cnt=k
            sqrt_leg1=sqrt_leg
            
    x_place=x_max1-x_min1
    y_place=y_max1-y_min1
    x = [rows_leg2_max[row_cnt][2]-x_place , rows_leg2_max[row_cnt][2]-x_place , rows_leg2_max[row_cnt][2]  , rows_leg2_max[row_cnt][2] ]
    y = [rows_leg2_max[row_cnt][0] ,rows_leg2_max[row_cnt][0] +y_place , rows_leg2_max[row_cnt][0]+y_place,rows_leg2_max[row_cnt][0]]
    ax_leg2.add_patch(patches.Polygon(xy=list(zip(x,y)), fill=False,label='Label',facecolor='red'))
    

    centerx =mean(x)
    centery =mean(y)
    
    plt.text(centerx, centery,name)
    
    cnt+=1
    rows_leg2_max[row_cnt][2]=rows_leg2_max[row_cnt][2] - x_place
    del ax_leg2.patches_leg[j]
    

#I/O pins for 2nd legalization
cnt=(int(nodes[1][2])-int(nodes[2][2]))+1
for i in range(int(nodes[2][2])):
    x=pl[cnt+i][1]
   
    y=pl[cnt+i][2]
   
    testCircle = Circle((int(x),int (y) * 1), radius = 1 * 1, color = 'blue', lw = 2, fill = True, zorder=0,clip_on=False)
    ax_leg2.add_patch(testCircle)





#2nd_legalization_tpwl=Total_Perimeter_Wire_length(patch_list_TWPL_leg,ax)



fig.canvas.set_window_title('Random placement')
fig_leg.canvas.set_window_title('First legalization')
fig_leg2.canvas.set_window_title('Second Legalization')
fig_TWPL.canvas.set_window_title('TWPL Legalization')




patch_list_leg1_after1=deepcopy(patch_list_leg1)
patch_list_leg1_after2=deepcopy(patch_list_leg1)






snd=Total_Perimeter_Wire_length(patch_list_leg1_after1,ax)
print("Size before the first detailed legalization: ",snd)



trigger=1
#1st detailed placement algorithm
while(trigger==1):
    ptc_cnt=3
    trigger=0
    for i in range(len(patch_list_leg1_after1)-8):
        
        size=patch_list_leg1_after1[nodes[ptc_cnt+i][0]][1]-patch_list_leg1_after1[nodes[ptc_cnt+i][0]][0]
        for j in range(len(patch_list_leg1_after1)-8):
            if not(patch_list_leg1_after1[nodes[ptc_cnt+i][0]][0]==patch_list_leg1_after1[nodes[ptc_cnt+j][0]][0]and patch_list_leg1_after1[nodes[ptc_cnt+i][0]][1]==patch_list_leg1_after1[nodes[ptc_cnt+j][0]][1]and patch_list_leg1_after1[nodes[ptc_cnt+i][0]][2]==patch_list_leg1_after1[nodes[ptc_cnt+j][0]][2] and patch_list_leg1_after1[nodes[ptc_cnt+i][0]][3] == patch_list_leg1_after1[nodes[ptc_cnt+j][0]][3]):
                size_tst=patch_list_leg1_after1[nodes[ptc_cnt+j][0]][1]-patch_list_leg1_after1[nodes[ptc_cnt+j][0]][0]
                if(size==size_tst):
                    temp_0=patch_list_leg1_after1[nodes[ptc_cnt+i][0]][0]
                    temp_1=patch_list_leg1_after1[nodes[ptc_cnt+i][0]][1]
                    temp_2=patch_list_leg1_after1[nodes[ptc_cnt+i][0]][2]
                    temp_3=patch_list_leg1_after1[nodes[ptc_cnt+i][0]][3]

                    patch_list_leg1_after1[nodes[ptc_cnt+i][0]][0]=patch_list_leg1_after1[nodes[ptc_cnt+j][0]][0]
                    patch_list_leg1_after1[nodes[ptc_cnt+i][0]][1]=patch_list_leg1_after1[nodes[ptc_cnt+j][0]][1]
                    patch_list_leg1_after1[nodes[ptc_cnt+i][0]][2]=patch_list_leg1_after1[nodes[ptc_cnt+j][0]][2]
                    patch_list_leg1_after1[nodes[ptc_cnt+i][0]][3]=patch_list_leg1_after1[nodes[ptc_cnt+j][0]][3]

                    patch_list_leg1_after1[nodes[ptc_cnt+j][0]][0]=temp_0
                    patch_list_leg1_after1[nodes[ptc_cnt+j][0]][1]=temp_1
                    patch_list_leg1_after1[nodes[ptc_cnt+j][0]][2]=temp_2
                    patch_list_leg1_after1[nodes[ptc_cnt+j][0]][3]=temp_3
                    if(Total_Perimeter_Wire_length(patch_list_leg1_after1,ax)<snd):
                        snd=Total_Perimeter_Wire_length(patch_list_leg1_after1,ax)
                        trigger=1
                        break
                    else:
                        temp_0=patch_list_leg1_after1[nodes[ptc_cnt+j][0]][0]
                        temp_1=patch_list_leg1_after1[nodes[ptc_cnt+j][0]][1]
                        temp_2=patch_list_leg1_after1[nodes[ptc_cnt+j][0]][2]
                        temp_3=patch_list_leg1_after1[nodes[ptc_cnt+j][0]][3]

                        patch_list_leg1_after1[nodes[ptc_cnt+j][0]][0]=patch_list_leg1_after1[nodes[ptc_cnt+i][0]][0]
                        patch_list_leg1_after1[nodes[ptc_cnt+j][0]][1]=patch_list_leg1_after1[nodes[ptc_cnt+i][0]][1]
                        patch_list_leg1_after1[nodes[ptc_cnt+j][0]][2]=patch_list_leg1_after1[nodes[ptc_cnt+i][0]][2]
                        patch_list_leg1_after1[nodes[ptc_cnt+j][0]][3]=patch_list_leg1_after1[nodes[ptc_cnt+i][0]][3]

                        patch_list_leg1_after1[nodes[ptc_cnt+i][0]][0]=temp_0
                        patch_list_leg1_after1[nodes[ptc_cnt+i][0]][1]=temp_1
                        patch_list_leg1_after1[nodes[ptc_cnt+i][0]][2]=temp_2
                        patch_list_leg1_after1[nodes[ptc_cnt+i][0]][3]=temp_3


ovr_after_det1=overlaps(patch_list_leg1_after1)
snd1=Total_Perimeter_Wire_length(patch_list_leg1_after1,ax)
print("Overlaps after 1st detailed placement: ",ovr_after_det1)
print("Size after the first detailed placement: ",snd1)

snd=Total_Perimeter_Wire_length(patch_list_leg1,ax)


swap_list=[]
trigger=1
#2nd detailed placement algorithm
while(trigger==1):
    
    trigger=0
    for i in range(len(patch_list_leg1_after2)-8):
        swap_list.clear()
        ptc_cnt=3
        size=patch_list_leg1_after2[nodes[ptc_cnt+i][0]][1]-patch_list_leg1_after2[nodes[ptc_cnt+i][0]][0]
        for j in range(len(patch_list_leg1_after2)-8):
            if not(patch_list_leg1_after2[nodes[ptc_cnt+i][0]][0]==patch_list_leg1_after2[nodes[ptc_cnt+j][0]][0]and patch_list_leg1_after2[nodes[ptc_cnt+i][0]][1]==patch_list_leg1_after2[nodes[ptc_cnt+j][0]][1]and patch_list_leg1_after2[nodes[ptc_cnt+i][0]][2]==patch_list_leg1_after2[nodes[ptc_cnt+j][0]][2] and patch_list_leg1_after2[nodes[ptc_cnt+i][0]][3] == patch_list_leg1_after2[nodes[ptc_cnt+j][0]][3]):
                size_tst=patch_list_leg1_after2[nodes[ptc_cnt+j][0]][1]-patch_list_leg1_after2[nodes[ptc_cnt+j][0]][0]
                if(size==size_tst):
                    temp_0=patch_list_leg1_after2[nodes[ptc_cnt+j][0]][0]
                    temp_1=patch_list_leg1_after2[nodes[ptc_cnt+j][0]][1]
                    temp_2=patch_list_leg1_after2[nodes[ptc_cnt+j][0]][2]
                    temp_3=patch_list_leg1_after2[nodes[ptc_cnt+j][0]][3]

                    patch_list_leg1_after2[nodes[ptc_cnt+j][0]][0]=patch_list_leg1_after2[nodes[ptc_cnt+i][0]][0]
                    patch_list_leg1_after2[nodes[ptc_cnt+j][0]][1]=patch_list_leg1_after2[nodes[ptc_cnt+i][0]][1]
                    patch_list_leg1_after2[nodes[ptc_cnt+j][0]][2]=patch_list_leg1_after2[nodes[ptc_cnt+i][0]][2]
                    patch_list_leg1_after2[nodes[ptc_cnt+j][0]][3]=patch_list_leg1_after2[nodes[ptc_cnt+i][0]][3]

                    patch_list_leg1_after2[nodes[ptc_cnt+i][0]][0]=temp_0
                    patch_list_leg1_after2[nodes[ptc_cnt+i][0]][1]=temp_1
                    patch_list_leg1_after2[nodes[ptc_cnt+i][0]][2]=temp_2
                    patch_list_leg1_after2[nodes[ptc_cnt+i][0]][3]=temp_3
                    if(Total_Perimeter_Wire_length(patch_list_leg1_after2,ax)<snd):
                        swap_list.append(tuple((ptc_cnt+j, Total_Perimeter_Wire_length(patch_list_leg1_after2,ax))))
                        
                        
                        trigger=1
                        temp_0=patch_list_leg1_after2[nodes[ptc_cnt+i][0]][0]
                        temp_1=patch_list_leg1_after2[nodes[ptc_cnt+i][0]][1]
                        temp_2=patch_list_leg1_after2[nodes[ptc_cnt+i][0]][2]
                        temp_3=patch_list_leg1_after2[nodes[ptc_cnt+i][0]][3]

                        patch_list_leg1_after2[nodes[ptc_cnt+i][0]][0]=patch_list_leg1_after2[nodes[ptc_cnt+j][0]][0]
                        patch_list_leg1_after2[nodes[ptc_cnt+i][0]][1]=patch_list_leg1_after2[nodes[ptc_cnt+j][0]][1]
                        patch_list_leg1_after2[nodes[ptc_cnt+i][0]][2]=patch_list_leg1_after2[nodes[ptc_cnt+j][0]][2]
                        patch_list_leg1_after2[nodes[ptc_cnt+i][0]][3]=patch_list_leg1_after2[nodes[ptc_cnt+j][0]][3]

                        patch_list_leg1_after2[nodes[ptc_cnt+j][0]][0]=temp_0
                        patch_list_leg1_after2[nodes[ptc_cnt+j][0]][1]=temp_1
                        patch_list_leg1_after2[nodes[ptc_cnt+j][0]][2]=temp_2
                        patch_list_leg1_after2[nodes[ptc_cnt+j][0]][3]=temp_3
                        
                    else:
                        temp_0=patch_list_leg1_after2[nodes[ptc_cnt+i][0]][0]
                        temp_1=patch_list_leg1_after2[nodes[ptc_cnt+i][0]][1]
                        temp_2=patch_list_leg1_after2[nodes[ptc_cnt+i][0]][2]
                        temp_3=patch_list_leg1_after2[nodes[ptc_cnt+i][0]][3]

                        patch_list_leg1_after2[nodes[ptc_cnt+j][0]][0]=patch_list_leg1_after2[nodes[ptc_cnt+i][0]][0]
                        patch_list_leg1_after2[nodes[ptc_cnt+j][0]][1]=patch_list_leg1_after2[nodes[ptc_cnt+i][0]][1]
                        patch_list_leg1_after2[nodes[ptc_cnt+j][0]][2]=patch_list_leg1_after2[nodes[ptc_cnt+i][0]][2]
                        patch_list_leg1_after2[nodes[ptc_cnt+j][0]][3]=patch_list_leg1_after2[nodes[ptc_cnt+i][0]][3]

                        patch_list_leg1_after2[nodes[ptc_cnt+i][0]][0]=temp_0
                        patch_list_leg1_after2[nodes[ptc_cnt+i][0]][1]=temp_1
                        patch_list_leg1_after2[nodes[ptc_cnt+i][0]][2]=temp_2
                        patch_list_leg1_after2[nodes[ptc_cnt+i][0]][3]=temp_3
        if Enquiry(swap_list):
            swap_list.sort(key=lambda x:x[1])
            
            index_sort=swap_list[0][0]
            temp_0=patch_list_leg1_after2[nodes[index_sort][0]][0]
            temp_1=patch_list_leg1_after2[nodes[index_sort][0]][1]
            temp_2=patch_list_leg1_after2[nodes[index_sort][0]][2]
            temp_3=patch_list_leg1_after2[nodes[index_sort][0]][3]

            patch_list_leg1_after2[nodes[index_sort][0]][0]=patch_list_leg1_after2[nodes[ptc_cnt+i][0]][0]
            patch_list_leg1_after2[nodes[index_sort][0]][1]=patch_list_leg1_after2[nodes[ptc_cnt+i][0]][1]
            patch_list_leg1_after2[nodes[index_sort][0]][2]=patch_list_leg1_after2[nodes[ptc_cnt+i][0]][2]
            patch_list_leg1_after2[nodes[index_sort][0]][3]=patch_list_leg1_after2[nodes[ptc_cnt+i][0]][3]

            patch_list_leg1_after2[nodes[ptc_cnt+i][0]][0]=temp_0
            patch_list_leg1_after2[nodes[ptc_cnt+i][0]][1]=temp_1
            patch_list_leg1_after2[nodes[ptc_cnt+i][0]][2]=temp_2
            patch_list_leg1_after2[nodes[ptc_cnt+i][0]][3]=temp_3
            snd=Total_Perimeter_Wire_length(patch_list_leg1_after2,ax)               
        
        

 
ovr_after_det2=overlaps(patch_list_leg1_after2)

print("Overlaps after 2nd detailed placement: ",ovr_after_det2)


snd=Total_Perimeter_Wire_length(patch_list_leg1_after2,ax)

print("Size after the second detailed placement: ",snd)

##3rd detailed placement algorithm

patch_list_leg1_after3=deepcopy(patch_list_leg1)
patch_list_leg1_after3_leg=deepcopy(patch_list_leg1)




trigger=1

while(trigger==1):
    ptc_cnt=3
    
    for i in range(len(patch_list_leg1_after3)-8):
        trigger=0
        
        size=patch_list_leg1_after3[nodes[ptc_cnt+i][0]][1]-patch_list_leg1_after3[nodes[ptc_cnt+i][0]][0]
        for j in range(len(patch_list_leg1_after3)-8):
            if not(patch_list_leg1_after3[nodes[ptc_cnt+i][0]][0]==patch_list_leg1_after3[nodes[ptc_cnt+j][0]][0]and patch_list_leg1_after3[nodes[ptc_cnt+i][0]][1]==patch_list_leg1_after3[nodes[ptc_cnt+j][0]][1]and patch_list_leg1_after3[nodes[ptc_cnt+i][0]][2]==patch_list_leg1_after3[nodes[ptc_cnt+j][0]][2] and patch_list_leg1_after3[nodes[ptc_cnt+i][0]][3] == patch_list_leg1_after3[nodes[ptc_cnt+j][0]][3]):
                
                temp_0=patch_list_leg1_after3[nodes[ptc_cnt+i][0]][0]
                temp_1=patch_list_leg1_after3[nodes[ptc_cnt+i][0]][1]
                temp_2=patch_list_leg1_after3[nodes[ptc_cnt+i][0]][2]
                temp_3=patch_list_leg1_after3[nodes[ptc_cnt+i][0]][3]

                patch_list_leg1_after3[nodes[ptc_cnt+i][0]][0]=patch_list_leg1_after3[nodes[ptc_cnt+j][0]][0]
                patch_list_leg1_after3[nodes[ptc_cnt+i][0]][1]=patch_list_leg1_after3[nodes[ptc_cnt+j][0]][1]
                patch_list_leg1_after3[nodes[ptc_cnt+i][0]][2]=patch_list_leg1_after3[nodes[ptc_cnt+j][0]][2]
                patch_list_leg1_after3[nodes[ptc_cnt+i][0]][3]=patch_list_leg1_after3[nodes[ptc_cnt+j][0]][3]

                patch_list_leg1_after3[nodes[ptc_cnt+j][0]][0]=temp_0
                patch_list_leg1_after3[nodes[ptc_cnt+j][0]][1]=temp_1
                patch_list_leg1_after3[nodes[ptc_cnt+j][0]][2]=temp_2
                patch_list_leg1_after3[nodes[ptc_cnt+j][0]][3]=temp_3
                if(Total_Perimeter_Wire_length(patch_list_leg1_after3,ax)<snd):
                    snd=Total_Perimeter_Wire_length(patch_list_leg1_after3,ax)
                    trigger=1
                    
                else:
                    temp_0=patch_list_leg1_after3[nodes[ptc_cnt+j][0]][0]
                    temp_1=patch_list_leg1_after3[nodes[ptc_cnt+j][0]][1]
                    temp_2=patch_list_leg1_after3[nodes[ptc_cnt+j][0]][2]
                    temp_3=patch_list_leg1_after3[nodes[ptc_cnt+j][0]][3]

                    patch_list_leg1_after3[nodes[ptc_cnt+j][0]][0]=patch_list_leg1_after3[nodes[ptc_cnt+i][0]][0]
                    patch_list_leg1_after3[nodes[ptc_cnt+j][0]][1]=patch_list_leg1_after3[nodes[ptc_cnt+i][0]][1]
                    patch_list_leg1_after3[nodes[ptc_cnt+j][0]][2]=patch_list_leg1_after3[nodes[ptc_cnt+i][0]][2]
                    patch_list_leg1_after3[nodes[ptc_cnt+j][0]][3]=patch_list_leg1_after3[nodes[ptc_cnt+i][0]][3]

                    patch_list_leg1_after3[nodes[ptc_cnt+i][0]][0]=temp_0
                    patch_list_leg1_after3[nodes[ptc_cnt+i][0]][1]=temp_1
                    patch_list_leg1_after3[nodes[ptc_cnt+i][0]][2]=temp_2
                    patch_list_leg1_after3[nodes[ptc_cnt+i][0]][3]=temp_3
    patch_list_leg1_after3_leg=deepcopy(patch_list_leg1_after3)
    for l in range(len(patch_list_leg1_after3)-8):
        k=0
        x_min1=patch_list_leg1_after3_leg[nodes[ptc_cnt+k][0]][0]
        x_max1=patch_list_leg1_after3_leg[nodes[ptc_cnt+k][0]][1]
        y_min1=patch_list_leg1_after3_leg[nodes[ptc_cnt+k][0]][2]
        y_max1=patch_list_leg1_after3_leg[nodes[ptc_cnt+k][0]][3]
        height1=int(patch_list_leg1_after3_leg[nodes[ptc_cnt+k][0]][1])-int(patch_list_leg1_after3_leg[nodes[ptc_cnt+k][0]][0])
        min1=patch_list_leg1_after3_leg[nodes[ptc_cnt+k][0]][0]
    
        for k in range(len(patch_list_leg1_after3_leg)):
        
            x_min1=patch_list_leg1_after3_leg[nodes[ptc_cnt+k][0]][0]
            x_max1=patch_list_leg1_after3_leg[nodes[ptc_cnt+k][0]][1]
            y_min1=patch_list_leg1_after3_leg[nodes[ptc_cnt+k][0]][2]
            y_max1=patch_list_leg1_after3_leg[nodes[ptc_cnt+k][0]][3]
            height1=int(patch_list_leg1_after3_leg[nodes[ptc_cnt+k][0]][1])-int(patch_list_leg1_after3_leg[nodes[ptc_cnt+k][0]][0])
      
       
        # If another patch has a smaller x_min it becomes the patch to be placed
            if (x_min1 < min1):
                
                x_min1=patch_list_leg1_after3_leg[nodes[ptc_cnt+k][0]][0]
                x_max1=patch_list_leg1_after3_leg[nodes[ptc_cnt+k][0]][1]
                y_min1=patch_list_leg1_after3_leg[nodes[ptc_cnt+k][0]][2]
                y_max1=patch_list_leg1_after3_leg[nodes[ptc_cnt+k][0]][3]
                height1=int(patch_list_leg1_after3_leg[nodes[ptc_cnt+k][0]][1])-int(patch_list_leg1_after3_leg[nodes[ptc_cnt+k][0]][0])
                min1=patch_list_leg1_after3_leg[nodes[ptc_cnt+k][0]][0]
                break
            break
        ptc_cnt=3


        #find the selected patch and store its place for other functions
        for t in range(len(patch_list_leg1_after3)-8):
            name=nodes[ptc_cnt][0]
            
            if(x_min1==patch_list_leg1_after3[nodes[ptc_cnt][0]][0] and x_max1==patch_list_leg1_after3[nodes[ptc_cnt][0]][1] and  y_min1==patch_list_leg1_after3[nodes[ptc_cnt][0]][2] and  y_max1==patch_list_leg1_after3[nodes[ptc_cnt][0]][3]):
                
                name=nodes[ptc_cnt][0]
                ptc_cnt+=1
                break
            else:
                ptc_cnt+=1

        #checking from first row
        g=0
        row_cnt=0
        x_min_leg=(rows_3rd_detailed[g][2]-int(x_min1))**2
        x_max_leg=(rows_3rd_detailed[g][2]-int(x_max1))**2
        y_min_leg=(rows_3rd_detailed[g][0]-int(y_min1))**2
        y_max_leg=(((rows_3rd_detailed[g][0])+height1)-int(y_max1))**2
        sum_leg=x_min_leg+x_max_leg+y_min_leg+y_max_leg
        sqrt_leg1=math.sqrt(sum_leg)
        
        #get the nearest row for selected cell based on euclidean distance
        for g in range(len(rows_3rd_detailed)):
            x_min_leg=(rows_3rd_detailed[g][2]-int(x_min1))**2
            x_max_leg=(rows_3rd_detailed[g][2]-int(x_max1))**2
            y_min_leg=(rows_3rd_detailed[g][0]-int(y_min1))**2
            y_max_leg=(((rows_3rd_detailed[g][0])+height1)-int(y_max1))**2
            sum_leg=x_min_leg+x_max_leg+y_min_leg+y_max_leg
            sqrt_leg=math.sqrt(sum_leg)
            
            if(sqrt_leg<sqrt_leg1):
                row_cnt=g
                sqrt_leg1=sqrt_leg

        x_place=int(x_max1)-int(x_min1)
        y_place=int(y_max1)-int(y_min1)
        x = [rows_3rd_detailed[row_cnt][2] , rows_3rd_detailed[row_cnt][2] , rows_3rd_detailed[row_cnt][2] + x_place , rows_3rd_detailed[row_cnt][2] + x_place]
        y = [rows_3rd_detailed[row_cnt][0] ,rows_3rd_detailed[row_cnt][0] +y_place , rows_3rd_detailed[row_cnt][0]+y_place,rows_3rd_detailed[row_cnt][0]]
        patch_list_leg1_after3_leg[name].append(int(rows_3rd_detailed[row_cnt][2]))
        patch_list_leg1_after3_leg[name].append(int(rows_3rd_detailed[row_cnt][2]) + int(x_place))
        patch_list_leg1_after3_leg[name].append(int(rows_3rd_detailed[row_cnt][0]))
        patch_list_leg1_after3_leg[name].append(int(rows_3rd_detailed[row_cnt][0]) + int(y_place))
        
        rows_3rd_detailed[row_cnt][2]=rows_3rd_detailed[row_cnt][2] + x_place
        del patch_list_leg1_after3_leg[name]


ovr_after_det3=overlaps(patch_list_leg1_after3)

print("Overlaps after 3rd detailed placement: ",ovr_after_det3)
snd_after3=Total_Perimeter_Wire_length(patch_list_leg1_after3,ax)
print("Size after the third detailed placement: ",snd_after3)


##4th detailed placement algorithm


snd=Total_Perimeter_Wire_length(patch_list_leg1,ax)

patch_list_leg1_after4=deepcopy(patch_list_leg1)
patch_list_leg1_after4_leg=deepcopy(patch_list_leg1)

trigger=1
snd=Total_Perimeter_Wire_length(patch_list_leg1_after4,ax)


while(trigger==1):
    ptc_cnt=3
    
    for i in range(len(patch_list_leg1_after4)-8):
        swap_list.clear()
        
        trigger=0
        
        
        for j in range(len(patch_list_leg1_after4)-8):
            if not(patch_list_leg1_after4[nodes[ptc_cnt+i][0]][0]==patch_list_leg1_after4[nodes[ptc_cnt+j][0]][0]and patch_list_leg1_after4[nodes[ptc_cnt+i][0]][1]==patch_list_leg1_after4[nodes[ptc_cnt+j][0]][1]and patch_list_leg1_after4[nodes[ptc_cnt+i][0]][2]==patch_list_leg1_after4[nodes[ptc_cnt+j][0]][2] and patch_list_leg1_after4[nodes[ptc_cnt+i][0]][3] == patch_list_leg1_after4[nodes[ptc_cnt+j][0]][3]):
                
                temp_0=patch_list_leg1_after4[nodes[ptc_cnt+i][0]][0]
                temp_1=patch_list_leg1_after4[nodes[ptc_cnt+i][0]][1]
                temp_2=patch_list_leg1_after4[nodes[ptc_cnt+i][0]][2]
                temp_3=patch_list_leg1_after4[nodes[ptc_cnt+i][0]][3]

                patch_list_leg1_after4[nodes[ptc_cnt+i][0]][0]=patch_list_leg1_after4[nodes[ptc_cnt+j][0]][0]
                patch_list_leg1_after4[nodes[ptc_cnt+i][0]][1]=patch_list_leg1_after4[nodes[ptc_cnt+j][0]][1]
                patch_list_leg1_after4[nodes[ptc_cnt+i][0]][2]=patch_list_leg1_after4[nodes[ptc_cnt+j][0]][2]
                patch_list_leg1_after4[nodes[ptc_cnt+i][0]][3]=patch_list_leg1_after4[nodes[ptc_cnt+j][0]][3]

                patch_list_leg1_after4[nodes[ptc_cnt+j][0]][0]=temp_0
                patch_list_leg1_after4[nodes[ptc_cnt+j][0]][1]=temp_1
                patch_list_leg1_after4[nodes[ptc_cnt+j][0]][2]=temp_2
                patch_list_leg1_after4[nodes[ptc_cnt+j][0]][3]=temp_3
                if(Total_Perimeter_Wire_length(patch_list_leg1_after4,ax)<snd):
                    swap_list.append(tuple((ptc_cnt+j, Total_Perimeter_Wire_length(patch_list_leg1_after4,ax))))
                       
                        
                    trigger=1
                    temp_0=patch_list_leg1_after4[nodes[ptc_cnt+i][0]][0]
                    temp_1=patch_list_leg1_after4[nodes[ptc_cnt+i][0]][1]
                    temp_2=patch_list_leg1_after4[nodes[ptc_cnt+i][0]][2]
                    temp_3=patch_list_leg1_after4[nodes[ptc_cnt+i][0]][3]

                    patch_list_leg1_after4[nodes[ptc_cnt+i][0]][0]=patch_list_leg1_after4[nodes[ptc_cnt+j][0]][0]
                    patch_list_leg1_after4[nodes[ptc_cnt+i][0]][1]=patch_list_leg1_after4[nodes[ptc_cnt+j][0]][1]
                    patch_list_leg1_after4[nodes[ptc_cnt+i][0]][2]=patch_list_leg1_after4[nodes[ptc_cnt+j][0]][2]
                    patch_list_leg1_after4[nodes[ptc_cnt+i][0]][3]=patch_list_leg1_after4[nodes[ptc_cnt+j][0]][3]

                    patch_list_leg1_after4[nodes[ptc_cnt+j][0]][0]=temp_0
                    patch_list_leg1_after4[nodes[ptc_cnt+j][0]][1]=temp_1
                    patch_list_leg1_after4[nodes[ptc_cnt+j][0]][2]=temp_2
                    patch_list_leg1_after4[nodes[ptc_cnt+j][0]][3]=temp_3
                    
                        
                else:
                    temp_0=patch_list_leg1_after4[nodes[ptc_cnt+i][0]][0]
                    temp_1=patch_list_leg1_after4[nodes[ptc_cnt+i][0]][1]
                    temp_2=patch_list_leg1_after4[nodes[ptc_cnt+i][0]][2]
                    temp_3=patch_list_leg1_after4[nodes[ptc_cnt+i][0]][3]

                    patch_list_leg1_after4[nodes[ptc_cnt+i][0]][0]=patch_list_leg1_after4[nodes[ptc_cnt+j][0]][0]
                    patch_list_leg1_after4[nodes[ptc_cnt+i][0]][1]=patch_list_leg1_after4[nodes[ptc_cnt+j][0]][1]
                    patch_list_leg1_after4[nodes[ptc_cnt+i][0]][2]=patch_list_leg1_after4[nodes[ptc_cnt+j][0]][2]
                    patch_list_leg1_after4[nodes[ptc_cnt+i][0]][3]=patch_list_leg1_after4[nodes[ptc_cnt+j][0]][3]

                    patch_list_leg1_after4[nodes[ptc_cnt+j][0]][0]=temp_0
                    patch_list_leg1_after4[nodes[ptc_cnt+j][0]][1]=temp_1
                    patch_list_leg1_after4[nodes[ptc_cnt+j][0]][2]=temp_2
                    patch_list_leg1_after4[nodes[ptc_cnt+j][0]][3]=temp_3
        if Enquiry(swap_list):
            swap_list.sort(key=lambda x:x[1])
            
            index_sort=swap_list[0][0]
            temp_0=patch_list_leg1_after4[nodes[index_sort][0]][0]
            temp_1=patch_list_leg1_after4[nodes[index_sort][0]][1]
            temp_2=patch_list_leg1_after4[nodes[index_sort][0]][2]
            temp_3=patch_list_leg1_after4[nodes[index_sort][0]][3]

            patch_list_leg1_after4[nodes[index_sort][0]][0]=patch_list_leg1_after4[nodes[ptc_cnt+i][0]][0]
            patch_list_leg1_after4[nodes[index_sort][0]][1]=patch_list_leg1_after4[nodes[ptc_cnt+i][0]][1]
            patch_list_leg1_after4[nodes[index_sort][0]][2]=patch_list_leg1_after4[nodes[ptc_cnt+i][0]][2]
            patch_list_leg1_after4[nodes[index_sort][0]][3]=patch_list_leg1_after4[nodes[ptc_cnt+i][0]][3]

            patch_list_leg1_after4[nodes[ptc_cnt+i][0]][0]=temp_0
            patch_list_leg1_after4[nodes[ptc_cnt+i][0]][1]=temp_1
            patch_list_leg1_after4[nodes[ptc_cnt+i][0]][2]=temp_2
            patch_list_leg1_after4[nodes[ptc_cnt+i][0]][3]=temp_3
            snd=Total_Perimeter_Wire_length(patch_list_leg1_after4,ax)

            


    patch_list_leg1_after4_leg=deepcopy(patch_list_leg1_after4)
    for l in range(len(patch_list_leg1_after4)-8):
        k=0
        x_min1=patch_list_leg1_after4_leg[nodes[ptc_cnt+k][0]][0]
        x_max1=patch_list_leg1_after4_leg[nodes[ptc_cnt+k][0]][1]
        y_min1=patch_list_leg1_after4_leg[nodes[ptc_cnt+k][0]][2]
        y_max1=patch_list_leg1_after4_leg[nodes[ptc_cnt+k][0]][3]
        height1=int(patch_list_leg1_after4_leg[nodes[ptc_cnt+k][0]][1])-int(patch_list_leg1_after4_leg[nodes[ptc_cnt+k][0]][0])
        min1=patch_list_leg1_after4_leg[nodes[ptc_cnt+k][0]][0]
    
        for k in range(len(patch_list_leg1_after4_leg)):
        
            x_min1=patch_list_leg1_after4_leg[nodes[ptc_cnt+k][0]][0]
            x_max1=patch_list_leg1_after4_leg[nodes[ptc_cnt+k][0]][1]
            y_min1=patch_list_leg1_after4_leg[nodes[ptc_cnt+k][0]][2]
            y_max1=patch_list_leg1_after4_leg[nodes[ptc_cnt+k][0]][3]
            height1=int(patch_list_leg1_after4_leg[nodes[ptc_cnt+k][0]][1])-int(patch_list_leg1_after4_leg[nodes[ptc_cnt+k][0]][0])
      
       
        # If another patch has a smaller x_min it becomes the patch to be placed
            if (x_min1 < min1):
                
                x_min1=patch_list_leg1_after4_leg[nodes[ptc_cnt+k][0]][0]
                x_max1=patch_list_leg1_after4_leg[nodes[ptc_cnt+k][0]][1]
                y_min1=patch_list_leg1_after4_leg[nodes[ptc_cnt+k][0]][2]
                y_max1=patch_list_leg1_after4_leg[nodes[ptc_cnt+k][0]][3]
                height1=int(patch_list_leg1_after4_leg[nodes[ptc_cnt+k][0]][1])-int(patch_list_leg1_after4_leg[nodes[ptc_cnt+k][0]][0])
                min1=patch_list_leg1_after4_leg[nodes[ptc_cnt+k][0]][0]
                break
            break
        ptc_cnt=3


        #find the selected patch and store its place for other functions
        for t in range(len(patch_list_leg1_after4)-8):
            name=nodes[ptc_cnt][0]
            
            if(x_min1==patch_list_leg1_after4[nodes[ptc_cnt][0]][0] and x_max1==patch_list_leg1_after4[nodes[ptc_cnt][0]][1] and  y_min1==patch_list_leg1_after4[nodes[ptc_cnt][0]][2] and  y_max1==patch_list_leg1_after4[nodes[ptc_cnt][0]][3]):
                
                name=nodes[ptc_cnt][0]
                ptc_cnt+=1
                break
            else:
                ptc_cnt+=1

        #checking from first row
        g=0
        row_cnt=0
        x_min_leg=(rows_4th_detailed[g][2]-int(x_min1))**2
        x_max_leg=(rows_4th_detailed[g][2]-int(x_max1))**2
        y_min_leg=(rows_4th_detailed[g][0]-int(y_min1))**2
        y_max_leg=(((rows_4th_detailed[g][0])+height1)-int(y_max1))**2
        sum_leg=x_min_leg+x_max_leg+y_min_leg+y_max_leg
        sqrt_leg1=math.sqrt(sum_leg)
        
        #get the nearest row for selected cell based on euclidean distance
        for g in range(len(rows_4th_detailed)):
            x_min_leg=(rows_4th_detailed[g][2]-int(x_min1))**2
            x_max_leg=(rows_4th_detailed[g][2]-int(x_max1))**2
            y_min_leg=(rows_4th_detailed[g][0]-int(y_min1))**2
            y_max_leg=(((rows_4th_detailed[g][0])+height1)-int(y_max1))**2
            sum_leg=x_min_leg+x_max_leg+y_min_leg+y_max_leg
            sqrt_leg=math.sqrt(sum_leg)
            
            if(sqrt_leg<sqrt_leg1):
                row_cnt=g
                sqrt_leg1=sqrt_leg

        x_place=int(x_max1)-int(x_min1)
        y_place=int(y_max1)-int(y_min1)
        x = [rows_4th_detailed[row_cnt][2] , rows_4th_detailed[row_cnt][2] , rows_4th_detailed[row_cnt][2] + x_place , rows_3rd_detailed[row_cnt][2] + x_place]
        y = [rows_4th_detailed[row_cnt][0] ,rows_4th_detailed[row_cnt][0] +y_place , rows_4th_detailed[row_cnt][0]+y_place,rows_3rd_detailed[row_cnt][0]]
        patch_list_leg1_after4_leg[name].append(int(rows_4th_detailed[row_cnt][2]))
        patch_list_leg1_after4_leg[name].append(int(rows_4th_detailed[row_cnt][2]) + int(x_place))
        patch_list_leg1_after4_leg[name].append(int(rows_4th_detailed[row_cnt][0]))
        patch_list_leg1_after4_leg[name].append(int(rows_4th_detailed[row_cnt][0]) + int(y_place))
        
            
        rows_4th_detailed[row_cnt][2]=rows_4th_detailed[row_cnt][2] + x_place
        del patch_list_leg1_after4_leg[name]



ovr_after_det4=overlaps(patch_list_leg1_after4)

print("Overlaps after 4th detailed placement: ",ovr_after_det4)

snd_after4=Total_Perimeter_Wire_length(patch_list_leg1_after4,ax)
print("Size after the fourth detailed placement: ",snd_after4)



#Nodes dataframe
cnt=3
columns=['Node_name','Width','Height','Coordinate_x','Coordinate_y','Row_number','Nets','Terminal']
nets_fin=[]
terminals=[]
my_tuple=[]
for i in range(len(patch_list_leg1_after4)-8):
    name=nodes[cnt+i][0]
    node_name=nodes[cnt+i][0]
    width=patch_list_leg1_after4[nodes[cnt+i][0]][1]-patch_list_leg1_after4[nodes[cnt+i][0]][0]
    height=patch_list_leg1_after4[nodes[cnt+i][0]][3]-patch_list_leg1_after4[nodes[cnt+i][0]][2]
    Coordinate_x=patch_list_leg1_after4[nodes[cnt+i][0]][1]
    Coordinate_y=patch_list_leg1_after4[nodes[cnt+i][0]][3]

    num = patch_list_leg1_after4[nodes[cnt+i][0]][3]
    row=str(num)
    res = list(map(int, str(row)))

    
    
    row_fin=res[1]
    
    for j in range(len(nets)):
        if(name in nets[j]):
            nets_fin.append(nets[j])
            for k in range(len(nets[j])):
                if nets[j][k] == 'p1' or nets[j][k] == 'p2' or nets[j][k] == 'p3' or nets[j][k] == 'p4' or nets[j][k] == 'p5' or nets[j][k] == 'p6' or nets[j][k] == 'p7' or nets[j][k] == 'p8':
                    terminals.append(nets[j][k])
        
    nets_in=deepcopy(nets_fin)
    terminals_in=deepcopy(terminals)
    my_tuple.append([node_name,width,height,Coordinate_x,Coordinate_y,row_fin,nets_in,terminals_in])
    nets_fin.clear()
    terminals.clear()
    



df_nodes = pd.DataFrame(my_tuple,columns=columns)

my_tuple.clear()
print(df_nodes)


#Rows dataframe
columns=['Row_name','Density','Cells','Nets','Coordinate_x','Coordinate_y']
nodes_fin=[]
terminals=[]

nets_rows_fin=[]
for i in range(len(rows_4th_detailed)):
    name=i+1
    
    max_val=df_nodes.loc[  (df_nodes['Row_number']==i+1) ]
    maxValue = max_val["Coordinate_x"].max()
    if not maxValue:
        density=0
    else:
        density=maxValue/100
    
    list_a=df_nodes.loc[  (df_nodes['Row_number']==i+1) ]['Node_name']
    nodes_fin = list_a.values.tolist()
    list_c=df_nodes.loc[  (df_nodes['Row_number']==i+1) ]['Nets']
    nets_rows = list_c.values.tolist()
    
    for l in nets_rows:
        if not (nets_rows in nets_rows_fin):
            nets_rows_fin.append(nets_rows)

    
    nodes_in=deepcopy(nodes_fin)
    coo_y=rows_leg[i][0]+10
    nets_rows_fin_1=deepcopy(nets_rows_fin)
    my_tuple.append([name,density,nodes_in,nets_rows_fin_1,maxValue,coo_y])
    nets_rows_fin.clear()

    nodes_fin.clear()

  
    



df_rows = pd.DataFrame(my_tuple,columns=columns)
df_rows = df_rows.fillna(0)  
print(df_rows)


my_tuple.clear()

#Design dataframe
columns=['Density','Number_of_cells','Number_of_terminals','Number_of_nets','Width','Height',"Total_area","Total_cell_area"]

terminals=[]

nets_rows_fin=[]

density = df_rows['Density'].sum()
density=density/8

no_cells=len(patch_list_leg1_after4)-8
no_terminals=8
no_nets=len(nets)
width_design=100
height_design=80
total_area=width_design*height_design
cnt=3
total_cell_area=0
for i in range(len(patch_list_leg1_after4)-8):
    index=cnt+i
    cell_width=patch_list_leg1_after4[nodes[index][0]][1]-patch_list_leg1_after4[nodes[index][0]][0]
    cell_height=patch_list_leg1_after4[nodes[index][0]][3]-patch_list_leg1_after4[nodes[index][0]][2]
    cell_area=cell_width*cell_height
    total_cell_area+=cell_area

my_tuple.append([density,no_cells,no_terminals,no_nets,width_design,height_design,total_area,total_cell_area])


df_design = pd.DataFrame(my_tuple,columns=columns)
print(df_design)

my_tuple.clear()

#Nets dataframe
columns=['Net_name','Nodes','Half_Perimeter_Wirelength','Rows','Internal_nodes','External_nodes']

Half_Perimeter_Wirelength=0
Internal_nodes=[]
External_nodes=[]
nodes_df=[]
list_b=[]
for i in range(len(nets)):
    Net_name=i
    x_min_HPWL_df=[]
    x_max_HPWL_df=[]
    y_min_HPWL_df=[]
    y_max_HPWL_df=[]
    for j in range(len(nets[i])):
        nodes_df.append(nets[i][j])
        x_min_HPWL_df.append(int(patch_list_leg1_after4[nets[i][j]][0]))
        x_max_HPWL_df.append(int(patch_list_leg1_after4[nets[i][j]][1]))
        y_min_HPWL_df.append(int(patch_list_leg1_after4[nets[i][j]][2]))
        y_max_HPWL_df.append(int(patch_list_leg1_after4[nets[i][j]][3]))
        list_b.append(df_nodes.loc[  df_nodes.Node_name==nets[i][j],'Row_number'])
        
        #rows_df = list_b.values.tolist()
        rows_df = [x for x in list_b]
        

    xminHPWL_df=min(x_min_HPWL_df)
    xmaxHPWL_df=max(x_max_HPWL_df)
    yminHPWL_df=min(y_min_HPWL_df)
    ymaxHPWL_df=max(y_max_HPWL_df)
    HPWL_df=(xmaxHPWL_df-xminHPWL_df)+(ymaxHPWL_df-yminHPWL_df)
    min_index_x = x_min_HPWL_df.index(xminHPWL_df)
    max_index_x = x_max_HPWL_df.index(xmaxHPWL_df)
    min_index_y = y_min_HPWL_df.index(yminHPWL_df)
    max_index_y = y_max_HPWL_df.index(ymaxHPWL_df)
    Internal_nodes.append(nets[i][min_index_x])
    if not (nets[i][max_index_y] in Internal_nodes ):
        Internal_nodes.append(nets[i][max_index_y])
    elif not (nets[i][max_index_x] in Internal_nodes ):
        Internal_nodes.append(nets[i][max_index_x])
    else:
        Internal_nodes.append(nets[i][min_index_y])
    
    
    for j in range(len(nets[i])):
        if not (nets[i][j]  in Internal_nodes ):
            External_nodes.append(nets[i][j])


    nodes_df_in=deepcopy(nodes_df)
    rows_df_in=deepcopy(rows_df)
    Internal_nodes_in=deepcopy(Internal_nodes)
    External_nodes_in=deepcopy(External_nodes)
    

    my_tuple.append([Net_name,nodes_df_in,HPWL_df,rows_df_in,Internal_nodes_in,External_nodes_in])
    x_min_HPWL.clear()
    x_max_HPWL.clear()
    y_min_HPWL.clear()
    y_max_HPWL.clear()
    rows_df.clear()
    Internal_nodes.clear()
    External_nodes.clear()
    nodes_df.clear()
    list_b.clear()

df_nets = pd.DataFrame(my_tuple,columns=columns)
print(df_nets)


#largest cell
list_a=df_nodes.loc[  (df_nodes['Width'].idxmax()) ]['Node_name']

print("The largest cell of the curcuit is: ",list_a)

#smallest cell
list_a=df_nodes.loc[  (df_nodes['Width'].idxmin()) ]['Node_name']
print("The smallest cell of the curcuit is: ",list_a)

#average cell area
list_a=df_design.iloc[0]['Total_cell_area']
np.log10(list_a.astype(np.float64))
list_b=df_design.iloc[0]['Number_of_cells']
np.log10(list_b.astype(np.float64))
result=list_a/list_b
print("The average area of a cell is: ",result)

#the most dense row
list_a=df_rows.loc[  (df_rows['Density'].idxmax()) ]['Row_name']
print("The most dense row is row number: ",list_a)

#the least  dense row
list_a=df_rows.loc[  (df_rows['Density'].idxmin()) ]['Row_name']
print("The less dense row is row number: ",list_a)

#the average row density
list_a=df_design.iloc[0]['Density']
print("The average density of each row is: ",list_a)

#Total_Perimeter_Wire_length 
Total_Perimeter_Wire_length_fin = df_nets['Half_Perimeter_Wirelength'].sum()
np.log10(Total_Perimeter_Wire_length_fin.astype(np.float64))
print("The total wire perimeter lenght is : ",Total_Perimeter_Wire_length_fin)

#Adding row for no_connections each cell has
df_nodes['Length'] = df_nodes.Nets.map(len)
#The cell with the most connections
list_a=df_nodes.loc[  (df_nodes['Length'].idxmax()) ]['Node_name']
print("The cell with the most connections is the cell :",list_a)

#The cell with the least connections
list_a=df_nodes.loc[  (df_nodes['Length'].idxmin()) ]['Node_name']
print("The cell with the least connections is the cell :",list_a)


#The average connections for each cell
length_sum = df_nodes['Length'].sum()
np.log10(length_sum.astype(np.float64))
no_nodes=len(df_nodes.Node_name)
print("The average connections of each cell are : ",length_sum/no_nodes)

#creating a length collumn where the lenght of each net is stored
df_nets['Length'] = df_nets.Nodes.map(len)
#The largest net
list_a=df_nets.loc[  (df_nets['Length'].idxmax()) ]['Net_name']
print("The largest net is net : ",list_a)
#The smallest net
list_a=df_nets.loc[  (df_nets['Length'].idxmin()) ]['Net_name']
print("The smallest net is net : ",list_a)





width=[]
height=[]
def net_area(net_name):
    total_net_area=0
    for i in range(len(nets[net_name])):

        width=df_nodes[  (df_nodes['Node_name']==nets[net_name][i]) ]['Width'].iloc[0]
        np.log10(width.astype(np.float64))
        
        
        height=df_nodes[  (df_nodes['Node_name']==nets[net_name][i]) ]['Height'].iloc[0]
        np.log10(height.astype(np.float64))  

        
        
        net_area=width*height
        
        total_net_area+=net_area

    
           
       
      

    return total_net_area





def swap_nodes(name1,name2):
    tempx=df_nodes.loc[df_nodes.Node_name == name1,'Coordinate_x']
    np.log10(tempx.astype(np.float64))
    
    tempx1=df_nodes.loc[df_nodes.Node_name == name2,'Coordinate_x']
    np.log10(tempx1.astype(np.float64))
    
    tempy=df_nodes.loc[df_nodes.Node_name == name1,'Coordinate_y']
    np.log10(tempy.astype(np.float64))
    
    tempy1=df_nodes.loc[df_nodes.Node_name == name2,'Coordinate_y']
    np.log10(tempy1.astype(np.float64))

    df_nodes.loc[df_nodes.Node_name == name1,'Coordinate_x']=int(tempx1)
    df_nodes.loc[df_nodes.Node_name == name2,'Coordinate_x']=int(tempx)
    df_nodes.loc[df_nodes.Node_name == name1,'Coordinate_y']=int(tempy1)
    df_nodes.loc[df_nodes.Node_name == name2,'Coordinate_y']=int(tempy)

    for j in range(len(rows_4th_detailed)):
        name=j+1
    
        max_val=df_nodes.loc[  (df_nodes['Row_number']==j+1) ]
        maxValue = max_val["Coordinate_x"].max()
        if not maxValue:
            density=0
        else:
            density=maxValue/100 

        df_rows.loc[df_rows.Row_name == name,'Density']=density

    '''
    Half_Perimeter_Wirelength=0
    Internal_nodes=[]
    External_nodes=[]
    nodes_df=[]
    list_b=[]
    
    for i in range(len(nets)):
        Net_name=i
        x_min_HPWL_df=[]
        x_max_HPWL_df=[]
        y_min_HPWL_df=[]
        y_max_HPWL_df=[]
        for k in range(len(nets[i])):
            nodes_df.append(nets[i][j])
            x_min_HPWL_df.append(int(patch_list_leg1_after4[nets[i][k]][0]))
            x_max_HPWL_df.append(int(patch_list_leg1_after4[nets[i][k]][1]))
            y_min_HPWL_df.append(int(patch_list_leg1_after4[nets[i][k]][2]))
            y_max_HPWL_df.append(int(patch_list_leg1_after4[nets[i][k]][3]))
            list_b.append(df_nodes.loc[  df_nodes.Node_name==nets[i][k],'Row_number'])
            
            #rows_df = list_b.values.tolist()
            rows_df = [x for x in list_b]
            

        xminHPWL_df=min(x_min_HPWL_df)
        xmaxHPWL_df=max(x_max_HPWL_df)
        yminHPWL_df=min(y_min_HPWL_df)
        ymaxHPWL_df=max(y_max_HPWL_df)
        HPWL_df=(xmaxHPWL_df-xminHPWL_df)+(ymaxHPWL_df-yminHPWL_df)


        min_index_x = x_min_HPWL_df.index(xminHPWL_df)
        max_index_x = x_max_HPWL_df.index(xmaxHPWL_df)
        min_index_y = y_min_HPWL_df.index(yminHPWL_df)
        max_index_y = y_max_HPWL_df.index(ymaxHPWL_df)
        Internal_nodes.append(nets[i][min_index_x])
        if not (nets[i][max_index_y] in Internal_nodes ):
            Internal_nodes.append(nets[i][max_index_y])
        elif not (nets[i][max_index_x] in Internal_nodes ):
            Internal_nodes.append(nets[i][max_index_x])
        else:
            Internal_nodes.append(nets[i][min_index_y])
        
        
        for j in range(len(nets[i])):
            if not (nets[i][j]  in Internal_nodes ):
                External_nodes.append(nets[i][j])
    '''
    


def swap_rows(name1,name2):
    temp1=df_rows.at[name1-1,'Coordinate_y']
    df_rows.at[name1-1,'Coordinate_y']=df_rows.at[name2-1,'Coordinate_y']
    df_rows.at[name2-1,'Coordinate_y']=temp1
    temp=df_rows.iloc[name1-1]
    df_rows.iloc[name1-1]=df_rows.iloc[name2-1]
    df_rows.iloc[name2-1]=temp
    df_rows.at[name1-1,'Row_name']=name2-1
    df_rows.at[name2-1,'Row_name']=name1+1
    list_name1=list(df_rows.at[name1-1,'Cells'])
    list_name2=list(df_rows.at[name2-1,'Cells'])
    for i in range(len(list_name2)):
        
        df_nodes.loc[df_nodes['Node_name'] == list_name2[i], 'Coordinate_y'] = df_rows.at[name1,'Coordinate_y']
        df_nodes.loc[df_nodes['Node_name'] == list_name2[i], 'Row_number'] = name1+1

    for i in range(len(list_name1)):
        
        df_nodes.loc[df_nodes['Node_name'] == list_name1[i], 'Coordinate_y'] = df_rows.at[name2,'Coordinate_y']
        df_nodes.loc[df_nodes['Node_name'] == list_name1[i], 'Row_number'] = name2+1


    x_min_HPWL.clear()
    x_max_HPWL.clear()
    y_min_HPWL.clear()
    y_max_HPWL.clear()
    
    for i in range(len(nets)):
        hpwl=0
        list_name=list(df_nets.at[i,'Nodes'])
        if(lists_overlap(list_name, list_name1)):
            

            for j in range(len(list_name1)):
                
                
                x_min_HPWL.append(pd.to_numeric(df_nodes.loc[df_nodes['Node_name'] == list_name1[j], 'Coordinate_x'].values))
                
                x_max_HPWL.append(pd.to_numeric(df_nodes.loc[df_nodes['Node_name'] == list_name1[j], 'Coordinate_x'].values)+pd.to_numeric(df_nodes.loc[df_nodes['Node_name'] == list_name1[j], 'Width'].values))
                
                y_min_HPWL.append(df_nodes.loc[df_nodes['Node_name'] == list_name1[j], 'Coordinate_y'].values-df_nodes.loc[df_nodes['Node_name'] == list_name1[j], 'Height'].values)
                
                y_max_HPWL.append(df_nodes.loc[df_nodes['Node_name'] == list_name1[j], 'Coordinate_y'].values)
                
                
                
            xminHPWL=min(x_min_HPWL)
            xmaxHPWL=max(x_max_HPWL)
            yminHPWL=min(y_min_HPWL)
            ymaxHPWL=max(y_max_HPWL)    
            hpwl=(xmaxHPWL-xminHPWL)+(ymaxHPWL-yminHPWL)
            df_nets.at[i,'Half_Perimeter_Wirelength']=hpwl
            hpwl=0
            x_min_HPWL.clear()
            x_max_HPWL.clear()
            y_min_HPWL.clear()
            y_max_HPWL.clear()
            

                
            
            

        if(lists_overlap(list_name, list_name2)):

            for j in range(len(list_name2)):
                    
                
                x_min_HPWL.append(pd.to_numeric(df_nodes.loc[df_nodes['Node_name'] == list_name2[j], 'Coordinate_x'].values))

                x_max_HPWL.append(pd.to_numeric(df_nodes.loc[df_nodes['Node_name'] == list_name2[j], 'Coordinate_x'].values)+pd.to_numeric(df_nodes.loc[df_nodes['Node_name'] == list_name2[j], 'Width'].values))
                
                y_min_HPWL.append(df_nodes.loc[df_nodes['Node_name'] == list_name2[j], 'Coordinate_y'].values-df_nodes.loc[df_nodes['Node_name'] == list_name2[j], 'Height'].values)
                
                y_max_HPWL.append(df_nodes.loc[df_nodes['Node_name'] == list_name2[j], 'Coordinate_y'].values)
            
            xminHPWL=min(x_min_HPWL)
            xmaxHPWL=max(x_max_HPWL)
            yminHPWL=min(y_min_HPWL)
            ymaxHPWL=max(y_max_HPWL)    
            hpwl=(xmaxHPWL-xminHPWL)+(ymaxHPWL-yminHPWL)
            df_nets.at[i,'Half_Perimeter_Wirelength']=hpwl
            hpwl=0
            x_min_HPWL.clear()
            x_max_HPWL.clear()
            y_min_HPWL.clear()
            y_max_HPWL.clear()
          
                

            
        
        
print(df_nodes) 
swap_nodes('a2','a3')
print("After swaping nodes")
print(df_nodes) 
  

print("net area with index 8 is :",net_area(8))

print(df_rows) 
swap_rows(2,3)
print("After swaping nodes")
print(df_rows) 

print(df_rows) 



def add_cell(df_nodes):
    nets_fin=[]
    add_tuple=[]
    nets_add=[]
    name='a31'
    width=random.randint(1, 44)
    height=10
    Coordinate_x=random.randint(1, 90)
    Coordinate_y=random.randint(100, 170)
    Row_number=random.randint(1, 8)
    nets_cnt=random.randint(1, 5)
    for i in range(nets_cnt):
        random_net=random.randint(0, 39)
        nets_list=list(df_nets.at[random_net,'Nodes'])
        random_index=random.randint(1, len(nets_list)-1)
        nets_add.append(nets_list[random_index])
    term_rnd=random.randint(0, 8)
    if(term_rnd==0):
        terminal=[]
    else:
        terminal='p' + str(term_rnd)

    lenght=len(nets_add)
    for j in range(len(nets)):
        if(lists_overlap(nets_add, nets[j])):
            nets_fin.append([nets[j],name])
            
            


    df2 = {'Node_name': name, 'Width': width, 'Height': height,'Coordinate_x': Coordinate_x,'Coordinate_y': Coordinate_y,'Row_number': Row_number,'Nets': nets_fin,'Terminal': terminal,'Length': lenght}
    df_nodes = df_nodes.append(df2, ignore_index = True)


    
    return df_nodes
   
print(df_nodes)
df_nodes=add_cell(df_nodes)
print("After adding a cell")
print(df_nodes)






    



    
    




    

















plt.show() 