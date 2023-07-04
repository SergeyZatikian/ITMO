alist = [6,5,12,10,9,1]
print(alist)

def mergeSort(alist):
    print('разделение->', alist)
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i, j, k = 0, 0, 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i +=1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i, k = i + 1, k + 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j, k = j + 1, k + 1
    print('слияние ->', alist)
mergeSort(alist)