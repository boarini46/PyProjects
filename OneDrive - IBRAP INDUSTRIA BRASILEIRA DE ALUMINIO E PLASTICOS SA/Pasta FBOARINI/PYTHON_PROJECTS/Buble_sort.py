v = [24,48,37,12,57,86,33,92]

def bubble_sort(v):
    for i in range(len(v)-1):
        for j in range(len(v)-i-1):
            if(v[j]>v[j+1]):
                v[j],v[j+1] = v[j+1],v[j]


def insertion_sort(v):
    for i in range(1,len(v)):
        x = v[i]
        j = i-1
        while j >=0 and x < v[j]:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = x



#insertion_sort(v)
#print(v)
bubble_sort(v)
print(v)