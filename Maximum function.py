lst = [1,2,5,8,6,10,100,4,1,20,7] #sample list

def maxx(lst : (list, tuple)) -> int :
    x = 0
    for i in lst :
        if i > x :
            x = i
    print(x)
    
maxx(lst)
