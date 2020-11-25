def Selction_Sort(datas):
    for i in range(len(datas)-1):              
        min = i 
        for j in range(i+1, len(datas)):   
            if datas[j] > datas[min]:       
                min = j             

        datas[i], datas[min] = datas[min], datas[i]  

        print(datas)          
        print('---'*16)          
    return datas             
    




    
if __name__ == '__main__':
    import random
    b = []
    for i in range(0,8):
        a = random.randint(0,9)
        b += [a]
    random.shuffle(b)
    print(b)
    b = Selction_Sort(b)
    
    
