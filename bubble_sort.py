def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
print("enter the number yu want to sort:")
input1=input().split()
input1=[int(i) for i in input1]
nlist=input1
bubbleSort(nlist)
print(nlist)