#Merge Sort

array = []


#opening the text file containing the numbers and putting them into an array
with open("twelve.txt") as f:
    n = len(f.readlines())
    f.seek(0)
    for i in range(0, n):
        array.append(int(f.readline()))
print("the length is ", n)
print("the array is: ", array)




def merge(a, b, array):
    i = 0
    j = 0
    k = 0
    n1 = len(a)
    n2 = len(b)
    while( i < n1 and j < n2 ):
        if a[i] <= b[j]:
            array[k] = a[i]
            i += 1
            k += 1
        elif b[j] < a[i]:
            array[k] = b[j]
            j += 1
            k += 1
    while( i < n1 ):
        array[k] = a[i]
        k += 1
        i += 1
    while( j < n2 ):
        array[k] = b[j]
        k += 1
        j += 1

def merge_sort(array):
    n = len(array)
    if (n <= 1):
        return
    mid = int(n/2)
    left = array[:mid]
    right = array[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, array)


merge_sort(array)
print("The sorted array is ", array)
