def fibonacci(n):
    while n!=0:
       a,b = 0,1
       c = a+b
       a=b,b=c
    if c<=n:
        print(c)
    else:
        n = n-n    

p = int(input('n'))            
fibonacci(p)            
  
        


