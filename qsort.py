def qsort(lis):
    def partition(lis, start, end):
        flag = lis[end]
        i = start - 1
        for j in range(start, end):
            if lis[j] > flag: pass
            else:
                i += 1
                lis[i], lis[j] = lis[j], lis[i]
        lis[end], lis[i + 1] = lis[i+1], lis[end]
        return i + 1

    def quicksort(lis, start, end):
        if start >= end: return
        pos = partition(lis, start, end)
        quicksort(lis, start, pos - 1)
        quicksort(lis, pos + 1, end)

    quicksort(lis, 0, len(lis) - 1)

    
