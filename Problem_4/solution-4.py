def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

lista = [1,2,0]
mergeSort(lista)
print(lista)

#Done with sorting, We need to find the first missing positive integer now
j=0; flag=0;
for i in range(len(lista)):
    if(lista[i]>0):
        j+=1;
        if(lista[i] != j):
            print(j)
            flag = 1
            break
if (flag==0):
    print(lista[-1]+1)
