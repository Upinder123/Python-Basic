def binary_search(l,start,end,key):
    while start<=end:
        mid=(start+end-1)//2
        if key<l[mid]:
            end=mid
        elif key>l[mid]:
            start=mid+1
        else:
            return mid
    return -1
    
key=int(input('enter value to be found'))        
size=int(input('size'))
for i in range(size)
list=([int(input('enter value'))] for i in range(size))
flag=binary_search(list,0,size,key)
if flag>0:
    print(key,'found at', flag+1,'th position')
else:
    print('not found')

