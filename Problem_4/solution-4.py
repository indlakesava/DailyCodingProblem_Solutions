def mergeSort(alist):
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

def missing_int(lst):
    j=0; flag=0;
    for i in range(len(lst)):
        if(lst[i]>0):
            j+=1;
            if(lst[i] != j):
                print(j)
                flag = 1
                break
    if (flag==0):
        print(lst[-1]+1)

lista = [1,2,0]
mergeSort(lista)
missing_int(lista)
