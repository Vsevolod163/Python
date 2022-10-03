import time

def random1(n, min, max):

    list1 = []
    
    for i in range(1, n + 1):
       
        x = round(i * (time.time() * 1000) % (10 ** (len(str(max)) - 1)))
        
        while x > max or x < min:
            x = round(i * (time.time() * 10 ** len(str(max))) % (10 ** (len(str(max)))))
        
        if i % 2 == 0 and -x > min:
            list1.append(-x)
        else: 
            list1.append(x)   
    
    return list1

result_list = random1(5, -500, 1000)
print(result_list)


