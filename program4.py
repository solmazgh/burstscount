'''Project 5 - Program 4
by Solmaz Gharagozloo
11/27/18
'''


burstlenghts=[]
burstList=[]


listsize=int(input("please enter the number of digits you would like to enter( it could be a number between 1 to 15: "))
def getnum():
    for i in range (listsize):
      x=int(input("please enter the digit number "+str(i+1)+ " : "))
      burstList.append(x)
    return burstList  
print(getnum()) 
burstcounts=[]
counter=0
flag=False
for i in range (listsize):
    if burstList[i]==0 :
     counter+=1
     flag=True
    else:
     flag=False
     counter=0
    if flag==True:
      burstcounts.append(counter)   
print(burstcounts) 

print(len(burstcounts))
bursts=[]
for i in range(len(burstcounts)):
    if burstcounts[i]==1 and i!=0:
        x=burstcounts[i-1]
        bursts.append(x)
    
    if( i == len(burstcounts)-1 and burstcounts[len(burstcounts)-1]==1):
        bursts.append(1)
        

print(bursts)   

print("Burst   Length") 

for i in range(len(bursts)):
    print(str(i+1)+"         "  , bursts[i])

'''print(str(j+1)+"         "  , bursts[1] )'''    
print("Average burst length is ", format(sum(bursts)/len(bursts),",.2f") ) 
print("Minimum burst length is " , min(bursts))
print("Maximum burst length is ",max(bursts))
print("Total number of zeros is ", sum(bursts))
