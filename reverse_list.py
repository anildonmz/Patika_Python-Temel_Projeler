def rev(l):
    for i in l:
        if type(i) ==list:
            i.reverse()
            rev(i)
    return l

a=rev([[1,2,3],4,[2,3],[4,5]])
a.reverse()
print(f"reverse a: {a}")

b=rev([[1, 2], [3, 4], [5, 6, 7]])
b.reverse()
print(f"reverse b: {b}")

        



  



    

    
 

   




        






  

