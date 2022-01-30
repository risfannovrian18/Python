import time
start_time = time.time()

def mergeSort(myList) :
    if len(myList) > 1 :
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators fro traversing the two halves
        i = 0
        j = 0

        # Iterations for the main list
        k = 0

        while i < len(left) and j < len(right) :
            if left[i] <= right[i] :
                # The value from the left half has been used
                myList[k] = left[i]
            # move the iterator forward
                i+=1
            else:
                 myList[k] = right[j]
                 j+=1
            # move to the next slot
            k+=1
            # for all the remaining values
            while i < len(left):
                myList[k] = left[i]
                i+=1
                k+=1
            while j < len(right) :
                myList[k] = right[j]
                j+=1
                k+=1

myList = [23,7,32,99,4,15,11,20,55,85,64]
mergeSort(myList)
print(myList)

print(f"Proses finished {time.time()-start_time}")