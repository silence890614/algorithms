import random

def Insertion_Sort(datas):
    for i in range(1, len(datas)):   
        for j in range(i):    
            current = datas[i] 
            if current < datas[j]: 
                for k in range(i,j):  
                  print(datas) 
    return datas           
   


def insertionSort(arr):
    for i in range(len(arr)): 
        preIndex = i-1   
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex-=1
        arr[preIndex+1] = current
        print(arr)
    return arr

if __name__ == '__main__':
    import random
    b = []
    for i in range(0,8):
        a = random.randint(0,9)
        b += [a]
    random.shuffle(b)
    c = b.copy()

    arr = insertionSort(b)
    print('---'*16)
    Insertion_Sort(c)
  
