a = [1,2,3,5,8,13,21,34,55,89]
b = []
number = int(input("please give a number "))
for i in a:
    if i<number:
       b.append(a[i])
for j in b:       
    print(b[j])       
    

   